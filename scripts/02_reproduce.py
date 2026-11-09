"""Adım 0: WAMM XGBoost sonuçlarının yeniden üretimi + birebir-tekrar duyarlı bölme.

Kullanım: python scripts/02_reproduce.py <dataset> [split ...]
  split: random (WAMM ile aynı, 80/20 stratified) | exact (ham istek hash'ine göre grup bölmesi)
Çıktı: results/repro_<dataset>_<split>.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.utils.class_weight import compute_sample_weight

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from features import ASSUMPTIONS, WammFeaturizer, handcrafted  # noqa: E402
from splits import group_stratified, overlap_rate, random_stratified  # noqa: E402
from wamm_data import CACHE, ROOT, load  # noqa: E402

SEED = 42
XGB_PARAMS = dict(n_estimators=300, max_depth=8, learning_rate=0.1, tree_method="hist",
                  subsample=1.0, colsample_bytree=1.0, n_jobs=16, random_state=SEED)


def hand_features(name: str, df: pd.DataFrame) -> pd.DataFrame:
    p = CACHE / f"{name}_hand.parquet"
    if p.exists():
        return pd.read_parquet(p)
    t = time.time()
    h = handcrafted(df["request"])
    h.to_parquet(p)
    print(f"  elle tasarlanmış özellikler: {time.time() - t:.0f} sn", flush=True)
    return h


def run(name: str, split: str) -> dict:
    df = load(name)
    hashes = pd.read_parquet(CACHE / f"{name}_hashes.parquet")
    hand = hand_features(name, df)
    y_str = df["label"].astype(str)
    classes = sorted(y_str.unique())
    y = y_str.map({c: i for i, c in enumerate(classes)}).values

    if split == "random":
        tr, te = random_stratified(y_str, seed=SEED)
    elif split == "exact":
        tr, te = group_stratified(y_str, hashes["h_raw"], seed=SEED)
    else:
        raise ValueError(split)

    t0 = time.time()
    fz = WammFeaturizer()
    X_tr = fz.fit_transform(df["request"].iloc[tr], hand.iloc[tr])
    X_te = fz.transform(df["request"].iloc[te], hand.iloc[te])
    t_feat = time.time() - t0

    w = compute_sample_weight("balanced", y[tr])
    clf = xgb.XGBClassifier(objective="multi:softprob", num_class=len(classes), **XGB_PARAMS)
    t0 = time.time()
    clf.fit(X_tr, y[tr], sample_weight=w)
    t_fit = time.time() - t0
    pred = clf.predict(X_te)

    rep = classification_report(y[te], pred, labels=range(len(classes)), target_names=classes,
                                output_dict=True, zero_division=0)
    res = {
        "dataset": name,
        "split": split,
        "n_train": int(len(tr)),
        "n_test": int(len(te)),
        "test_rows_with_exact_raw_copy_in_train": round(overlap_rate(hashes["h_raw"], tr, te), 4),
        "test_rows_with_exact_payload_copy_in_train": round(overlap_rate(hashes["h_payload"], tr, te), 4),
        "accuracy": round(accuracy_score(y[te], pred), 4),
        "macro_f1": round(f1_score(y[te], pred, average="macro"), 4),
        "weighted_f1": round(f1_score(y[te], pred, average="weighted"), 4),
        "per_class": {c: {k: round(v, 4) for k, v in rep[c].items()} for c in classes},
        "confusion_matrix": confusion_matrix(y[te], pred, labels=range(len(classes))).tolist(),
        "classes": classes,
        "time_features_s": round(t_feat, 1),
        "time_fit_s": round(t_fit, 1),
        "xgb_params": XGB_PARAMS,
        "assumptions": ASSUMPTIONS,
    }
    return res


def main() -> None:
    name = sys.argv[1]
    splits = sys.argv[2:] or ["random", "exact"]
    for split in splits:
        print(f"[repro] {name} / {split} ...", flush=True)
        r = run(name, split)
        out = ROOT / "results" / f"repro_{name}_{split}.json"
        out.write_text(json.dumps(r, indent=2, ensure_ascii=False))
        print(f"[repro] {name}/{split}: acc={r['accuracy']:.4f} macroF1={r['macro_f1']:.4f} "
              f"train-kopyası olan test oranı (ham)={r['test_rows_with_exact_raw_copy_in_train']:.3f} "
              f"fit={r['time_fit_s']:.0f}s", flush=True)


if __name__ == "__main__":
    main()
