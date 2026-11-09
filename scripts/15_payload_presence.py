"""Etiket kalitesi kontrolü: her sınıfta, çözülmüş saldırı yüzeyinde o sınıfa özgü bir gösterge geçen satır oranı.

Kullanım: python scripts/15_payload_presence.py <dataset> [<sınıf başına örnek>=3000]
Göstergeler kaba ve kasıtlı olarak geniştir; amaç, göstergesi HİÇ olmayan satırların oranını görmektir.
Çıktı: results/payload_presence_<dataset>.md
"""
from __future__ import annotations
import re, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from families import decode  # noqa: E402
from http_parse import parse  # noqa: E402
from wamm_data import ROOT, load  # noqa: E402

IND = {
    "sql": r"'|\"|\b(select|union|sleep|benchmark|waitfor|or\s+\d+=\d+|and\s+\d+=\d+)\b",
    "xss": r"<\s*[a-z/!]|alert\s*\(|prompt\s*\(|confirm\s*\(|javascript:|on[a-z]+\s*=|document\.",
    "cmd": r"[|;&`]\s*(ping|sleep|echo|cat|id|whoami|nslookup|curl|wget|uname|ls|dir|type)\b|\$\(|\$\{ifs",
    "ssti": r"\{\{|\$\{|<%|#\{|\{%|\{\$|<!--\s*#\s*(set|echo|exec|include)",
    "path": r"\.\./|\.\.\\|/etc/passwd|win\.ini|\.git/",
    "ssrf": r"oastify\.com|https?://(127\.|localhost|169\.254|0\.0\.0\.0|\[::)|xinclude|<!entity",
    "code": r"\b(eval|exec|system|passthru|assert|compile|__import__|sleep)\s*\(|\$\{|<\?php|;\s*\w+\(",
}
CLS = {"sql": "sql", "cross-site": "xss", "os command": "cmd", "command injection": "cmd", "ssti": "ssti",
       "path traversal": "path", "ssrf": "ssrf", "code injection": "code"}

def kind(label):
    l = label.lower()
    return next((v for k, v in CLS.items() if k in l), None)

def main():
    name = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    df = load(name); lab = df["label"].astype(str).values; rng = np.random.default_rng(0)
    rx = {k: re.compile(v, re.I) for k, v in IND.items()}
    rows = []
    for c in sorted(set(lab)):
        idx = np.flatnonzero(lab == c); idx = rng.choice(idx, min(n, len(idx)), replace=False)
        surf = [decode(parse(df["request"].iloc[i]).attack_surface(), rounds=40) for i in idx]
        r = {"Sınıf": c, "n": len(idx)}
        for k, p in rx.items():
            r[k] = round(100 * np.mean([bool(p.search(s)) for s in surf]), 1)
        own = kind(c)
        r["kendi göstergesi"] = r[own] if own else None
        r["hiç gösterge yok"] = round(100 * np.mean([not any(p.search(s) for p in rx.values()) for s in surf]), 1)
        rows.append(r)
    t = pd.DataFrame(rows)
    out = ROOT / "results" / f"payload_presence_{name}.md"
    out.write_text(f"# Gösterge varlığı — {name}\n\nDeğerler: satırların yüzdesi (sınıf başına en fazla {n} satır).\n\n"
                   + t.to_markdown(index=False) + "\n")
    print(t.to_string(index=False))

if __name__ == "__main__":
    main()
