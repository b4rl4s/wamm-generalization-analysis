"""Bölüm B ve C için modelleri eğitip diske kaydeder (aynı modeller iki bölümde de kullanılır).

Kullanım: python scripts/08_train_save.py <dataset> <split> [<seed>=42]
Çıktı: models/<dataset>_<split>_s<seed>/{model.json, featurizer.joblib, split.npz, result.json}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import joblib
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from experiment import run  # noqa: E402
from wamm_data import ROOT  # noqa: E402


def main() -> None:
    name, split = sys.argv[1], sys.argv[2]
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    out = ROOT / "models" / f"{name}_{split}_s{seed}"
    if (out / "model.json").exists():
        print(f"[train] atlandı (var): {out.name}", flush=True)
        return
    out.mkdir(parents=True, exist_ok=True)
    print(f"[train] {name} / {split} / seed {seed} ...", flush=True)
    res, m = run(name, split, seed, return_model=True)
    m["clf"].save_model(out / "model.json")
    joblib.dump(m["featurizer"], out / "featurizer.joblib")
    np.savez_compressed(out / "split.npz", train_idx=m["train_idx"], test_idx=m["test_idx"], pred=m["pred"])
    (out / "result.json").write_text(json.dumps(res, indent=2, ensure_ascii=False))
    print(f"[train] {out.name}: macroF1={res['macro_f1']:.4f} fit={res['time_fit_s']:.0f}s", flush=True)


if __name__ == "__main__":
    main()
