# Fashion Affiliate Women — Video Reels Thời Trang Nữ

Project cho skill `fashion-affiliate-women`: video affiliate quần áo
thời trang nữ cho Facebook Reels / TikTok, theo 4 phong cách quan sát
từ tổng cộng 487 Reels: Tô Thu Hà (35 reel, đời sống im lặng),
Thảo Nhi Shop (32 reel, lookbook trong nhà + nói trực tiếp),
Thanh Huyền (40 reel, review giơ đồ trong phòng cố định),
Nhun Lên Đồ (35 reel, tips phối đồ chia đôi màn hình),
Thuỷ Thuỷ Boutique (1 reel), Ninh Anh (30 reel, nhảy nhẹ/lip-sync),
Khánh Chi Daily (17 reel, chuỗi Look theo ngày),
Lê Khánh Vân (40 reel, lụa sang ngoài phố),
Phối Đồ Cùng Mei (40 reel, mở đầu đồ ngủ → outfit công sở),
NuocLoc7Mao (30 reel, OOTD + so sánh mùa),
Huyền Kem (30 reel, review lồng tiếng + chuỗi đếm ngược Tết),
Thảo Nguyên Daily (1 reel), Lương 5 triệu mặc gì đây ? (1 reel),
Machi.clo (35 reel, đi bộ + giơ đồ trong hành lang),
Hoàng Liên Hoa (40 reel, one-take im lặng + chuỗi sưu tập),
Vũ Thị Linh (40 reel, "Chọn đi" hai phong cách),
Thảo Vy (40 reel, quần tất làm nhân vật chính + unboxing).
Xem các file `analysis-*.md` để biết chi tiết.

- `prompts/` — 24 template: 01 sân thượng quán cà phê, 02 ngồi quán
  cạnh cửa sổ, 03 đi bộ trên phố, 04 sân pickleball, 05 cận mặt hài,
  06 giơ hàng lên trước rồi mặc lên sau, 07 lookbook trong nhà,
  08 trình bày trực tiếp (user thu voiceover sau), 09 ngồi ghế sau
  ô tô, 10 giơ đồ rồi mặc trong phòng ấm cố định, 11 cận cảnh chứng
  minh chất liệu, 12 demo phụ kiện trên người, 13 Trước/Sau mặc
  chia đôi màn hình (ghép ở editor), 14 tips "1 món mặc nhiều kiểu"
  chia đôi màn hình, 15 nhiều look trong 1 reel, 16 review lồng
  tiếng "Chấm điểm", 17 mở đầu đồ ngủ → cắt sang outfit, 18 chuỗi
  đếm ngược Tết, 19 nhảy nhẹ/lip-sync trong phòng, 20 đi bộ + giơ
  đồ trong 1 reel, 21 phụ kiện làm nhân vật chính thử theo biến
  thể, 22 mở hộp rồi mặc thử, 23 chuỗi sưu tập đánh số "Tủ đồ 100
  chiếc [món]", 24 "Chọn đi" hai phong cách đối lập.
- `phong-cach-lua-chon.md` — bảng chọn 25 kiểu theo số.
- `tong-hop-skill-theo-trang-phuc.md` — tổng hợp kiểu làm video
  theo từng loại trang phục bán.
- `input/` — ảnh sản phẩm của từng job (không commit lên repo công khai).
- `character-reference/` — ảnh nhân vật chuẩn của kênh (không commit).
- `output/` — clip và video đã ghép (không commit).
- Script ghép dùng chung: `~/workspace/fashion-affiliate/scripts/`
  (`concat.sh` cho 2–3 clip 10s; template 13, 14 ghép chia đôi ở editor).

Skill dùng trong chat: `~/workspace/custom-skills/fashion-affiliate-women/SKILL.md`.
Luồng chat-native, không cookie login, không gateway.
Video sinh ra luôn sạch (không chữ, không lời); chữ POV, chữ tên sản
phẩm, chữ Trước/Sau, caption, hashtag, nhạc, voiceover do user thêm
ở editor lúc đăng.
