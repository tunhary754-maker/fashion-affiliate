# 20 — Đi bộ + giơ đồ trong 1 reel (phong cách Machi.clo)

Khi nào dùng: món đồ vừa cần khoe dáng mặc vừa có chi tiết đáng
khoe (cúc, vải, đệm ngực, khóa kéo) — muốn cả hai trong cùng 1
reel thay vì tách thành 2 reel. Machi.clo (shop 4,9K followers,
35 reel): hành lang hẹp tường trắng làm "studio" cố định, người
mẫu đi dọc hành lang rồi giơ chính món đang mặc lên cận cảnh chất
vải — giơ đồ là một NHỊP trong reel mặc đồ, không phải toàn bộ
reel. Reel cao nhất kênh (159K lượt xem) dùng đúng cấu trúc 3
nhịp: đi xa → đi về phía máy quay → giơ váy lên cận cảnh. Khác
template 10 (giơ đồ là công thức chính, ít đi lại) và template 03
(chỉ đi bộ, không giơ đồ).

Độ dài: 2 clip x 10 giây = 20 giây.

## Chữ trên màn hình gợi ý (thêm ở editor lúc đăng)

- Chữ CHỨNG MINH chi tiết cấu tạo (mới, Machi.clo): 1 dòng ngắn
  nêu đúng 1 chi tiết may mặc đã xác nhận, ví dụ "có đệm ngực
  được may chắc chắn", "có khoá kéo hai bên", "chất dạ mềm, hạn
  chế xù lông". Chỉ ghi điều user xác nhận là thật — không bịa.
- Tên outfit ngắn kiểu chữ viết tay, ví dụ "summer outfit",
  "basic outfit" (tùy chọn).

## Caption gợi ý

- Shop bán trực tiếp (mẫu Machi.clo): "[Tên áo] x [Tên
  quần/váy] 🤎 / [Mô tả chất vải ngắn] / ▪️[SIZE] / — / CMT CHẤM
  (.) MACHI TƯ VẤN VÀ BÁO GIÁ Ạ" — chỉ dùng khi user là shop bán
  qua inbox; giá chỉ ghi khi user đưa (gợi ý "3xx/2xx/1xx" nếu
  user muốn giấu giá thật).
- Affiliate: dùng caption mẫu phong cách C (link Shopee).

## Prompt sinh video (tiếng Anh)

Điền mô tả sản phẩm THẬT từ ảnh của user vào [PRODUCT]. Giữ nguyên
mọi chi tiết sản phẩm trong cả 2 clip.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật, mặc đúng đồ trong ảnh sản phẩm: [PRODUCT].
- Vertical 9:16, static camera, full-body shot, narrow bright hallway with white walls and black pendant lights, true colours.
- No on-screen text, no subtitles, no speech, no voiceover in the generated clip. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Đi bộ tự nhiên, giơ đồ chậm rãi để thấy rõ chi tiết.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'
- GIỮ NGUYÊN TRANG SỨC/PHỤ KIỆN: liệt kê TỪNG món trang sức/phụ kiện có trong ảnh (dây chuyền, khuyên tai, nhẫn, đồng hồ, vòng tay, kẹp tóc...) kèm vị trí đeo. Mỗi prompt phải kèm câu: 'Keep every accessory exactly as in the reference photos: [ACCESSORIES with positions]. They stay on her body and visible in every frame from start to finish — never vanish, change shape, or swap sides during movement.' Ảnh không có trang sức thì ghi rõ 'no jewellery or accessories' để model khỏi tự thêm.
- MỖI CLIP CHỈ 1 HÀNH ĐỘNG CHÍNH: đi bộ HOẶC xoay người HOẶC giơ đồ — không gộp nhiều động tác nhanh trong 1 clip. Chuyển động CHẬM và nhẹ nhàng (đi chậm, xoay chậm, tay di chuyển từ tốn): cử động nhanh/phức tạp làm model rớt chi tiết nhỏ (trang sức, nút, họa tiết) giữa chừng.
- Chi tiết nhỏ quan trọng KHÔNG trông chờ vào clip đi bộ: quay riêng 1 cảnh cận cảnh (template 11/12) để chi tiết to trong khung hình — càng to càng khó mất.

Clip 1, 10 seconds (đi bộ trong hành lang):
"Vertical 9:16 video, static camera, full-body shot. A young Vietnamese woman with [CHARACTER: long dark hair, natural makeup] wearing [PRODUCT] walks toward the camera down a narrow bright hallway with white walls and black pendant lights, then turns slowly to show the front, side and back of the outfit, smiling naturally. She walks like she is on her way somewhere, not posing for a photoshoot. No text, no subtitles, no audible speech."

Clip 2, 10 seconds (giơ đồ lên cận cảnh):
"Vertical 9:16 video, static camera, full-body shot, same narrow hallway, same woman wearing [PRODUCT]. She gently lifts the hem of the [PRODUCT: skirt/top] with both hands toward the camera to show the fabric and [DETAIL: buttons / stitching / lining] up close, lets it fall back naturally, then stands facing the camera and smiles. Slow, clear product demonstration, no text, no subtitles, no audible speech."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó.
