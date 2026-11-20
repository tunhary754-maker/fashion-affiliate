# 08 — Trình bày trực tiếp (phong cách Thảo Nhi, nói + user thu voiceover sau)

Khi nào dùng: chân váy tơ, váy ren, set peplum — những món cần
giới thiệu bằng lời. Mẫu vừa giơ đồ trên móc vừa chạm/chỉ chi tiết,
cử chỉ như đang giới thiệu với khách.

QUAN TRỌNG: video sinh ra LUÔN SẠCH, không có lời nói. Diễn xuất
trình bày trong clip chỉ là hình ảnh; LỜI NÓI do user tự thu
voiceover và lồng vào lúc đăng. Không sinh video có tiếng nói giả.
Giao kèm kịch bản nói ngắn dưới đây để user thu.

Độ dài: 2 clip x 10 giây = 20 giây.

## Kịch bản voiceover gợi ý (user tự thu, 3–4 câu ngắn)

"Mấy bà ơi, em [TÊN MÓN] này về rồi nè. [ĐIỂM NỔI BẬT 1, ví dụ:
chất tơ mềm, mặc mát], [ĐIỂM NỔI BẬT 2, ví dụ: phom xòe che bụng
tốt]. Ai ưng thì nhắn tin cho shop nha."

Điền tên món và 2 điểm nổi bật THẬT do user xác nhận, không bịa
giá/size/chất liệu.

## Caption gợi ý

"Em này xinh quá mấy bà ơi 🥹 #viral #outfitideas #goiyphoido #xuhuong"

## Prompt sinh video (tiếng Anh)

Điền mô tả sản phẩm THẬT từ ảnh của user vào [PRODUCT] và chi tiết
cần chỉ (ren, cổ áo, đai, vạt peplum) vào [DETAIL]. Giữ nguyên mọi
chi tiết sản phẩm trong cả 2 clip.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật, mặc đúng đồ trong ảnh sản phẩm: [PRODUCT].
- Vertical 9:16, static camera at eye level, warm yellow indoor light, true colours.
- No on-screen text, no subtitles, no speech, no voiceover in the generated clip. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Cử chỉ trình bày tự nhiên, thân mật, không làm quá.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'

Clip 1, 10 seconds (giơ đồ trên móc):
"Vertical 9:16 video, static eye-level camera, medium-full shot. A young Vietnamese woman with [CHARACTER: long dark hair, friendly natural makeup] wearing [PRODUCT] stands in a warm living room with yellow ambient light and a wooden cabinet. She holds the matching garment on a hanger up in front of her with both hands, gestures toward [DETAIL] with one hand as if presenting it to a customer, looks at the camera with a warm friendly smile, then looks down at the garment and touches the fabric lightly. Presenting gestures only, no speech in the clip, no text, no subtitles."

Clip 2, 10 seconds (mặc lên, chỉ chi tiết):
"Vertical 9:16 video, static eye-level camera, full-body shot, same warm living room, same woman wearing [PRODUCT]. She faces the camera, touches [DETAIL] gently with both hands to draw attention to it, adjusts the fit slightly, then turns to show the side silhouette and smiles at the camera. Presenting gestures only, no speech in the clip, no text, no subtitles."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó.
