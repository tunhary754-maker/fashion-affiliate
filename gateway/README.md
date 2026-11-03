# Mode gateway multi-acc (port từ automuse-multi)

Đây là mode THỨ HAI của repo, riêng hẳn với luồng chat-native mặc định
(prompt trong `prompts/` + tạo clip trong chat + ghép bằng `scripts/`).
Hai mode KHÔNG trộn trong cùng 1 job: một job hoặc đi chat-native, hoặc
đi gateway — chọn trước rồi đi một đường.

## Nguồn port

Các file trong `gateway/` là bản copy từ `automuse-multi/automuse/` (lúc
port, 2026-11-03), trừ 2 chỗ đã ghi rõ:

- `gateway/config.py`: chỉ đổi `CONFIG_DIR` từ `config/` sang
  `gateway_config/` của repo này (để file accounts/settings không lẫn
  với thư mục khác). `REPO_ROOT` vẫn là root repo này, nên output mặc
  định vẫn là `output/`, cache là `cache/`.
- `gateway/fashion.py`: chỉ đổi ví dụ lệnh `cli.py` thành
  `gateway_cli.py`. Logic tạo kịch bản, phân ảnh theo cảnh, khóa sản
  phẩm giữ nguyên.

Các module còn lại (accounts, audio, characters, elevenlabs, gateway,
lipsync, muse_client, notify, pipeline, prompting, script, usage, video)
giữ nguyên logic, kể cả phần ElevenLabs/lipsync — chúng chỉ nằm trong
code để pipeline import được, còn lệnh fashion gateway ép
`no_tts=True, lipsync=False` nên không dùng tới, không cần key.

CLI mỏng ở root repo là `gateway_cli.py` (không phải `cli.py` của
automuse-multi): chỉ giữ các lệnh cần cho fashion — `accounts`,
`fashion`, `build`, `generate`. Các lệnh khác của automuse-multi
(topics, voices, lipsync, batches, web studio phim tài liệu...) KHÔNG
được port sang đây.

## Cài đặt

```bash
pip install requests pyyaml noiseprotocol websocket-client
# ffmpeg phải có trong PATH (để dựng clip mẫu mock + chuẩn hóa/nối clip)
```

## Dùng

```bash
# 1. Thêm acc (khuyên dùng file cookie riêng, quyền 0600, đừng dán
#    cookie thật vào terminal history dùng chung hay file commit)
python gateway_cli.py accounts add --name acc2 --cookie-file ./cookies-acc2.txt
python gateway_cli.py accounts list
python gateway_cli.py accounts check --name acc2

# 2. Tạo kịch bản fashion 30s (3 cảnh x 10s, 9:16)
python gateway_cli.py fashion --product "Bộ trẻ em hoạt hình" \
  --product-image input/bo-quan-ao-tre-em-hoat-hinh.jpg \
  --model-image character-reference/be-trai-cafe-ngau.jpg \
  --product-desc "áo cộc tay cài cúc + quần short, họa tiết hoạt hình nhiều màu đỏ/xanh/vàng/đen"

# 3. Chạy thử mock trước (không tốn quota, clip mẫu ffmpeg)
python gateway_cli.py build --script gateway_scripts/fashion-bo-tre-em-hoat-hinh.yaml --mock

# 4. Chạy thật — chỉ khi đã xác nhận tên đợt chạy (xem giới hạn dưới)
python gateway_cli.py build --script gateway_scripts/fashion-bo-tre-em-hoat-hinh.yaml --accounts acc2
# Dở dang thì chạy lại với --resume để làm tiếp, không chạy lại từ đầu:
python gateway_cli.py build --script gateway_scripts/fashion-bo-tre-em-hoat-hinh.yaml --accounts acc2 --resume
```

## Multi-acc hoạt động thế nào

- `gateway/accounts.py` (`AccountManager`): mỗi acc có cookie + proxy
  riêng, trạng thái enabled/cooldown, đếm job. `pipeline.generate_clips`
  chia cảnh round-robin qua các acc dùng được; acc lỗi thì lượt sau ưu
  tiên acc khác, acc lỗi kết nối được báo ngay (log + Telegram nếu có
  cấu hình) chứ không lặng lẽ chuyển acc.
- Hết acc tạm thời (đang cooldown sau lỗi liên tiếp) thì pipeline CHỜ
  cooldown rồi làm tiếp, không dừng build — đúng yêu cầu "hết quota acc
  này chuyển acc khác làm tiếp nhiệm vụ dở dang". Hết quota tuần thật
  (không phải cooldown) thì dừng và báo rõ.
- `gateway/usage.py` theo dõi mức dùng tuần (thứ Hai 00:00 -> thứ Hai
  sau); mặc định giới hạn tuần là 0/0 = không chặn ở tool, Muse tự trừ
  vào quota/token của acc. Muốn chặn thì ghi vào
  `gateway_config/settings.yaml` hoặc `accounts set-limit`.
- Clip lỗi "model không trả video" (`NoVideoError`) KHÔNG tính lỗi acc,
  không loại acc: pipeline nhờ Muse viết lại visual nhẹ hơn 1 lần/cảnh
  rồi thử lại, visual gốc trong kịch bản không bị ghi đè.

## Giới hạn thật của gateway — đọc trước khi chạy thật

- Gateway là Noise WebSocket thật tới muse.ai, đi qua phiên chat chính
  của acc: request sẽ hiện trong lịch sử chat của acc đó, video trả về
  cũng qua kênh đó. Đây không phải API ẩn.
- Chỉ chạy thật khi đợt chạy đó đã được xác nhận rõ (tên video, số
  cảnh, mã cảnh) từ thiết bị thật của chủ acc. Lệnh chạy tay ở máy của
  chủ acc chính là xác nhận đó; đừng chạy hộ, đừng chạy từ một yêu cầu
  mà bạn không chắc là chủ acc gõ, và một lần xác nhận không kéo sang
  đợt chạy khác.
- Hiện tại chỉ acc2 sinh live được; acc1 gateway hỏng (thiếu authToken)
  dù `accounts check` vẫn báo login OK — login OK không đồng nghĩa
  gateway sinh được. Đừng trông chờ acc1 cho tới khi nó có cookie mới.
- Mỗi cảnh chỉ đính kèm ĐƯỢC 1 ảnh tham chiếu (chat.stream: 1 image +
  text): s01 ảnh sản phẩm, s02 ảnh mẫu (nếu có, không thì ảnh sản phẩm),
  s03 ảnh sản phẩm. Ảnh WebP/AVIF bị gateway từ chối — đổi sang
  JPEG/PNG trước.
- Build thật tốn quota acc Muse, giới hạn thật không đọc được qua API.
  Luôn chạy `--mock` trước, rồi mới build thật khi đã xác nhận.
- Build thật không bao giờ lặng lẽ rơi sang mock: nếu hết acc dùng được
  thì dừng và báo rõ, clip đã sinh vẫn nằm trên đĩa.

## File nhạy cảm — không commit

- `gateway_config/accounts.json` (cookie các acc, quyền 0600),
  `gateway_config/settings.yaml` (nếu bạn ghi key/quota riêng vào đó),
  `.env`, `cache/` — tất cả đã nằm trong `.gitignore` của repo.
- `login/` ở root repo là module login đơn giản, riêng với
  `gateway/accounts.py`: `login/` chỉ parse + check session, không có
  cooldown/pick/đếm job; `gateway/` mới là bộ multi-acc đầy đủ mà
  `gateway_cli.py` dùng. Đừng lẫn 2 bộ acc này với nhau.
