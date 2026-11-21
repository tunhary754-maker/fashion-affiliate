# 13 — Trước/Sau mặc, chia đôi màn hình (phong cách C, Thanh Huyền)

Khi nào dùng: đồ định hình — quần độn hông, đai chống gù, shapewear,
đồ nịt. Thanh Huyền quay màn hình chia đôi "Trước mặc / Sau mặc" cho
quần độn hông (reel 38, 121K lượt xem). Video sinh ra là 2 CLIP RIÊNG
cùng dáng đứng, cùng góc quay, cùng bối cảnh: clip 1 CHƯA mặc đồ định
hình, clip 2 ĐÃ mặc. User đặt 2 clip cạnh nhau trong editor và thêm
chữ "Trước mặc" / "Sau mặc" — phần chia đôi và chữ đều làm ở editor,
không sinh cùng video.

Độ dài: 2 clip x 10 giây = 20 giây (khi đặt cạnh nhau trong editor,
mỗi bên là 1 clip 10 giây; hoặc cắt mỗi clip còn 5 giây để reel tổng
10 giây — tùy user).

## Câu POV gợi ý (chọn 1, thêm ở editor lúc đăng)

- "POV: Trước và sau khi mặc, khác nhau thế này đây."
- "POV: Món này mặc vào là thấy khác ngay, không cần nói nhiều."
- "POV: Ai bảo đồ định hình khó mặc thì xem này."

## Caption gợi ý

"Link mua [tên món] - Shopee: [link] — Bấm vào link để xem chi tiết và mua hàng. #viral #outfitideas #goiyphoido #xuhuong"

## Prompt sinh video (tiếng Anh)

Điền mô tả đồ định hình THẬT từ ảnh của user vào [SHAPER], trang phục
mặc ngoài vào [OUTFIT]. Hai clip PHẢI giống nhau tuyệt đối về dáng
đứng, góc quay, bối cảnh, ánh sáng — chỉ khác ở chỗ có mặc [SHAPER]
hay không. Giữ nguyên mọi chi tiết sản phẩm trong cả 2 clip.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật; đồ định hình là [SHAPER].
- Vertical 9:16, static eye-level camera, full-body shot, warm indoor light, true colours.
- No on-screen text, no subtitles, no speech, no voiceover. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Trình bày kín đáo, đời thường. Chuyển động chậm, tối thiểu.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'
- GIỮ NGUYÊN TRANG SỨC/PHỤ KIỆN: liệt kê TỪNG món trang sức/phụ kiện có trong ảnh (dây chuyền, khuyên tai, nhẫn, đồng hồ, vòng tay, kẹp tóc...) kèm vị trí đeo. Mỗi prompt phải kèm câu: 'Keep every accessory exactly as in the reference photos: [ACCESSORIES with positions]. They stay on her body and visible in every frame from start to finish — never vanish, change shape, or swap sides during movement.' Ảnh không có trang sức thì ghi rõ 'no jewellery or accessories' để model khỏi tự thêm.
- MỖI CLIP CHỈ 1 HÀNH ĐỘNG CHÍNH: đi bộ HOẶC xoay người HOẶC giơ đồ — không gộp nhiều động tác nhanh trong 1 clip. Chuyển động CHẬM và nhẹ nhàng (đi chậm, xoay chậm, tay di chuyển từ tốn): cử động nhanh/phức tạp làm model rớt chi tiết nhỏ (trang sức, nút, họa tiết) giữa chừng.
- Chi tiết nhỏ quan trọng KHÔNG trông chờ vào clip đi bộ: quay riêng 1 cảnh cận cảnh (template 11/12) để chi tiết to trong khung hình — càng to càng khó mất.

Clip 1, 10 seconds (CHƯA mặc đồ định hình):
"Vertical 9:16 video, static eye-level camera, full-body shot. A young Vietnamese woman with [CHARACTER: long dark wavy hair, natural makeup] wearing [OUTFIT] stands in the centre of a warm living room with a white sofa, dark curtains and a warm floor lamp, facing the camera with her arms relaxed at her sides. She stands still, then turns slowly to show her side profile, then turns back to face the camera. Warm indoor light, calm everyday mood, no text, no subtitles, no speech."

Clip 2, 10 seconds (ĐÃ mặc đồ định hình — cùng dáng, cùng góc):
"Vertical 9:16 video, static eye-level camera, full-body shot, same warm living room, same woman wearing [OUTFIT] over [SHAPER], standing in the exact same centre position facing the camera with her arms relaxed at her sides. She stands still, then turns slowly to show her side profile, then turns back to face the camera. Warm indoor light, calm everyday mood, no text, no subtitles, no speech."

Ghép: KHÔNG dùng concat.sh nối tiếp 2 clip. Đặt 2 clip cạnh nhau
trong editor (chia đôi màn hình dọc) + thêm chữ "Trước mặc" bên trái,
"Sau mặc" bên phải. Nếu muốn bản nối tiếp thì ghép bằng
~/workspace/fashion-affiliate/scripts/concat.sh như thường.

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó. Khi sinh clip 2, nhắc rõ trong prompt là cô đang
mặc [SHAPER] bên trong [OUTFIT].
