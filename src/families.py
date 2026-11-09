"""Payload iskeleti çıkarma ve yakın-kopya (payload ailesi) gruplama.

Plan Bölüm 7, A1–A4:
  - Header'lar hariç payload (URI + body) kullanılır.
  - İskelet: tekrarlı URL decode, küçük harf, sayılar -> N, tırnak içi -> S,
    site içerik slug'ları -> W, yorum/boşluk dizileri -> tek boşluk.
  - Yakın kopyalar: iskelet üzerinde karakter 5-gram MinHash + LSH, ardından union-find
    ile bağlı bileşenler (aile). Zincirlenmeye karşı bileşen boyutları raporlanır.
"""
from __future__ import annotations

import re
import zlib
from urllib.parse import unquote_plus

import numpy as np

_NUM = re.compile(r"\d+")
_HEX = re.compile(r"\b0x[0-9a-f]+\b")
_SQ = re.compile(r"'[^']{0,200}'")
_DQ = re.compile(r'"[^"]{0,200}"')
_SLUG = re.compile(r"\b[a-z]+(?:-[a-z]+){2,}\b")  # lorem-ipsum-dolor tipi içerik slug'ları
_COMMENT = re.compile(r"/\*.*?\*/", re.S)
_WS = re.compile(r"[\s+]+")
_LONG_TOKEN = re.compile(r"[a-z0-9_\-]{25,}")  # uzun rastgele değerler (token, hash, cookie benzeri)


def decode(s: str, rounds: int = 10) -> str:
    for _ in range(rounds):
        try:
            d = unquote_plus(s)
        except Exception:
            break
        if d == s:
            break
        s = d
    return s


def skeleton(payload: str, max_len: int = 4000) -> str:
    """İskelet; uzunluk sınırı decode ve normalizasyondan SONRA uygulanır."""
    s = decode(payload).lower()
    s = _COMMENT.sub(" ", s)
    s = _HEX.sub("N", s)
    s = _SQ.sub("'S'", s)
    s = _DQ.sub('"S"', s)
    s = _SLUG.sub("W", s)
    s = _LONG_TOKEN.sub("T", s)
    s = _NUM.sub("N", s)
    s = _WS.sub(" ", s)
    return s.strip()[:max_len]


# ---------------------------------------------------------------- MinHash / LSH
_P = (1 << 61) - 1


def minhash_signatures(texts: list[str], num_perm: int = 64, k: int = 5, seed: int = 1) -> np.ndarray:
    """Karakter k-gram kümeleri için MinHash imzaları (numpy ile vektörize)."""
    rng = np.random.default_rng(seed)
    # a, b < 2^32 ve h < 2^32 olduğundan a*h + b < 2^64: uint64 taşması olmaz
    a = rng.integers(1, 1 << 32, size=num_perm, dtype=np.uint64)
    b = rng.integers(0, 1 << 32, size=num_perm, dtype=np.uint64)
    out = np.empty((len(texts), num_perm), dtype=np.uint64)
    for i, t in enumerate(texts):
        sh = shingles(t, k)
        # crc32: süreçten bağımsız, tekrar üretilebilir 32-bit hash (Python hash() rastgeledir)
        h = np.fromiter((zlib.crc32(x) for x in sh), dtype=np.uint64, count=len(sh))
        v = (h[:, None] * a[None, :] + b[None, :]) % np.uint64(_P)
        out[i] = v.min(axis=0)
    return out


def lsh_families(sig: np.ndarray, threshold: float, bands: int = 16) -> np.ndarray:
    """LSH bantlarıyla aday çiftler + imza tabanlı Jaccard doğrulaması → aile kimlikleri.

    Her kovada üyeler kovanın ilk üyesiyle (yıldız) karşılaştırılır; tahmini Jaccard >= threshold
    ise birleştirilir. Bu, tüm çiftleri karşılaştırmadan bağlı bileşenleri yaklaşık bulur.
    """
    n, m = sig.shape
    r = m // bands
    uf = UnionFind(n)
    for bi in range(bands):
        block = sig[:, bi * r:(bi + 1) * r]
        keys = np.ascontiguousarray(block).view(np.dtype((np.void, block.dtype.itemsize * r))).ravel()
        order = np.argsort(keys, kind="stable")
        sk = keys[order]
        starts = np.flatnonzero(np.r_[True, sk[1:] != sk[:-1]])
        ends = np.r_[starts[1:], n]
        for s, e in zip(starts, ends):
            if e - s < 2:
                continue
            members = order[s:e]
            anchor = members[0]
            sims = (sig[members[1:]] == sig[anchor]).mean(axis=1)
            for j in members[1:][sims >= threshold]:
                uf.union(int(anchor), int(j))
    return uf.labels()


def shingles(s: str, k: int = 5) -> set[bytes]:
    if len(s) <= k:
        return {s.encode("utf-8", "surrogatepass")}
    b = s.encode("utf-8", "surrogatepass")
    return {b[i:i + k] for i in range(len(b) - k + 1)}


class UnionFind:
    def __init__(self, n: int):
        self.p = np.arange(n)

    def find(self, x: int) -> int:
        p = self.p
        root = x
        while p[root] != root:
            root = p[root]
        while p[x] != root:
            p[x], x = root, p[x]
        return root

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)

    def labels(self) -> np.ndarray:
        return np.array([self.find(i) for i in range(len(self.p))])
