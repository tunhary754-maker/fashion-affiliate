# 15 — Nhiều look trong 1 reel (phong cách D, Nhun Lên Đồ)

Khi nào dùng: muốn khoe NHIỀU OUTFIT trong 1 reel — "7 ngày không
trùng outfit", "LOOK 1... LOOK 5", "Lên 5 outfit với áo len cho hội
ce sắp đi Đà Lạt" (Nhun Lên Đồ reel 27, 28, 29). Mỗi look là 1 clip
10 giây, cùng nhân vật, cùng góc phòng, cùng góc quay — chỉ đổi
outfit. User thêm nhãn "LOOK 1", "LOOK 2"... ở editor lúc đăng.

Độ dài: mặc định 3 clip x 10 giây = 30 giây (3 look). Muốn 5 look
thì sinh 5 clip rồi cắt mỗi clip còn ~4–6 giây ở editor, hoặc làm 2
reel (3 look + 2 look).

## Câu hook gợi ý (chọn 1, thêm ở editor lúc đăng)

Dạng hook câu hỏi của kênh này (giọng "🗣️: ..."):

- "Mỗi ngày 1 giao diện, 7 ngày không trùng outfit"
- "Mùa đông này mặc gì đi làm, đi ăn cưới, đi cà phê?"
- "Những món đồ basic đáng đầu tư cho tủ đồ mùa đông năm nay:"

## Caption gợi ý

"[Câu chốt nhẹ về bộ sưu tập, ví dụ: Đầu tư vào đồ basic chưa bao
giờ sai] #viral #outfitideas #goiyphoido #xuhuong #mixandmatch"

## Prompt sinh video (tiếng Anh)

Điền mô tả từng outfit THẬT từ ảnh của user vào [OUTFIT 1/2/3].
Các clip PHẢI giống nhau tuyệt đối về nhân vật, dáng đứng, góc quay,
bối cảnh, ánh sáng — chỉ khác outfit. Mỗi outfit giữ nguyên tuyệt
đối chi tiết của nó trong clip của nó.

Quy tắc chung cho mọi clip:

- Dùng đúng nhân vật trong ảnh nhân vật.
- Vertical 9:16, static eye-level camera, full-body shot, bright white room, wooden floor, white cabinet, true colours.
- No on-screen text, no subtitles, no speech, no voiceover. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Trình bày kín đáo, đời thường. Chuyển động chậm, tối thiểu.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'
- GIỮ NGUYÊN TRANG SỨC/PHỤ KIỆN: liệt kê TỪNG món trang sức/phụ kiện có trong ảnh (dây chuyền, khuyên tai, nhẫn, đồng hồ, vòng tay, kẹp tóc...) kèm vị trí đeo. Mỗi prompt phải kèm câu: 'Keep every accessory exactly as in the reference photos: [ACCESSORIES with positions]. They stay on her body and visible in every frame from start to finish — never vanish, change shape, or swap sides during movement.' Ảnh không có trang sức thì ghi rõ 'no jewellery or accessories' để model khỏi tự thêm.
- MỖI CLIP CHỈ 1 HÀNH ĐỘNG CHÍNH: đi bộ HOẶC xoay người HOẶC giơ đồ — không gộp nhiều động tác nhanh trong 1 clip. Chuyển động CHẬM và nhẹ nhàng (đi chậm, xoay chậm, tay di chuyển từ tốn): cử động nhanh/phức tạp làm model rớt chi tiết nhỏ (trang sức, nút, họa tiết) giữa chừng.
- Chi tiết nhỏ quan trọng KHÔNG trông chờ vào clip đi bộ: quay riêng 1 cảnh cận cảnh (template 11/12) để chi tiết to trong khung hình — càng to càng khó mất.

Clip 1, 10 seconds (LOOK 1):
"Vertical 9:16 video, static eye-level camera, full-body shot. A young Vietnamese woman with [CHARACTER: long straight black hair, natural makeup] wearing [OUTFIT 1] stands in the centre of a bright white room with a wooden floor and a white cabinet, facing the camera. She stands still, then turns slowly to show her side profile, then turns back to face the camera. Bright natural daylight, calm everyday mood, no text, no subtitles, no speech."

Clip 2, 10 seconds (LOOK 2 — cùng dáng, cùng góc, đổi outfit):
"Vertical 9:16 video, static eye-level camera, full-body shot, same bright white room, same woman wearing [OUTFIT 2], standing in the exact same centre position facing the camera. She stands still, then turns slowly to show her side profile, then turns back to face the camera. Bright natural daylight, calm everyday mood, no text, no subtitles, no speech."

Clip 3, 10 seconds (LOOK 3 — cùng dáng, cùng góc, đổi outfit):
"Vertical 9:16 video, static eye-level camera, full-body shot, same bright white room, same woman wearing [OUTFIT 3], standing in the exact same centre position facing the camera. She stands still, then turns slowly to show her side profile, then turns back to face the camera. Bright natural daylight, calm everyday mood, no text, no subtitles, no speech."

Ghép: nối tiếp bằng ~/workspace/fashion-affiliate/scripts/concat.sh
(3 clip = 30 giây). Thêm nhãn "LOOK 1/2/3" ở editor, mỗi nhãn hiện
đúng lúc clip của look đó bắt đầu.

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm của look đó
sau, rồi đến văn bản mô tả clip đó.
