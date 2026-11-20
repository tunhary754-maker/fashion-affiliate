# 16 — Review lồng tiếng "Chấm điểm" (phong cách Huyền Kem)

Khi nào dùng: phụ kiện chức năng (quần tất, đai, miếng dán), đồ
giữ nhiệt lót lông, boots/giày, món cần ĐÁNH GIÁ bằng lời — khác
template 08 (nói trực tiếp vào camera): ở đây người mẫu CHỈ tạo
dáng/demo, giọng nói chạy LỒNG TIẾNG phía trên cảnh quay (Huyền
Kem: 14/30 reel có voiceover, không reel nào nói trực tiếp vào
camera). Dạng "Chấm điểm [sản phẩm]" — review chấm điểm, tên sản
phẩm + thương hiệu ghi rõ trên màn hình ở editor.

QUAN TRỌNG: video sinh ra LUÔN SẠCH, không có lời nói. Lời lồng
tiếng do user tự thu và lồng vào lúc đăng. Không sinh video có
tiếng nói giả. Giao kèm kịch bản lồng tiếng ngắn dưới đây để user
thu.

Độ dài: 2 clip x 10 giây = 20 giây.

## Kịch bản lồng tiếng gợi ý (user tự thu, 3–4 câu ngắn)

"Mấy bà ơi, hôm nay em chấm điểm [TÊN MÓN + THƯƠNG HIỆU] nè.
[ĐIỂM CHỨNG MINH 1, ví dụ: lót lông bên trong dày mà không bị
cộm], [ĐIỂM CHỨNG MINH 2, ví dụ: mặc ôm vừa, không tuột]. Em này
[ĐÁNH GIÁ NGẮN, ví dụ: đáng tiền lắm]. Link em để ở bình luận nha."

Điền tên món, thương hiệu và điểm chứng minh THẬT do user xác nhận
— không bịa giá/size/chất liệu. Điểm chứng minh phải KHỚP với động
tác demo trong clip (kéo vạt khoe lót lông, kéo giãn, giơ bao bì).

## Chữ trên màn hình gợi ý (thêm ở editor lúc đăng)

- "Chấm điểm [TÊN MÓN + THƯƠNG HIỆU]"
- Tên sản phẩm + thương hiệu 1 dòng ngắn, ví dụ "Quần tất filter
  mịn da T61 Dolly Secret", "ÁO GIỮ NHIỆT LÓT LÔNG KEVA - KGE".

## Caption gợi ý

"[Câu trò chuyện nêu lợi ích, ví dụ: Mặc nó ôm k bị cộm mà siu ấm
luôn] #viral #outfitideas #goiyphoido #xuhuong"

## Prompt sinh video (tiếng Anh)

Điền mô tả sản phẩm THẬT từ ảnh của user vào [PRODUCT] và động tác
demo vào [DEMO]. Giữ nguyên mọi chi tiết sản phẩm trong cả 2 clip.

Quy tắc chung cho cả 2 clip:

- Dùng đúng nhân vật trong ảnh nhân vật, mặc đúng đồ trong ảnh sản phẩm: [PRODUCT].
- Vertical 9:16, static camera at eye level, full-body shot, bright real room with wooden floor and a mirror, true colours.
- No on-screen text, no subtitles, no speech, no voiceover in the generated clip. Natural ambient sound only.
- Giữ nguyên tuyệt đối sản phẩm và nhân vật. Demo rõ ràng, chậm rãi để người xem thấy được chi tiết.
- GIỮ NGUYÊN SẢN PHẨM TUYỆT ĐỐI: mô tả sản phẩm y hệt ảnh gốc (màu, phom, vị trí từng chi tiết), không thêm/bớt/đổi bất kỳ chi tiết nào. Mỗi prompt phải kèm câu: 'Match the product reference photo EXACTLY: same colour, same cut, same stitching, same details in the exact same positions. Do not redesign, recolour, add, remove or move any detail.'

Clip 1, 10 seconds (giơ sản phẩm/bao bì lên):
"Vertical 9:16 video, static eye-level camera, full-body shot. A young Vietnamese woman with [CHARACTER: long dark hair, natural makeup] wearing [PRODUCT] stands in a bright room with a wooden floor and a mirror leaning against the wall. She holds the product [and its packaging] up toward the camera with both hands, turns it slightly to show it from different angles, then lowers it and smiles at the camera. Clear product demonstration, no speech in the clip, no text, no subtitles."

Clip 2, 10 seconds (mặc lên + demo chứng minh):
"Vertical 9:16 video, static eye-level camera, full-body shot, same bright room, same woman wearing [PRODUCT]. She [DEMO: pulls the hem gently to show the fleece lining inside / stretches the fabric to show elasticity / puts on the boots and takes a few steps / pulls the tights up her leg] slowly so the viewer can see the detail clearly, then stands facing the camera and poses. Clear product demonstration, no speech in the clip, no text, no subtitles."

Ghép bằng: ~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4

Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi đến văn
bản mô tả clip đó.
