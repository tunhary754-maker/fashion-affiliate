# 22 — Mở hộp (unboxing) rồi mặc thử (phong cách Thảo Vy)

Khi nào dùng: hàng MỚI VỀ từ 1 shop — muốn 2 reel liên tiếp: reel
1 mở hộp khoe đồ mới, reel 2 mặc thử đồ vừa mở. Thảo Vy (64K
followers, 40 reel): unboxing là 1 format riêng — thùng carton /
bưu kiện làm đạo cụ, người mẫu mặc outfit nền (áo đen + quần ống
rộng) rồi lấy món đồ trong hộp ra, giơ lên trước người ("Unboxing
/ Rocky Denim" 24K, "Unboxing / Daneji" 113K, "Unbox phụ kiện /
NHÃ BẠCH TUỘC" 38K); reel sau đó nối tiếp bằng try-on ("Try on 2
set trong vid unbox mí bà nè"). Template này là REEL MỞ HỘP; reel
mặc thử sau đó dùng template 07 (lookbook) hoặc 10 (giơ rồi mặc).

Độ dài: 2 clip x 10 giây = 20 giây (reel mở hộp).

## Chữ trên màn hình gợi ý (thêm ở editor lúc đăng)

- "Unboxing / [TÊN SHOP]" (ví dụ "Unboxing / Daneji", "Unbox phụ
  kiện / NHÃ BẠCH TUỘC").
- Reel mặc thử tiếp theo ghi caption "Try on [số] set trong vid
  unbox mí bà nè".

## Caption gợi ý (reel mở hộp)

"[Câu cảm thán ngắn, ví dụ: 👖mớiiiiii / qá tời đồ rồiiii, cá tính
đơn giản cho các bácccc] #viral #outfitideas #goiyphoido #xuhuong"

## Prompt sinh video (tiếng Anh)

Điền mô tả sản phẩm THẬT từ ảnh của user vào [PRODUCT]. Giữ nguyên
mọi chi tiết sản phẩm trong cả 2 clip — món đồ lấy ra khỏi hộp
phải giống hệt ảnh gốc.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật; món đồ trong hộp là [PRODUCT].
- Vertical 9:16, static camera, full-body shot, one fixed bright room (white walls, wooden floor), true colours.
- No on-screen text, no subtitles, no speech, no voiceover in the generated clip. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Mở hộp chậm rãi, giơ đồ rõ ràng.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'
- GIỮ NGUYÊN TRANG SỨC/PHỤ KIỆN: liệt kê TỪNG món trang sức/phụ kiện có trong ảnh (dây chuyền, khuyên tai, nhẫn, đồng hồ, vòng tay, kẹp tóc...) kèm vị trí đeo. Mỗi prompt phải kèm câu: 'Keep every accessory exactly as in the reference photos: [ACCESSORIES with positions]. They stay on her body and visible in every frame from start to finish — never vanish, change shape, or swap sides during movement.' Ảnh không có trang sức thì ghi rõ 'no jewellery or accessories' để model khỏi tự thêm.
- MỖI CLIP CHỈ 1 HÀNH ĐỘNG CHÍNH: đi bộ HOẶC xoay người HOẶC giơ đồ — không gộp nhiều động tác nhanh trong 1 clip. Chuyển động CHẬM và nhẹ nhàng (đi chậm, xoay chậm, tay di chuyển từ tốn): cử động nhanh/phức tạp làm model rớt chi tiết nhỏ (trang sức, nút, họa tiết) giữa chừng.
- Chi tiết nhỏ quan trọng KHÔNG trông chờ vào clip đi bộ: quay riêng 1 cảnh cận cảnh (template 11/12) để chi tiết to trong khung hình — càng to càng khó mất.

Clip 1, 10 seconds (ôm bưu kiện, mở hộp):
"Vertical 9:16 video, static camera, full-body shot. A young Vietnamese woman with [CHARACTER: long dark hair, natural makeup] wearing a simple black sleeveless top and white wide-leg trousers stands in a bright room with white walls and a wooden floor, holding a sealed silver parcel against her chest. She opens the parcel slowly, pulls out [PRODUCT] folded inside, and smiles at the camera. No text, no subtitles, no audible speech."

Clip 2, 10 seconds (giơ món đồ lên khoe):
"Vertical 9:16 video, static camera, full-body shot, same bright room, same woman. She holds [PRODUCT] up in front of her with both hands, unfolding it to show the full shape, turning it slightly so the viewer can see the front and the details, then holds it against her body to show the size. No text, no subtitles, no audible speech."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4

Reel mặc thử tiếp theo: dùng template 07 hoặc 10 với cùng nhân vật
và cùng [PRODUCT], caption "Try on [số] set trong vid unbox mí bà
nè".

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó.
