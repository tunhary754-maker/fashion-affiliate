"""Ví dụ dùng cookie_login + CLI kiểm tra nhanh một acc.

Chạy (không cần repo automuse-multi, chỉ cần requests):

    pip install requests
    python example.py --cookies "hatch_sess=abc; hatch_gw=xyz"
    python example.py --cookies-file ./cookies.txt
    python example.py --cookies-file ./cookies.json --proxy http://user:pass@host:8080

KHÔNG dán cookie thật vào code, terminal history dùng chung, hay file
commit lên git. Cách an toàn nhất: để cookie trong file riêng (0600)
rồi truyền --cookies-file.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from cookie_login import (  # noqa: E402
    CookieAccount,
    build_session,
    check_login,
    fetch_gateway_init,
)


def main() -> int:
    ap = argparse.ArgumentParser(description="Kiểm tra login Muse bằng cookies")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--cookies", help="Chuỗi header Cookie thô")
    g.add_argument("--cookies-file", help="File cookies.txt (Netscape) hoặc .json")
    ap.add_argument("--proxy", default="", help="vd: http://user:pass@host:port")
    ap.add_argument("--base-url", default="https://muse.ai")
    ap.add_argument("--name", default="acc1")
    args = ap.parse_args()

    acc = CookieAccount(
        name=args.name,
        cookie=args.cookies or "",
        cookie_file=args.cookies_file or "",
        proxy=args.proxy,
    )
    cookies = acc.cookies()
    print(f"acc: {acc.name} | parse được {len(cookies)} cookie | proxy: {acc.proxy_config().masked()}")
    if not cookies:
        print("Cookie rỗng — kiểm tra lại chuỗi/file cookie.")
        return 2

    session = build_session(acc)
    ok, msg = check_login(session, args.base_url)
    print(f"check_login: {msg}")
    if not ok:
        return 1

    try:
        init = fetch_gateway_init(session, args.base_url)
        print(
            "gateway init: OK | gatewayUrl: "
            f"{init.get('gatewayUrl', '')[:60]}... | "
            f"vmName: {init.get('vmName', '')[:8]}... | "
            f"có authToken: {bool(init.get('authToken'))}"
        )
    except Exception as e:  # noqa: BLE001 - demo in lỗi gọn
        print(f"gateway init: FAIL ({e})")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
