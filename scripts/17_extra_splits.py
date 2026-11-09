"""Ek bölme deneyleri: Deney C (çelişkili etiketler) ve Deney A (host bazlı bölme).

Kullanım: python scripts/17_extra_splits.py <dataset> <variant> <seed>
  variant:
    fam08_nolabel    — grup anahtarı = yakın-kopya kümesi (0.8), etiketten BAĞIMSIZ (Deney C-c)
    fam08_dropconf   — birden fazla etiketle görülen ham istekler veriden çıkarılır; anahtar (küme, etiket) (Deney C-b)
    random_dropconf  — aynı satırlar çıkarılır; rastgele stratified bölme (Deney C-b referansı)
    host             — saldırılar için anahtar (Host header, etiket); Normal için (küme 0.8, etiket) (Deney A)
Çıktı: results/extra_splits/<dataset>_<variant>_s<seed>.json
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
from experiment import XGB_PARAMS, hand_features  # noqa: E402
from features import WammFeaturizer  # noqa: E402
from http_parse import parse  # noqa: E402
from splits import group_stratified, random_stratified  # noqa: E402
from wamm_data import CACHE, ROOT, load  # noqa: E402


def host_of(raw: str) -> str:
    return parse(raw).headers.get("host", "").lower().split(":")[0]


def main() -> None:
    name, variant, seed = sys.argv[1], sys.argv[2], int(sys.argv[3])
    od = ROOT / "results" / "extra_splits"
    od.mkdir(parents=True, exist_ok=True)
    out = od / f"{name}_{variant}_s{seed}.json"
    if out.exists():
        print(f"[extra] atlandı (var): {out.name}", flush=True)
        return
    df = load(name)
    hand = hand_features(name, df)
    lab = df["label"].astype(str).values
    h = pd.read_parquet(CACHE / f"{name}_hashes.parquet")["h_raw"].values
    fam = pd.read_parquet(CACHE / f"{name}_families.parquet")["family_0.8"].astype(str).values
    n_labels = pd.Series(lab).groupby(h).nunique()
    conflict = np.isin(h, n_labels[n_labels > 1].index.values)

    keep = np.ones(len(df), bool)
    if variant in ("fam08_dropconf", "random_dropconf"):
        keep = ~conflict
    rows = np.flatnonzero(keep)
    y_str = pd.Series(lab[rows])

    if variant == "fam08_nolabel":
        keys = pd.Series(fam[rows])
    elif variant == "fam08_dropconf":
        keys = pd.Series(fam[rows] + "|" + lab[rows])
    elif variant == "host":
        cache = CACHE / f"{name}_host.parquet"
        if cache.exists():
            hosts = pd.read_parquet(cache)["host"].values
        else:
            hosts = df["request"].map(host_of).values
            pd.DataFrame({"host": hosts}).to_parquet(cache)
        normal = np.array(["normal" in l.lower() for l in lab])
        k = np.where(normal, "F" + fam, "H" + hosts)
        keys = pd.Series(k[rows] + "|" + lab[rows])
    if variant == "random_dropconf":
        tr_l, te_l = random_stratified(y_str, seed=seed)
    else:
        tr_l, te_l = group_stratified(y_str, keys, seed=seed)
    tr, te = rows[tr_l], rows[te_l]

    classes = sorted(set(lab))
    cidx = {c: i for i, c in enumerate(classes)}
    y = np.array([cidx[l] for l in lab])
    t0 = time.time()
    fz = WammFeaturizer()
    X_tr = fz.fit_transform(df["request"].iloc[tr], hand.iloc[tr])
    X_te = fz.transform(df["request"].iloc[te], hand.iloc[te])
    clf = xgb.XGBClassifier(objective="multi:softprob", num_class=len(classes), random_state=seed, **XGB_PARAMS)
    clf.fit(X_tr, y[tr], sample_weight=compute_sample_weight("balanced", y[tr]))
    pred = clf.predict(X_te)
    rep = classification_report(y[te], pred, labels=range(len(classes)), target_names=classes,
                                output_dict=True, zero_division=0)
    train_h = set(h[tr])
    res = {
        "dataset": name, "variant": variant, "seed": seed, "n_rows_used": int(len(rows)),
        "n_removed_conflict_rows": int((~keep).sum()), "n_train": int(len(tr)), "n_test": int(len(te)),
        "test_fraction_per_class": {c: round(float((lab[te] == c).sum() / max((lab[rows] == c).sum(), 1)), 3)
                                    for c in classes},
        "test_rows_with_h_raw_in_train": round(float(np.mean([x in train_h for x in h[te]])), 5),
        "accuracy": round(accuracy_score(y[te], pred), 4),
        "macro_f1": round(f1_score(y[te], pred, average="macro"), 4),
        "per_class": {c: {k: round(v, 4) for k, v in rep[c].items()} for c in classes},
        "confusion_matrix": confusion_matrix(y[te], pred, labels=range(len(classes))).tolist(),
        "classes": classes, "time_s": round(time.time() - t0, 1),
    }
    out.write_text(json.dumps(res, indent=2, ensure_ascii=False))
    print(f"[extra] {name}/{variant}/s{seed}: macroF1={res['macro_f1']:.4f} acc={res['accuracy']:.4f} "
          f"kalan_birebir={res['test_rows_with_h_raw_in_train']:.4%} ({res['time_s']:.0f}s)", flush=True)


if __name__ == "__main__":
    main()
