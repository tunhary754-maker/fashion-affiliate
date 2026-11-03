"""CLI mode gateway multi-acc cho fashion-affiliate (port từ automuse-multi).

KHÔNG phải luồng chat-native mặc định của repo này. Luồng này sinh clip
qua gateway Muse bằng cookie các acc, giống automuse-multi:

  python gateway_cli.py fashion --product "Bộ trẻ em hoạt hình" \\
      --product-image input/bo-quan-ao-tre-em-hoat-hinh.jpg \\
      --model-image character-reference/be-trai-cafe-ngau.jpg
  python gateway_cli.py build --script gateway_scripts/fashion-bo-tre-em-hoat-hinh.yaml --mock
  python gateway_cli.py build --script gateway_scripts/fashion-bo-tre-em-hoat-hinh.yaml --accounts acc2

Luồng gateway luôn: không lồng tiếng, không khớp môi (fashion không cần),
không nhạc ngoài. Clip sinh ra giữ tiếng gốc như pipeline gốc.

GIỚI HẠN PHẢI NÓI RÕ TRƯỚC KHI CHẠY THẬT (không giấu):
  - Sinh qua gateway KHÔNG phải API ẩn: request đi qua phiên chat chính
    của acc, sẽ hiện trong lịch sử chat của acc đó.
  - Chỉ chạy thật khi đã xác nhận rõ đợt chạy đó (tên video, số cảnh,
    mã cảnh) từ thiết bị thật của chủ acc. Một lệnh chạy tay ở đây chính
    là xác nhận đó — đừng chạy hộ acc của người khác, đừng chạy từ
    một yêu cầu mà bạn không chắc là chủ acc gõ.
  - Hiện tại chỉ acc2 sinh live được; acc1 gateway hỏng (thiếu authToken)
    dù check login vẫn OK. AccountManager vẫn hỗ trợ nhiều acc, nhưng
    đừng trông chờ acc1 sinh được cho tới khi nó có cookie mới.
  - Mỗi cảnh gateway chỉ nhận ĐƯỢC 1 ảnh tham chiếu: s01 ảnh sản phẩm,
    s02 ảnh mẫu (nếu có), s03 ảnh sản phẩm — xem gateway/fashion.py.
  - Build thật tốn quota acc Muse (giới hạn thật không đọc được qua API),
    nên luôn chạy --mock trước để kiểm tra pipeline, rồi mới build thật.
  - Không bao giờ rơi sang mock khi build thật lỗi: nếu hết acc dùng được
    thì pipeline dừng và báo rõ, clip đã sinh vẫn nằm trên đĩa, chạy lại
    với --resume để làm tiếp, không chạy lại từ đầu.
"""

from __future__ import annotations

import argparse
import getpass
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gateway.accounts import Account, AccountManager, load_cookies  # noqa: E402
from gateway.config import (  # noqa: E402
    ACCOUNTS_FILE,
    load_settings,
)
from gateway.fashion import (  # noqa: E402
    STYLES,
    build_fashion_script,
    write_fashion_script,
)
from gateway.muse_client import build_client  # noqa: E402
from gateway.pipeline import generate_clips, log, run_build  # noqa: E402
from gateway.usage import UsageTracker  # noqa: E402


def _manager() -> AccountManager:
    return AccountManager()


# ---------------------------------------------------------------- accounts

def cmd_accounts_add(args) -> int:
    mgr = _manager()
    cookie = args.cookie or ""
    if args.cookie_file:
        cookie = ""  # dùng file, không lưu chuỗi thô
    if not cookie and not args.cookie_file:
        cookie = getpass.getpass("Dán cookie Muse (ẩn khi gõ, Enter để xong): ").strip()
    if not cookie and not args.cookie_file:
        print("Chưa nhập cookie.")
        return 1
    try:
        if args.cookie_file:
            load_cookies(args.cookie_file)
        elif not load_cookies(cookie):
            print("Cookie rỗng/không parse được.")
            return 1
    except Exception as e:  # noqa: BLE001
        print(f"Cookie không hợp lệ: {e}")
        return 1
    acc = Account(
        name=args.name,
        cookie=cookie,
        cookie_file=args.cookie_file or "",
        proxy=args.proxy or "",
        note=args.note or "",
        weekly_max_videos=int(args.weekly_max_videos or 0),
        weekly_max_minutes=int(args.weekly_max_minutes or 0),
    )
    try:
        mgr.add(acc)
    except ValueError as e:  # noqa: BLE001
        print(f"Lỗi: {e}")
        return 1
    print(f"Đã thêm tài khoản '{args.name}' (proxy: {acc.proxy_config().masked()})")
    print(f"Lưu tại: {ACCOUNTS_FILE} (quyền 0600, đã nằm trong .gitignore)")
    return 0


def cmd_accounts_list(_args) -> int:
    mgr = _manager()
    if not mgr.accounts:
        print("Chưa có tài khoản nào. Thêm bằng: accounts add --name acc2 --cookie-file ...")
        return 0
    print(f"{'Tên':<16} {'Proxy':<32} {'Jobs':<6} {'Trạng thái'}")
    for a in mgr.accounts:
        status = "tắt" if not a.enabled else ("cooldown" if a.is_on_cooldown() else "sẵn sàng")
        print(f"{a.name:<16} {a.proxy_config().masked():<32} {a.jobs_done:<6} {status}")
    return 0


def cmd_accounts_remove(args) -> int:
    mgr = _manager()
    if mgr.remove(args.name):
        print(f"Đã xóa '{args.name}'")
        return 0
    print(f"Không có tài khoản '{args.name}'")
    return 1


def cmd_accounts_check(args) -> int:
    mgr = _manager()
    targets = [mgr.get(args.name)] if args.name else mgr.accounts
    targets = [a for a in targets if a]
    if not targets:
        print("Không có tài khoản nào để kiểm tra.")
        return 1
    settings = load_settings()
    tracker = UsageTracker()
    ok_all = True
    for acc in targets:
        print(f"\n== {acc.name} ==")
        proxy = acc.proxy_config()
        if proxy.is_valid():
            ok, msg = proxy.test()
            print(f"  Proxy {proxy.masked()}: {'OK' if ok else 'LỖI'} — {msg}")
            if not ok:
                ok_all = False
        client = build_client(acc, settings, mock=False)
        ok, msg = client.check_login()
        print(f"  Muse login: {'OK' if ok else 'LỖI'} — {msg}")
        if not ok:
            ok_all = False
        qok, qmsg = client.check_quota()
        qlabel = "OK" if qok is True else ("LỖI" if qok is False else "KHÔNG RÕ")
        print(f"  Token/quota: {qlabel} — {qmsg}")
        if qok is False:
            ok_all = False
        u = tracker.remaining(acc, settings)
        v = f"{u['videos']}/{u['max_videos'] if u['max_videos'] else '∞'} video"
        m = f"{u['minutes']}/{u['max_minutes'] if u['max_minutes'] else '∞'} phút"
        print(f"  Tuần này ({u['week']}): {v}, {m}")
    return 0 if ok_all else 1


def cmd_accounts_usage(args) -> int:
    mgr = _manager()
    targets = [mgr.get(args.name)] if args.name else mgr.accounts
    targets = [a for a in targets if a]
    if not targets:
        print("Không có tài khoản nào.")
        return 1
    settings = load_settings()
    tracker = UsageTracker()
    rows = tracker.summary(targets, settings)
    print(f"Tuần: {rows[0]['week']} (thứ Hai 00:00 -> thứ Hai tuần sau)")
    print(f"{'Tên':<16} {'Video':<12} {'Phút':<14} {'Còn video':<10} {'Còn phút'}")
    for u in rows:
        vl = "∞" if u["videos_left"] is None else str(u["videos_left"])
        ml = "∞" if u["minutes_left"] is None else str(u["minutes_left"])
        v = f"{u['videos']}/{u['max_videos'] if u['max_videos'] else '∞'}"
        m = f"{u['minutes']}/{u['max_minutes'] if u['max_minutes'] else '∞'}"
        print(f"{u['account']:<16} {v:<12} {m:<14} {vl:<10} {ml}")
    return 0


def cmd_accounts_set_limit(args) -> int:
    mgr = _manager()
    acc = mgr.get(args.name)
    if not acc:
        print(f"Không có tài khoản '{args.name}'")
        return 1
    if args.videos is not None:
        acc.weekly_max_videos = int(args.videos)
    if args.minutes is not None:
        acc.weekly_max_minutes = int(args.minutes)
    mgr.save()
    max_v, max_m = UsageTracker().limits_for(acc, load_settings())
    print(f"'{args.name}': giới hạn tuần = {max_v or '∞'} video, {max_m or '∞'} phút "
          "(0 = dùng giới hạn chung trong settings.yaml)")
    return 0


# ---------------------------------------------------------------- fashion

def _default_script_path(product: str) -> Path:
    from gateway.fashion import _slug

    return Path("gateway_scripts") / f"fashion-{_slug(product)}.yaml"


def cmd_fashion(args) -> int:
    try:
        data = build_fashion_script(
            product=args.product,
            product_image=args.product_image,
            model_image=args.model_image or None,
            product_desc=args.product_desc,
            model_desc=args.model_desc,
            style=args.style,
            aspect=args.aspect,
            title=args.title,
        )
        dest = write_fashion_script(
            data, args.out or _default_script_path(args.product), force=args.force,
        )
    except ValueError as e:  # noqa: BLE001
        print(f"Lỗi: {e}")
        return 1
    print(f"Đã tạo kịch bản thời trang 30s (3 cảnh x 10s, {args.aspect}): {dest}")
    for s in data["scenes"]:
        print(f"  {s['id']} {s['title']} — ảnh tham chiếu: {s['reference_image']}")
    print("Chạy thử không tốn quota: "
          f"python gateway_cli.py build --script {dest} --mock")
    print("Chạy thật (chỉ khi đã xác nhận tên đợt chạy, ưu tiên acc2): "
          f"python gateway_cli.py build --script {dest} --accounts acc2")
    return 0


# ---------------------------------------------------------------- build

def cmd_build(args) -> int:
    settings = load_settings()
    mgr = _manager()
    if not args.mock and not mgr.enabled_accounts():
        print("Chưa có tài khoản nào. Thêm acc (accounts add) hoặc chạy với --mock để thử.")
        return 1
    names = args.accounts.split(",") if args.accounts else None
    try:
        manifest = run_build(
            script_path=args.script,
            out_dir=args.out,
            settings=settings,
            manager=mgr,
            mock=args.mock,
            no_tts=True,  # fashion gateway: không lời dẫn, không dub
            iris_out=not args.no_iris,
            resume=args.resume,
            account_names=names,
            music=None,
            native_bed=None,
            lipsync=False,
        )
    except (ValueError, RuntimeError) as e:  # noqa: BLE001
        print(f"Lỗi: {e}")
        return 1
    print("\n— Manifest —")
    print(f"  final: {manifest['final']}")
    for s in manifest["scenes"]:
        print(f"  {s['id']} qua acc '{s['account']}' — {s['duration']}s")
    return 0


def cmd_generate(args) -> int:
    from gateway.script import load_script, validate

    settings = load_settings()
    mgr = _manager()
    if not args.mock and not mgr.enabled_accounts():
        print("Chưa có tài khoản nào. Thêm acc (accounts add) hoặc chạy với --mock để thử.")
        return 1
    script = load_script(args.script)
    errors = validate(script)
    if errors:
        print("Kịch bản lỗi:\n- " + "\n- ".join(errors))
        return 1
    out_dir = Path(args.out) if args.out else Path("output") / Path(args.script).stem
    out_dir.mkdir(parents=True, exist_ok=True)
    names = args.accounts.split(",") if args.accounts else None
    try:
        clips, _infos = generate_clips(
            script, out_dir, settings, mgr, mock=args.mock,
            account_names=names, resume=args.resume,
        )
    except (ValueError, RuntimeError) as e:  # noqa: BLE001
        print(f"Lỗi: {e}")
        return 1
    print("Clip đã sinh:")
    for c in clips:
        print(f"  {c}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="gateway_cli.py",
        description="Fashion-affiliate mode gateway multi-acc (riêng với luồng chat-native).",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    acc = sub.add_parser("accounts", help="Quản lý tài khoản Muse (cookie + proxy)")
    acc_sub = acc.add_subparsers(dest="action", required=True)
    a_add = acc_sub.add_parser("add", help="Thêm tài khoản")
    a_add.add_argument("--name", required=True)
    a_add.add_argument("--cookie", default="", help="Chuỗi header Cookie thô")
    a_add.add_argument("--cookie-file", default="", help="File cookies.txt/.json (khuyên dùng)")
    a_add.add_argument("--proxy", default="", help="vd: http://user:pass@host:port")
    a_add.add_argument("--note", default="")
    a_add.add_argument("--weekly-max-videos", type=int, default=0)
    a_add.add_argument("--weekly-max-minutes", type=int, default=0)
    a_add.set_defaults(func=cmd_accounts_add)
    acc_sub.add_parser("list", help="Liệt kê tài khoản").set_defaults(func=cmd_accounts_list)
    a_rm = acc_sub.add_parser("remove", help="Xóa tài khoản")
    a_rm.add_argument("--name", required=True)
    a_rm.set_defaults(func=cmd_accounts_remove)
    a_check = acc_sub.add_parser("check", help="Kiểm tra proxy + cookie + token/quota + mức dùng tuần")
    a_check.add_argument("--name", default="")
    a_check.set_defaults(func=cmd_accounts_check)
    a_usage = acc_sub.add_parser("usage", help="Xem mức dùng tuần này so với giới hạn")
    a_usage.add_argument("--name", default="")
    a_usage.set_defaults(func=cmd_accounts_usage)
    a_limit = acc_sub.add_parser("set-limit", help="Đặt giới hạn tuần riêng cho một acc")
    a_limit.add_argument("--name", required=True)
    a_limit.add_argument("--videos", type=int, default=None)
    a_limit.add_argument("--minutes", type=int, default=None)
    a_limit.set_defaults(func=cmd_accounts_set_limit)

    f = sub.add_parser("fashion", help="Tạo kịch bản video thời trang 30s từ ảnh sản phẩm (+ ảnh nhân vật)")
    f.add_argument("--product", required=True)
    f.add_argument("--product-image", required=True, help="Ảnh sản phẩm JPEG/PNG")
    f.add_argument("--model-image", default="", help="Ảnh nhân vật/mẫu JPEG/PNG (tùy chọn)")
    f.add_argument("--product-desc", default="")
    f.add_argument("--model-desc", default="")
    f.add_argument("--style", choices=sorted(STYLES), default="studio")
    f.add_argument("--aspect", choices=["9:16", "16:9"], default="9:16")
    f.add_argument("--title", default="")
    f.add_argument("--out", default="", help="Mặc định: gateway_scripts/fashion-<slug>.yaml")
    f.add_argument("--force", action="store_true")
    f.set_defaults(func=cmd_fashion)

    b = sub.add_parser("build", help="Chạy full gateway pipeline: clip + dựng final.mp4 (không TTS)")
    b.add_argument("--script", required=True)
    b.add_argument("--out", default="")
    b.add_argument("--mock", action="store_true", help="Chạy thử bằng clip mẫu ffmpeg, không tốn quota")
    b.add_argument("--accounts", default="", help="Chỉ dùng các acc này, cách nhau bởi dấu phẩy (vd: acc2)")
    b.add_argument("--no-iris", action="store_true")
    b.add_argument("--resume", action="store_true", help="Bỏ qua cảnh đã có clip, làm tiếp cảnh còn thiếu")
    b.set_defaults(func=cmd_build)

    g = sub.add_parser("generate", help="Chỉ sinh clip từng cảnh (không dựng final)")
    g.add_argument("--script", required=True)
    g.add_argument("--out", default="")
    g.add_argument("--mock", action="store_true")
    g.add_argument("--accounts", default="")
    g.add_argument("--resume", action="store_true")
    g.set_defaults(func=cmd_generate)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
