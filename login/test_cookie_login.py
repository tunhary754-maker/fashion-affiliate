"""Kiểm chứng cookie_login standalone — CHỈ dùng dữ liệu giả.

Chạy từ bất kỳ thư mục nào (không cần repo automuse-multi):

    python test_cookie_login.py

Không đọc, không chạm tới cookie thật hay file accounts thật nào.
"""

import json
import os
import stat
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import requests  # noqa: E402

from cookie_login import (  # noqa: E402
    CookieAccount,
    MuseLoginError,
    ProxyConfig,
    build_session,
    check_login,
    cookies_to_header,
    fetch_gateway_init,
    load_accounts_file,
    load_cookies,
    parse_cookie_header,
    parse_cookie_json,
    parse_gateway_init,
    parse_netscape_file,
    save_accounts_file,
)

FAKE = 0


def check(name, cond):
    global FAKE
    assert cond, f"FAIL: {name}"
    FAKE += 1
    print(f"  ok: {name}")


class FakeResp:
    def __init__(self, status=200, url="https://muse.ai/", text=""):
        self.status_code = status
        self.url = url
        self.text = text


class FakeSession:
    def __init__(self, mapping, exc_url=None):
        self.mapping = mapping  # url -> FakeResp
        self.exc_url = exc_url

    def get(self, url, timeout=None):
        if self.exc_url and url.endswith(self.exc_url):
            raise requests.RequestException("boom")
        return self.mapping.get(url, FakeResp(404, url, ""))


def gateway_html(init):
    inner = json.dumps({"x": "window.__HATCH_GATEWAY_INIT__=" + json.dumps(init)})
    return "<html><script>self.__next_f.push([1," + json.dumps(inner) + "])</script></html>"


def main():
    print("== parse cookie ==")
    check("header + prefix Cookie:",
          parse_cookie_header("Cookie: a=1; b=2") == {"a": "1", "b": "2"})
    check("trùng khóa giữ bản đầu khác rỗng:",
          parse_cookie_header("hatch_gw=AAA; x=1; hatch_gw=")["hatch_gw"] == "AAA")
    check("trùng khóa bản sau khác rỗng không ghi đè bản đầu rỗng sai:",
          parse_cookie_header("hatch_gw=; hatch_gw=BBB")["hatch_gw"] == "BBB")
    check("json dict:", parse_cookie_json({"a": "1"}) == {"a": "1"})
    check("json list:",
          parse_cookie_json([{"name": "a", "value": "1"}, {"name": "b"}]) == {"a": "1"})
    try:
        parse_cookie_json("nope")
        check("json sai raise", False)
    except ValueError:
        check("json sai raise", True)

    with tempfile.TemporaryDirectory() as td:
        netscape = Path(td) / "cookies.txt"
        netscape.write_text(
            "# Netscape HTTP Cookie File\n"
            ".muse.ai\tTRUE\t/\tFALSE\t0\thatch_sess\tSESS123\n"
            ".muse.ai\tTRUE\t/\tFALSE\t0\thatch_gw\tGW456\n"
            "plainname=plainvalue\n",
            encoding="utf-8",
        )
        check("netscape file:", parse_netscape_file(netscape) == {
            "hatch_sess": "SESS123", "hatch_gw": "GW456", "plainname": "plainvalue"})
        js = Path(td) / "cookies.json"
        js.write_text(json.dumps([{"name": "a", "value": "9"}]), encoding="utf-8")
        check("load_cookies file json:", load_cookies(str(js)) == {"a": "9"})
        check("load_cookies file txt:", load_cookies(str(netscape))["hatch_sess"] == "SESS123")
        check("load_cookies chuỗi thô:", load_cookies("a=1; b=2") == {"a": "1", "b": "2"})
        check("load_cookies chuỗi json:", load_cookies('{"a": "5"}') == {"a": "5"})
        long_str = "a=" + "x" * 5000 + "; b=2"
        check("load_cookies chuỗi dài không crash:", load_cookies(long_str)["b"] == "2")
        check("cookies_to_header:", cookies_to_header({"a": "1", "b": "2"}) == "a=1; b=2")

    print("== proxy ==")
    p = ProxyConfig.parse("http://user:pass@host:8080")
    check("proxy parse:", (p.scheme, p.host, p.port, p.username) == ("http", "host", 8080, "user"))
    check("proxy masked che pass:", p.masked() == "http://user:***@host:8080")
    check("proxy không scheme tự thêm http:", ProxyConfig.parse("host:3128").scheme == "http")
    check("proxy cổng chữ không raise + invalid:", not ProxyConfig.parse("http://host:abc").is_valid())
    check("proxy rỗng invalid:", not ProxyConfig.parse("").is_valid())

    print("== account + session ==")
    acc = CookieAccount(name="t", cookie="a=1; b=2", proxy="http://h:8080")
    check("account.cookies:", acc.cookies() == {"a": "1", "b": "2"})
    check("public_dict che cookie:", acc.public_dict()["cookie"] == "***")
    s = build_session(acc)
    check("session có cookie:", s.cookies.get("a") == "1" and s.cookies.get("b") == "2")
    check("session có proxy:", s.proxies.get("http") == "http://h:8080")
    check("session có UA:", "Chrome" in s.headers.get("User-Agent", ""))

    print("== check_login (fake session) ==")
    big = "x" * 11_000
    ok, msg = check_login(FakeSession({
        "https://muse.ai/": FakeResp(200, "https://muse.ai/", big)}))
    check("login OK qua trang chủ:", ok and "trang chủ" in msg)
    ok, msg = check_login(FakeSession({
        "https://muse.ai/": FakeResp(200, "https://muse.ai/", "nho"),
        "https://muse.ai/api/me": FakeResp(200, "https://muse.ai/api/me", big)}))
    check("login OK qua api/me khi trang chủ nhỏ:", ok and "api/me" in msg)
    ok, msg = check_login(FakeSession({
        "https://muse.ai/": FakeResp(401, "https://muse.ai/", "")}))
    check("401 = hết hạn:", (not ok) and "401" in msg)
    ok, msg = check_login(FakeSession({
        "https://muse.ai/": FakeResp(200, "https://auth.muse.ai/login", big)}))
    check("redirect sang host khác = chưa login:", (not ok) and "auth.muse.ai" in msg)
    ok, msg = check_login(FakeSession({}, exc_url="/"))
    check("lỗi mạng:", (not ok) and "Lỗi mạng" in msg)
    ok, msg = check_login(FakeSession({
        "https://muse.ai/": FakeResp(200, "https://muse.ai/", "nho"),
        "https://muse.ai/api/me": FakeResp(200, "https://muse.ai/api/me", "nho")}))
    check("cả 2 đều nhỏ = fail:", not ok)

    print("== gateway init ==")
    init_full = {
        "version": 1,
        "gatewayUrl": "wss://11111111-2222-3333-4444-555555555555.metaaivm.com/",
        "vmName": "11111111-2222-3333-4444-555555555555",
        "authToken": "s0:fake",
        "noiseNotaryToken": "endorsement.v1.fake",
    }
    parsed = parse_gateway_init(gateway_html(init_full))
    check("parse double-escaped:", parsed["authToken"] == "s0:fake")
    init_no_token = {k: v for k, v in init_full.items() if k != "authToken"}
    parsed2 = parse_gateway_init(gateway_html(init_no_token))
    check("thiếu authToken vẫn parse (fix 2026-10-30):", parsed2["gatewayUrl"].startswith("wss://"))
    try:
        parse_gateway_init(gateway_html({"vmName": "x"}))
        check("thiếu gatewayUrl raise", False)
    except MuseLoginError:
        check("thiếu gatewayUrl raise", True)
    try:
        parse_gateway_init("<html>no init here</html>")
        check("không có blob raise", False)
    except MuseLoginError:
        check("không có blob raise", True)
    fs = FakeSession({"https://muse.ai/": FakeResp(200, "https://muse.ai/", gateway_html(init_full))})
    check("fetch_gateway_init OK:", fetch_gateway_init(fs)["vmName"] == init_full["vmName"])
    fs2 = FakeSession({"https://muse.ai/": FakeResp(200, "https://muse.ai/", "<html>shell</html>")})
    try:
        fetch_gateway_init(fs2)
        check("fetch 200 không blob raise", False)
    except MuseLoginError:
        check("fetch 200 không blob raise", True)
    fs3 = FakeSession({"https://muse.ai/": FakeResp(403, "https://muse.ai/", "")})
    try:
        fetch_gateway_init(fs3)
        check("fetch non-200 raise", False)
    except MuseLoginError:
        check("fetch non-200 raise", True)

    print("== accounts file ==")
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "accounts.json"
        save_accounts_file(p, [CookieAccount(name="a", cookie="x=1"),
                                CookieAccount(name="b", cookie_file="c.txt", proxy="http://h:1")])
        check("file quyền 0600:", stat.S_IMODE(os.stat(p).st_mode) == 0o600)
        loaded = load_accounts_file(p)
        check("load round-trip:", [a.name for a in loaded] == ["a", "b"]
              and loaded[0].cookies() == {"x": "1"})
        p.write_text(json.dumps({"accounts": [{"name": "c", "cookie": "y=2",
                                               "jobs_done": 99, "cooldown_until": 1}]}),
                     encoding="utf-8")
        check("trường lạ bị bỏ qua:", load_accounts_file(p)[0].name == "c")

    print(f"\nTẤT CẢ {FAKE} CHECK PASS (dữ liệu giả, không chạm cookie thật).")


if __name__ == "__main__":
    main()
