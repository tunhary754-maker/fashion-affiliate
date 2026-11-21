# 18 — Chuỗi đếm ngược Tết (Huyền Kem, NuocLoc7Mao, reel lẻ Tết)

Khi nào dùng: đồ Tết (áo dài, đồ đỏ, set đi chơi Tết, đồ đi tiệc
cuối năm) — làm thành CHUỖI nhiều reel, mỗi reel 1 outfit, đánh số
phần và đếm ngược số ngày còn lại đến Tết. 3 kênh cùng làm format
này: Huyền Kem "Đếm ngược 78–84 ngày đến Tết 2027 / Tết mặc gì? |
P3–P9" (7 phần), NuocLoc7Mao "Còn 88 ngày nữa là đến Tết 🧧 Vậy
Tết nay mặc gì?", reel lẻ Lương 5 triệu mặc gì đây ? "còn 140 ngày
nữa đến Tết 2027 / Tết này mặc gì, ngày 1". Đăng từ HÀNG THÁNG
trước Tết (140 ngày ≈ 4,5 tháng), không đợi sát ngày.

Đây là format CHUỖI, không phải 1 reel đơn: mỗi phần là 1 reel
riêng (2 clip x 10 giây = 20 giây), cùng nhân vật, cùng góc phòng,
cùng góc quay — chỉ đổi outfit theo từng phần. Chữ đếm ngược + số
phần user thêm ở editor lúc đăng từng phần.

Độ dài mỗi phần: 2 clip x 10 giây = 20 giây.

## Chữ trên màn hình gợi ý (thêm ở editor lúc đăng từng phần)

- "Đếm ngược [N] ngày đến Tết 2027 / Tết mặc gì? | P[n]"
- Hoặc: "Còn [N] ngày nữa đến Tết 🧧 / Tết này mặc gì, ngày [n]:"

Số ngày [N] đếm lùi theo ngày đăng thật; số phần [n] tăng dần
(P1, P2, P3... hoặc ngày 1, ngày 2...). Không bịa số ngày — tính
từ ngày đăng thật đến Tết.

## Caption gợi ý

"[Câu hỏi về outfit Tết, ví dụ: Lên đồ tết từ bây giờ có sớm quá
không nhỉ ?] #viral #outfitideas #goiyphoido #xuhuong #Tet2027
#tetmacgi"

## Prompt sinh video (tiếng Anh) — dùng lại cho mọi phần

Điền mô tả outfit Tết THẬT từ ảnh của user vào [OUTFIT]. Mọi phần
PHẢI giống nhau tuyệt đối về nhân vật, dáng đứng, góc quay, bối
cảnh, ánh sáng — chỉ khác outfit.

Quy tắc chung cho mọi clip:

- Dùng đúng nhân vật trong ảnh nhân vật, mặc đúng đồ trong ảnh sản phẩm: [OUTFIT].
- Vertical 9:16, static eye-level camera, full-body shot, same fixed bright room, wooden floor, true colours.
- No on-screen text, no subtitles, no speech, no voiceover. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Trình bày kín đáo, đời thường, không khí Tết nhẹ nhàng (không cần đạo cụ Tết cầu kỳ trong clip — chữ đếm ngược ở editor đã đủ gắn dịp).
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'
- GIỮ NGUYÊN TRANG SỨC/PHỤ KIỆN: liệt kê TỪNG món trang sức/phụ kiện có trong ảnh (dây chuyền, khuyên tai, nhẫn, đồng hồ, vòng tay, kẹp tóc...) kèm vị trí đeo. Mỗi prompt phải kèm câu: 'Keep every accessory exactly as in the reference photos: [ACCESSORIES with positions]. They stay on her body and visible in every frame from start to finish — never vanish, change shape, or swap sides during movement.' Ảnh không có trang sức thì ghi rõ 'no jewellery or accessories' để model khỏi tự thêm.
- MỖI CLIP CHỈ 1 HÀNH ĐỘNG CHÍNH: đi bộ HOẶC xoay người HOẶC giơ đồ — không gộp nhiều động tác nhanh trong 1 clip. Chuyển động CHẬM và nhẹ nhàng (đi chậm, xoay chậm, tay di chuyển từ tốn): cử động nhanh/phức tạp làm model rớt chi tiết nhỏ (trang sức, nút, họa tiết) giữa chừng.
- Chi tiết nhỏ quan trọng KHÔNG trông chờ vào clip đi bộ: quay riêng 1 cảnh cận cảnh (template 11/12) để chi tiết to trong khung hình — càng to càng khó mất.

Clip 1, 10 seconds (outfit toàn thân, đứng tạo dáng):
"Vertical 9:16 video, static eye-level camera, full-body shot. A young Vietnamese woman with [CHARACTER: long straight black hair, natural makeup] wearing [OUTFIT] stands in the centre of a bright room with a wooden floor, facing the camera. She stands still, smiles gently, then turns slowly to show her side profile. Bright natural daylight, calm festive mood, no text, no subtitles, no speech."

Clip 2, 10 seconds (xoay người / khoe mặt sau):
"Vertical 9:16 video, static eye-level camera, full-body shot, same bright room, same woman wearing [OUTFIT], standing in the exact same centre position. She turns slowly to show the back of the outfit, looks back over her shoulder at the camera with a smile, then turns back to face the camera. Bright natural daylight, calm festive mood, no text, no subtitles, no speech."

Ghép mỗi phần bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-tet-p[n]-20s.mp4 clip1.mp4 clip2.mp4

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm của phần đó
sau, rồi đến văn bản mô tả clip đó.
