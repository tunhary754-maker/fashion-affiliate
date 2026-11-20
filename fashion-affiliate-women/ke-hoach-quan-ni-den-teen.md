# Kế hoạch reel quần nỉ ống rộng ĐEN bản teen — kiểu 1 (đi bộ phố, góc rộng toàn thân)

Chuẩn bị ngày 2026-11-20 (chưa chạy — chờ user nhắn đồng ý trong side chat).
Ảnh sản phẩm: `input/quan-ni-ong-rong-den.jpg` (đã có từ 11:38).
Ảnh nhân vật: `character-reference/mau-teen-quan-ni.jpg` (cùng mẫu teen ~14 tuổi
đã dùng cho bản xám teen, để 2 màu nhất quán).

## Vì sao làm bản này tiếp

- Quần có 2 màu, bản xám teen đã giao 11:51 (`output/video-quan-ni-xam-teen-16s.mp4`,
  16s, đã kiểm chứng). Bản đen chưa làm — phân tích ghi rõ "Bản đen chưa làm
  (dùng lại cùng nhân vật teen khi làm)".
- Assistant đã hỏi user về bản đen lúc 11:42, user chưa trả lời mà chuyển sang
  phân tích rồi xem kênh mới; không phải user từ chối.

## Đã kiểm chứng trước khi làm (từ phan-tich-quan-ni-ong-rong.md)

- Đen than hơi có vân tiêu, KHÔNG phải đen trơn tuyệt đối — cần ánh sáng ngoài
  trời SÁNG, không quay trong ánh sáng yếu (đen dễ bệt, mất phom).
- Dây rút ĐEN, đầu dây có đầu kim loại MÀU BẠC — điểm khác biệt duy nhất với
  bản xám (dây trắng, đầu trơn) ngoài màu vải. Prompt phải ghi rõ chi tiết này.
- Ống rất rộng, suông thẳng, dài phủ giày; túi chéo 2 bên; đường may dọc ngoài
  ống; hoàn toàn trơn, không logo — cả mặt trước lẫn mặt sau.
- Quần trơn nên góc quay lưng ĐI RA XA làm được (khác quần jean thêu ngựa) —
  đã kiểm chứng ở bản xám: mặt sau trơn đúng mẫu.

## Quy tắc rút ra từ bản xám teen (bắt buộc)

- Kiểu 1, template 03; nhân vật teen ~14 tuổi; bối cảnh phố trà sữa; đạo cụ
  TRÀ SỮA thay cà phê cho hợp tuổi teen.
- Quần thì toàn thân góc RỘNG, quần chiếm nửa dưới khung hình.
- Mọi prompt có câu giữ nguyên sản phẩm bắt buộc.
- Cả 2 clip bản xám teen đều bắt đầu đứng yên ~2s → CẮT 2s đầu mỗi clip
  trước khi ghép; dự kiến còn ~16s.
- Kiểm chứng: phóng to vùng cạp/dây rút + ĐẾM đúng 2 dây rút, thấy đầu kim
  loại bạc ở frame đầu mỗi clip; kiểm tra ống trơn, không logo, không thêm
  chi tiết; kiểm tra mối nối.

## Mô tả sản phẩm (dùng chung cả 2 clip)

Charcoal-black heather wide-leg fleece sweatpants, high elastic waist, very
wide straight legs, full length covering the shoes, two BLACK drawstrings at
the front with SILVER metal tips, slanted side pockets, outer side seam on
each leg, soft heather fleece fabric, completely plain with no logo, no text,
no pattern, no embroidery. Match the product reference photo EXACTLY: same
colour, same cut, same stitching, same details in the exact same positions.
Do not redesign, recolour, add, remove or move any detail.

Outfit: fitted long-sleeve top in mauve, chunky light sneakers, same as the
product photo styling — but with the BLACK sweatpants from the product photo.

## Clip 1 — 10s, đi bộ phố về phía camera

Thứ tự gửi: ảnh nhân vật trước, ảnh sản phẩm sau, rồi prompt.

"Vertical 9:16 video, static eye-level camera, wide full-body shot, pants
filling the lower half of the frame. A Vietnamese teenage girl around 14
years old with long dark hair, natural look, wearing [PRODUCT as above],
walks slowly toward the camera at a three-quarter front angle along a bright
sunny street outside a milk tea shop, natural daylight, holding a cup of milk
tea in her right hand. She smiles gently as she walks, the very wide-leg
fabric moving naturally with each step. Calm, candid everyday mood, no text,
no subtitles, no speech, no voiceover. Match the product reference photo
EXACTLY: same colour, same cut, same stitching, same details in the exact
same positions. Do not redesign, recolour, add, remove or move any detail."

## Clip 2 — 10s, đi ra xa quay lưng nhìn lại

"Vertical 9:16 video, static eye-level camera, wide full-body shot, same
teenage girl wearing [PRODUCT as above], walking away from the camera along
the same bright milk-tea street, then turning her head back with a light
smile, holding a cup of milk tea. The back of the pants is completely plain.
Same bright daylight, same street setting as clip 1. Calm, candid everyday
mood, no text, no subtitles, no speech, no voiceover. Match the product
reference photo EXACTLY: same colour, same cut, same stitching, same details
in the exact same positions. Do not redesign, recolour, add, remove or move
any detail."

## Ghép + kiểm chứng

- Cắt 2s đầu đứng yên mỗi clip, ghép bằng
  `~/workspace/fashion-affiliate/scripts/concat.sh` → dự kiến
  `output/video-quan-ni-den-teen-16s.mp4`.
- Kiểm chứng trước khi giao: phóng to vùng cạp ở frame đầu + giữa mỗi clip,
  đếm đúng 2 dây rút đen có đầu kim loại bạc; ống trơn, không logo; kiểm tra
  mối nối đi tới → đi ra xa.

## Câu POV + caption gợi ý (thêm ở editor lúc đăng)

- "POV: Quần nỉ ống rộng màu đen mặc đi trà sữa với bạn là auto thành nhân vật chính."
- "POV: Tìm được chiếc quần vừa rộng vừa thoải mái, mặc đi học đi chơi đều hợp."
- Caption: "Quần nỉ ống rộng cho teen đi học đi chơi đều hợp 🥤 #viral #outfitideas #goiyphoido #xuhuong #quanniong #thoitrangteen"

## Chưa biết — không bịa vào caption

Tên sản phẩm, giá, size, thành phần vải, có lót trong hay không (như đã ghi
trong phân tích).
