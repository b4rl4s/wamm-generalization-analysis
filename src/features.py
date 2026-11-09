"""WAMM makalesinde tarif edilen XGBoost özellik uzayının yeniden kurulumu.

Makale (arXiv 2512.23610, Bölüm IV):
  - TF-IDF karakter n-gram (1,2), en fazla 2000 özellik
  - Elle tasarlanmış: uzunluk, özel karakter sayıları (tırnak, açılı parantez, noktalı virgül...),
    SQL anahtar kelime ve path traversal göstergeleri, sayısal ve yüzde-encoded karakter sayıları,
    Shannon entropisi, URL derinliği, benzersiz karakter sayısı
  - Regex imzaları: XSS, SQLi, RFI, LFI, SSTI, RCE, CMDi, path traversal

Makalede verilmeyen ayrıntılar (tam regex listesi, TF-IDF'in girdiyi kesip kesmediği vb.)
bizim varsayımımızdır; bkz. ASSUMPTIONS.
"""
from __future__ import annotations

import math
import re
import warnings

warnings.filterwarnings("ignore", message="This pattern is interpreted as a regular expression")
from collections import Counter
from urllib.parse import unquote_plus

import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer

ASSUMPTIONS = [
    "TF-IDF: analyzer='char', ngram_range=(1,2), max_features=2000, lowercase=False, ham istek metni",
    "Elle tasarlanmış özellikler ve regex imzaları URL-decode edilmiş, küçük harfe çevrilmiş metin üzerinde",
    "Regex imzaları makalede listelenmediği için yaygın kalıplardan derlendi",
]

SPECIAL_CHARS = {
    "sq": "'", "dq": '"', "lt": "<", "gt": ">", "semi": ";", "lpar": "(", "rpar": ")",
    "eq": "=", "pct": "%", "dash": "-", "hash": "#", "slash": "/", "bslash": "\\",
    "pipe": "|", "amp": "&", "dollar": "$", "brace_l": "{", "brace_r": "}", "backtick": "`",
    "star": "*", "plus": "+", "comma": ",", "dot": ".", "colon": ":", "at": "@", "space": " ",
}

SQL_KW = re.compile(r"\b(select|union|insert|update|delete|drop|from|where|sleep|benchmark|waitfor|or\s+\d+=\d+|and\s+\d+=\d+|order\s+by|group\s+by|information_schema|concat|char\()", re.I)
TRAVERSAL = re.compile(r"(\.\./|\.\.\\|%2e%2e|\.\.%2f|\.\.%5c)", re.I)

SIGNATURES = {
    "sig_xss": r"(<script|javascript:|on(error|load|mouseover|focus|click)\s*=|<img[^>]+src|<svg|alert\s*\(|document\.cookie|<iframe)",
    "sig_sqli": r"(union(\s|/\*.*?\*/)+(all\s+)?select|'\s*(or|and)\s+['\d]|sleep\s*\(\d|benchmark\s*\(|waitfor\s+delay|--\s|#\s*$|/\*.*?\*/|\bselect\b.+\bfrom\b)",
    "sig_rfi": r"(=\s*(https?|ftp|php|data|expect)://|include\s*\(|require\s*\()",
    "sig_lfi": r"(/etc/passwd|/etc/shadow|win\.ini|boot\.ini|/proc/self|php://filter|\.\./\.\./)",
    "sig_ssti": r"(\{\{.*?\}\}|\{%.*?%\}|\$\{.*?\}|<%=.*?%>|#\{.*?\})",
    "sig_rce": r"(\b(eval|exec|system|passthru|shell_exec|popen|proc_open|assert)\s*\(|runtime\.getruntime)",
    "sig_cmdi": r"([;&|`]\s*(cat|ls|id|whoami|uname|wget|curl|nc|ping|sleep|echo)\b|\$\(.*?\)|\$ifs)",
    "sig_traversal": r"(\.\./|\.\.\\)",
}
_SIG = {k: re.compile(v, re.I | re.S) for k, v in SIGNATURES.items()}


def _decode(s: str) -> str:
    try:
        return unquote_plus(s).lower()
    except Exception:
        return s.lower()


def _entropy(s: str) -> float:
    if not s:
        return 0.0
    n = len(s)
    return -sum(c / n * math.log2(c / n) for c in Counter(s).values())


def _uri(raw: str) -> str:
    first = raw.split("\n", 1)[0]
    parts = first.split(" ")
    return parts[1] if len(parts) >= 2 else ""


def handcrafted(requests: pd.Series) -> pd.DataFrame:
    raw = requests.astype(str)
    dec = raw.map(_decode)
    uri = raw.map(_uri)
    f = pd.DataFrame(index=raw.index)
    f["len"] = raw.str.len()
    f["len_decoded"] = dec.str.len()
    for name, ch in SPECIAL_CHARS.items():
        f[f"cnt_{name}"] = dec.str.count(re.escape(ch))
    f["cnt_digit"] = raw.str.count(r"\d")
    f["cnt_pct_encoded"] = raw.str.count(r"%[0-9a-fA-F]{2}")
    f["sql_kw_count"] = dec.str.count(SQL_KW)
    f["has_sql_kw"] = (f["sql_kw_count"] > 0).astype(np.int8)
    f["has_traversal"] = raw.str.contains(TRAVERSAL).astype(np.int8)
    f["entropy"] = raw.map(_entropy)
    f["url_depth"] = uri.str.split("?", n=1).str[0].str.count("/")
    f["uri_len"] = uri.str.len()
    f["n_params"] = uri.str.count("&") + uri.str.contains(r"\?").astype(int)
    f["unique_chars"] = raw.map(lambda s: len(set(s)))
    for k, rx in _SIG.items():
        f[k] = dec.str.contains(rx).astype(np.int8)
    return f.astype(np.float32)


class WammFeaturizer:
    """TF-IDF (yalnızca eğitim verisine fit) + elle tasarlanmış özellikler."""

    def __init__(self, max_features: int = 2000):
        self.tfidf = TfidfVectorizer(analyzer="char", ngram_range=(1, 2), max_features=max_features,
                                     lowercase=False, dtype=np.float32)
        self.hand_cols: list[str] = []

    def feature_names(self) -> list[str]:
        return [f"tfidf[{t!r}]" for t in self.tfidf.get_feature_names_out()] + self.hand_cols

    def fit_transform(self, requests: pd.Series, hand: pd.DataFrame) -> sparse.csr_matrix:
        X_t = self.tfidf.fit_transform(requests.astype(str))
        self.hand_cols = list(hand.columns)
        return sparse.hstack([X_t, sparse.csr_matrix(hand.values)], format="csr")

    def transform(self, requests: pd.Series, hand: pd.DataFrame) -> sparse.csr_matrix:
        X_t = self.tfidf.transform(requests.astype(str))
        return sparse.hstack([X_t, sparse.csr_matrix(hand[self.hand_cols].values)], format="csr")
