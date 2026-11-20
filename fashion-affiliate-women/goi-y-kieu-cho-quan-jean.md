# Gợi ý chọn kiểu cho quần jean suông thêu ngựa đen

Ngày lập: 2026-11-19 (tối). Dựa trên bảng 14 kiểu đã lưu ở
`phong-cach-lua-chon.md` + các quy tắc user đã chốt hôm nay cho riêng
quần jean này: đời sống candid (đi bộ / ngồi quán / làm việc khác,
không tạo dáng nhìn camera), góc quay RỘNG toàn thân (quần chiếm nửa
dưới khung hình, không thì nhìn như giới thiệu áo), giữ nguyên tuyệt
đối sản phẩm — chỉ 1 hình thêu ngựa nhỏ màu vàng đồng ở mép trên túi
trước bên PHẢI (bên tay cầm cà phê), đùi/ống/gấu trơn hoàn toàn.

## 3 kiểu hợp quần jean nhất

### 1 — Đi bộ về phía camera + xoay người (Tô Thu Hà, template 01/03)
- Kiểu đã làm ra bản v4 vừa giao (`output/video-jean-den-wide-v4-16s.mp4`,
  16,50s, 720x1280): đi bộ tới ghế dài rồi ngồi xuống, ngựa đúng túi
  phải, đã phóng to kiểm chứng ở 10,5s / 13s / 16s.
- Hợp vì: toàn thân góc rộng, candid, khoe được phom ống suông khi đi.

### 2 — Ngồi quán cà phê bên cửa sổ (Tô Thu Hà, template 02)
- Đúng gu user đã nói ("ngồi quán, đang làm việc khác"): ngồi uống cà
  phê đá, lướt điện thoại, cười — không tạo dáng.
- Hợp vì: tư thế ngồi duỗi chân khoe được độ dài + ống suông của quần;
  đã từng làm ở bản candid, chỉ cần giữ góc rộng toàn thân.

### 11 — Tips "1 món mặc nhiều kiểu" chia đôi màn hình (Nhun Lên Đồ, template 14)
- Viral nhất cả 4 kênh (3,3 triệu lượt xem với cardigan; dây cột tóc
  thành áo yếm cũng 3,3 triệu). Áp cho jean: cùng 1 quần, đổi áo phối
  (kiểu 1: sơ mi xanh nhạt như ảnh mẫu; kiểu 2: áo thun trắng sơ vin).
- Hợp NHẤT cho riêng món này vì: 2 clip cùng dáng đứng, cùng góc quay,
  cùng phòng — chỉ đổi áo, quần giữ nguyên tuyệt đối. Né được đúng lỗi
  đã gặp ở v2/v3: quần đổi không khớp qua mối nối, ngựa mọc thêm
  (clip f02b có tới 3 hình thêu ở frame đầu). Chia đôi làm ở editor,
  không concat.

## 2 kiểu nên bỏ qua với quần jean này

- **7 — Giơ đồ rồi mới mặc (Thanh Huyền, template 10):** đã làm thử
  hôm nay, user chê "nhìn k được tự nhiên". Đừng chọn lại cho jean.
- **13 — Try-on đứng tạo dáng + hook "🗣️: ..." (Nhun Lên Đồ):**
  try-on thuần lượt xem thấp (258–5,7K), lại là tạo dáng — ngược gu
  candid của user.
- **4, 5, 6, 9, 10:** cận mặt / lookbook tạo dáng chậm / nói trực
  tiếp / demo phụ kiện / Trước-Sau định hình — không bán được quần
  ống suông, hoặc không phải món này.

## Prompt nháp sẵn cho kiểu 11 (chỉ chạy khi user chọn)

Theo template 14, điền sẵn [ITEM] = quần jean đen AN TÂY STORE68.
2 clip x 10s, cùng phòng sáng tường trắng / sàn gỗ, cùng dáng đứng,
máy tĩnh toàn thân:

- Clip 1: quần jean + sơ mi xanh nhạt (như ảnh mẫu), đứng giữa phòng,
  xoay chậm khoe nghiêng rồi quay lại.
- Clip 2: CÙNG quần jean đó + áo thun trắng sơ vin, cùng vị trí, cùng
  góc, cùng động tác xoay.
- Cả 2 clip kèm câu giữ nguyên sản phẩm bắt buộc + mô tả ngựa: "one
  small gold-bronze horse embroidery on the upper edge of the RIGHT
  front pocket only; thigh, leg and hem completely plain".
- Ghép: đặt 2 clip cạnh nhau trong editor + chữ "Mặc đúng" / "Mặc theo
  tui" — KHÔNG dùng concat.sh.
- Thứ tự gửi mỗi clip: ảnh nhân vật trước, ảnh sản phẩm sau, rồi prompt.

## Chờ user

User chỉ cần nhắn số, ví dụ "1, 11" — làm theo số đã lưu trong
`phong-cach-lua-chon.md`. Chưa sinh clip nào thêm.
