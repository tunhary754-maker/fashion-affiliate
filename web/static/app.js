let state = { products: [], characters: [], prompts: [], jobs: [], outputs: [], accounts: [] };
let sel = { product: "", character: "" };
let concatSel = [];

function el(id) { return document.getElementById(id); }
async function api(path, opts) {
  const r = await fetch(path, opts);
  const d = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(d.error || ("Lỗi " + r.status));
  return d;
}
function esc(s) { return String(s || "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }

document.querySelectorAll("#tabs button").forEach(b => {
  b.onclick = () => {
    document.querySelectorAll("#tabs button").forEach(x => x.classList.remove("active"));
    document.querySelectorAll(".tab").forEach(x => x.classList.remove("active"));
    b.classList.add("active");
    el("tab-" + b.dataset.tab).classList.add("active");
  };
});

async function loadAll() {
  const ov = await api("/api/overview");
  el("overview").innerHTML = [
    ["Prompt mẫu", ov.prompts], ["Job", ov.jobs], ["Job đã xong", ov.jobs_done],
    ["Video kết quả", ov.outputs], ["Ảnh sản phẩm", ov.products], ["Ảnh nhân vật", ov.characters],
    ["Tài khoản gateway", ov.accounts || 0],
  ].map(([k, v]) => `<div class="card"><b>${v}</b>${k}</div>`).join("");
  state.accounts = await api("/api/accounts");
  el("accounts").innerHTML = state.accounts.length ? state.accounts.map(a => `
    <div class="job"><b>${esc(a.name)}</b> — ${esc(a.status)} — ${a.jobs} job
    <br>Proxy: ${esc(a.proxy || "(không có)")}
    <br><button onclick="checkAccount('${esc(a.name)}')">Kiểm tra</button>
    <button class="secondary" onclick="delAccount('${esc(a.name)}')">Xoá</button></div>`).join("") : "<p>Chưa có tài khoản gateway nào.</p>";
  state.prompts = await api("/api/prompts");
  state.products = await api("/api/products");
  state.characters = await api("/api/character");
  state.jobs = await api("/api/jobs");
  state.outputs = await api("/api/outputs");
  el("job-prompt").innerHTML = state.prompts.map(p => `<option value="${esc(p.name)}">${esc(p.title)}</option>`).join("");
  renderThumbs("products", state.products, "/input/", "product");
  renderThumbs("characters", state.characters, "/character/", "character");
  renderThumbs("character-list", state.characters, "/character/", "character", true);
  el("jobs").innerHTML = state.jobs.length ? state.jobs.map(job => `
    <div class="job"><b>${esc(job.product)}</b> — ${esc(job.prompt)} — ${job.status === "done" ? "✅ Đã xong" : "⏳ Chờ tạo"}
    <br>Ảnh SP: ${esc(job.product_image || "(chưa chọn)")} | Ảnh NV: ${esc(job.character_image || "(chưa có)")}
    <pre>${esc(job.prompt_text || "")}</pre>
    <button onclick="copyPrompt(${job.id})">Copy prompt</button>
    ${job.status !== "done" ? `<button class="secondary" onclick="markDone(${job.id})">Đã xong</button>` : ""}
    </div>`).join("") : "<p>Chưa có job nào.</p>";
  el("outputs").innerHTML = state.outputs.length ? state.outputs.map(o => `
    <div class="output"><b>${esc(o.name)}</b> (${(o.size / 1048576).toFixed(1)} MB)<br>
    <video controls preload="metadata" src="/output/${encodeURIComponent(o.name)}"></video><br>
    <a href="/output/${encodeURIComponent(o.name)}" download>Tải video</a></div>`).join("") : "<p>Chưa có video nào trong output/.</p>";
  el("concat-clips").innerHTML = state.outputs.map(o => `
    <button class="${concatSel.includes(o.name) ? "selected" : ""}" onclick="toggleConcat('${esc(o.name)}')">
    ${concatSel.indexOf(o.name) >= 0 ? (concatSel.indexOf(o.name) + 1) + ". " : ""}${esc(o.name)}</button>`).join("");
}
function renderThumbs(target, items, prefix, kind, withDelete) {
  el(target).innerHTML = items.length ? items.map(it => `
    <figure class="${sel[kind] === it.name ? "selected" : ""}" onclick="selectImg('${kind}','${esc(it.name)}')">
      <img src="${prefix}${encodeURIComponent(it.name)}" alt="">
      <figcaption>${esc(it.name)}</figcaption>
    </figure>
    ${withDelete ? `<button class="secondary" onclick="delImg('${kind}','${esc(it.name)}')">Xoá</button>` : ""}`).join("") : "<p>Chưa có ảnh.</p>";
}
window.selectImg = (kind, name) => { sel[kind] = name; loadAll(); };
window.toggleConcat = (name) => {
  const i = concatSel.indexOf(name);
  if (i >= 0) concatSel.splice(i, 1); else concatSel.push(name);
  loadAll();
};
window.copyPrompt = async (id) => {
  const job = state.jobs.find(j => String(j.id) === String(id));
  if (!job) return;
  const text = `Ảnh nhân vật: ${job.character_image || "(chưa có)"}\nẢnh sản phẩm: ${job.product_image || ""}\n\n${job.prompt_text || ""}`;
  await navigator.clipboard.writeText(text);
  alert("Đã copy prompt. Trong chat với Muse, gửi ảnh nhân vật trước, ảnh sản phẩm sau, rồi dán prompt này.");
};
window.markDone = async (id) => { await api(`/api/jobs/${id}/done`, { method: "POST" }); loadAll(); };
window.checkAccount = async (name) => {
  el("account-result").innerHTML = "<p>⏳ Đang kiểm tra...</p>";
  try {
    const r = await api(`/api/accounts/${encodeURIComponent(name)}/check`, { method: "POST" });
    el("account-result").innerHTML = `<div class="job"><b>${esc(r.name)}</b><br>
      Muse login: ${r.login_ok ? "✅ OK" : "❌ Lỗi"} — ${esc(r.login_msg)}<br>
      Token/quota: ${r.quota_ok === true ? "✅ OK" : (r.quota_ok === false ? "❌ Lỗi" : "Không rõ")} — ${esc(r.quota_msg)}<br>
      Tuần ${esc(r.week)}: ${esc(r.videos)} video, ${esc(r.minutes)} phút</div>
      <p class="note">Login OK chỉ chứng minh session web còn sống, chưa chứng minh gateway sinh video được.</p>`;
  } catch (e) { el("account-result").innerHTML = `<p>❌ ${esc(e.message)}</p>`; }
};
window.delAccount = async (name) => {
  if (!confirm(`Xoá tài khoản ${name}? Không khôi phục được, muốn dùng lại phải thêm cookie mới.`)) return;
  await api(`/api/accounts/${encodeURIComponent(name)}`, { method: "DELETE" });
  await loadAll();
};
el("btn-add-account").onclick = async () => {
  try {
    const acc = await api("/api/accounts", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: el("acc-name").value,
        proxy: el("acc-proxy").value,
        cookie: el("acc-cookie").value,
      }),
    });
    el("account-add-result").innerHTML = `<p>✅ Đã thêm tài khoản <b>${esc(acc.name)}</b>. Bấm Kiểm tra để xác nhận login trước khi dùng.</p>`;
    el("acc-name").value = ""; el("acc-proxy").value = ""; el("acc-cookie").value = "";
    await loadAll();
  } catch (e) { el("account-add-result").innerHTML = `<p>❌ ${esc(e.message)}</p>`; }
};
window.delImg = async (kind, name) => {
  if (!confirm("Xoá ảnh này?")) return;
  const path = kind === "product" ? "products" : "characters";
  await api(`/api/${path}/${encodeURIComponent(name)}`, { method: "DELETE" });
  if (sel[kind] === name) sel[kind] = "";
  loadAll();
};

async function upload(kind, file) {
  const data = await new Promise(res => {
    const rd = new FileReader();
    rd.onload = () => res(rd.result);
    rd.readAsDataURL(file);
  });
  const out = await api("/api/uploads", {
    method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ kind, name: file.name, data }),
  });
  if (kind === "product") sel.product = out.name; else sel.character = out.name;
  await loadAll();
}
function bindDrop(dropId, fileId, kind) {
  const drop = el(dropId);
  drop.ondragover = e => { e.preventDefault(); drop.style.borderColor = "#e11d48"; };
  drop.ondragleave = () => drop.style.borderColor = "";
  drop.ondrop = async e => {
    e.preventDefault();
    const f = e.dataTransfer.files[0];
    if (f) await upload(kind, f);
  };
  el(fileId).onchange = async e => { if (e.target.files[0]) await upload(kind, e.target.files[0]); };
}
bindDrop("drop-product", "file-product", "product");
bindDrop("drop-character", "file-character", "character");

el("btn-create-job").onclick = async () => {
  try {
    const job = await api("/api/jobs", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        product: el("job-product").value,
        details: el("job-details").value,
        prompt: el("job-prompt").value,
        notes: el("job-notes").value,
        product_image: sel.product,
        character_image: sel.character,
      }),
    });
    el("job-result").innerHTML = `<p>✅ Đã tạo job #${job.id} cho <b>${esc(job.product)}</b>. Copy prompt ở danh sách job, rồi trong chat gửi ảnh nhân vật trước, ảnh sản phẩm sau, rồi dán prompt.</p><pre>${esc(job.prompt_text)}</pre>`;
    await loadAll();
  } catch (e) { alert(e.message); }
};
el("btn-concat").onclick = async () => {
  if (concatSel.length < 2) { alert("Chọn ít nhất 2 clip theo đúng thứ tự."); return; }
  el("concat-result").innerHTML = "<p>⏳ Đang ghép, chờ một lúc...</p>";
  try {
    const out = await api("/api/concat", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ clips: concatSel, mode: el("concat-mode").value, output: el("concat-output").value }),
    });
    el("concat-result").innerHTML = `<p>✅ Đã ghép xong: <b>${esc(out.name)}</b> (${(out.size / 1048576).toFixed(1)} MB). Xem ở tab Kết quả.</p>`;
    concatSel = [];
    await loadAll();
  } catch (e) { el("concat-result").innerHTML = `<p>❌ ${esc(e.message)}</p>`; }
};

loadAll().catch(e => alert("Không tải được dữ liệu: " + e.message));
