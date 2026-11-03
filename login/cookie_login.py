"""Login Muse bằng cookies — bản standalone, tách từ automuse-multi.

Dùng cho tool khác mà không cần cả repo automuse-multi. Chỉ phụ thuộc
gói ``requests`` (``pip install requests``); còn lại toàn stdlib.

Gồm 3 lớp, đúng như logic gốc:
  1. Parse cookie (3 định dạng) + gắn proxy riêng từng acc.
  2. Session đã đăng nhập + ``check_login`` (phép thử sống/chết của cookie).
  3. ``fetch_gateway_init`` / ``parse_gateway_init`` — bằng chứng mạnh hơn
     cho Muse: cookie sống thì trang chủ trả 200 kèm blob gateway init.

KHÔNG gồm (thuộc tầng khác, không phải login):
  - Noise WebSocket handshake, chat.stream/subscribe, sinh video.
  - Round-robin chọn acc, cooldown, đếm job, UsageTracker.
  - Làm mới authToken (POST /api/hatch/token): khi init thiếu authToken,
    tầng Noise sẽ tự refresh bằng gatewayUrl + vmName; xem README.

Bảo mật: KHÔNG hardcode cookie thật vào code. Cookie nạp từ chuỗi, file
cookies.txt/.json, hoặc file accounts JSON (lưu quyền 0600). Không bao giờ
commit file chứa cookie thật lên git.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

__all__ = [
    "MuseLoginError",
    "DEFAULT_HEADERS",
    "DEFAULT_BASE_URL",
    "parse_cookie_header",
    "parse_netscape_file",
    "parse_cookie_json",
    "load_cookies",
    "cookies_to_header",
    "ProxyConfig",
    "CookieAccount",
    "build_session",
    "check_login",
    "parse_gateway_init",
    "fetch_gateway_init",
    "load_accounts_file",
    "save_accounts_file",
]

DEFAULT_BASE_URL = "https://muse.ai"

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://muse.ai/",
    "Origin": "https://muse.ai",
}


class MuseLoginError(Exception):
    """Lỗi thuộc tầng login (cookie chết, không có blob gateway...)."""


# ---------------------------------------------------------------- cookie utils

def parse_cookie_header(raw: str) -> dict[str, str]:
    """'a=1; b=2' -> {'a': '1', 'b': '2'} (bỏ phần 'Cookie:' nếu có)."""
    raw = raw.strip()
    if raw.lower().startswith("cookie:"):
        raw = raw[len("cookie:"):].strip()
    out: dict[str, str] = {}
    for part in raw.split(";"):
        part = part.strip()
        if not part or "=" not in part:
            continue
        name, value = part.split("=", 1)
        name, value = name.strip(), value.strip()
        # Chuỗi cookie export từ trình duyệt đôi khi có khóa trùng nhau,
        # trong đó một bản rỗng (vd: hatch_gw=...; ...; hatch_gw=).
        # Giữ bản đầu tiên khác rỗng, đừng để bản rỗng sau ghi đè mất.
        if name in out:
            if not out[name] and value:
                out[name] = value
            continue
        out[name] = value
    return out


def parse_netscape_file(path: Path | str) -> dict[str, str]:
    """Đọc file cookies.txt chuẩn Netscape (7 cột, tab-separated)."""
    out: dict[str, str] = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) >= 7:
            out[cols[5].strip()] = cols[6].strip()
        elif "=" in line:  # fallback: dòng dạng name=value
            name, value = line.split("=", 1)
            out[name.strip()] = value.strip()
    return out


def parse_cookie_json(data) -> dict[str, str]:
    """JSON export: list[{name,value}] hoặc dict {name: value}."""
    if isinstance(data, dict):
        return {str(k): str(v) for k, v in data.items()}
    if isinstance(data, list):
        out: dict[str, str] = {}
        for item in data:
            if isinstance(item, dict) and "name" in item and "value" in item:
                out[str(item["name"])] = str(item["value"])
        return out
    raise ValueError("Định dạng JSON cookie không hỗ trợ")


def load_cookies(source: str) -> dict[str, str]:
    """Tự nhận diện: đường dẫn file (.txt/.json) hoặc chuỗi cookie thô."""
    # Chuỗi cookie thô rất dài và chứa ';' — đừng để Path().exists()
    # crash (OSError: File name too long) mà phải rơi xuống parse header.
    if ";" in source or "=" in source:
        stripped = source.strip()
        if stripped.startswith(("{", "[")):
            return parse_cookie_json(json.loads(source))
        return parse_cookie_header(source)
    p = Path(source)
    try:
        exists = p.exists()
    except OSError:
        exists = False
    if exists:
        if p.suffix.lower() == ".json":
            return parse_cookie_json(json.loads(p.read_text(encoding="utf-8")))
        return parse_netscape_file(p)
    if source.strip().startswith(("{", "[")):
        return parse_cookie_json(json.loads(source))
    return parse_cookie_header(source)


def cookies_to_header(cookies: dict[str, str]) -> str:
    return "; ".join(f"{k}={v}" for k, v in cookies.items())


# ---------------------------------------------------------------- proxy

@dataclass
class ProxyConfig:
    raw: str = ""
    scheme: str = ""
    host: str = ""
    port: int = 0
    username: str = ""
    password: str = ""

    @classmethod
    def parse(cls, raw: str) -> "ProxyConfig":
        raw = (raw or "").strip()
        if not raw:
            return cls()
        if "://" not in raw:
            raw = "http://" + raw
        try:
            u = urlparse(raw)
            return cls(
                raw=raw,
                scheme=(u.scheme or "http").lower(),
                host=u.hostname or "",
                port=u.port or 0,
                username=u.username or "",
                password=u.password or "",
            )
        except ValueError:
            # Cổng sai định dạng (chữ, vượt 0-65535...) -> coi như proxy
            # không hợp lệ thay vì ném lỗi làm sập cả chương trình
            # (u.port là property, lỗi chỉ nổ khi truy cập chứ không nổ
            # ở urlparse, nên try phải bao cả khối dựng này.)
            return cls(raw=raw)

    def is_valid(self) -> bool:
        return bool(self.host and self.port)

    def to_requests(self) -> dict[str, str]:
        """Dict proxies cho requests. socks5 cần gói PySocks (pip install pysocks)."""
        if not self.is_valid():
            return {}
        return {"http": self.raw, "https": self.raw}

    def masked(self) -> str:
        if not self.is_valid():
            return "-"
        auth = f"{self.username}:***@" if self.username else ""
        return f"{self.scheme}://{auth}{self.host}:{self.port}"

    def test(self, timeout: int = 10) -> tuple[bool, str]:
        """Kiểm tra proxy có dùng được không (qua httpbin.org/ip)."""
        if not self.is_valid():
            return False, "proxy không hợp lệ"
        try:
            r = requests.get(
                "https://httpbin.org/ip",
                proxies=self.to_requests(),
                timeout=timeout,
            )
            if r.status_code == 200:
                return True, f"OK, IP qua proxy: {r.json().get('origin')}"
            return False, f"HTTP {r.status_code}"
        except Exception as e:  # noqa: BLE001 - báo lỗi gọn cho CLI
            return False, str(e)


# ---------------------------------------------------------------- account

@dataclass
class CookieAccount:
    """Một tài khoản chỉ gồm thứ login cần (không đếm job, không cooldown)."""

    name: str
    cookie: str = ""          # chuỗi header Cookie thô
    cookie_file: str = ""     # hoặc đường dẫn file cookies.txt / .json
    proxy: str = ""           # vd: http://user:pass@host:port
    note: str = ""

    def cookies(self) -> dict[str, str]:
        if self.cookie_file:
            return load_cookies(self.cookie_file)
        return parse_cookie_header(self.cookie)

    def proxy_config(self) -> ProxyConfig:
        return ProxyConfig.parse(self.proxy)

    def public_dict(self) -> dict:
        """Bản in/log được: cookie che đi, proxy che mật khẩu."""
        d = asdict(self)
        d["cookie"] = "***" if self.cookie else ""
        d["proxy"] = self.proxy_config().masked()
        return d


def load_accounts_file(path: Path | str) -> list[CookieAccount]:
    """Đọc file accounts JSON: {"accounts": [...]} hoặc [...].

    Chỉ lấy các trường CookieAccount biết; trường lạ (jobs_done...) bỏ qua.
    """
    p = Path(path)
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    items = data.get("accounts", []) if isinstance(data, dict) else data
    known = set(CookieAccount.__dataclass_fields__)
    return [
        CookieAccount(**{k: v for k, v in item.items() if k in known})
        for item in items if isinstance(item, dict) and item.get("name")
    ]


def save_accounts_file(path: Path | str, accounts: list[CookieAccount]) -> None:
    """Ghi file accounts JSON với quyền 0600 (cookie là bí mật)."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = {"accounts": [asdict(a) for a in accounts]}
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    try:
        os.chmod(p, 0o600)
    except OSError:
        pass


# ---------------------------------------------------------------- session + login check

def build_session(account: CookieAccount) -> requests.Session:
    """Session requests đã gắn header, cookie và proxy của acc."""
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    session.cookies.update(account.cookies())
    proxy = account.proxy_config()
    if proxy.is_valid():
        session.proxies.update(proxy.to_requests())
    return session


def _url(base_url: str, path: str) -> str:
    return urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))


def check_login(session: requests.Session,
                base_url: str = DEFAULT_BASE_URL) -> tuple[bool, str]:
    """Kiểm tra cookie có thực sự đăng nhập được vào Muse hay không.

    Đã xác minh bằng thử nghiệm thật (2026-10-26, cookie dạng
    hatch_native_auth_state / hatch_sess / hatch_gw):
    - GET {base}/ với cookie hợp lệ -> 200, trang app đầy đủ (~250KB),
      ở lại đúng host muse.ai.
    - Cookie hết hạn/giả -> bị redirect sang auth.muse.ai (400) hoặc 401.
    - /api/auth/session KHÔNG dùng được cho loại cookie này: nó trả 401
      ngay cả khi cookie còn sống, nên không được dùng làm phép thử nữa.
    Phép thử chính là GET trang chủ; /api/me là phép thử phụ.
    Lưu ý: đây chỉ kiểm tra session web còn sống, không đảm bảo API
    sinh video (endpoint chưa công khai) sẽ chấp nhận cookie.
    """
    base_host = urlparse(base_url).hostname or ""
    last_reason = ""
    for label, path in (("trang chủ", "/"), ("api/me", "/api/me")):
        try:
            r = session.get(_url(base_url, path), timeout=20)
        except requests.RequestException as e:
            return False, f"Lỗi mạng/proxy khi kiểm tra {label}: {e}"
        final_host = urlparse(r.url).hostname or ""
        if (
            r.status_code == 200
            and final_host == base_host
            and len(r.text) > 10_000
        ):
            return True, f"Đăng nhập OK (session web còn sống, kiểm tra qua {label})"
        if r.status_code in (401, 403):
            last_reason = f"Cookie hết hạn hoặc bị từ chối (HTTP {r.status_code} ở {label})"
            break
        if final_host != base_host:
            last_reason = f"Chưa đăng nhập (bị chuyển sang {final_host})"
            break
        last_reason = (
            f"{label}: HTTP {r.status_code}, trang trả về không giống app đã đăng nhập"
        )
    return False, last_reason or "Không xác định được trạng thái đăng nhập"


# ---------------------------------------------------------------- gateway init

def parse_gateway_init(html: str) -> dict:
    """Parse window.__HATCH_GATEWAY_INIT__ từ HTML trang chủ muse.ai.

    Object nằm trong RSC payload bị JSON-escape 2 lớp nên phải gỡ escape
    lặp trước khi quét ngoặc cân bằng.
    Chỉ gatewayUrl + vmName là bắt buộc; authToken thiếu thì tầng Noise
    tự refresh sau (đừng fail cứng ở đây — bài học 2026-10-30: blob có đủ
    2 khóa kia nhưng thiếu authToken vẫn là session sống).
    """
    i = html.find("window.__HATCH_GATEWAY_INIT__=")
    if i < 0:
        raise MuseLoginError("Không thấy __HATCH_GATEWAY_INIT__ trong trang chủ muse.ai")
    seg = html[i:i + 6000]
    for _ in range(4):
        seg2 = seg.replace('\\"', '"').replace("\\\\", "\\")
        if seg2 == seg:
            break
        seg = seg2
    j = seg.find("{")
    if j < 0:
        raise MuseLoginError("Không parse được __HATCH_GATEWAY_INIT__ (không thấy '{')")
    depth = 0
    end = None
    for k in range(j, len(seg)):
        if seg[k] == "{":
            depth += 1
        elif seg[k] == "}":
            depth -= 1
            if depth == 0:
                end = k + 1
                break
    if end is None:
        raise MuseLoginError("Không parse được __HATCH_GATEWAY_INIT__ (ngoặc không cân)")
    try:
        init = json.loads(seg[j:end])
    except ValueError as e:
        raise MuseLoginError(f"Không parse được __HATCH_GATEWAY_INIT__: {e}") from None
    for key in ("gatewayUrl", "vmName"):
        if not init.get(key):
            raise MuseLoginError(f"__HATCH_GATEWAY_INIT__ thiếu khóa {key}")
    return init


def fetch_gateway_init(session: requests.Session,
                       base_url: str = DEFAULT_BASE_URL) -> dict:
    """GET trang chủ muse.ai, parse __HATCH_GATEWAY_INIT__.

    Trang chủ trả 200 nhưng không có blob gateway nghĩa là phiên đăng nhập
    không còn sống (cookie chết nhưng server vẫn trả trang shell thay vì
    redirect về auth) — trường hợp này raise MuseLoginError thay vì trả
    dict rỗng, để caller không tưởng là login OK.
    """
    r = session.get(_url(base_url, "/"), timeout=20)
    if r.status_code != 200:
        raise MuseLoginError(
            f"Không tải được trang chủ muse.ai (HTTP {r.status_code}) — "
            "cookie có thể đã hết hạn"
        )
    try:
        return parse_gateway_init(r.text)
    except MuseLoginError as e:
        raise MuseLoginError(
            f"{e} — phiên đăng nhập có thể đã hết hạn (trang chủ trả về "
            "nhưng không có thông tin gateway). Kiểm tra lại cookie, "
            "lấy cookie mới nếu cần."
        ) from None
