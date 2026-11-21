# 17 — Mở đầu đồ ngủ → cắt sang outfit (phong cách Phối Đồ Cùng Mei)

Khi nào dùng: đồ công sở, đồ đi tiệc, set đồ "sang, thanh lịch" —
muốn mở đầu bằng 1 câu chuyện/tình huống rồi "biến hình" sang
outfit chỉn chu. Cấu trúc của Phối Đồ Cùng Mei (39K followers, reel
cao nhất 1,2 triệu lượt xem): mở đầu mặc đồ ngủ/áo phông xuề xòa
ở nhà, nói chuyện với camera (nói và ra dấu tay, chỉ vào camera/
áo), sau đó CẮT CẢNH NGAY TẠI CHỖ sang outfit trên nền nhạc. Độ
tương phản "xuề xòa → sang" là chính cú hook.

QUAN TRỌNG: video sinh ra LUÔN SẠCH, không có lời nói. Phần "nói"
ở clip 1 chỉ là diễn xuất (môi cử động, ra dấu tay như đang giải
thích); LỜI NÓI do user tự thu voiceover và lồng vào lúc đăng.
Không sinh video có tiếng nói giả. Giao kèm kịch bản nói ngắn dưới
đây để user thu.

Độ dài: 2 clip x 10 giây = 20 giây. Clip 1 là hook (đồ ngủ), clip
2 là outfit (sản phẩm chính).

## Kịch bản voiceover gợi ý cho clip 1 (user tự thu, 2–3 câu ngắn)

"[CÂU HOOK, ví dụ: Đi làm mà lương 5 triệu thì mặc gì cho sang?
Để em chỉ cho.] [CÂU DẪN, ví dụ: Chỉ cần 1 chiếc chân váy dài
này thôi là đủ.]"

Điền câu hook THẬT theo món đồ và đối tượng user nhắm tới, không
bịa giá/size.

## Câu hook chữ gợi ý (chọn 1, thêm ở editor lúc đăng)

- "Lương 5tr nhưng đi làm vẫn phải sang như quý cô 50tr"
- "Team mê [TÊN MÓN] đi làm thì phối sao cho thật sang"
- "Đi làm phối sao cho vừa sang vừa thanh lịch"
- "Đi đám cưới NYC tuyệt đối đừng mặc như này …"

## Caption gợi ý

"[Câu hỏi/móc câu giống chữ trên màn hình]… #viral #outfitideas
#goiyphoido #xuhuong #phoidoxinh"

## Prompt sinh video (tiếng Anh)

Điền mô tả outfit THẬT từ ảnh của user vào [OUTFIT]. Clip 1 mặc
đồ ngủ/áo phông bình thường (không phải sản phẩm); clip 2 mặc đúng
[OUTFIT]. Cả 2 clip CÙNG 1 góc phòng, CÙNG góc quay, CÙNG nhân
vật — chỉ đổi đồ.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật.
- Vertical 9:16, static eye-level camera, full-body shot, same fixed room (wooden floor, wardrobe/wooden door), true colours.
- No on-screen text, no subtitles, no speech, no voiceover in the generated clip. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Diễn xuất tự nhiên, thân mật, không làm quá.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'
- GIỮ NGUYÊN TRANG SỨC/PHỤ KIỆN: liệt kê TỪNG món trang sức/phụ kiện có trong ảnh (dây chuyền, khuyên tai, nhẫn, đồng hồ, vòng tay, kẹp tóc...) kèm vị trí đeo. Mỗi prompt phải kèm câu: 'Keep every accessory exactly as in the reference photos: [ACCESSORIES with positions]. They stay on her body and visible in every frame from start to finish — never vanish, change shape, or swap sides during movement.' Ảnh không có trang sức thì ghi rõ 'no jewellery or accessories' để model khỏi tự thêm.
- MỖI CLIP CHỈ 1 HÀNH ĐỘNG CHÍNH: đi bộ HOẶC xoay người HOẶC giơ đồ — không gộp nhiều động tác nhanh trong 1 clip. Chuyển động CHẬM và nhẹ nhàng (đi chậm, xoay chậm, tay di chuyển từ tốn): cử động nhanh/phức tạp làm model rớt chi tiết nhỏ (trang sức, nút, họa tiết) giữa chừng.
- Chi tiết nhỏ quan trọng KHÔNG trông chờ vào clip đi bộ: quay riêng 1 cảnh cận cảnh (template 11/12) để chi tiết to trong khung hình — càng to càng khó mất.

Clip 1, 10 seconds (mở đầu đồ ngủ, như đang nói chuyện):
"Vertical 9:16 video, static eye-level camera, full-body shot. A young Vietnamese woman with [CHARACTER: long dark hair, natural makeup, hair in a loose braid] wearing casual home pyjamas stands in a fixed room with a wooden floor and a wardrobe, facing the camera. She gestures with her hands as if explaining something to a friend, points toward the camera, crosses her arms briefly, then smiles and gestures toward herself as if introducing what comes next. Speaking gestures only, no audible speech in the clip, no text, no subtitles."

Clip 2, 10 seconds (cắt sang outfit, nhạc nền):
"Vertical 9:16 video, static eye-level camera, full-body shot, same fixed room, same woman now wearing [OUTFIT]. She stands facing the camera, poses confidently, turns slowly to show the side and back of the outfit, then turns back and smiles at the camera. Calm confident posing, no speech in the clip, no text, no subtitles."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4
(Cắt cảnh giữa 2 clip là CỐ TÌNH — cú "biến hình" đồ ngủ → outfit.)

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau (clip 1
không có sản phẩm thì chỉ gửi ảnh nhân vật), rồi đến văn bản mô tả
clip đó.
