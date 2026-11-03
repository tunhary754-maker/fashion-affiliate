# cookie-login — Login Muse bằng cookies (module tùy chọn trong repo này)

Module này là bản tách riêng phần logic login bằng cookies từ
`automuse-multi`, được tích hợp vào repo fashion-affiliate để dùng khi cần
đăng nhập bằng cookie cho tool khác / tầng gateway. Chỉ phụ thuộc gói
`requests`.

Lưu ý ranh giới: luồng tạo video mặc định của repo này vẫn là chat-native
(đoạn trên) và KHÔNG dùng module này. Module login chỉ kiểm tra session
và lấy gateway init — nó không sinh video, không có Noise handshake,
không có round-robin/cooldown/đếm job. Đừng trộn 2 luồng trong cùng 1 job
khi chưa quyết rõ job đó đi đường nào.

```bash
pip install requests
python example.py --cookies-file ./cookies.txt
```

## Gồm những gì

| Hàm | Việc |
|---|---|
| `parse_cookie_header` | Chuỗi header `a=1; b=2` (bỏ `Cookie:` nếu có; khóa trùng giữ bản đầu khác rỗng) |
| `parse_netscape_file` | File `cookies.txt` chuẩn Netscape (7 cột, tab-separated) |
| `parse_cookie_json` | JSON export: `[{name, value}]` hoặc `{name: value}` |
| `load_cookies` | Tự nhận diện: chuỗi thô / chuỗi JSON / đường dẫn file (tránh crash với chuỗi dài) |
| `cookies_to_header` | Dict cookie → chuỗi header |
| `ProxyConfig` | Parse proxy `http/https/socks5`, `is_valid`, `masked` (che mật khẩu), `test` |
| `CookieAccount` | Một acc: tên + cookie/chuỗi hoặc file + proxy (không đếm job, không cooldown) |
| `load/save_accounts_file` | File accounts JSON, ghi quyền 0600 |
| `build_session` | `requests.Session` đã gắn header, cookie, proxy |
| `check_login` | Phép thử sống/chết: GET trang chủ rồi `/api/me` |
| `parse/fetch_gateway_init` | Parse `window.__HATCH_GATEWAY_INIT__` từ trang chủ |

## Logic `check_login` (đã xác minh bằng thử nghiệm thật 2026-10-26)

- Cookie sống → GET trang chủ trả 200, ở đúng host `muse.ai`, trang app đầy đủ (>10KB).
- Cookie chết/giả → redirect sang `auth.muse.ai` (400) hoặc 401/403.
- **Không dùng `/api/auth/session` làm phép thử**: nó trả 401 ngay cả khi cookie còn sống.
- Phép thử chính là GET trang chủ; `/api/me` là phép thử phụ.
- Lưu ý: đây chỉ chứng minh session web còn sống, không đảm bảo endpoint sinh video sẽ chấp nhận cookie.

## Logic `parse_gateway_init` (bài học 2026-10-30)

- Blob nằm trong RSC payload bị JSON-escape 2 lớp → gỡ escape lặp rồi quét ngoặc cân bằng.
- Chỉ `gatewayUrl` + `vmName` là bắt buộc. `authToken` thiếu/rỗng **không** fail — tầng Noise sẽ refresh sau. Fail cứng ở đây từng chặn mất đường refresh đã có sẵn.
- Trang chủ trả 200 nhưng không có blob = phiên đã chết (server trả trang shell thay vì redirect) → raise lỗi, đừng tưởng là login OK.

## Không gồm (thuộc tầng khác)

- Noise WebSocket handshake, `chat.stream`/`subscribe`, sinh video.
- Round-robin chọn acc, cooldown, đếm job, UsageTracker.
- Làm mới authToken (`POST /api/hatch/token` với `{vmAddress, vmName}`): khi init thiếu authToken, tầng Noise tự gọi refresh này; bản này dừng ở "lấy được init".

## Bảo mật

- Không hardcode cookie thật vào code, không commit file chứa cookie thật.
- File accounts ghi quyền 0600. Khi in/log acc, dùng `public_dict()` (cookie che `***`, proxy che mật khẩu).
- Cookie thật chỉ nạp từ file riêng hoặc biến môi trường lúc chạy.

## Kiểm chứng

```bash
python test_cookie_login.py   # chỉ dùng dữ liệu giả, không chạm cookie thật
```
