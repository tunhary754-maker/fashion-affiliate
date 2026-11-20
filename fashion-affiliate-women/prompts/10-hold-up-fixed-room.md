# 10 — Giơ đồ rồi mặc, phòng cố định (phong cách C, Thanh Huyền)

Khi nào dùng: mọi món đồ — đầm, áo, set bộ, quần. Công thức cốt lõi
của Thanh Huyền (22/40 reel): nhịp 1 giơ món đồ che trước người,
mặt vẫn thấy ở phía trên món đồ; nhịp 2 đã mặc xong, xoay nhẹ.
Cùng MỘT góc phòng ấm cho mọi video: sofa trắng, rèm tối, đèn đứng
ánh vàng, hộp hoa hồng. Chuyển động tối thiểu, sản phẩm làm trung
tâm. Khác template 06 ở chỗ: bối cảnh phòng ngủ đời thường → phòng
khách ấm cố định, và nhịp giơ đồ là hook chính của cả reel chứ
không chỉ là cầu nối.

Độ dài: 2 clip x 10 giây = 20 giây.

## Câu POV gợi ý (chọn 1, thêm ở editor lúc đăng)

- "POV: Nhìn món đồ này ngoài đời còn xinh hơn trên ảnh."
- "POV: Giơ lên đã thấy ưng, mặc lên thì chốt luôn."
- "POV: Món này treo trên móc thì bình thường, mặc lên mới thấy khác."

## Caption gợi ý

"Link mua [tên món] - Shopee: [link] — Bấm vào link để xem chi tiết và mua hàng. #viral #outfitideas #goiyphoido #xuhuong"

## Prompt sinh video (tiếng Anh)

Điền mô tả sản phẩm THẬT từ ảnh của user vào [PRODUCT]. Giữ nguyên
mọi chi tiết sản phẩm trong cả 2 clip.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật; sản phẩm là [PRODUCT].
- Vertical 9:16, static camera at eye level, warm indoor light,
  true colours.
- No on-screen text, no subtitles, no speech, no voiceover. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Chuyển động chậm, tối thiểu.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'

Clip 1, 10 seconds (giơ đồ):
"Vertical 9:16 video, static eye-level camera, full-body shot. A young Vietnamese woman with [CHARACTER: long dark wavy hair, natural makeup] wearing a simple plain top and shorts stands in a warm living room with a white sofa, dark curtains, a warm floor lamp and a box of roses on the sofa arm. She holds [PRODUCT] up in front of her body with both hands, her face visible above the garment, turning it slightly to show the front and the shape. She smiles softly at the camera. Warm indoor light, calm everyday mood, no text, no subtitles, no speech."

Clip 2, 10 seconds (mặc lên, xoay nhẹ):
"Vertical 9:16 video, static eye-level camera, full-body shot, same warm living room, same woman now wearing [PRODUCT]. She stands in the centre of the frame, sways gently, slowly turns to show the side and back of the outfit, then turns back to face the camera and smiles. Warm indoor light, calm everyday mood, no text, no subtitles, no speech."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó. Clip 1 cần nói rõ trong prompt là cô đang mặc đồ
khác và cầm sản phẩm trên tay, không mặc sản phẩm. Biến thể nhịp giơ:
giơ trên móc (đồ bộ, áo), hoặc áp sát vào người để so độ dài/dáng
(quần, đầm dài).
