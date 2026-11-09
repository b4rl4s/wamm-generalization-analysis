"""Bölüm A, A5: bölme stratejilerinin karşılaştırılması.

Kullanım: python scripts/05_split_eval.py <dataset> <seed> <split> [<split> ...]
  split: random | h_raw | h_payload | skeleton_id | family_0.8 | family_0.9 | ...
Çıktı: results/splits/<dataset>_<split>_s<seed>.json (var olanlar atlanır)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from experiment import run  # noqa: E402
from wamm_data import ROOT  # noqa: E402


def main() -> None:
    name, seed, splits = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
    out_dir = ROOT / "results" / "splits"
    out_dir.mkdir(parents=True, exist_ok=True)
    for split in splits:
        out = out_dir / f"{name}_{split}_s{seed}.json"
        if out.exists():
            print(f"[split] atlandı (var): {out.name}", flush=True)
            continue
        print(f"[split] {name} / {split} / seed {seed} ...", flush=True)
        r = run(name, split, seed)
        out.write_text(json.dumps(r, indent=2, ensure_ascii=False))
        print(f"[split] {name}/{split}/s{seed}: acc={r['accuracy']:.4f} macroF1={r['macro_f1']:.4f} "
              f"fit={r['time_fit_s']:.0f}s", flush=True)


if __name__ == "__main__":
    main()
