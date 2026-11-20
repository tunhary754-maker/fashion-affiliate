# 19 — Nhảy nhẹ / lip-sync trong phòng (phong cách Ninh Anh)

Khi nào dùng: đồ trẻ trung, đồ dạo phố, áo thun oversize, áo trễ
vai, chân váy mini, quần short — muốn không khí vui, trẻ, theo
trend nhạc thay vì lookbook tạo dáng chậm. Ninh Anh (16K
followers): phòng cố định, máy tĩnh, mẫu nhảy nhẹ/lắc hông/nhún
vai theo nhạc, lip-sync, giơ tay hình trái tim; 2 trong 5 reel cao
nhất kênh là dạng này (nhảy/lip-sync 18K lượt xem, nhảy nhẹ 11K).
Khác template 07 (tạo dáng chậm, trang trọng): ở đây chuyển động
nhiều hơn, vui hơn, theo nhịp nhạc.

Biến thể: selfie trước gương phòng gym (Ninh Anh reel 14, 13K lượt
xem) — cầm điện thoại selfie trước gương, hợp với đồ tập/đồ co
giãn tôn dáng. Ghi rõ trong prompt clip khi user chọn biến thể
này.

Độ dài: 2 clip x 10 giây = 20 giây.

## Caption gợi ý

"[Câu cảm thán ngắn giọng thân mật, ví dụ: Ỏ, áo này xinh quá đi
mất] #viral #outfitideas #goiyphoido #xuhuong"

Không gợi ý hook chữ — kênh gốc gần như không có chữ trên màn hình
(1/30 reel). Nhạc thịnh hành user chọn trong thư viện nhạc lúc
đăng.

## Prompt sinh video (tiếng Anh)

Điền mô tả sản phẩm THẬT từ ảnh của user vào [PRODUCT]. Giữ nguyên
mọi chi tiết sản phẩm trong cả 2 clip.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật, mặc đúng đồ trong ảnh sản phẩm: [PRODUCT].
- Vertical 9:16, static camera, full-body or half-body shot, fixed indoor room, true colours. Góc máy hơi thấp (low angle) để chân dài hơn trong khung toàn thân.
- No on-screen text, no subtitles, no speech, no voiceover in the generated clip. Natural ambient sound only. Lip-sync chỉ là cử động môi theo nhạc, không thu tiếng nói.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Nhảy nhẹ nhàng, vui vẻ, không quá đà; trình bày kín đáo, đời thường.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'

Clip 1, 10 seconds (nhảy nhẹ, tay chống hông):
"Vertical 9:16 video, static camera at a slightly low angle, full-body shot. A young Vietnamese woman with [CHARACTER: long dark hair, natural makeup] wearing [PRODUCT] stands in a fixed indoor room, dancing lightly to an unheard beat — gentle hip sway, small shoulder bounces, one hand on her hip, smiling at the camera, lips moving as if singing along. Playful everyday mood, no text, no subtitles, no audible speech."

Clip 2, 10 seconds (nhảy nhẹ, vuốt tóc / giơ tay trái tim):
"Vertical 9:16 video, static camera at a slightly low angle, full-body shot, same fixed indoor room, same woman wearing [PRODUCT]. She keeps dancing lightly to the beat, runs a hand through her hair, makes a small heart shape with her hands toward the camera, then turns slightly to show the side of the outfit. Playful everyday mood, no text, no subtitles, no audible speech."

Biến thể gương gym (thay clip 2 khi user chọn): "Vertical 9:16 video, static camera, mirror selfie shot in a gym. A young Vietnamese woman with [CHARACTER] wearing [PRODUCT — sportswear] stands in front of a large gym mirror holding her phone up to film herself, one hand on her hip, shifting her weight slightly to show the fit of the outfit. Bright gym lighting, no text, no subtitles, no audible speech."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó.
