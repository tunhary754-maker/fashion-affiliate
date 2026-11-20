# 11 — Cận cảnh chứng minh chất liệu (phong cách C, Thanh Huyền)

Khi nào dùng: món có điểm đáng chứng minh bằng tay — vải mềm/co giãn,
cúc/nút đẹp, độ ôm ở eo, tag/mác. Thanh Huyền dùng cận cảnh làm bằng
chứng, không phải để khoe vải cho đẹp: tay sờ vải và cúc áo (reel 15),
kéo giãn gấu áo chứng minh co giãn (reel 22), kéo nhẹ gấu áo khoe độ
ôm ở eo (reel 25). Chọn MỘT cử chỉ chứng minh duy nhất mỗi video,
đừng gộp nhiều cử chỉ vào 1 clip.

Độ dài: 2 clip x 10 giây = 20 giây.

## Câu POV gợi ý (chọn 1, thêm ở editor lúc đăng)

- "POV: Chất vải này sờ vào mới biết nó xịn cỡ nào."
- "POV: Co giãn thế này thì mặc cả ngày cũng thoải mái."
- "POV: Nhìn cúc áo này là biết đồ được làm tử tế."

## Caption gợi ý

"Link mua [tên món] - Shopee: [link] — Bấm vào link để xem chi tiết và mua hàng. #viral #outfitideas #goiyphoido #xuhuong"

## Prompt sinh video (tiếng Anh)

Điền mô tả sản phẩm THẬT từ ảnh của user vào [PRODUCT], cử chỉ
chứng minh vào [PROOF: touching the fabric and buttons / gently
stretching the hem to show the stretch / pulling the hem lightly to
show the fit at the waist]. Giữ nguyên mọi chi tiết sản phẩm trong
cả 2 clip.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật; sản phẩm là [PRODUCT].
- Vertical 9:16, static camera, warm indoor light, true colours.
- No on-screen text, no subtitles, no speech, no voiceover. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Chuyển động chậm, tự nhiên.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'

Clip 1, 10 seconds (cận cảnh chứng minh):
"Vertical 9:16 video, static camera, close-up on the torso and hands. A young Vietnamese woman with [CHARACTER: long dark wavy hair, natural makeup] wearing [PRODUCT] stands in a warm living room with a white sofa. Her hands [PROOF], showing the fabric and details clearly to the camera in a slow, natural movement. Warm indoor light, calm everyday mood, no text, no subtitles, no speech."

Clip 2, 10 seconds (mặc lên, toàn thân):
"Vertical 9:16 video, static eye-level camera, full-body shot, same warm living room, same woman wearing [PRODUCT]. She stands in the centre of the frame, sways gently, turns slightly to show the side fit, then faces the camera and smiles softly. Warm indoor light, calm everyday mood, no text, no subtitles, no speech."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó. Chỉ dùng template này khi ảnh sản phẩm thể hiện rõ
chi tiết cần chứng minh (vải, cúc, độ ôm) — không bịa chất liệu.
