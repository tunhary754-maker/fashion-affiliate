# Kế hoạch reel quần jean XANH NHẠT — kiểu 1 (đi bộ phố, góc rộng toàn thân)

Chuẩn bị ngày 2026-11-20 (chưa chạy — chờ user nhắn đồng ý).
Ảnh sản phẩm: `input/quan-jean-xanh-nhat.jpg` (104x253, đã cắt sẵn từ screenshot 1/9).
Ảnh nhân vật: `character-reference/mau-quan-jean.jpg` (cùng mẫu như bản đen).

## Đã kiểm chứng trước khi làm

- Phóng to vùng túi (8x) của ảnh xanh nhạt: có 1 vết nhỏ màu vàng đồng ở mép
  trên túi trước bên PHẢI (bên người mặc) — cùng vị trí như bản đen. Vẫn chỉ là
  vệt mờ, không đọc được dáng/màu/kích cỡ thật của con ngựa → prompt dùng đúng
  câu mô tả đã làm được ở bản đen, không đoán thêm chi tiết.
- Đùi/ống/gấu trơn hoàn toàn, không có hình thêu phụ.
- Clip ngồi g02c của bản đen KHÔNG dùng lại được (quần đen) → clip 2 phải sinh
  mới, vẫn giữ góc an toàn nghiêng 3/4 mặt trước.

## Quy tắc rút ra từ bản đen (bắt buộc)

- Góc an toàn duy nhất: nghiêng 3/4 MẶT TRƯỚC (túi trước hướng camera, túi sau
  khuất). KHÔNG quay lưng / đi ra xa / nghiêng hẳn profile — model chuyển ngựa
  sang túi sau hoặc nhân đôi dù đã cấm.
- Quần thì toàn thân góc RỘNG, quần chiếm nửa dưới khung hình.
- Mọi prompt có câu giữ nguyên sản phẩm bắt buộc.
- Kiểm chứng: phóng to vùng túi + ĐẾM số hình thêu ở frame đầu mỗi clip trước
  khi báo user.

## Mô tả sản phẩm (dùng chung cả 2 clip)

Light-wash wide-leg straight jeans in pale blue, high waist, full length, with
exactly one small golden-brown horse embroidery on the upper edge of the right
front pocket; thighs, legs and hems completely plain, no other embroidery, no
distressing. Match the product reference photo EXACTLY: same colour, same cut,
same stitching, same details in the exact same positions. Do not redesign,
recolour, add, remove or move any detail.

Outfit: same as the character reference photo — pale blue denim shirt, brown
leather belt, small brown shoulder bag — but with the LIGHT BLUE jeans from the
product photo.

## Clip 1 — 10s, đi bộ phố nghiêng 3/4

Thứ tự gửi: ảnh nhân vật trước, ảnh sản phẩm sau, rồi prompt.

"Vertical 9:16 video, static eye-level camera, wide full-body shot, jeans
filling the lower half of the frame. A young Vietnamese woman with long dark
hair worn loose, natural makeup, wearing [PRODUCT as above], walks slowly
toward the camera at a three-quarter front angle along a quiet café-lined
sidewalk in the morning, natural daylight, holding a coffee cup in her right
hand and a phone in her left hand, small brown shoulder bag. She smiles gently
as she walks, the wide-leg fabric moving naturally with each step. Calm,
candid everyday mood, no text, no subtitles, no speech, no voiceover.
Match the product reference photo EXACTLY: same colour, same cut, same
stitching, same details in the exact same positions. Do not redesign, recolour,
add, remove or move any detail."

## Clip 2 — 10s, ngồi ghế quán cà phê (SINH MỚI, không dùng template 03 mặc định)

"Vertical 9:16 video, static eye-level camera, wide full-body shot, same
woman wearing [PRODUCT as above], sitting on an outdoor café bench at a
three-quarter front angle facing the camera, legs extended to show the full
length of the jeans, holding a coffee cup in her right hand and a phone in her
left hand. She sips her coffee and glances at her phone, relaxed and candid,
never turning her back to the camera. Same morning daylight, same sidewalk
café setting as clip 1. Calm, everyday mood, no text, no subtitles, no speech,
no voiceover. Match the product reference photo EXACTLY: same colour, same cut,
same stitching, same details in the exact same positions. Do not redesign,
recolour, add, remove or move any detail."

(Lý do không dùng clip 2 mặc định của template 03: đi bộ ra xa + quay lại cười
đã hỏng 4 lần ở bản đen vì ngựa nhảy sang túi sau.)

## Ghép + kiểm chứng

- Ghép bằng `~/workspace/fashion-affiliate/scripts/concat.sh` → dự kiến
  `output/video-jean-xanh-nhat-street-v1-16s.mp4` hoặc 20s tùy clip.
- Kiểm chứng trước khi giao: phóng to vùng túi ở frame đầu + giữa mỗi clip,
  đếm đúng 1 ngựa ở túi phải, đùi trơn; kiểm tra mối nối đứng → ngồi.

## Câu POV + caption gợi ý (thêm ở editor lúc đăng)

- "POV: Quần jean ống suông màu xanh nhạt mặc đi dạo phố là auto thành nhân vật chính."
- Caption: "Chiếc outfit đơn giản đi cà phê sáng mùa này 🥹 #viral #outfitideas #goiyphoido #xuhuong"
