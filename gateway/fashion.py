"""Video thời trang AI 30 giây từ ảnh sản phẩm (+ ảnh nhân vật nếu có).

Luồng dùng:
  1. ``python gateway_cli.py fashion --product-image <ảnh SP> [--model-image <ảnh mẫu>]
     --product "Váy lụa trắng" --out scripts/vay-lua.yaml``
  2. ``python gateway_cli.py build --script scripts/vay-lua.yaml --no-tts
     --accounts acc2``   (video thời trang: không lời dẫn, không dub)

Khung mặc định 30s = 3 cảnh x 10s (model Muse trả clip 10s), tỉ lệ
mặc định 9:16 (TikTok/Reels/Shorts). Muốn ngang thì ``--aspect 16:9``.

Giới hạn thật của gateway, phải nói rõ cho user (không giấu):
  - Ảnh tham chiếu chỉ nhận JPEG/PNG (gateway từ chối WebP...). File
    .webp/.avif phải đổi sang .jpg/.png trước.
  - Mỗi cảnh chỉ đính kèm ĐƯỢC 1 ảnh (chat.stream: 1 image item + text).
    Nên tool phân ảnh theo cảnh, không gửi cả 2 ảnh cùng lúc:
      s01: ảnh SẢN PHẨM — cận cảnh sản phẩm, giữ nguyên thiết kế.
      s02: ảnh NHÂN VẬT nếu có, không thì ảnh sản phẩm — mẫu mặc sản phẩm.
      s03: ảnh SẢN PHẨM — chi tiết chất liệu + dáng mặc, chốt dáng đẹp.
    Khi s02 dùng ảnh mẫu thì bản sắc sản phẩm giữ bằng MÔ TẢ CHỮ
    (--product-desc: tên, màu, chất liệu, họa tiết, điểm nhấn) — mô tả
    càng cụ thể thì model càng ít tự "thiết kế lại" sản phẩm.
  - Không có chữ/text overlay trong prompt: model hay sinh chữ lỗi.
    Logo chỉ là logo vốn có trên sản phẩm, không thêm logo mới.
  - Build thật tốn quota acc Muse (giới hạn thật không đọc được qua API),
    nên luôn chạy ``--mock`` trước để kiểm tra pipeline, rồi mới build
    thật khi user xác nhận tên đợt chạy.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

SCENE_DURATION = 10
SCENE_COUNT = 3
TOTAL_DURATION = SCENE_COUNT * SCENE_DURATION  # 30s

_ALLOWED_IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}

# Phong cách -> cụm từ đưa vào prompt (tiếng Anh, model hiểu tốt hơn).
STYLES = {
    "studio": "clean minimal studio, soft diffused lighting, seamless light background, high-end e-commerce fashion film",
    "street": "urban street style, golden hour city backdrop, candid editorial fashion film, natural light",
    "elegant": "elegant editorial fashion film, soft warm light, luxurious minimal interior, slow graceful camera",
    "casual": "bright casual lifestyle fashion film, airy daylight, relaxed natural setting, friendly energy",
}

PRODUCT_LOCK = (
    "Keep the exact product from the reference image: same design, same color, "
    "same pattern, same fabric texture and same logo placement. "
    "Do not redesign, recolor, simplify or replace the product."
)


def _slug(text: str) -> str:
    """Tên sản phẩm -> slug file (bỏ dấu tiếng Việt đơn giản)."""
    table = str.maketrans(
        "àáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ",
        "aaaaaăaaaaaâaaaaađeeeeeêeeeeeiiiiioooooôooooơooooouuuuuưữuuuuuyyyyy",
    )
    s = text.lower().translate(table)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "san-pham"


def validate_image(path: str | Path, label: str) -> Path:
    p = Path(path).expanduser()
    if not p.exists():
        raise ValueError(f"Không thấy {label}: {p}")
    if p.suffix.lower() not in _ALLOWED_IMAGE_SUFFIXES:
        raise ValueError(
            f"{label} phải là JPEG/PNG (gateway từ chối {p.suffix or 'không đuôi'}): "
            f"{p} — đổi sang .jpg/.png rồi chạy lại."
        )
    return p


def build_fashion_script(
    product: str,
    product_image: str | Path,
    model_image: str | Path | None = None,
    product_desc: str = "",
    model_desc: str = "",
    style: str = "studio",
    aspect: str = "9:16",
    title: str = "",
) -> dict:
    """Trả về dict kịch bản fashion (đủ để ghi YAML + đưa vào build).

    product_desc càng cụ thể càng tốt, vd: "váy lụa trắng, cổ V, tay
    lỡ, eo chiết, dài qua gối, không họa tiết". Nếu để trống, tool chỉ
    khóa bằng ảnh (s01/s03) và tên sản phẩm ở s02.
    """
    product = (product or "").strip()
    if not product:
        raise ValueError("Thiếu tên sản phẩm (--product).")
    if style not in STYLES:
        raise ValueError(
            f"Phong cách '{style}' không có — chọn: {', '.join(STYLES)}."
        )
    if aspect not in ("9:16", "16:9"):
        raise ValueError("Tỉ lệ chỉ nhận 9:16 hoặc 16:9.")
    prod_path = validate_image(product_image, "ảnh sản phẩm")
    model_path = validate_image(model_image, "ảnh nhân vật") if model_image else None

    style_text = STYLES[style]
    prod_text = product_desc.strip() or product
    model_text = model_desc.strip()
    # s02: nếu có ảnh mẫu thì model là nhân vật chính; mô tả mẫu (nếu có)
    # khóa thêm bằng chữ, còn không thì để ảnh tự nói.
    model_clause = f"Model: {model_text}. " if model_text else ""
    wear_clause = (
        f"The model wears the product: {prod_text}. "
        "The product must stay clearly visible and identical in every shot."
    )

    scenes = [
        {
            "id": "s01",
            "title": "Cận cảnh sản phẩm",
            "duration": SCENE_DURATION,
            "visual": (
                f"{style_text}. Close-up hero shot of the product "
                f"({prod_text}), slow elegant camera orbit, fabric texture "
                f"and details in sharp focus, soft studio light. "
                f"{PRODUCT_LOCK} No text, no watermark, no extra logo."
            ),
            "reference_image": str(prod_path),
        },
        {
            "id": "s02",
            "title": "Mẫu mặc sản phẩm",
            "duration": SCENE_DURATION,
            "visual": (
                f"{style_text}. Full-body shot, {model_clause}"
                f"{wear_clause} The model walks naturally toward camera, "
                "then turns and poses, showing how the product moves and "
                "fits on the body. Smooth cinematic camera, realistic "
                "motion. No text, no watermark."
            ),
            # 1 ảnh/cảnh: ưu tiên ảnh mẫu (giữ mặt/dáng mẫu), sản phẩm
            # giữ bằng mô tả chữ ở trên; không có ảnh mẫu thì dùng ảnh SP.
            "reference_image": str(model_path or prod_path),
        },
        {
            "id": "s03",
            "title": "Chi tiết và dáng chốt",
            "duration": SCENE_DURATION,
            "visual": (
                f"{style_text}. Detail shots of the product's fabric, "
                f"stitching, drape and movement ({prod_text}), then a "
                "confident final pose holding the look, clean ending "
                "frame suitable for cutting to a shop link. "
                f"{PRODUCT_LOCK} No text, no watermark."
            ),
            "reference_image": str(prod_path),
        },
    ]
    # Nếu có ảnh mẫu thì ghi vào bảng characters để khung mô tả được
    # khóa (ảnh trong bảng hiện chỉ để tham chiếu, chưa đính kèm qua
    # gateway — ảnh đính kèm thật nằm ở reference_image của s02).
    characters = {}
    if model_path:
        characters["model"] = {
            "description": model_text or "the model from the reference image",
            "image": str(model_path),
        }
        scenes[1]["character"] = "model"

    return {
        "title": title.strip() or f"Thời trang — {product}",
        "kind": "fashion",
        "aspect": aspect,
        "fps": 30,
        "scenes": scenes,
        **({"characters": characters} if characters else {}),
    }


def write_fashion_script(data: dict, out_path: str | Path, force: bool = False) -> Path:
    dest = Path(out_path)
    if dest.exists() and not force:
        raise ValueError(f"{dest} đã tồn tại, thêm --force để ghi đè.")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        yaml.dump(data, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return dest


def default_out_path(product: str) -> Path:
    return Path("scripts") / f"fashion-{_slug(product)}.yaml"
