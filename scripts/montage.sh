#!/bin/bash
# Ghép montage ngầu: cắt mỗi đoạn còn 4 giây, bắt đầu từ giây thứ 1,
# rồi ghép lại thành video khoảng 20 giây với 5 đoạn.
# Cách dùng: ./scripts/montage.sh output/video-20s.mp4 clip1.mp4 clip2.mp4 clip3.mp4 clip4.mp4 clip5.mp4
# Khác bản gốc ở repo tham chiếu: chuẩn hóa mỗi phần về 720x1280, 30 fps.
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Cách dùng: $0 <output.mp4> <clip1.mp4> <clip2.mp4> [clip3.mp4 ...]"
  exit 1
fi

output="$1"
shift
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT
list_file="$tmp_dir/list.txt"

i=1
for clip in "$@"; do
  part="$tmp_dir/part$i.mp4"
  ffmpeg -y -v error -ss 1 -t 4 -i "$clip" \
    -vf "scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2:black,fps=30,format=yuv420p" \
    -an -c:v libx264 "$part"
  printf "file '%s'\n" "$part" >> "$list_file"
  i=$((i + 1))
done

mkdir -p "$(dirname "$output")"
ffmpeg -y -v error -f concat -safe 0 -i "$list_file" \
  -c:v libx264 -pix_fmt yuv420p -r 30 "$output"
echo "Đã ghép xong: $output"
