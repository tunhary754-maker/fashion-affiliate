#!/usr/bin/env python3
"""Web Studio đơn giản cho Fashion Affiliate Video Tool.

Chỉ chạy trên máy của bạn (127.0.0.1), không có đăng nhập, không gửi
cookie hay key ra ngoài. Giao diện giúp quản lý: tổng quan, tạo video
(tạo job + prompt để dùng trong chat với Muse), nhân vật, kết quả và
ghép clip.

Video vẫn được tạo trong chat với Muse, rồi lưu vào output/ (hoặc đã
nằm sẵn ở đó khi tạo bằng chat này). Giao diện không tự tạo video bằng
API ngoài.

Tab Tài khoản chỉ phục vụ mode gateway (gateway_cli.py): thêm/kiểm tra/
xoá acc Muse bằng cookie. Cookie chỉ lưu local ở gateway_config/
accounts.json (quyền 0600, đã nằm trong .gitignore, không đẩy lên
GitHub), chỉ dùng để kiểm tra đăng nhập với Muse, và API không bao giờ
trả cookie ra ngoài. Luồng chat-native mặc định không cần đăng nhập.

Chạy:
    python3 web/server.py
    python3 web/server.py --port 8080
Mở: http://127.0.0.1:8080
"""

import argparse
import base64
import json
import os
import subprocess
import sys
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
STATIC = Path(__file__).resolve().parent / "static"
JOBS_FILE = ROOT / "jobs" / "jobs.json"
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(ROOT))  # để import được gateway.accounts (mode gateway)


def _gateway():
    """Import lười gateway để tab cũ không hỏng nếu thiếu dependency."""
    from gateway.accounts import Account, AccountManager, load_cookies

    return Account, AccountManager, load_cookies


def _safe_account_name(name):
    raw = str(name or "").strip()
    if not raw or len(raw) > 64:
        return ""
    if not all(c.isalnum() or c in ("-", "_") for c in raw):
        return ""
    return raw


def _account_public(acc):
    status = "tắt" if not acc.enabled else (
        "cooldown" if acc.is_on_cooldown() else "sẵn sàng"
    )
    return {
        "name": acc.name,
        "proxy": acc.proxy_config().masked(),
        "jobs": acc.jobs_done,
        "status": status,
    }


def _list_accounts():
    try:
        _, AccountManager, _ = _gateway()
        return [_account_public(a) for a in AccountManager().accounts]
    except Exception:
        return []

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
IMAGE_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
}
MAX_UPLOAD_BYTES = 12 * 1024 * 1024


def _list_files(folder, suffixes):
    folder = ROOT / folder
    if not folder.exists():
        return []
    out = []
    for path in sorted(folder.iterdir()):
        if path.is_file() and path.suffix.lower() in suffixes:
            out.append({"name": path.name, "size": path.stat().st_size})
    return out


def _read_jobs():
    if not JOBS_FILE.exists():
        return []
    try:
        data = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def _write_jobs(jobs):
    JOBS_FILE.parent.mkdir(parents=True, exist_ok=True)
    JOBS_FILE.write_text(
        json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def _safe_name(name, suffixes=IMAGE_SUFFIXES):
    """Chỉ giữ tên file ảnh hợp lệ, chặn đường dẫn ra ngoài thư mục."""
    base = Path(str(name or "")).name.strip()
    safe = "".join(c for c in base if c.isalnum() or c in ("-", "_", "."))
    if not safe or safe.startswith("."):
        return ""
    if Path(safe).suffix.lower() not in suffixes:
        return ""
    return safe


def _safe_video_name(name):
    base = Path(str(name or "")).name.strip()
    safe = "".join(c for c in base if c.isalnum() or c in ("-", "_", "."))
    if not safe or safe.startswith(".") or Path(safe).suffix.lower() != ".mp4":
        return ""
    return safe


def _read_prompt(name):
    # Chỉ đọc file trong prompts/, không cho đường dẫn ra ngoài.
    safe = Path(name).name
    path = ROOT / "prompts" / safe
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _fill_prompt(text, product, details):
    """Thay placeholder trong mẫu prompt bằng thông tin thật của job."""
    filled = text
    filled = filled.replace("[TÊN SẢN PHẨM + CHI TIẾT]", f"{product} — {details}".strip(" —"))
    filled = filled.replace("[TÊN SẢN PHẨM]", product)
    filled = filled.replace("[CHI TIẾT]", details)
    return filled


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path, content_type):
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path in ("/", "/index.html"):
            return self._send_file(STATIC / "index.html", "text/html; charset=utf-8")
        if path == "/app.js":
            return self._send_file(STATIC / "app.js", "text/javascript; charset=utf-8")
        if path == "/style.css":
            return self._send_file(STATIC / "style.css", "text/css; charset=utf-8")
        if path == "/api/overview":
            jobs = _read_jobs()
            return self._send_json({
                "prompts": len(_list_files("prompts", {".md"})),
                "jobs": len(jobs),
                "jobs_done": sum(1 for j in jobs if j.get("status") == "done"),
                "outputs": len(_list_files("output", {".mp4"})),
                "products": len(_list_files("input", IMAGE_SUFFIXES)),
                "characters": len(_list_files("character-reference", IMAGE_SUFFIXES)),
                "accounts": len(_list_accounts()),
            })
        if path == "/api/prompts":
            items = []
            for item in _list_files("prompts", {".md"}):
                text = _read_prompt(item["name"])
                first = next(
                    (line.lstrip("# ").strip() for line in text.splitlines() if line.strip()),
                    item["name"],
                )
                items.append({"name": item["name"], "title": first, "text": text})
            return self._send_json(items)
        if path == "/api/jobs":
            return self._send_json(_read_jobs())
        if path == "/api/outputs":
            return self._send_json(_list_files("output", {".mp4"}))
        if path == "/api/character":
            return self._send_json(_list_files("character-reference", IMAGE_SUFFIXES))
        if path == "/api/products":
            return self._send_json(_list_files("input", IMAGE_SUFFIXES))
        if path == "/api/accounts":
            return self._send_json(_list_accounts())
        if path.startswith("/input/"):
            name = _safe_name(unquote(path[len("/input/"):]))
            target = ROOT / "input" / name if name else None
            if target and target.exists():
                return self._send_file(target, IMAGE_TYPES[target.suffix.lower()])
            return self._send_json({"error": "not found"}, status=404)
        if path.startswith("/character/"):
            name = _safe_name(unquote(path[len("/character/"):]))
            target = ROOT / "character-reference" / name if name else None
            if target and target.exists():
                return self._send_file(target, IMAGE_TYPES[target.suffix.lower()])
            return self._send_json({"error": "not found"}, status=404)
        if path.startswith("/output/"):
            name = Path(unquote(path[len("/output/"):])).name
            target = ROOT / "output" / name
            if target.exists() and target.suffix.lower() == ".mp4":
                return self._send_file(target, "video/mp4")
            return self._send_json({"error": "not found"}, status=404)
        return self._send_json({"error": "not found"}, status=404)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        try:
            body = json.loads(raw.decode("utf-8")) if raw else {}
        except ValueError:
            body = {}

        if path == "/api/uploads":
            kind = str(body.get("kind") or "")
            folder = {"product": "input", "character": "character-reference"}.get(kind)
            name = _safe_name(body.get("name"))
            raw_data = str(body.get("data") or "")
            if "," in raw_data:
                raw_data = raw_data.split(",", 1)[1]
            if not folder or not name:
                return self._send_json(
                    {"error": "Thiếu loại ảnh hoặc tên file không hợp lệ (png/jpg/webp)"},
                    status=400,
                )
            try:
                content = base64.b64decode(raw_data, validate=True)
            except (ValueError, Exception):
                return self._send_json({"error": "Ảnh không đúng định dạng"}, status=400)
            if not content or len(content) > MAX_UPLOAD_BYTES:
                return self._send_json(
                    {"error": "Ảnh quá lớn (tối đa 12 MB)"}, status=400
                )
            target_dir = ROOT / folder
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / name
            stem, suffix = target.stem, target.suffix
            n = 2
            while target.exists():
                target = target_dir / f"{stem}-{n}{suffix}"
                n += 1
            target.write_bytes(content)
            return self._send_json({"name": target.name, "size": len(content)}, status=201)

        if path == "/api/jobs":
            jobs = _read_jobs()
            prompt_name = str(body.get("prompt") or "")
            product = str(body.get("product") or "").strip()
            details = str(body.get("details") or "").strip()
            if not product or not prompt_name:
                return self._send_json(
                    {"error": "Thiếu tên sản phẩm hoặc prompt"}, status=400
                )
            job = {
                "id": str(len(jobs) + 1),
                "product": product,
                "product_image": _safe_name(body.get("product_image")),
                "character_image": _safe_name(body.get("character_image")),
                "details": details,
                "prompt": prompt_name,
                "prompt_text": _fill_prompt(_read_prompt(prompt_name), product, details),
                "notes": str(body.get("notes") or "").strip(),
                "status": "cho_tao",
                "created_at": datetime.now().isoformat(timespec="seconds"),
            }
            jobs.append(job)
            _write_jobs(jobs)
            return self._send_json(job, status=201)

        if path.startswith("/api/jobs/") and path.endswith("/done"):
            job_id = path.split("/")[3]
            jobs = _read_jobs()
            for job in jobs:
                if job["id"] == job_id:
                    job["status"] = "done"
                    _write_jobs(jobs)
                    return self._send_json(job)
            return self._send_json({"error": "not found"}, status=404)

        if path == "/api/accounts":
            name = _safe_account_name(body.get("name"))
            cookie = str(body.get("cookie") or "").strip()
            proxy = str(body.get("proxy") or "").strip()
            if not name or not cookie:
                return self._send_json(
                    {"error": "Thiếu tên tài khoản hoặc cookie"}, status=400
                )
            try:
                Account, AccountManager, load_cookies = _gateway()
                if not load_cookies(cookie):
                    return self._send_json(
                        {"error": "Cookie rỗng/không parse được"}, status=400
                    )
                mgr = AccountManager()
                acc = Account(name=name, cookie=cookie, proxy=proxy)
                mgr.add(acc)
            except ValueError as e:
                return self._send_json({"error": str(e)}, status=400)
            except Exception as e:
                return self._send_json({"error": f"Không thêm được: {e}"}, status=500)
            return self._send_json(_account_public(acc), status=201)

        if path.startswith("/api/accounts/") and path.endswith("/check"):
            name = _safe_account_name(unquote(path[len("/api/accounts/"):-len("/check")].strip("/")))
            if not name:
                return self._send_json({"error": "not found"}, status=404)
            try:
                # Dùng module login/ (chỉ cần requests) thay vì muse_client
                # (cần websocket/noise) để nút Kiểm tra chạy được ngay cả
                # khi python chạy web chưa cài đủ dependency gateway.
                _, AccountManager, _ = _gateway()
                from gateway.config import load_settings
                from gateway.usage import UsageTracker
                from login.cookie_login import (
                    CookieAccount,
                    build_session,
                    check_login,
                )

                acc = AccountManager().get(name)
                if not acc:
                    return self._send_json({"error": "not found"}, status=404)
                simple = CookieAccount(
                    name=acc.name, cookie=acc.cookie,
                    cookie_file=acc.cookie_file, proxy=acc.proxy,
                )
                login_ok, login_msg = check_login(build_session(simple))
                usage = UsageTracker().remaining(acc, load_settings())
                return self._send_json({
                    "name": name,
                    "login_ok": login_ok,
                    "login_msg": login_msg,
                    "quota_ok": None,
                    "quota_msg": "Không đọc được token/quota qua API (API không công khai) — dùng giới hạn tuần cục bộ thay thế",
                    "week": usage["week"],
                    "videos": f"{usage['videos']}/{usage['max_videos'] if usage['max_videos'] else '∞'}",
                    "minutes": f"{usage['minutes']}/{usage['max_minutes'] if usage['max_minutes'] else '∞'}",
                })
            except Exception as e:
                return self._send_json({"error": f"Kiểm tra lỗi: {e}"}, status=500)

        if path == "/api/concat":
            clips = body.get("clips") or []
            mode = str(body.get("mode") or "concat")
            out_name = _safe_video_name(body.get("output") or "video-ghep.mp4")
            if not out_name or len(clips) < 2:
                return self._send_json(
                    {"error": "Cần ít nhất 2 clip và tên file .mp4"}, status=400
                )
            script = SCRIPTS / ("montage.sh" if mode == "montage" else "concat.sh")
            clip_paths = []
            for name in clips:
                safe = Path(str(name)).name
                target = ROOT / "output" / safe
                if not target.exists() or target.suffix.lower() != ".mp4":
                    return self._send_json(
                        {"error": f"Không thấy clip: {safe}"}, status=400
                    )
                clip_paths.append(str(target))
            out_path = ROOT / "output" / out_name
            try:
                proc = subprocess.run(
                    [str(script), str(out_path)] + clip_paths,
                    capture_output=True, text=True, timeout=600,
                )
            except subprocess.TimeoutExpired:
                return self._send_json({"error": "Ghép quá lâu, thử lại sau"}, status=500)
            if proc.returncode != 0 or not out_path.exists():
                return self._send_json(
                    {"error": f"Ghép lỗi: {proc.stderr.strip()[-300:]}"}, status=500
                )
            return self._send_json(
                {"name": out_name, "size": out_path.stat().st_size}
            )

        return self._send_json({"error": "not found"}, status=404)

    def do_DELETE(self):
        parts = [p for p in urlparse(self.path).path.split("/") if p]
        if len(parts) == 3 and parts[0] == "api" and parts[1] == "accounts":
            name = _safe_account_name(unquote(parts[2]))
            if name:
                try:
                    _, AccountManager, _ = _gateway()
                    if AccountManager().remove(name):
                        return self._send_json({"deleted": name})
                except Exception:
                    pass
            return self._send_json({"error": "not found"}, status=404)
        if len(parts) == 3 and parts[0] == "api" and parts[1] in ("products", "characters"):
            folder = "input" if parts[1] == "products" else "character-reference"
            name = _safe_name(unquote(parts[2]))
            target = ROOT / folder / name if name else None
            if target and target.exists():
                target.unlink()
                return self._send_json({"deleted": name})
        return self._send_json({"error": "not found"}, status=404)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Fashion Affiliate Tool đang chạy: http://{args.host}:{args.port}")
    print("Nhấn Ctrl+C để dừng. Server chỉ nghe trên máy của bạn.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
