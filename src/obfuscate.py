"""Bölüm B: anlamı koruyan gizleme dönüşümleri.

Tasarım
-------
Saldırılar isteğin farklı yerlerinde (URI, body, Cookie/Referer gibi header'lar) ve farklı, hatta aynı
parça içinde karışık derinlikte URL encoding ile bulunabilir. Bu yüzden:

  1. Her alan, ham hâlde görünen yapısal ayraçlardan (/ ? & = ; , boşluk) parçalara bölünür.
  2. Parça bir katman çözülür; her çözülmüş karakterin hangi ham birimden (%XX, '+', düz karakter)
     geldiği tutulur. Çözülecek kodlama kalmayana kadar özyinelemeli olarak devam edilir.
  3. Dönüşüm (tek bir regex geçişi) en içteki, tamamen çözülmüş metne uygulanır ve değiştirdiği
     aralıkları bildirir.
  4. Geri dönerken bu aralıklar her katmanda ham birimlere eşlenir: değişmeyen bölgeler bayt bayt
     kopyalanır; yalnızca yeni karakterler o katmanın stiliyle kodlanır (o katmanda zaten ham görünen
     karakterler ham bırakılır, diğerleri %XX; boşluk için '+' tercihi ve hex harf büyüklüğü korunur).

Böylece dönüşümün dokunmadığı her şey (karışık derinlikli bölgeler dahil) birebir korunur.

Kabuk komutu dönüşümü yalnızca önünde bir kabuk ayıracı bulunan sözcüklere, SQL dönüşümleri yalnızca SQL'e benzeyen
parçalara uygulanır; böylece parametre adları (ör. `dir=`, `pwd=`, `order=`) değiştirilmez.

Dönüşümler saldırı kategorisine özgüdür (ör. SQL dönüşümleri yalnızca SQLi satırlarına uygulanır),
çünkü aynı metin farklı bağlamlarda farklı anlam taşır (ör. 'sleep 15' kabukta harfe duyarlıdır).
Anlam koruma varsayımları TRANSFORMS[...]["assumption"] içinde belirtilmiştir.
"""
from __future__ import annotations

import random
import re
from urllib.parse import quote, unquote_plus

from http_parse import BOILERPLATE_HEADERS

MAX_DEPTH = 40
_HEXCH = set("0123456789abcdefABCDEF")
_SPLIT_HEAD_BODY = re.compile(r"\r?\n\r?\n")
_DELIMS_URI = re.compile(r"([/?&=;,])")
_DELIMS_VAL = re.compile(r"([/?&=;,]|\s+)")


# --------------------------------------------------------------------------- kodlama katmanları
def _units(s: str) -> list[tuple[str, str]]:
    """Bir katman çözümü: (ham birim, çözülmüş karakter). %XX bayt olarak (latin-1) çözülür, '+' boşluk."""
    out, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c == "%" and i + 2 < n and s[i + 1] in _HEXCH and s[i + 2] in _HEXCH:
            out.append((s[i:i + 3], chr(int(s[i + 1:i + 3], 16))))
            i += 3
        elif c == "+":
            out.append(("+", " "))
            i += 1
        else:
            out.append((c, c))
            i += 1
    return out


class _Style:
    def __init__(self, units):
        self.encoded = {ch for u, ch in units if len(u) == 3}
        self.literal = {ch for u, ch in units if len(u) == 1 and u != "+"} - self.encoded
        self.plus_space = any(u == "+" for u, _ in units)
        lettered = [u for u, _ in units if len(u) == 3 and any(c.isalpha() for c in u[1:])]
        self.lower = bool(lettered) and sum(1 for u in lettered if u != u.upper()) > len(lettered) / 2

    def enc(self, c: str) -> str:
        if c == " " and self.plus_space:
            return "+"
        if (c.isascii() and c.isalnum()) or (c in self.literal and c not in "%+ "):
            return c
        h = "%{:02X}".format(ord(c) & 0xFF)
        return h.lower() if self.lower else h


def _encode_raw(text: str) -> str:
    """Hiç kodlanmamış bir parçaya yeni eklenen boşluk/kontrol karakterlerini kodlar."""
    return re.sub(r"[\s\x00-\x1f]", lambda m: "%{:02X}".format(ord(m.group(0))), text)


Edit = tuple  # (başlangıç, bitiş, yeni metin)


def _splice(s: str, edits) -> str:
    out, pos = [], 0
    for a, b, t in edits:
        out.append(s[pos:a])
        out.append(t)
        pos = b
    out.append(s[pos:])
    return "".join(out)


def _rewrite(s: str, rule, depth: int = 0):
    """s'ye kuralı uygular; (yeni metin, s koordinatlarında düzenlemeler) döndürür."""
    units = _units(s)
    if depth >= MAX_DEPTH or all(u == ch for u, ch in units):
        edits = rule(s)
        if depth == 0:
            edits = [(a, b, _encode_raw(t)) for a, b, t in edits]
        return _splice(s, edits), edits
    dec = "".join(ch for _, ch in units)
    _, inner = _rewrite(dec, rule, depth + 1)
    if not inner:
        return s, []
    off = [0]
    for u, _ in units:
        off.append(off[-1] + len(u))
    st = _Style(units)
    edits = [(off[a], off[b], "".join(st.enc(c) for c in t)) for a, b, t in inner]
    return _splice(s, edits), edits


def _normalize_depth(tok: str) -> str:
    """Çok katmanlı kodlamayı tek katmana indirir (yalnızca 2+ katmanlı parçalar)."""
    layers = [tok]
    for _ in range(MAX_DEPTH):
        d = unquote_plus(layers[-1])
        if d == layers[-1]:
            break
        layers.append(d)
    if len(layers) <= 2:
        return tok
    st = _Style(_units(tok))
    safe = "".join(c for c in st.literal if c.isascii() and c not in "%+ \t\r\n")
    out = quote(layers[-1], safe=safe)
    return out.replace("%20", "+") if st.plus_space else out


def _apply_field(text: str, rule, splitter: re.Pattern) -> str:
    parts = splitter.split(text)
    return "".join(p if (i % 2 == 1 or not p) else
                   (_normalize_depth(p) if rule is None else _rewrite(p, rule)[0])
                   for i, p in enumerate(parts))


def apply_request(raw: str, rule) -> str:
    """İsteğin URI, body ve saldırı yüzeyindeki header değerlerine kuralı uygular.
    rule=None: kodlama derinliği normalizasyonu."""
    m = _SPLIT_HEAD_BODY.search(raw)
    head, sep, body = (raw[:m.start()], m.group(0), raw[m.end():]) if m else (raw, "", "")
    lines = re.split(r"(\r?\n)", head)
    first = lines[0].split(" ")
    if len(first) >= 3:
        uri = " ".join(first[1:-1])
        path, q, query = uri.partition("?")
        new_uri = _apply_field(path, rule, _DELIMS_URI) + q + _apply_field(query, rule, _DELIMS_URI)
        lines[0] = " ".join([first[0], new_uri, first[-1]])
    for i in range(2, len(lines), 2):
        name, colon, val = lines[i].partition(":")
        key = name.strip().lower()
        if not colon or key in BOILERPLATE_HEADERS or key.startswith("sec-"):
            continue
        lead = val[: len(val) - len(val.lstrip())]
        lines[i] = name + colon + lead + _apply_field(val.lstrip(), rule, _DELIMS_VAL)
    new_body = _apply_field(body, rule, _DELIMS_VAL) if body else body
    return "".join(lines) + sep + new_body


# --------------------------------------------------------------------------- kurallar (tek regex geçişi)
def _regex_rule(pattern: re.Pattern, repl, gate=None):
    """repl(match) -> yeni metin. Düzenlemeleri (başlangıç, bitiş, yeni) döndüren bir kural üretir."""
    def rule(s: str):
        if gate is not None and not gate(s):
            return []
        edits = []
        for m in pattern.finditer(s):
            t = repl(m)
            if t != m.group(0):
                edits.append((m.start(), m.end(), t))
        return edits
    return rule


def _rand_case(word: str, rng: random.Random) -> str:
    for _ in range(8):
        w = "".join(c.upper() if rng.random() < 0.5 else c.lower() for c in word)
        if w != word:
            return w
    return word.swapcase()


SQL_KW = (r"select|union|all|from|where|and|or|not|null|order|group|by|having|limit|sleep|benchmark|waitfor|"
          r"delay|case|when|then|else|end|rlike|like|insert|into|values|update|delete|drop|concat|char|chr|cast|"
          r"convert|information_schema|table_name|column_name|exec|xp_cmdshell|substring|ascii|if|extractvalue|updatexml")
_SQL_KW = re.compile(rf"\b(?:{SQL_KW})\b", re.I)
_SQL_WS = re.compile(rf"(\b(?:{SQL_KW})\b)([ \t]+)|([ \t]+)(?=\b(?:{SQL_KW})\b)", re.I)
_HTML_NAMES = re.compile(r"(<\s*/?)([a-z][a-z0-9]*)|(?<=[\s/\"'])(on[a-z]+|src|href|style|action|formaction|srcdoc)(?=\s*=)", re.I)
_HTML_WS = re.compile(r"(<\s*[a-z][a-z0-9]*)[ \t]+|(?<=[\"'a-z0-9])[ \t]+(?=(?:on[a-z]+|src|href|style)\s*=)", re.I)
_SHELL_CMD = re.compile(r"(?<=[;&|`(\s$])(cat|ls|id|whoami|uname|ping|sleep|echo|nslookup|curl|wget|nc|ncat|"
                        r"bash|sh|ifconfig|ipconfig|dir|type|timeout|netstat|hostname|pwd|perl|python|php)(?=[\s;&|`)<>]|$)")
_DOTDOT = re.compile(r"(?<![^/\\])\.\.(?=[/\\]|$)")
_OASTIFY = re.compile(r"oastify\.com\b", re.I)
_SQLISH_CH = re.compile(r"['\"()]")


def _sqlish(s: str) -> bool:
    """Parametre adı gibi tek kelimelik parçaları dışarıda bırakır: en az iki SQL anahtar kelimesi ya da tırnak/parantez."""
    return len(_SQL_KW.findall(s)) >= 2 or bool(_SQLISH_CH.search(s))


_PAYLOADISH = re.compile(rf"[<>'\"`;|(){{}}$]|\b(?:{SQL_KW})\b", re.I)


def make_rule(name: str, cat: str, rng: random.Random):
    if name == "case":
        if cat == "sql":
            return _regex_rule(_SQL_KW, lambda m: _rand_case(m.group(0), rng), gate=_sqlish)
        return _regex_rule(_HTML_NAMES, lambda m: (m.group(1) + _rand_case(m.group(2), rng)) if m.group(2)
                           else _rand_case(m.group(0), rng))
    if name == "whitespace":
        return _regex_rule(re.compile(r" +"), lambda m: "\t" * len(m.group(0)),
                           gate=lambda s: bool(_PAYLOADISH.search(s)))
    if name == "sql_comment":
        return _regex_rule(_SQL_WS, lambda m: (m.group(1) + "/**/") if m.group(1) else "/**/", gate=_sqlish)
    if name == "html_slash":
        return _regex_rule(_HTML_WS, lambda m: (m.group(1) + "/") if m.group(1) else "/")
    if name == "cmd_quote":
        return _regex_rule(_SHELL_CMD, lambda m: m.group(0)[0] + '""' + m.group(0)[1:])
    if name == "path_dot":
        return _regex_rule(_DOTDOT, lambda m: "." + (m.string[m.end():m.end() + 1] or "/") + "..")
    if name == "artifact":
        return _regex_rule(_OASTIFY, lambda m: "cb-listener.net")
    raise KeyError(name)


# --------------------------------------------------------------------------- dönüşüm tanımları
def category(label: str) -> str:
    """Saldırı kategorisi, etiket adından (iki veri setinde de aynı adlar)."""
    l = label.lower()
    if "normal" in l:
        return "normal"
    if "sql" in l:
        return "sql"
    if "cross-site" in l or "xss" in l:
        return "xss"
    if "command injection" in l:
        return "cmd"
    if "path traversal" in l:
        return "path"
    return "other"


ALL = {"sql", "xss", "cmd", "path", "other"}

TRANSFORMS = {
    "case": dict(cats={"sql", "xss"},
                 assumption="SQLi: SQL anahtar kelimeleri; XSS: HTML etiket/öznitelik adları büyük/küçük harfe duyarsızdır."),
    "whitespace": dict(cats=ALL,
                       assumption="Payload benzeri parçalarda boşluk yerine sekme: SQL, HTML öznitelik ayırıcısı, "
                                  "POSIX kabuk (IFS), HTTP header OWS için eşdeğer."),
    "sql_comment": dict(cats={"sql"},
                        assumption="SQL anahtar kelimelerine bitişik boşluk yerine /**/ (MySQL, PostgreSQL, MSSQL'de eşdeğer)."),
    "html_slash": dict(cats={"xss"},
                       assumption="HTML etiketinde ad/öznitelik arasında boşluk yerine '/' (HTML5 ayrıştırıcısında eşdeğer)."),
    "cmd_quote": dict(cats={"cmd"},
                      assumption='Kabuk komut adına boş tırnak çifti ("") eklemek (bash/sh ve cmd.exe komut adını değiştirmez).'),
    "path_dot": dict(cats={"path"},
                     assumption="'../' yerine './../' (yol çözümlemesinde eşdeğer)."),
    "artifact": dict(cats=ALL,
                     assumption="Burp Collaborator alan adı (oastify.com) saldırganın seçtiği başka bir geri çağırma "
                                "alan adıyla değiştirilir (alt alan adı korunur)."),
    "encoding_norm": dict(cats=ALL,
                          assumption="ÇÖZÜCÜYE BAĞLI: çok katmanlı URL encoding tek katmana indirilir; hedef "
                                     "yinelemeli çözüyorsa eşdeğer."),
}
COMBO_ORDER = ["artifact", "sql_comment", "html_slash", "cmd_quote", "path_dot", "case", "whitespace"]
TRANSFORMS["combo"] = dict(cats=ALL, assumption="Kategoriye uygulanabilen tüm dönüşümler birlikte: "
                           + ", ".join(COMBO_ORDER) + " (çözücüye bağlı encoding_norm hariç).")


def applicable(name: str, label: str) -> bool:
    c = category(label)
    return c != "normal" and c in TRANSFORMS[name]["cats"]


def transform(raw: str, name: str, label: str, seed: int = 0) -> str:
    """Dönüşümü uygular; kategori dışındaysa isteği değiştirmeden döndürür."""
    if not applicable(name, label):
        return raw
    if name == "combo":
        for n in COMBO_ORDER:
            raw = transform(raw, n, label, seed)
        return raw
    if name == "encoding_norm":
        return apply_request(raw, None)
    return apply_request(raw, make_rule(name, category(label), random.Random(seed)))
