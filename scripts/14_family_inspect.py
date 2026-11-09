"""Bölüm A: aile gruplamasının elle doğrulanması için örnek çıkarımı.

Kullanım: python scripts/14_family_inspect.py <dataset> [<eşik>=0.8] [<sınıf başına aile>=3]
Her sınıftan, en az 5 üyeli rastgele aileler seçilir (seed 0); her aileden 3 üyenin çözülmüş saldırı
yüzeyi ve iskeleti yazılır. Ayrıca aile içinde URI yolu ve çözülmüş saldırı yüzeyinin ne kadar
paylaşıldığına dair basit ölçüler verilir.

Çıktı: results/family_validation_<dataset>_<eşik>.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from families import decode  # noqa: E402
from http_parse import parse  # noqa: E402
from wamm_data import CACHE, ROOT, load  # noqa: E402


def clip(s: str, n: int = 260) -> str:
    s = s.replace("\r", "").replace("\n", " ⏎ ").replace("`", "'")
    return s if len(s) <= n else s[:n] + " …"


def main() -> None:
    name = sys.argv[1]
    thr = sys.argv[2] if len(sys.argv) > 2 else "0.8"
    k = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    df = load(name)
    fam = pd.read_parquet(CACHE / f"{name}_families.parquet")
    lab = df["label"].astype(str).values
    key = fam[f"family_{thr}"].astype(str).values + "|" + lab
    sizes = pd.Series(key).value_counts()
    rng = np.random.default_rng(0)
    out = [f"# Aile doğrulaması — {name}, eşik {thr}", "",
           "Her sınıftan en az 5 üyeli rastgele aileler; her aileden 3 rastgele üye. "
           "'Yüzey' = tamamen çözülmüş saldırı yüzeyi (method+URI, standart dışı header'lar, body).", ""]
    summary = []
    for c in sorted(set(lab)):
        fams = [f for f in sizes.index if f.endswith("|" + c) and sizes[f] >= 5]
        if not fams:
            continue
        pick = rng.choice(fams, min(k, len(fams)), replace=False)
        out += [f"## {c}", "", f"Sınıfta {sum(1 for f in sizes.index if f.endswith('|' + c))} aile; ≥5 üyeli: {len(fams)}.", ""]
        for f in pick:
            idx = np.flatnonzero(key == f)
            mem = rng.choice(idx, min(3, len(idx)), replace=False)
            surf_all = [decode(parse(df['request'].iloc[i]).attack_surface(), rounds=40) for i in idx[:200]]
            paths = [parse(df['request'].iloc[i]).path for i in idx[:200]]
            same_path = pd.Series(paths).value_counts(normalize=True).iloc[0]
            uniq_surf = len(set(surf_all)) / len(surf_all)
            summary.append((c, int(len(idx)), round(float(same_path), 2), round(float(uniq_surf), 2)))
            out += [f"### Aile `{f.split('|')[0]}` — {len(idx)} üye · en yaygın yol payı {same_path:.0%} · "
                    f"farklı yüzey oranı {uniq_surf:.0%}", ""]
            for i in mem:
                out.append(f"- `{clip(decode(parse(df['request'].iloc[i]).attack_surface(), rounds=40))}`")
            out.append("")
    out += ["## Özet", "", "| Sınıf | Aile boyutu | En yaygın yol payı | Farklı yüzey oranı |", "|---|---:|---:|---:|"]
    out += [f"| {c} | {n} | {p:.0%} | {u:.0%} |" for c, n, p, u in summary]
    path = ROOT / "results" / f"family_validation_{name}_{thr}.md"
    path.write_text("\n".join(out) + "\n")
    print(f"yazıldı: {path}")


if __name__ == "__main__":
    main()
