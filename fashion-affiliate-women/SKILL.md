# Video Affiliate Thời Trang Nữ — Phong Cách Reels

Làm video affiliate quần áo thời trang nữ cho Facebook Reels (và
TikTok) theo 4 phong cách đã quan sát từ tổng cộng 487 Reels: Tô Thu
Hà (35 reel), Thảo Nhi Shop (32 reel), Thanh Huyền (40 reel), Nhun
Lên Đồ (35 reel), Thuỷ Thuỷ Boutique (1 reel), Ninh Anh (30 reel),
Khánh Chi Daily (17 reel — toàn bộ kênh), Lê Khánh Vân (40 reel),
Phối Đồ Cùng Mei (40 reel), NuocLoc7Mao (30 reel), Huyền Kem
(30 reel), Thảo Nguyên Daily (1 reel), Lương 5 triệu mặc gì đây ?
(1 reel), Machi.clo (35 reel), Hoàng Liên Hoa (40 reel), Vũ Thị
Linh (40 reel), Thảo Vy (40 reel). Chi tiết phân tích ở
`~/workspace/fashion-affiliate-women/`:
`analysis-to-thu-ha-reels.md`, `analysis-thao-nhi-shop-reels.md`,
`analysis-thanh-huyen-reels.md`, `analysis-nhun-len-do-reels.md`,
`analysis-reel-1479507580953286.md`,
`analysis-ninh-anh-reels.md`, `analysis-khanh-chi-daily-reels.md`,
`analysis-le-khanh-van-reels.md`,
`analysis-phoi-do-cung-mei-reels.md`,
`analysis-nuocloc7mao-reels.md`, `analysis-huyen-kem-reels.md`,
`analysis-reel-1840153680605228.md`,
`analysis-reel-1734056391187699.md`,
`analysis-machi-clo-reels.md`, `analysis-hoang-lien-hoa-reels.md`,
`analysis-vu-thi-linh-reels.md`, `analysis-thao-vy-reels.md`. TikTok @quynhtrang3108_
("Chang mặc gì ?") chưa xem được video nào do TikTok chặn (403) —
chỉ ghi lại được lưới 35 video, xem
`analysis-quynhtrang3108-tiktok.md`; chưa đưa gì từ kênh này vào
skill.

Thư mục project: `~/workspace/fashion-affiliate-women/` — `prompts/`,
`input/`, `character-reference/`, `output/`. Script ghép dùng chung
của project fashion-affiliate: `~/workspace/fashion-affiliate/scripts/`.

Skill này KHÁC skill `fashion-affiliate` (đồ trẻ em, studio/flatlay,
khoe chi tiết sản phẩm). Skill này KHÔNG dùng cookie login, KHÔNG
dùng gateway: clip sinh trong chat này, ghép bằng ffmpeg. Không trộn
với luồng gateway trong 1 job.

## Bốn phong cách (chọn 1 mỗi video, không trộn trong 1 reel)

### A. Đời sống im lặng (Tô Thu Hà, Thuỷ Thuỷ)

- Bối cảnh đời thường THAY ĐỔI: quán cà phê, đường phố, sân
  pickleball, trong ô tô, vườn, phòng ngủ — ánh sáng ban ngày tự
  nhiên, không studio.
- Chỉ có nhạc, không nói với camera, không lồng tiếng bán hàng
  (24/25 reel bổ sung của Tô Thu Hà).
- Động tác: đi bộ về phía camera, xoay người khoe trước/nghiêng/
  sau, quay lưng nhìn qua vai; biến thể: đi lùi ra xa, đi bộ quay
  lưng ra xa, ngồi ghế sau ô tô, ngồi bàn ăn.
- Chữ POV trên màn hình chỉ là 1 DẠNG HOOK, không phải quy tắc:
  đa số reel thời trang KHÔNG có chữ nào trên video, chỉ có caption
  ngắn + hashtag. Khi có chữ thì thường là câu POV hài, câu đùa,
  hoặc thông tin ngắn của phụ kiện (dáng kính, chống tia UV).
- CTA: banner "Đủ điều kiện nhận tiền hoa hồng" + hashtag trong
  caption; một số caption nói "chốt ngay", "+1 em… nên có trong
  tủ đồ". Không ghi giá/mã/size.
- Bổ sung đợt 2 — Lê Khánh Vân (19K followers, 40 reel): phong
  cách A thuần túy nhất — lụa/satin "sang", đi bộ ngoài phố, im
  lặng 100%, KHÔNG có chữ trên màn hình trong cả 40 reel. Bối cảnh
  mới: trước cửa hàng hiệu (Prada), thang cuốn trung tâm thương
  mại, phòng trà. 1 outfit (corset ren trắng + váy lụa sâm panh)
  tái dùng 3 reel, cả 3 đều nằm trong top 5 lượt xem của kênh
  (81K/98K/197K) — bằng chứng mạnh nhất cho quy tắc 1 outfit →
  3–4 reel.

### B. Lookbook trong nhà + nói trực tiếp (Thảo Nhi Shop)

- Bối cảnh CỐ ĐỊNH: cùng 1 phòng trong nhà, ánh sáng vàng ấm, sàn
  gỗ, tủ gỗ, sofa trắng. Máy tĩnh ngang tầm mắt, khung toàn thân
  ở giữa, 1 cảnh quay liên tục.
- Khoảng 60% chỉ nhạc: tạo dáng chậm, xoay lưng/nghiêng, nhìn qua
  vai, tay đặt eo hoặc vuốt tóc.
- Khoảng 40% NÓI trực tiếp với camera: vừa nói vừa giơ váy/áo
  trên móc, chạm vào ren, cổ áo, đai, vạt peplum để chỉ chi tiết.
- LƯU Ý QUAN TRỌNG: video sinh ra vẫn SẠCH, không có lời nói.
  Phần "nói trực tiếp" là do USER TỰ THU voiceover/lồng tiếng
  sau khi có video — template 08 chỉ đạo diễn xuất trình bày
  (giơ đồ, chạm chi tiết, cử chỉ như đang giới thiệu). Không sinh
  video có tiếng nói giả.
- Không ghi giá/mã/size trên màn hình; chốt đơn ngầm qua bình
  luận/inbox.
- Bổ sung đợt 2 — 2 biến thể mới của lookbook phòng cố định:
  (1) Nhảy nhẹ/lip-sync theo nhạc (Ninh Anh, 16K followers, 30
  reel): phòng cố định, máy tĩnh, góc máy hơi thấp, mẫu nhảy nhẹ/
  lắc hông/nhún vai theo nhạc, lip-sync, giơ tay hình trái tim;
  2/5 reel cao nhất kênh là dạng này. Biến thể selfie trước gương
  phòng gym cho đồ tập (13K lượt xem). Template 19. (2) Mở đầu
  đồ ngủ nói chuyện → cắt cảnh sang outfit (Phối Đồ Cùng Mei,
  39K followers, 40 reel): mở đầu mặc đồ ngủ xuề xòa nói chuyện
  với camera, cắt cảnh ngay tại chỗ sang outfit chỉn chu trên
  nền nhạc; độ tương phản "xuề xòa → sang" là cú hook. Video
  sinh ra vẫn SẠCH — lời nói do user thu voiceover sau, như
  template 08. Template 17. Ngách đồ công sở của Mei (blazer,
  chân váy dài đuôi cá, áo satin thắt nơ) với thông điệp "sang,
  thanh lịch, hack tuổi" trên ngân sách thấp ("lương 3tr/5tr").
- Bổ sung đợt 3 — 2 biến thể mới của phòng cố định im lặng:
  (1) One-take im lặng + chuỗi sưu tập đánh số (Hoàng Liên Hoa,
  6,7K followers Facebook, TikTok 1,2M, 40 reel): chỉ 3 bối cảnh
  cố định (phòng rèm voan, khung cửa gỗ, sân gỗ nhà gỗ), 1 reel =
  1 outfit = 1 take liên tục, im lặng 100%, nhún nhảy nhẹ tại
  chỗ, kéo gấu áo khoe độ ôm, quay lưng khoe lưng trần (reel áo
  lụa hở lưng 6,8K like — cao nhất kênh). Series "Tủ đồ 100
  chiếc áo tay dài" đánh số Chiếc số 1/2 + tự nhận "đại sứ áo
  tay dài". Template 23. (2) Vlog thử đồ ở phòng thử đồ + câu
  hỏi chọn 2 phong cách (Vũ Thị Linh, 21K followers, 40 reel):
  voiceover tiếng Việt kể chuyện thử đồ ở studio, POV cầu thang
  + selfie gương, hỏi "bánh bèo hay xì lay" (162K lượt xem);
  biến thể Tết mặc cả 2 look (áo dài và bà ba) trong 1 reel,
  hỏi "Team áo dài hay bà ba" (133K). Video sinh ra vẫn SẠCH —
  lời nói do user thu voiceover sau. Template 24.

### C. Review giơ đồ trong phòng cố định (Thanh Huyền)

- Bối cảnh CỐ ĐỊNH HƠN CẢ B: đúng MỘT góc phòng cho cả 40 reel —
  sofa trắng, rèm tối, đèn đứng ánh vàng, hộp hoa hồng trên tay
  vịn sofa. Không đổi góc máy, không đổi đạo cụ.
- Công thức cốt lõi: "giơ đồ rồi mới mặc" (22/40 reel) — giơ món
  đồ che trước người, mặt vẫn thấy ở phía trên món đồ (có khi treo
  trên móc, có khi áp sát vào người để so độ dài/dáng), rồi cắt
  sang cảnh đã mặc, xoay nhẹ.
- Chuyển động tối thiểu, sản phẩm làm trung tâm: đứng yên, đu đưa
  nhẹ, xoay chậm, cầm váy, chỉnh cạp/quai. Không đi bộ lifestyle.
- Im lặng 100%: nhạc nền, không nói chuyện trước máy quay trong cả
  40 reel (khác B có ~40% nói).
- Cận cảnh CHỨNG MINH, không phải cận cảnh khoe: tay sờ vải/cúc,
  kéo giãn gấu áo chứng minh co giãn, kéo nhẹ gấu áo khoe độ ôm
  ở eo.
- Demo phụ kiện trên người: ngồi kéo quần tất lên chân, cầm phụ
  kiện trước người để cho thấy công dụng ngay trên cơ thể.
- Chữ trên màn hình hiếm (5/40) nhưng hiệu quả: 3 trong 5 reel có
  chữ nằm trong top lượt xem — chữ tên sản phẩm + thương hiệu
  ("Bodysuit 2 dây cổ U HANA LADY"), chữ "Trước mặc / Sau mặc"
  chia đôi màn hình, end-card khoanh đỏ link. Chữ thêm ở editor,
  không sinh cùng video.
- Caption rập khuôn 1 mẫu: "Link mua [món đồ] - Shopee: [link] —
  Bấm vào link để xem chi tiết và mua hàng." Biến thể: chia link
  (món chính ở caption, món còn lại "để ở Bình luận") hoặc để toàn
  bộ link ở bình luận (gắn góc "outfit đón Tết, dự tiệc").
- Hàng hóa rộng: ngoài đầm/áo/set đồ còn có đồ ngủ, đồ mặc nhà,
  phụ kiện chức năng (đai chống gù, quần tất, miếng dán ngực, quần
  độn hông), máy uốn tóc — và các reel phụ kiện chiếm 4/5 vị trí
  top lượt xem của kênh.
- Bổ sung đợt 2 — Review lồng tiếng "Chấm điểm" (Huyền Kem, 10K
  followers, 30 reel): 14/30 reel có GIỌNG NÓI LỒNG TIẾNG giới
  thiệu/đánh giá sản phẩm trong lúc người mẫu tạo dáng — KHÔNG
  nói trực tiếp vào camera. Format "Chấm điểm [sản phẩm]", tên
  sản phẩm + thương hiệu ghi rõ trên màn hình. Demo mới: giơ bao
  bì sản phẩm lên camera, kéo vạt áo khoe lớp lót lông bên trong.
  Video sinh ra vẫn SẠCH — lời lồng tiếng do user thu sau.
  Template 16. Phụ kiện chức năng lại chiếm top: 2/3 reel cao
  nhất kênh là về quần tất (737K, 292K lượt xem) — khớp bài học
  ở Thanh Huyền.
- Bổ sung đợt 3 — 3 biến thể mới của phòng cố định: (1) Lai đi
  bộ + giơ đồ trong 1 reel (Machi.clo, shop 4,9K followers, 35
  reel): hành lang hẹp tường trắng làm studio cố định, đi dọc
  hành lang rồi giơ chính món đang mặc lên cận cảnh chất vải —
  giơ đồ là 1 nhịp trong reel mặc đồ, không phải toàn bộ reel.
  Reel cao nhất kênh 159K lượt xem. Template 20. (2) Review im
  lặng bằng chữ trên màn hình thay đổi giữa reel (Thảo Vy, 64K
  followers, 40 reel): quần tất/legging làm nhân vật chính, thử
  qua 2–3 outfit trong 1 reel, chữ đổi từ tên shop + mã sang câu
  lợi ích ("Độ D càng thấp độ trong càng cao"). 3/5 top kênh là
  reel quần tất (410K, 132K, 121K). Template 21. (3) Unboxing
  thành format riêng rồi nối tiếp bằng reel try-on (Thảo Vy):
  thùng carton/bưu kiện làm đạo cụ, mở hộp giơ đồ lên, reel sau
  mặc thử ("Try on 2 set trong vid unbox mí bà nè"). Template 22.

### D. Tips phối đồ chia đôi màn hình + try-on phòng cố định (Nhun Lên Đồ)

- Bối cảnh CỐ ĐỊNH: đúng MỘT phòng sáng cho cả 35 reel — tường
  trắng, sàn gỗ nâu, tủ trắng có đèn bàn, cửa gỗ. Mẫu gần như luôn
  chân trần, đứng cùng một góc phòng. Máy tĩnh, khung toàn thân.
- Im lặng 100%: chỉ nhạc nền, không nói chuyện trước máy quay
  trong cả 35 reel. Ký tự "🗣️:" chỉ là chữ trên màn hình, không
  phải lời nói thật.
- Dạng VIRAL nhất trong cả 4 kênh: tips/hack "1 món mặc nhiều
  kiểu" với màn hình chia đôi — "Mặc đúng / Mặc sai", "Mặc đúng
  HDSD / Mặc sai HDSD" (reel 2, 3: cùng 3,3 triệu lượt xem; reel 1:
  1,1 triệu). Dạng try-on đồ ngủ thông thường chỉ đạt 258–5,7K
  lượt xem dù đăng rất nhiều — mẹo có giá trị dùng lại được thắng
  try-on thuần túy.
- Chữ hook câu hỏi trên màn hình gần như reel nào cũng có: "🗣️:
  [câu hỏi / tình huống]..." — là 1 dạng hook chữ riêng, khác POV
  hài của Tô Thu Hà và chữ tên sản phẩm của Thanh Huyền. Thỉnh
  thoảng có nhãn "LOOK 1 / LOOK 5", "Unbox đồ mới".
- Dạng nhiều look trong 1 reel: "7 ngày không trùng outfit",
  "LOOK 1... LOOK 5", "Lên 5 outfit với áo len" — cùng nhân vật,
  cùng góc phòng, chỉ đổi outfit (template 15).
- Chủ yếu mặc sẵn rồi tạo dáng, KHÔNG giơ đồ lên trước (chỉ 3/35
  reel giơ đồ, 1 reel unbox). Không có cận cảnh vải/chi tiết.
- Sản phẩm áp đảo là đồ ngủ/pyjama (khoảng 25/35 reel: lụa satin,
  kẻ sọc, pastel, hoa nhỏ). Try-on đồ ngủ thuần túy lượt xem thấp
  — nếu làm đồ ngủ thì nên gắn với tips hoặc nhiều look.
- CTA yếu nhất trong 4 kênh: không link Shopee, không inbox, chỉ
  caption hỏi ngược khán giả ("Phối ... như này ổn k mấy bà", "Gu
  bà nào đâyy") + hashtag cố định #nhunlendo #phoidoxinh #ootd
  #xuhuong #mixandmatch. Gần như mọi reel đều gắn #sponsoredcontent.
- CẢNH BÁO — lỗi KHÔNG học theo: kênh này dùng lại caption/chữ
  trên màn hình không khớp sản phẩm trong video rất thường xuyên
  (chữ nói cardigan/chân váy/áo dài trong khi mẫu mặc đồ ngủ).
  Chữ và caption PHẢI khớp đúng món đồ trong video.
- Reel phụ kiện có demo/giơ đồ lại thắng try-on thuần: reel giơ
  quần tất đạt 1,2K like, cao nhất nhóm đồ ngủ — khớp bài học ở
  Thanh Huyền.
- Bổ sung đợt 2 — 2 biến thể mới của tips/nhiều look: (1) Chuỗi
  "1 món mặc cả tuần" theo ngày/dịp (Khánh Chi Daily, 1,5K
  followers, 17 reel — toàn bộ kênh): cùng 1 món đồ chủ đạo, mỗi
  reel 1 Look, đánh số Look 1/2 và nhãn ngày/dịp (Monday, Đi cà
  phê, Tết); chữ trên màn hình nêu tên món + câu hỏi gợi mở trong
  gần như mọi reel. Reel cao nhất 197K lượt xem với hook "Vắt
  kiệt giá trị với chân váy iu thích" — hook + cấu trúc quan
  trọng hơn lượng followers. Đây là dạng CHUỖI nhiều reel của
  template 15. (2) Chia đôi SO SÁNH MÙA/DỊP (NuocLoc7Mao, 53K
  followers, 30 reel): cùng 1 món đồ qua 2 mùa hoặc 2 dịp
  (Thu/Đông vs Tết, Thu/Đông vs Xuân/Hạ) — biến thể của template
  14, 1 reel dạng này đạt 342K lượt xem. Kênh này cũng có try-on
  áo dài Tết có nhãn riêng và hook giá trị "Là mua 1, được 2,
  phối ra 5 outfits".

### Cầu nối giữa các phong cách: giơ hàng lên trước, mặc lên sau

Giơ sản phẩm lên bằng 2 tay khoe chi tiết (túi, logo, tag) rồi
cắt sang cảnh mặc lên người — vừa khoe được chi tiết như Thảo
Nhi, vừa giữ cảm giác đời thường im lặng như Tô Thu Hà
(template 06). Ở phong cách C, "giơ đồ" không còn là cầu nối mà
là công thức chính của cả kênh (template 10).

## Những gì đã sửa sau khi xem đủ 30–40 reel/kênh

- Chữ POV KHÔNG phải lúc nào cũng có — bản đầu của skill viết
  như quy tắc, đã sửa: POV là 1 lựa chọn hook, mặc định video
  không có chữ, caption mới là chỗ bán hàng bằng lời.
- "Không có cận cảnh" chỉ đúng với váy/đầm ở phong cách A (không
  cận chất liệu vải để khoe). Đã có cận cảnh ở phụ kiện và đồ giơ
  lên: tay cầm kính cận cảnh, giơ áo phao thấy cả tag size. Ở
  phong cách C, cận cảnh là BẰNG CHỨNG: tay sờ vải/cúc, kéo giãn
  gấu áo chứng minh co giãn, kéo nhẹ gấu áo khoe độ ôm ở eo.
- 1 outfit tái dùng tới 3–4 reel (set vàng nhạt 4 reel, corset
  đen 3 reel, kính 3 reel), không chỉ 2–3.
- Có nhóm nội dung đời sống/hài không bán hàng (food reviewer,
  pijama, câu đùa, vlog sự kiện) — chỉ dùng làm reel câu tương
  tác (template 05), không phải template bán hàng.
- Chữ tên sản phẩm + thương hiệu trên màn hình (phong cách C)
  tương quan với lượt xem cao: 3/5 reel có chữ nằm trong top
  lượt xem của Thanh Huyền. Chữ này thêm ở editor, video sinh ra
  vẫn sạch.
- Reel phụ kiện chức năng có demo trên người (quần tất, miếng dán
  ngực, quần độn hông) chiếm 4/5 top lượt xem của Thanh Huyền —
  demo công dụng bán tốt hơn lookbook thuần túy ở kênh này.
- Dạng tips "1 món mặc nhiều kiểu" chia đôi màn hình là dạng có
  lượt xem vượt trội nhất trong cả 4 kênh (3,3 triệu, Nhun Lên Đồ)
  — đã có template riêng (template 14).
- Hook chữ dạng câu hỏi "🗣️: ..." gần như có ở mọi reel của Nhun
  Lên Đồ — là 1 dạng hook chữ riêng, thêm vào mục chữ/caption.
- Reel nhiều look trong 1 video ("7 ngày không trùng outfit",
  "LOOK 1... LOOK 5") là 1 dạng nữa của Nhun Lên Đồ (template 15).
- Try-on đồ ngủ thuần túy lượt xem thấp (258–5,7K) — nếu làm đồ
  ngủ thì gắn với tips hoặc nhiều look, đừng chỉ đứng tạo dáng.
- Chữ/caption KHÔNG khớp món đồ trong video là lỗi sản xuất hàng
  loạt của Nhun Lên Đồ — không học theo: chữ và caption phải khớp
  đúng món đồ trong video.
- Chuỗi đếm ngược Tết là format chuỗi theo mùa rõ ràng nhất đợt
  2: 3 kênh cùng làm (Huyền Kem "Đếm ngược 78–84 ngày đến Tết
  2027 | P3–P9", NuocLoc7Mao "Còn 88 ngày nữa là đến Tết", reel
  lẻ "còn 140 ngày nữa đến Tết 2027, ngày 1") — đăng từ hàng
  tháng trước Tết, đánh số phần/ngày. Template 18.
- Review bằng lồng tiếng trên cảnh tạo dáng (Huyền Kem) là dạng
  thứ ba của "nói": khác nói trực tiếp (template 08) và im lặng
  hoàn toàn — video sinh ra vẫn sạch, user thu voiceover sau.
  Template 16.
- Hook đối chiếu ngân sách ("Lương 5tr nhưng sang như quý cô
  50tr"), hook giá trị ("Vắt kiệt giá trị với [món]", "Mua 1,
  được 2, phối ra 5 outfits"), hook phủ định ("Đừng mặc [món] như
  thế này", "tuyệt đối đừng mặc kiểu này ❌"), hook câu thoại
  kịch ("Đừng đi chơi với anh nữa..."), hook hối tiếc ("Hối hận
  vì k mua sớm 😢"), công thức caption "Team mê [món]…" — thêm
  vào mục chữ/caption.
- CTA có thêm biến thể: link mua ở BÌNH LUẬN (Phối Đồ Cùng Mei,
  ghi trong tiểu sử), link gắn ở GÓC TRÁI video + bình luận
  (Huyền Kem), mã giảm trong bio (Ninh Anh).
- Công khai số đo/dáng người là yếu tố tin cậy lặp lại: Nhun
  (1m60-49kg), NuocLoc7Mao (1m62-45kg), Huyền Kem ghi cả dáng
  "1m62 - 48kg, Dáng HCN" ngay trên màn hình.
- Kênh nhỏ vẫn có thể viral mạnh: Khánh Chi Daily 1,5K followers
  nhưng reel cao nhất 197K lượt xem; Huyền Kem 10K followers
  nhưng reel cao nhất 737K. Hook + sản phẩm đúng quan trọng hơn
  lượng followers — nhưng độ chênh lệch trong cùng 1 kênh rất lớn
  (Huyền Kem: 689 lượt xem ở reel thấp nhất vs 737K ở reel cao
  nhất), hiệu quả phụ thuộc mạnh vào sản phẩm và hook.
- Đợt 3 (2026-11-21, 155 reel, 4 kênh): quần tất/legging làm nhân
  vật chính với chữ trên màn hình thay đổi giữa reel là dạng
  review im lặng mới — Thảo Vy 410K (5D-10D-15D), 132K (legging
  bt19), 121K (quần tất len tăm T54); 3/5 top kênh. Template 21.
- Haul đánh số để đặt hàng: "Quần 1 / Quần 2", "Try on 3 jean" —
  cùng 1 áo trên, đổi nhiều quần, số thứ tự thay cho tên món
  (Thảo Vy, haul Bahychic 242K lượt xem).
- Unboxing là 1 format riêng (thùng carton/bưu kiện làm đạo cụ),
  nối tiếp bằng reel try-on riêng — Thảo Vy. Template 22.
- Chuỗi sưu tập đánh số "Tủ đồ 100 chiếc [món]" + tự nhận "đại
  sứ [món]" — Hoàng Liên Hoa. Template 23.
- Tái dùng 1 món đồ KHÔNG gắn nhãn series: cùng 1 món đăng lại
  thành nhiều reel riêng, caption khác nhau — Hoàng Liên Hoa:
  áo lụa satin xanh bạc hà 5 lần (tổng 310K lượt xem), đầm body
  đỏ rượu 4 lần (176K); Machi.clo: cùng sản phẩm đăng lại nhiều
  bản cắt (cùng caption + nhạc, mở đầu khác). Bổ sung cho quy tắc
  1 outfit → 3–4 reel: tái dùng có thể là đăng lại cùng món với
  caption/cắt khác, không nhất thiết đổi bối cảnh.
- Series biến thể màu: cùng 1 mẫu, cùng mẫu caption, khác màu,
  đăng thành reel riêng (Machi.clo: áo len trễ vai tím/xám/trắng).
- Góc quay lưng là góc BÁN CHÍNH với đồ hở lưng — Hoàng Liên Hoa:
  reel áo lụa hở lưng quay từ phía sau đạt 6,8K like, cao nhất
  kênh. Quy tắc "không quay lưng" CHỈ áp dụng khi chi tiết bán
  nằm ở MẶT TRƯỚC (thêu túi trước...); với đồ hở lưng, lưng trần
  chính là điểm bán.
- Hook theo dáng người: "Dáng tam giác ngược bơi vô đây liền
  chontui" — Vũ Thị Linh, 169K lượt xem, cao nhất kênh. Tư vấn
  theo dáng, không theo món/mùa.
- Hook theo yêu cầu khán giả: "Hôm bữa bà nào hỏi in4 em váy xanh
  nì, hôm nay tui lên video cho mấy bà luôn nha" — nội dung do
  bình luận kéo theo (Vũ Thị Linh, 58K).
- Góc mặc lại đồ cũ: "Chiếc áo tui mặc từ năm ngoái, năm nay lại
  mặc lại" — Thảo Vy, 179K lượt xem. Không phải lúc nào cũng mua
  mới.
- Hook "1 outfit cho 3 dịp" (mùa thu + noel + tết) và hook set
  mix-match ("Mua được set đồ mà có thể mixmatch thành nhìu
  outfit thì mấy bà có ưng không…", 113K) — Vũ Thị Linh.
- Chữ chứng minh chi tiết cấu tạo trên màn hình: "có đệm ngực được
  may chắc chắn", "chân váy dạ chéo (có khoá kéo hai bên)" —
  Machi.clo. Chữ không chỉ đặt tên mà CHỨNG MINH 1 chi tiết may
  mặc (chỉ ghi điều đã xác nhận).
- Tên shop + mã sản phẩm gắn ngay trên màn hình mỗi reel (Thảo
  Vy) — mỗi reel là 1 lần thử đồ theo shop, không phải lookbook
  chung chung.
- CTA tiến hóa theo thời gian (Hoàng Liên Hoa): không CTA → "để
  ở bình luận ghim" → "để ở bình luận" → "ghim sẵn dưới giỏ
  hàng". Shop bán trực tiếp dùng CTA bình luận "(.)" để báo giá
  qua inbox + gợi ý giá "3xx/2xx/1xx" và khan hiếm (Machi.clo) —
  chỉ dùng khi user là shop và xác nhận giá.
- Công khai số đo/dáng người tiếp tục lặp lại: Thảo Vy ghi
  "M60_47kg" ngay trong tiểu sử (kênh thứ 4 công khai số đo, sau
  Nhun, NuocLoc7Mao, Huyền Kem).
- Đồ ngủ CHÍNH LÀ trang phục (không phải mở đầu): Hoàng Liên Hoa
  mặc quần ngủ + áo hai dây và bộ pijama nguyên bộ, đạt 47K–83K
  lượt xem — khác try-on đồ ngủ thuần của Nhun (258–5,7K): ở đây
  đồ ngủ được phối thành outfit có chủ đích + caption/CTA rõ
  ràng. Bài học "không try-on đồ ngủ thuần" vẫn đúng; đồ ngủ cần
  được STYLING thành outfit hoặc gắn tips/nhiều look.
- Caption chỉ có emoji ("🫰✨", "✌️✨") vẫn hút xem khi hook nằm
  ở chữ trên màn hình + tên shop (Thảo Vy) — caption dài không
  phải lúc nào cũng cần.
- Chi tiết nhỏ (trang sức, khuyên tai, nhẫn, nút, họa tiết) dễ BIẾN
  MẤT giữa chừng khi nhân vật cử động — model vẽ lại từng frame
  nên chi tiết chỉ chiếm vài pixel hay bị "quên" lúc chuyển động
  nhanh (user phát hiện 2026-11-21). Khắc phục: câu giữ phụ kiện
  trong mọi prompt + mỗi clip 1 hành động chậm + cận cảnh riêng
  cho chi tiết quan trọng; kiểm chứng phải xem nhiều frame giữa
  clip, không chỉ frame đầu.

## Công thức 1 reel (phong cách A)

1. **Mở đầu:** khung hình đầu là outfit + tình huống (đi bộ,
   xoay người). Chữ POV là tùy chọn, thêm ở editor lúc đăng.
2. **Khoe đồ bằng cách mặc:** người mẫu đi bộ về phía camera,
   xoay người khoe mặt trước / nghiêng / sau, quay lưng nhìn
   qua vai, tay chống hông, vuốt tóc, cười nhìn thẳng camera —
   trong khi đang làm việc của tình huống (uống cà phê, đi dạo
   phố, ngồi xe).
3. **Không có phần "chi tiết" riêng cho váy/đầm;** phụ kiện và
   đồ giơ lên thì có cận cảnh ngắn.
4. **CTA không nói ra:** nằm ở banner hoa hồng + caption/hashtag,
   do user thêm lúc đăng.

## Công thức 1 reel (phong cách B)

1. **Mở đầu ngay bằng trang phục đang mặc,** không có móc riêng.
2. **Dạng im lặng:** tạo dáng chậm, xoay người. **Dạng nói:**
   giơ đồ trên móc, chạm/chỉ chi tiết, cử chỉ trình bày — lời
   nói do user thu voiceover sau. **Biến thể nhảy nhẹ** (template
   19): nhảy nhẹ/lắc hông/lip-sync theo nhạc trong phòng cố định.
   **Biến thể mở đầu đồ ngủ** (template 17): mở đầu đồ ngủ nói
   chuyện → cắt cảnh sang outfit trên nền nhạc.
   **Biến thể chuỗi sưu tập** (template 23): mỗi reel 1 món, cùng
   bối cảnh/góc quay, chữ "Tủ đồ 100 chiếc [món] / Chiếc số [N]"
   ở editor. **Biến thể "Chọn đi"** (template 24): 2 clip 2 phong
   cách đối lập, câu hỏi chọn ở caption; voiceover vlog tùy chọn
   do user thu sau.
3. **CTA ngầm:** caption ngắn + bình luận/inbox; không ghi
   giá/mã/size.

## Công thức 1 reel (phong cách C)

1. **Mở đầu bằng nhịp giơ đồ:** giơ món đồ che trước người, mặt
   vẫn thấy ở phía trên, xoay nhẹ cho thấy phom/dáng — hoặc giơ
   trên móc, hoặc áp sát vào người để so độ dài.
2. **Cắt sang cảnh đã mặc:** đứng yên, đu đưa nhẹ, xoay chậm khoe
   trước/nghiêng/sau. Thêm 1 nhịp chứng minh nếu món đồ có điểm
   đáng chứng minh: tay sờ vải/cúc, kéo giãn gấu áo, kéo nhẹ gấu
   áo khoe độ ôm ở eo.
3. **Phụ kiện chức năng:** demo ngay trên người thay vì chỉ giơ —
   ngồi mặc thử, cầm phụ kiện trước người, hoặc chia đôi
   Trước/Sau mặc. **Dạng lồng tiếng** (template 16): demo + giơ
   bao bì/kéo vạt khoe lót lông, giọng review lồng tiếng do user
   thu sau, chữ "Chấm điểm [sản phẩm]" ở editor.
   **Dạng lai đi bộ + giơ đồ** (template 20): đi bộ trong hành
   lang rồi giơ món đang mặc lên cận cảnh chất vải. **Dạng phụ
   kiện nhiều biến thể** (template 21): cùng 1 phụ kiện mặc qua
   2–3 outfit, chữ trên màn hình đổi theo clip để giải thích từng
   biến thể. **Dạng mở hộp** (template 22): mở thùng/bưu kiện,
   giơ đồ lên; reel mặc thử sau đó dùng template 07 hoặc 10.
4. **CTA rõ ràng nhất trong 3 phong cách:** caption mẫu link
   Shopee + có thể chia link (món chính ở caption, món còn lại
   ở bình luận) hoặc end-card khoanh đỏ link ở cuối video — làm
   ở editor lúc đăng.

## Công thức 1 reel (phong cách D)

1. **Mở đầu bằng chữ hook câu hỏi** "🗣️: [câu hỏi / tình huống]..."
   (hoặc câu mẹo "1 [món] nhưng [số] kiểu mặc...") phủ trên khung
   hình toàn thân — thêm ở editor lúc đăng.
2. **Dạng tips (template 14):** 2 clip cùng món đồ, cùng dáng, cùng
   góc — clip 1 mặc kiểu thường, clip 2 mặc kiểu mới; đặt cạnh nhau
   trong editor + chữ "Mặc đúng" / "Mặc theo tui".
   **Dạng nhiều look (template 15):** mỗi look 1 clip 10 giây, cùng
   nhân vật, cùng góc phòng, chỉ đổi outfit; nối tiếp bằng concat.sh
   + nhãn "LOOK 1/2/3" ở editor. **Dạng chuỗi nhiều reel:** 1 món
   mặc cả tuần, mỗi reel 1 Look + nhãn ngày/dịp (Khánh Chi Daily);
   chuỗi đếm ngược Tết, mỗi phần 1 outfit + số phần (template 18).
   **Dạng chia đôi so sánh mùa** (NuocLoc7Mao): cùng 1 món qua 2
   mùa/dịp (Thu/Đông vs Tết) — biến thể của template 14.
   **Dạng try-on thường:** mẫu đứng yên tại chỗ, tạo dáng/nhún nhảy
   nhẹ theo nhạc, khoe outfit đang mặc — giống template 07 nhưng
   phòng sáng trắng, không nói.
3. **CTA:** caption hỏi ngược khán giả ("Phối ... như này ổn k mấy
   bà", "Gu bà nào đâyy") + hashtag. Kênh gốc không gắn link mua
   hàng; nếu user bán affiliate thì thêm link Shopee + câu mẫu phong
   cách C vào caption — đừng học theo CTA yếu của kênh này.

## Quy tắc cứng cho mọi video

- Giữ nguyên TUYỆT ĐỐI sản phẩm trong ảnh: màu, phom, cổ áo, nút,
  logo, họa tiết — KHÔNG thay đổi bất cứ chi tiết nào của sản phẩm
  trong bất kỳ prompt nào. Mô tả sản phẩm PHẢI đọc từ ảnh gốc
  (phóng to ảnh nếu cần để thấy rõ vị trí từng chi tiết), không
  được bịa vị trí hay thêm chi tiết. Mọi prompt sinh video PHẢI
  kèm câu: "Match the product reference photo EXACTLY: same colour,
  same cut, same stitching, same details in the exact same
  positions. Do not redesign, recolour, add, remove or move any
  detail." Camera tĩnh, chuyển động chậm để chi tiết ít trôi.
- Giữ nguyên TRANG SỨC/PHỤ KIỆN như giữ sản phẩm: liệt kê từng món
  (dây chuyền, khuyên tai, nhẫn, đồng hồ, vòng tay, kẹp tóc...) kèm
  vị trí đeo. Mọi prompt PHẢI kèm câu: "Keep every accessory
  exactly as in the reference photos: [ACCESSORIES with positions].
  They stay on her body and visible in every frame from start to
  finish — never vanish, change shape, or swap sides during
  movement." Ảnh không có trang sức thì ghi rõ "no jewellery or
  accessories" để model khỏi tự thêm. Chi tiết nhỏ chỉ chiếm vài
  pixel nên dễ biến mất giữa chừng khi nhân vật cử động.
- MỖI CLIP CHỈ 1 HÀNH ĐỘNG CHÍNH, chuyển động CHẬM và nhẹ nhàng:
  đi bộ HOẶC xoay người HOẶC giơ đồ trong 1 clip — không gộp nhiều
  động tác nhanh. Cử động càng nhanh/phức tạp càng dễ rớt chi tiết
  nhỏ. Chi tiết nhỏ quan trọng thì quay riêng 1 cảnh cận cảnh
  (template 11/12) thay vì trông chờ clip đi bộ giữ nó — chi tiết
  càng to trong khung hình càng khó mất.
- Dọc 9:16. Một cảnh duy nhất mỗi reel (trừ template 06, 10 có 1
  lần cắt cảnh giơ hàng → mặc hàng; template 13, 14 sinh 2 clip
  cùng dáng để ghép chia đôi ở editor), máy quay gần như tĩnh, ít
  cắt cảnh. Độ dài mặc định 20 giây (2 clip x 10 giây), hoặc 30
  giây (3 clip x 10 giây) cho mẫu đi bộ.
- Góc quay theo món chính: quần → góc RỘNG toàn thân, cả người từ
  đầu tới giày, quần chiếm nửa dưới khung hình; áo → nửa thân
  được; đầm/váy → toàn thân. Góc hẹp khi giới thiệu quần làm
  người xem tưởng món chính là áo.
- Một nhân vật duy nhất trong 1 video. Không đổi nhân vật giữa các
  đoạn.
- Video sinh ra LUÔN SẠCH: không có chữ, phụ đề hay lời nói —
  kể cả template nói trực tiếp, lời nói là voiceover của user thu
  sau. Chữ POV, chữ tên sản phẩm, chữ Trước/Sau, caption, hashtag,
  nhạc đều thêm ở editor lúc đăng.
- Không bịa giá, mã sản phẩm, size, chất liệu hay khuyến mãi mà user
  không đưa và ảnh không thể hiện rõ. Thông tin bán hàng chỉ nằm ở
  caption + banner, không nằm trong video.
- Trình bày đời thường, kín đáo, phù hợp gia đình: trang phục nữ
  everyday, dáng đứng tự nhiên, không tạo dáng gợi cảm, không khung
  hình hay mô tả khêu gợi. Demo phụ kiện luôn mặc đủ đồ, demo bằng
  cách cầm trên tay hoặc mặc thử qua lớp quần áo bình thường.

## Thu thập thông tin trước (chỉ hỏi phần còn thiếu)

- Ảnh sản phẩm. Nếu ảnh có nhiều món hoặc món chính không rõ, hỏi
  lại món nào là món chính.
- Ảnh nhân vật chuẩn (xem dưới đây).
- Tên sản phẩm + 2–3 điểm nổi bật user xác nhận.
- Chọn phong cách A (đời sống im lặng), B (lookbook trong nhà /
  nói trực tiếp), C (review giơ đồ trong phòng cố định) hay D
  (tips phối đồ chia đôi màn hình / nhiều look trong 1 reel).
  Mặc định là A nếu user không nói.
- Với phong cách B dạng nói (template 08), dạng lồng tiếng
  (template 16, 17) và dạng "Chọn đi" có voiceover vlog tùy chọn
  (template 24): hỏi user có tự thu voiceover không hay chỉ
  cần bản im lặng.
- Dòng chữ POV user muốn dùng (nếu muốn hook chữ), hoặc để Muse
  gợi ý theo template.
- Hashtag thương hiệu (nếu có) + CTA/link affiliate user sẽ gắn.

## Ảnh nhân vật chuẩn của kênh

- Khi user gửi ảnh nhân vật, lưu 1 bản vào
  `~/workspace/fashion-affiliate-women/character-reference/` làm ảnh
  nhân vật chuẩn của kênh.
- Mọi video sau của kênh dùng đúng ảnh chuẩn đó + ảnh sản phẩm của
  video đó.
- Sinh bằng media video tool theo thứ tự: ảnh nhân vật trước, ảnh
  sản phẩm sau, rồi mới tới prompt text. Ngoại hình lấy từ ảnh nhân
  vật, quần áo lấy từ ảnh sản phẩm — không trộn 2 ảnh vào nhau.
- Giữ nhân vật nhất quán qua các video: cùng gương mặt, kiểu tóc,
  màu tóc, dáng người, thần thái; chỉ đổi outfit theo sản phẩm và đổi
  bối cảnh theo yêu cầu.
- Chưa có ảnh chuẩn: sinh đoạn đầu, lấy 1 frame mặt rõ làm ảnh
  chuẩn, rồi dùng ảnh đó cho mọi đoạn sau — và nói rõ với user đó
  là ảnh chuẩn tạm thời.

## Prompt template (trong `prompts/`)

Điền tên sản phẩm, cổ áo, nút, logo, vải và chi tiết THẬT từ ảnh của
user — không copy chi tiết ví dụ của template sang sản phẩm khác.

Phong cách A — đời sống im lặng:

- `01-pov-cafe-terrace.md` — sân thượng quán cà phê, đi bộ về phía
  camera + xoay người. Mẫu khoe đồ toàn thân, dùng cho set bộ, áo +
  quần short, outfit pastel.
- `02-pov-cafe-window.md` — ngồi bàn cạnh cửa sổ quán cà phê, uống
  cà phê đá, cầm điện thoại. Mẫu ngồi yên, khoe đồ qua dáng ngồi và
  góc nghiêng.
- `03-pov-street-walk.md` — đi bộ trên phố / vỉa hè, quay lại cười
  với camera; có biến thể đi bộ quay lưng ra xa và đi lùi. Dùng cho
  váy body, váy dài, váy lụa, outfit dạo phố.
- `04-pov-pickleball.md` — set thể thao trên sân pickleball, cầm
  vợt, di chuyển nhẹ / đánh bóng. Dùng cho đồ thể thao, set crop-top
  + chân váy.
- `05-pov-closeup-comedy.md` — cận mặt, tình huống hài, ít khoe đồ.
  Reel câu tương tác, không phải reel bán hàng — luôn đi kèm 1 reel
  khoe đồ cùng outfit.
- `09-car-back-seat.md` — ngồi ghế sau ô tô, tay chống má / tay đan
  trên đùi, cười. Dùng cho đầm corset, set body, đồ dạo phố sang.

Phong cách B — lookbook trong nhà / nói trực tiếp:

- `07-indoor-lookbook.md` — lookbook trong nhà ánh sáng vàng ấm,
  tạo dáng chậm, xoay lưng/nghiêng, nhìn qua vai. Dùng cho váy dài,
  ren, peplum, áo dài, đồ "sang" / dự tiệc.
- `08-talk-to-camera.md` — trình bày trực tiếp: giơ đồ trên móc,
  chạm/chỉ chi tiết, cử chỉ như đang giới thiệu; video sạch, user
  thu voiceover sau. Dùng cho chân váy tơ, váy ren, set peplum.
- `17-pajama-to-outfit.md` — mở đầu đồ ngủ nói chuyện → cắt cảnh
  sang outfit trên nền nhạc; video sạch, user thu voiceover sau.
  Dùng cho đồ công sở, đồ đi tiệc, set "sang, thanh lịch".
- `19-dance-lipsync-room.md` — nhảy nhẹ/lip-sync theo nhạc trong
  phòng cố định, góc máy hơi thấp; biến thể selfie trước gương
  phòng gym cho đồ tập. Dùng cho đồ trẻ trung, đồ dạo phố, áo
  thun oversize, áo trễ vai, chân váy mini, quần short.
- `23-collection-series.md` — chuỗi sưu tập đánh số "Tủ đồ 100
  chiếc [món]": mỗi reel 1 món, cùng bối cảnh/góc quay, chữ số
  thứ tự ở editor. Dùng cho shop/creator có nhiều món cùng 1 loại.
- `24-choose-two-styles.md` — "Chọn đi" hai phong cách đối lập
  trong 1 reel (bánh bèo vs xì lay, áo dài vs bà ba); câu hỏi
  chọn là hook chính; voiceover vlog tùy chọn do user thu sau.
  Dùng khi có 2 phong cách để người xem chọn.

Phong cách C — review giơ đồ trong phòng cố định:

- `10-hold-up-fixed-room.md` — giơ đồ che trước người (mặt thấy ở
  phía trên), cắt sang cảnh mặc lên + xoay nhẹ, cùng 1 góc phòng ấm.
  Dùng cho mọi món đồ, công thức chính của Thanh Huyền.
- `11-fabric-proof-closeup.md` — cận cảnh chứng minh: tay sờ vải/
  cúc, kéo giãn gấu áo chứng minh co giãn, kéo nhẹ gấu áo khoe độ
  ôm ở eo. Dùng cho món có điểm đáng chứng minh bằng tay.
- `12-accessory-demo.md` — demo phụ kiện đang dùng trên người:
  ngồi kéo quần tất lên chân, cầm phụ kiện trước người. Dùng cho
  phụ kiện chức năng (quần tất, đai, miếng dán, phụ kiện tóc).
- `13-before-after-split.md` — 2 clip cùng dáng/góc: chưa mặc vs
  đã mặc đồ định hình; ghép chia đôi + chữ "Trước mặc / Sau mặc"
  ở editor. Dùng cho quần độn hông, đai, shapewear.
- `16-voiceover-review.md` — review lồng tiếng "Chấm điểm":
  người mẫu chỉ tạo dáng/demo (giơ sản phẩm/bao bì, kéo vạt khoe
  lót lông), giọng nói lồng tiếng do user thu sau. Dùng cho phụ
  kiện chức năng, đồ giữ nhiệt, boots/giày, món cần đánh giá
  bằng lời.
- `20-walk-holdup-hybrid.md` — đi bộ trong hành lang + giơ đồ lên
  cận cảnh trong cùng 1 reel; giơ đồ là 1 nhịp, không phải toàn
  bộ reel. Dùng cho món vừa cần khoe dáng mặc vừa có chi tiết
  đáng khoe.
- `21-tights-variants.md` — phụ kiện (quần tất/legging) làm nhân
  vật chính, thử qua 2–3 outfit trong 1 reel, chữ trên màn hình
  thay đổi giữa reel để giải thích từng biến thể. Dùng cho phụ
  kiện có nhiều biến thể (độ dày, màu).
- `22-unboxing-try-on.md` — mở hộp hàng mới về (thùng carton/bưu
  kiện làm đạo cụ) rồi giơ đồ lên; reel mặc thử tiếp theo dùng
  template 07 hoặc 10. Dùng cho hàng mới về từ 1 shop.

Phong cách D — tips phối đồ / nhiều look:

- `14-split-screen-styling-tips.md` — tips "1 món mặc nhiều kiểu"
  chia đôi màn hình ("Mặc đúng / Mặc theo tui"): 2 clip cùng món
  đồ, cùng dáng, cùng góc, khác cách mặc; ghép cạnh nhau + chữ ở
  editor. Dùng cho món mặc được nhiều kiểu (áo trễ vai, cardigan,
  áo sơ mi, khăn, dây cột tóc). Dạng viral nhất trong cả 4 kênh
  (3,3 triệu lượt xem).
- `15-multi-look-one-reel.md` — nhiều look trong 1 reel ("7 ngày
  không trùng outfit", "LOOK 1... LOOK 5"): mỗi look 1 clip 10
  giây, cùng nhân vật, cùng góc phòng, chỉ đổi outfit; nối tiếp
  bằng concat.sh + nhãn LOOK ở editor. Dùng khi muốn khoe nhiều
  outfit trong 1 reel.
- `18-tet-countdown-series.md` — chuỗi đếm ngược Tết: mỗi phần
  1 outfit, cùng phòng/góc quay, chữ đếm ngược + số phần thêm ở
  editor; đăng từ hàng tháng trước Tết. Dùng cho đồ Tết (áo dài,
  đồ đỏ, set đi chơi Tết, đồ đi tiệc cuối năm).

Cầu nối các phong cách:

- `06-hold-then-wear.md` — giơ hàng lên trước, mặc lên sau (1 lần
  cắt cảnh), bối cảnh phòng ngủ đời thường. Dùng cho quần short,
  áo khoác, món có chi tiết đáng khoe (túi, logo, tag).

Chọn template theo loại đồ: set bộ / đồ dạo phố → 01 hoặc 03; váy
body / váy dài / váy lụa → 03; đầm corset / set body sang → 09;
đồ ngồi quán / đồ công sở nhẹ → 02; đồ thể thao → 04; váy dài /
ren / peplum / áo dài → 07 (im lặng) hoặc 08 (nói + voiceover);
món có chi tiết đáng khoe → 06 (phòng ngủ) hoặc 10 (phòng ấm cố
định); cần chứng minh chất liệu/co giãn/độ ôm → 11; phụ kiện chức
năng → 12; đồ định hình → 13; món mặc được nhiều kiểu → 14 (chia
đôi màn hình); muốn khoe nhiều outfit trong 1 reel → 15; cần thêm
1 reel hài cùng outfit → 05; món cần đánh giá bằng lời nói lồng
tiếng → 16; muốn mở đầu bằng câu chuyện/tình huống rồi biến hình
sang outfit → 17; đồ Tết làm thành chuỗi đếm ngược → 18; đồ trẻ
trung muốn nhảy nhẹ theo nhạc → 19; món vừa cần khoe dáng mặc vừa
có chi tiết đáng khoe → 20; phụ kiện có nhiều biến thể (độ dày,
màu) → 21; hàng mới về muốn mở hộp → 22; nhiều món cùng 1 loại
làm thành chuỗi sưu tập → 23; 2 phong cách đối lập để người xem
chọn → 24.

## Chữ POV + caption + hashtag (giao kèm video, thêm ở editor)

- Chữ POV là TÙY CHỌN, không phải mặc định: chỉ gợi ý khi user
  muốn hook chữ. 1 câu ngắn, giọng đời thường, hài nhẹ, nói về
  TÌNH HUỐNG chứ không nói về đồ. Mỗi video gợi ý 2–3 câu để user
  chọn, không chốt 1 câu duy nhất.
- Hook chữ dạng CÂU HỎI (phong cách D, Nhun Lên Đồ): "🗣️: [câu
  hỏi / tình huống]..." — ví dụ "🗣️: Mùa đông này mặc gì đi làm,
  đi ăn cưới, đi cà phê?". Dùng khi user muốn hook chữ mà không
  muốn giọng POV hài. Câu hỏi PHẢI khớp đúng món đồ trong video
  (kênh gốc hay dùng lại chữ không khớp đồ — lỗi không học theo).
- Hook GIÁ TRỊ (Khánh Chi Daily, NuocLoc7Mao): "Vắt kiệt giá trị
  với [món đồ iu thích]", "Là mua 1, được 2, phối ra 5 outfits"
  — nhấn mạnh 1 lần mua được nhiều cách mặc.
- Hook PHỦ ĐỊNH (Khánh Chi Daily, Phối Đồ Cùng Mei): "Đừng mặc
  [món] như thế này", "Đi [dịp] tuyệt đối đừng mặc kiểu này ❌"
  — mở bằng cách mặc sai rồi sửa.
- Hook ĐỐI CHIẾU NGÂN SÁCH (Phối Đồ Cùng Mei): "Lương 5tr nhưng
  đi làm vẫn phải sang như quý cô 50tr" — ngân sách thấp, vẻ
  ngoài đắt tiền; đánh đúng nữ công sở U30.
- Hook CÂU THOẠI KỊCH (Phối Đồ Cùng Mei, reel 898K lượt xem):
  "Đừng đi chơi với anh nữa, bạn bè anh nó cười ngại lắm" — mở
  bằng 1 câu thoại như trong tình huống thật.
- Hook HỐI TIẾC (Huyền Kem, 410K lượt xem): "Hối hận vì k mua
  sớm 😢" — tạo cảm giác sợ bỏ lỡ.
- Công thức caption "Team mê [món]…" (Phối Đồ Cùng Mei, reel cao
  nhất kênh 1,2M lượt xem): "Team mê mặc chân váy dài đi làm thì
  phối sao cho thật sang…" — gọi đúng nhóm người mê 1 món đồ cụ
  thể rồi hứa cách phối.
- Hook ĐẾM NGƯỢC (Huyền Kem, NuocLoc7Mao, reel lẻ Tết): "Đếm
  ngược [N] ngày đến Tết 2027 / Tết mặc gì? | P[n]", "Còn [N]
  ngày nữa là đến Tết 🧧 Vậy Tết nay mặc gì?" — gắn outfit với
  dịp lễ sắp tới + đánh số phần để người xem quay lại.
- Hook DỊP CỤ THỂ (Thảo Nguyên Daily): "Mua [món] mặc đi [nơi]
  chưa biết phối sao thì thử ngay [số] outfit này nhé" — mua đồ
  cho 1 chuyến đi/dịp cụ thể.
- Hook DÁNG NGƯỜI (Vũ Thị Linh, 169K lượt xem): "Dáng [tam giác
  ngược] bơi vô đây liền" — gọi đúng nhóm dáng người rồi hứa món
  đồ hợp dáng đó.
- Hook YÊU CẦU KHÁN GIẢ (Vũ Thị Linh, 58K): "Hôm bữa bà nào hỏi
  in4 em [món] nì, hôm nay tui lên video cho mấy bà luôn nha" —
  nội dung do bình luận kéo theo.
- Hook MẶC LẠI ĐỒ CŨ (Thảo Vy, 179K): "Chiếc áo tui mặc từ năm
  ngoái, năm nay lại mặc lại" — không phải lúc nào cũng mua mới.
- Hook 1 OUTFIT NHIỀU DỊP (Vũ Thị Linh, 66K): "1 outfit cho 3 dịp
  mùa thu + noel + tết".
- Hook MIX-MATCH (Vũ Thị Linh, 113K): "Mua được set đồ mà có thể
  mixmatch thành nhìu outfit thì mấy bà có ưng không…".
- Hook SƯU TẬP ĐÁNH SỐ (Hoàng Liên Hoa): "Tủ đồ 100 chiếc [món] /
  Chiếc số [N]" + tự nhận "đại sứ [món]" — chuỗi dài, mỗi reel
  1 món.
- Chữ CHỨNG MINH cấu tạo (Machi.clo): "có đệm ngực được may chắc
  chắn", "chân váy dạ chéo (có khoá kéo hai bên)" — chữ chứng minh
  1 chi tiết may mặc, chỉ ghi điều đã xác nhận.
- Caption: 1 câu ngắn + 1–2 emoji, giọng như đang kể với bạn.
  Có thể thêm câu chốt nhẹ kiểu "+1 em… nên có trong tủ đồ" khi
  user đồng ý giọng chốt đơn. Không liệt kê thông số trong caption
  trừ khi user đưa.
- Caption mẫu phong cách C (Shopee): "Link mua [tên món] -
  Shopee: [link] — Bấm vào link để xem chi tiết và mua hàng."
  Biến thể: chia link — món chính ở caption, món còn lại "để ở
  Bình luận" (kéo bình luận); hoặc để toàn bộ link ở bình luận
  (gắn góc dịp như "outfit đón Tết, dự tiệc").
- CTA biến thể mới: link mua ở BÌNH LUẬN (ghi trong tiểu sử trang,
  Phối Đồ Cùng Mei); link gắn ở GÓC TRÁI video + dưới bình luận
  (Huyền Kem); mã giảm trong bio (Ninh Anh: "có mã giảm 55k trong
  bio nha"); ghim sẵn dưới GIỎ HÀNG trên video (Hoàng Liên Hoa,
  Vũ Thị Linh — ghi trong tiểu sử "mua hàng vui lòng bấm vào giỏ
  hàng trên video"); bình luận "(.)" để báo giá qua inbox — chỉ
  cho shop bán trực tiếp (Machi.clo).
- Chữ tên sản phẩm + thương hiệu trên màn hình (phong cách C):
  gợi ý 1 dòng ngắn ("[Tên món] [thương hiệu]") để user thêm ở
  editor — reel có chữ này đạt lượt xem rất cao ở kênh Thanh Huyền.
- End-card khoanh đỏ link (phong cách C): cuối video hiện lại chữ
  chú thích/link, khoanh đỏ + mũi tên đỏ chỉ vào — gợi ý cho user
  làm ở editor khi muốn ép hành động bấm link.
- Hashtag cố định: `#viral #outfitideas #goiyphoido #xuhuong` +
  hashtag thương hiệu / loại đồ của user (ví dụ `#dopickleball`,
  `#modestdressing`, `#vaylua`).
- Nhạc: nhạc Việt remix / nhạc thịnh hành, user chọn trong thư viện
  nhạc của Facebook/TikTok lúc đăng (nhạc không sinh cùng video).
- Voiceover (template 08, 16, 17, 24): giao kèm kịch bản nói
  ngắn 3–4 câu (chào + tên món + 2 điểm nổi bật + mời inbox),
  user tự thu và lồng vào video lúc đăng. Template 16 là lồng
  tiếng review ("Chấm điểm"), template 17 là lời nói ở đoạn mở
  đầu đồ ngủ, template 24 là lời kể vlog thử đồ (tùy chọn).

## 1 outfit → 3–4 reels

Các kênh đều dùng lại 1 outfit cho nhiều reel khác nhau. Khi user
muốn khai thác 1 outfit, làm 3–4 reel khác nhau ở CẢ 3 điểm: tình
huống/bối cảnh, góc quay/động tác, template — giữ nguyên outfit và
nhân vật. Bằng chứng mạnh nhất: Lê Khánh Vân dùng 1 set (corset ren
trắng + váy lụa sâm panh) cho 3 reel, cả 3 đều nằm trong top 5 lượt
xem của kênh (81K/98K/197K). Dạng chuỗi: Khánh Chi Daily làm "1 món
mặc cả tuần" thành chuỗi nhiều reel (mỗi reel 1 Look, đánh số Look
1/2 + nhãn ngày/dịp); chuỗi đếm ngược Tết (template 18) cũng là
1 dạng chuỗi theo mùa.

- Ví dụ: set vàng nhạt → (1) sân quán cà phê, đi bộ về phía camera
  (template 01); (2) ngồi ghế sau ô tô, tay chống má (template 09);
  (3) ngoài trời, tạo dáng nghiêng/lưng (template 03); (4) đi bộ
  trên phố, kéo nhẹ gấu quần (template 03, góc khác).
- Tái dùng KHÔNG cần đổi bối cảnh (đợt 3): cùng 1 món đăng lại
  thành nhiều reel riêng với caption khác nhau (Hoàng Liên Hoa:
  áo lụa satin 5 lần, tổng 310K lượt xem); cùng 1 sản phẩm đăng
  lại nhiều bản cắt (cùng caption + nhạc, mở đầu khác — Machi.clo);
  series biến thể màu (cùng mẫu, khác màu, reel riêng — Machi.clo);
  chuỗi sưu tập đánh số (template 23).
- Liệt kê các combo trước để user thấy sự khác nhau, rồi làm từng
  reel một. Tối đa 6 video mỗi lượt nhắn, nên 3–4 reel x 2 clip =
  6–8 clip có thể cần 2 lượt.

## Sinh, ghép, kiểm chứng, giao

1. Lưu ảnh sản phẩm vào `input/`, ảnh nhân vật (nếu có) vào
   `character-reference/`; không commit ảnh thật lên repo public.
2. Chọn template, điền chi tiết thật của sản phẩm, sinh các đoạn
   theo thứ tự (ảnh nhân vật trước, ảnh sản phẩm sau, rồi text).
   Tối đa 6 video mỗi lượt nhắn. Sinh clip TUẦN TỰ, không song
   song: clip sau dùng snapshot của clip trước (resume) để giữ
   nguyên mẫu + quần áo — sinh 2 clip độc lập song song dễ làm
   quần/nhân vật lệch nhau. Viết prompt LIỀN MẠCH: clip sau bắt
   đầu đúng chỗ clip trước dừng (cùng vị trí, cùng động tác,
   cùng đạo cụ — ly cà phê phải có từ clip 1, không xuất hiện
   đột ngột ở clip 2); mô tả sản phẩm giống hệt từng chữ ở mọi
   clip, ghi rõ vị trí chi tiết (hình thêu ở đùi trái, tóc xõa
   hay buộc, góc quay nào).
3. Ghép bằng script dùng chung:
   - 2 x 10s thành 20s: `~/workspace/fashion-affiliate/scripts/concat.sh output/video-20s.mp4 clip1.mp4 clip2.mp4`
   - 3 x 10s thành 30s: `~/workspace/fashion-affiliate/scripts/concat.sh output/video-30s.mp4 clip1.mp4 clip2.mp4 clip3.mp4`
   Script chuẩn hóa clip về 720x1280, 30 fps trước khi ghép.
   Template 13, 14 không nối tiếp mà ghép chia đôi ở editor.
4. Kiểm chứng trước khi giao: `ffprobe` thời lượng (khoảng 20s hoặc
   30s) và 720x1280; xem 1 frame giữa mỗi clip để chắc đúng outfit,
   đúng bối cảnh, không có chữ lạ trong hình — VÀ xem frame CUỐI
   clip trước với frame ĐẦU clip sau để chắc mối nối liền mạch
   (cùng vị trí, cùng quần áo, cùng đạo cụ, cùng tay cầm đồ, cùng
   góc quay). Khi kiểm frame, SO SÁNH SẢN PHẨM với ảnh gốc: đếm
   số chi tiết (hình thêu, nút, logo), kiểm tra vị trí từng chi
   tiết — nếu sản phẩm lệch (thêm/bớt chi tiết, đổi màu, đổi vị
   trí họa tiết), sinh lại clip đó, không giao video có sản phẩm
   bị thay đổi. Kiểm tra CẢ trang sức/phụ kiện ở 3 điểm trong mỗi
   clip (đầu, giữa, cuối) — chi tiết nhỏ có thể đúng ở frame đầu
   nhưng biến mất giữa clip; nếu mất ở giữa thì cắt bỏ đoạn lỗi
   hoặc sinh lại clip đó. Nếu clip chỉ lỗi chi tiết trong vài giây
   đầu rồi
   tự hết, CẮT BỎ đoạn đầu lỗi bằng ffmpeg rồi ghép phần còn lại
   — đừng sinh lại mù quáng (sinh lại là xổ số: 3 lần liên tiếp
   đều đặt hình thêu sai bên túi dù đã ghi rõ neo tay cầm cà phê).
   Góc quay an toàn cho chi tiết ở túi trước: nghiêng 3/4 MẶT
   TRƯỚC (túi có chi tiết hướng camera, túi sau khuất). KHÔNG quay
   cảnh quay lưng/đi ra xa — model chuyển chi tiết sang túi sau
   (thậm chí nhân đôi) dù đã ghi rõ "back pockets plain" / "never
   turn back"; nghiêng hẳn (profile) cũng lộ túi sau và model thêu
   thêm chi tiết ở đó. Ngoại lệ: với đồ HỞ LƯNG, góc quay lưng là
   góc bán chính — lưng trần chính là điểm bán (Hoàng Liên Hoa:
   reel áo lụa hở lưng quay từ phía sau đạt 6,8K like, cao nhất
   kênh). Quy tắc "không quay lưng" chỉ áp dụng khi chi tiết bán
   nằm ở mặt trước. File tồn tại chưa đủ — phải kiểm số. Lưu ý:
   resume
   giữ được quần áo/bối cảnh nhưng có thể đổi kiểu tóc/góc quay —
   phải ghi rõ trong prompt clip sau và kiểm tra lại; sinh mới
   hoàn toàn (không resume) dễ lệch màu quần và góc quay hơn.
5. Giao video kèm: 2–3 câu POV để chọn (nếu user muốn hook chữ),
   1 caption gợi ý, hashtag, kịch bản voiceover ngắn (nếu là
   template 08, 16, 17 hoặc 24), và ghi chú user tự thêm chữ POV +
   nhạc + link affiliate trong editor lúc đăng.
6. Muốn thêm bản khác: đổi 1 yếu tố mỗi lần (góc quay, bối cảnh,
   hoặc câu POV), không dựng lại từ đầu.
