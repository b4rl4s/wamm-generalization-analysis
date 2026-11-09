"""Bölüm B/C: araç izi (oastify.com) karşı-olgusal testi — TÜM test kümesi, örneklem yok.

Kullanım: python scripts/13_artifact_full.py <model_dir_adı> [<model_dir_adı> ...]
Test kümesinde 'oastify' geçen tüm saldırı satırlarında yalnızca alan adı değiştirilir
(obfuscate.transform(..., "artifact")) ve tahmin önce/sonra karşılaştırılır.
Çıktı: results/artifact_full/<model>.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from features import handcrafted  # noqa: E402
from obfuscate import category, transform  # noqa: E402
from wamm_data import ROOT, load  # noqa: E402


def predict(clf, fz, requests: pd.Series) -> np.ndarray:
    requests = requests.reset_index(drop=True)
    return clf.predict(fz.transform(requests, handcrafted(requests)))


def run(model_name: str) -> dict:
    mdir = ROOT / "models" / model_name
    res = json.loads((mdir / "result.json").read_text())
    ds, classes = res["dataset"], res["classes"]
    clf = xgb.XGBClassifier()
    clf.load_model(mdir / "model.json")
    fz = joblib.load(mdir / "featurizer.joblib")  # yalnızca 08_train_save.py'nin yerelde ürettiği dosya
    te = np.load(mdir / "split.npz")["test_idx"]
    df = load(ds)
    lab = df["label"].astype(str).values
    normal = next(i for i, c in enumerate(classes) if category(c) == "normal")
    cidx = {c: i for i, c in enumerate(classes)}

    req_all = df["request"].iloc[te]
    has = req_all.str.contains("oastify", case=False, regex=False).values
    rows = te[has & (lab[te] != classes[normal])]
    req = df["request"].iloc[rows].reset_index(drop=True)
    new = pd.Series([transform(r, "artifact", lab[rows[k]]) for k, r in enumerate(req)])
    changed = (new != req).values
    y = np.array([cidx[l] for l in lab[rows]])
    p0 = predict(clf, fz, req)
    p1 = p0.copy()
    if changed.any():
        p1[changed] = predict(clf, fz, new[changed])
    out = {"model": model_name, "dataset": ds, "split": res["split"], "seed": res["seed"],
           "n_test": int(len(te)), "n_test_with_oastify": int(has.sum()),
           "n_normal_test_with_oastify": int((has & (lab[te] == classes[normal])).sum()),
           "per_class": {}}
    for c in classes:
        m = (y == cidx[c]) & changed
        if m.sum() == 0:
            continue
        out["per_class"][c] = {
            "n_class_test": int((lab[te] == c).sum()), "n_changed": int(m.sum()),
            "recall_before": float((p0[m] == y[m]).mean()), "recall_after": float((p1[m] == y[m]).mean()),
            "to_normal_after": float((p1[m] == normal).mean()),
            "pred_after": pd.Series([classes[p] for p in p1[m]]).value_counts().to_dict(),
        }
    return out


def main() -> None:
    od = ROOT / "results" / "artifact_full"
    od.mkdir(parents=True, exist_ok=True)
    for m in sys.argv[1:]:
        r = run(m)
        (od / f"{m}.json").write_text(json.dumps(r, indent=2, ensure_ascii=False))
        print(f"[artifact] {m}: oastify içeren test satırı={r['n_test_with_oastify']}", flush=True)
        for c, v in r["per_class"].items():
            print(f"   {c:28s} n={v['n_changed']:5d} recall {v['recall_before']:.3f} -> {v['recall_after']:.3f}", flush=True)


if __name__ == "__main__":
    main()
