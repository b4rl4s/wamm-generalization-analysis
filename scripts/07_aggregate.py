"""Bölme deneylerini seed'ler üzerinden özetler (ortalama, min, maks).

Kullanım: python scripts/07_aggregate.py
Çıktı: results/splits_summary.json, results/splits_summary.md
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wamm_data import ROOT  # noqa: E402

SPLITS = ["random", "h_raw", "skeleton_id", "family_0.9", "family_0.8"]


def normal_idx(classes):
    return next(i for i, c in enumerate(classes) if "normal" in c.lower())


def metrics(r):
    cm = np.array(r["confusion_matrix"])
    n = normal_idx(r["classes"])
    att = [i for i in range(len(cm)) if i != n]
    sub = cm[att]
    err = sub.sum() - sum(cm[i, i] for i in att)
    return {
        "macro_f1": r["macro_f1"],
        "accuracy": r["accuracy"],
        "normal_fpr_pct": 100 * (1 - cm[n, n] / cm[n].sum()),
        "attack_miss_pct": 100 * sub[:, n].sum() / sub.sum(),
        "attack_err_to_other_attack_pct": 100 * (err - sub[:, n].sum()) / err if err else 0.0,
        **{f"f1::{c}": r["per_class"][c]["f1-score"] for c in r["classes"]},
    }


def stat(v):
    v = np.asarray(v, dtype=float)
    return {"mean": float(v.mean()), "min": float(v.min()), "max": float(v.max()), "std": float(v.std()), "n": len(v)}


def main() -> None:
    runs = collections.defaultdict(dict)
    for f in (ROOT / "results" / "splits").glob("*.json"):
        r = json.loads(f.read_text())
        runs[(r["dataset"], r["split"])][r["seed"]] = metrics(r)

    out, md = {}, ["# Bölme deneyleri — seed özeti", ""]
    for ds in sorted({k[0] for k in runs}):
        base = runs[(ds, "random")]
        out[ds] = {}
        md += [f"## {ds}", "", "| Ölçüt | " + " | ".join(SPLITS) + " |", "|---|" + "---:|" * len(SPLITS)]
        keys = list(next(iter(base.values())).keys())
        for s in SPLITS:
            seeds = runs[(ds, s)]
            out[ds][s] = {k: stat([m[k] for m in seeds.values()]) for k in keys}
            common = sorted(set(seeds) & set(base))
            out[ds][s]["macro_f1_drop_pts"] = stat([100 * (seeds[x]["macro_f1"] - base[x]["macro_f1"]) for x in common])
            out[ds][s]["seeds"] = sorted(seeds)
        for k in keys + ["macro_f1_drop_pts"]:
            fmt = "{:.4f}" if k in ("macro_f1", "accuracy") or k.startswith("f1::") else "{:.2f}"
            cells = [f"{fmt.format(out[ds][s][k]['mean'])} [{fmt.format(out[ds][s][k]['min'])}–"
                     f"{fmt.format(out[ds][s][k]['max'])}]" for s in SPLITS]
            md.append(f"| {k} | " + " | ".join(cells) + " |")
        md.append("")
    md.append("Değerler: ortalama [min–maks], seed'ler: " + ", ".join(map(str, out[ds]["random"]["seeds"])))
    (ROOT / "results" / "splits_summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    (ROOT / "results" / "splits_summary.md").write_text("\n".join(md) + "\n")
    print("yazıldı: results/splits_summary.json, results/splits_summary.md")


if __name__ == "__main__":
    main()
