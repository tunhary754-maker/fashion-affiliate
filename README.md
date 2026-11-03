# Fashion Affiliate Video Tool — Video sản phẩm affiliate cho TikTok và Facebook

Tool này dùng để làm video giới thiệu sản phẩm từ ảnh sản phẩm do bạn gửi,
dạng dọc 9:16, đăng TikTok và Facebook Reels kèm link affiliate.

Luồng tạo video mặc định không dùng login bằng cookie, không gọi API nội
bộ của bất kỳ nền tảng nào. Video được tạo trong chat với Muse (ảnh nhân
vật trước, ảnh sản phẩm sau, rồi đến văn bản prompt), sau đó ghép bằng
ffmpeg trong repo này. Module login bằng cookie là phần tùy chọn riêng
trong `login/` (xem mục dưới), không làm thay đổi luồng mặc định này.

Skill đầy đủ nằm ở `~/workspace/custom-skills/fashion-affiliate/SKILL.md`.
Mô hình theo repo công khai `charlotteh618/tao-video-thoi-trang-ai`
(Aff Video Tool): cùng 7 mẫu prompt, cùng luồng ảnh nhân vật chuẩn,
cùng script ghép — viết lại cho chat này, không copy nguyên văn repo đó.

## Thể loại chính

- Quần áo bộ trẻ em đời thường (thể loại chính của repo gốc).
- Mẫu mặc sản phẩm, di chuyển tự nhiên trong đời sống hàng ngày.
- Studio cao cấp, boutique, flat-lay, góc nhà, móc treo trong cửa hàng.
- Nếu sản phẩm của bạn là đồ người lớn, chỉ cần đổi phần mô tả mẫu trong
  prompt, giữ nguyên mọi quy tắc còn lại.

## Quy tắc bắt buộc cho mọi video

- Giữ nguyên tuyệt đối hình ảnh sản phẩm trong ảnh tham chiếu: không đổi
  màu sắc, kiểu dáng, cổ áo, vị trí và hình dạng logo, họa tiết hay chi
  tiết khác.
- Không thêm phụ đề, không thêm chữ trong video, không thêm lời thoại hay
  thuyết minh, trừ khi bạn dặn cụ thể.
- Dạng dọc 9:16.
- Trong một video, chỉ dùng một nhân vật duy nhất xuyên suốt các cảnh.

## Giao diện web quản lý (Web Studio)

Repo có sẵn giao diện web quản lý, chỉ chạy trên máy của bạn, không có
đăng nhập, không gửi cookie hay key:

```
python3 web/server.py
python3 web/server.py --port 8080
```

Mở: http://127.0.0.1:8080

Các tab trong giao diện:

- **Tổng quan** — số prompt, số job, số job đã xong, số video kết quả,
  số ảnh nhân vật, và quy tắc bắt buộc.
- **Tạo video** — tải ảnh sản phẩm lên ngay trên giao diện (khung tải ảnh,
  kéo thả được, lưu vào `input/`), bấm vào ảnh để chọn cho job, tải và
  chọn ảnh nhân vật, rồi điền tên sản phẩm, chi tiết sản phẩm, chọn
  prompt, tạo job. Sau đó copy prompt của job đó vào chat với Muse, kèm
  ảnh nhân vật trước, ảnh sản phẩm sau, để tạo video.
- **Nhân vật** — tải ảnh nhân vật chuẩn lên ngay trên giao diện (lưu vào
  `character-reference/`), xem trước và xoá ảnh ngay tại đó.
- **Kết quả** — xem trước và tải video trong `output/`.
- **Ghép clip** — bấm chọn các clip trong `output/` theo đúng thứ tự,
  chọn ghép nguyên hoặc montage, bấm ghép là có video cuối trong
  `output/`.

Lưu ý: giao diện này quản lý job, prompt và kết quả. Nó không tự tạo video
bằng API ngoài, và không dùng cookie đăng nhập của bất kỳ nền tảng nào.
Video vẫn được tạo trong chat với Muse, rồi ghép ở đây.

## Login bằng cookie (module tùy chọn, thư mục `login/`)

Nếu bạn cần đăng nhập Muse bằng cookie cho tool khác / tầng gateway, dùng
module tách riêng trong `login/`, chỉ phụ thuộc gói `requests`, không
import gì từ repo automuse-multi:

```
pip install requests
python login/example.py --cookies-file ./cookies.txt
python login/test_cookie_login.py   # chỉ dùng dữ liệu giả, không chạm cookie thật
```

Module này gồm: parse cookie 3 dạng (header, cookies.txt Netscape, JSON)
+ proxy riêng từng acc, `build_session` + `check_login` (GET trang chủ
rồi `/api/me`; không dùng `/api/auth/session` làm phép thử vì nó trả 401
ngay cả khi cookie còn sống), và `parse/fetch_gateway_init` (chỉ
`gatewayUrl` + `vmName` bắt buộc, thiếu `authToken` vẫn parse được).

Nó KHÔNG gồm: Noise handshake, `chat.stream`/`subscribe`, sinh video,
round-robin/cooldown/đếm job, làm mới authToken. Nói cách khác, login
được không có nghĩa là sinh được video — đó là tầng khác. Chi tiết đầy
đủ trong `login/README.md`.

## Mode gateway multi-acc (tùy chọn, riêng với luồng mặc định)

Ngoài luồng chat-native trên, repo có thêm mode gateway port từ
automuse-multi, dùng khi bạn muốn sinh clip thẳng bằng cookie nhiều acc
thay vì tạo clip trong chat. Hai mode không trộn trong cùng 1 job.

```
pip install requests pyyaml noiseprotocol websocket-client
python gateway_cli.py accounts add --name acc2 --cookie-file ./cookies-acc2.txt
python gateway_cli.py fashion --product "Bộ trẻ em hoạt hình" \
  --product-image input/bo-quan-ao-tre-em-hoat-hinh.jpg \
  --model-image character-reference/be-trai-cafe-ngau.jpg
python gateway_cli.py build --script gateway_scripts/fashion-bo-tre-em-hoat-hinh.yaml --mock
python gateway_cli.py build --script gateway_scripts/fashion-bo-tre-em-hoat-hinh.yaml --accounts acc2
```

Code ở `gateway/` + CLI `gateway_cli.py`, chi tiết đầy đủ (multi-acc
round-robin/cooldown/failover, giới hạn gateway, file nhạy cảm) trong
`gateway/README.md`. Tóm tắt giới hạn: gateway đi qua phiên chat chính
của acc nên request hiện trong lịch sử chat; chỉ chạy thật khi đã xác
nhận rõ đợt chạy từ thiết bị thật của chủ acc; hiện tại chỉ acc2 sinh
live được, acc1 gateway hỏng dù check login vẫn OK; mỗi cảnh chỉ nhận
1 ảnh tham chiếu; luôn chạy `--mock` trước khi chạy thật.

## Cách dùng

1. Bỏ ảnh sản phẩm vào `input/` (ví dụ `input/product.png`).
2. Bỏ ảnh nhân vật chuẩn của kênh vào `character-reference/` (ví dụ
   `character-reference/character.png`). Nếu chưa có ảnh nhân vật, tạo
   cảnh đầu tiên rồi trích một khung hình rõ mặt làm ảnh nhân vật chuẩn,
   sau đó dùng ảnh đó cho mọi cảnh sau.
3. Chọn một prompt trong `prompts/`, thay đúng tên sản phẩm, cổ áo, logo
   và chi tiết trong ảnh của bạn.
4. Tạo từng đoạn video trong chat với Muse, dùng ảnh nhân vật trước, ảnh
   sản phẩm sau, rồi đến văn bản prompt.
5. Ghép các đoạn bằng script trong `scripts/`.

## Các dạng video có sẵn

- `prompts/01-store.md` — mẫu toàn thân trong cửa hàng quần áo trẻ em.
- `prompts/02-flatlay.md` — flat-lay sản phẩm, không có mẫu.
- `prompts/03-home-corner.md` — mẫu ở góc nhà đời thường.
- `prompts/04-hanger.md` — tay cầm móc treo bộ đồ trong cửa hàng.
- `prompts/05-natural-30s.md` — video 30 giây, 3 cảnh tự nhiên.
- `prompts/06-cool-montage-20s.md` — montage ngầu khoảng 20 giây, cắt
  nhanh 5 cảnh, mỗi cảnh 4 giây.
- `prompts/07-real-and-cool-30s.md` — vừa thật vừa ngầu, 30 giây.

## Ghép video bằng ffmpeg

Ghép 3 đoạn 10 giây thành video 30 giây:

```
./scripts/concat.sh output/video-30s.mp4 clip1.mp4 clip2.mp4 clip3.mp4
```

Ghép montage ngầu: cắt mỗi đoạn còn 4 giây, từ giây thứ 1, rồi ghép
thành khoảng 20 giây:

```
./scripts/montage.sh output/video-20s.mp4 clip1.mp4 clip2.mp4 clip3.mp4 clip4.mp4 clip5.mp4
```

Yêu cầu: đã cài `ffmpeg` trong PATH. Cả hai script đều chuẩn hóa clip về
720x1280, 30 fps trước khi ghép, nên clip lệch kích thước vẫn ghép được.

## Random bối cảnh và tình huống

Khi bạn muốn random, mỗi lần tạo phải bốc tổ hợp bối cảnh và tình huống
khác nhau, không lặp lại bộ vừa làm trước đó.

Bối cảnh có thể xoay vòng: công viên, sân chơi, gian hàng cửa hàng, nhà
sách, quán cà phê ngoài trời, phố đi bộ, ven biển, ven sông, sân vườn,
chợ, siêu thị, trung tâm thương mại, sân trường, thư viện, khu dân cư.

Tình huống có thể xoay vòng: đi dạo tự nhiên, chạy nhẹ vui vẻ, đứng nhìn
quanh, nhìn hàng hóa trên kệ, nắm tay người lớn đi dạo, chơi cầu trượt
hoặc xích đu, ngồi nghỉ trên ghế đá, cầm đồ chơi nhìn quanh, bước qua cầu
nhỏ, đi dọc hàng cây.

## Bộ 3 video từ 1 sản phẩm

Khi bạn yêu cầu 3 video từ 1 sản phẩm, 3 video phải khác nhau ở cả 3 điểm:
bối cảnh, nhân vật và cách trình bày. Xem chi tiết trong `SKILL.md`.

## Thư mục

- `prompts/` — mẫu prompt cho từng dạng video.
- `scripts/` — script ghép video bằng ffmpeg.
- `login/` — module login bằng cookie tùy chọn (code only, không chứa
  cookie thật): `cookie_login.py`, `example.py`, `test_cookie_login.py`,
  `README.md`.
- `gateway/` + `gateway_cli.py` — mode gateway multi-acc port từ
  automuse-multi (accounts, gateway Noise, pipeline, fashion script);
  `gateway_scripts/` là nơi chứa kịch bản fashion do mode này tạo ra.
- `input/` — ảnh sản phẩm bạn đưa vào, không commit ảnh thật lên repo
  công khai nếu không muốn lộ sản phẩm.
- `character-reference/` — ảnh nhân vật chuẩn của kênh.
- `output/` — video đã ghép xong.
- `jobs/` — chỗ ghi job (khi có giao diện quản lý job).

## Lưu ý

- Ảnh và video trong `input/`, `output/` và `character-reference/` đã được
  đưa vào `.gitignore`, trừ file `.gitkeep`.
- Đừng đưa cookie, mật khẩu, API key hay thông tin đăng nhập vào repo này.
  Module `login/` chỉ chứa code, không chứa cookie thật; file accounts
  (nếu bạn tự tạo lúc chạy) ghi quyền 0600 và đã nằm trong `.gitignore`.
- Skill này khác tool gateway trước đó (`automuse/fashion.py`): luồng tạo
  clip mặc định của skill này vẫn là tạo trong chat rồi ghép tay bằng
  script, không đăng nhập cookie; `login/` chỉ là module tùy chọn riêng
  cho tầng login, không thay đổi luồng đó.
