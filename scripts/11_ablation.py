"""Bölüm C, C3: özellik ablasyonu — yalnızca elle tasarlanmış / yalnızca TF-IDF (tam set = 05_split_eval).

Kullanım: python scripts/11_ablation.py <dataset> <split> <hand|tfidf> [<seed>=42]
Çıktı: results/ablation/<dataset>_<split>_<featureset>_s<seed>.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import xgboost as xgb
from scipy import sparse
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.utils.class_weight import compute_sample_weight

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from experiment import XGB_PARAMS, group_keys, hand_features, make_split  # noqa: E402
from features import WammFeaturizer  # noqa: E402
from wamm_data import ROOT, load  # noqa: E402


def main() -> None:
    name, split, fset = sys.argv[1], sys.argv[2], sys.argv[3]
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 42
    od = ROOT / "results" / "ablation"
    od.mkdir(parents=True, exist_ok=True)
    out = od / f"{name}_{split}_{fset}_s{seed}.json"
    if out.exists():
        print(f"[abl] atlandı (var): {out.name}", flush=True)
        return
    df = load(name)
    hand = hand_features(name, df)
    y_str = df["label"].astype(str)
    classes = sorted(y_str.unique())
    y = y_str.map({c: i for i, c in enumerate(classes)}).values
    tr, te = make_split(split, y_str, group_keys(name), seed)
    if fset == "hand":
        X_tr, X_te = sparse.csr_matrix(hand.values[tr]), sparse.csr_matrix(hand.values[te])
    elif fset == "tfidf":
        tf = WammFeaturizer().tfidf
        X_tr = tf.fit_transform(df["request"].iloc[tr].astype(str))
        X_te = tf.transform(df["request"].iloc[te].astype(str))
    else:
        raise SystemExit("featureset: hand | tfidf")
    print(f"[abl] {name}/{split}/{fset}: X_tr={X_tr.shape}", flush=True)
    clf = xgb.XGBClassifier(objective="multi:softprob", num_class=len(classes), random_state=seed, **XGB_PARAMS)
    t0 = time.time()
    clf.fit(X_tr, y[tr], sample_weight=compute_sample_weight("balanced", y[tr]))
    pred = clf.predict(X_te)
    rep = classification_report(y[te], pred, labels=range(len(classes)), target_names=classes,
                                output_dict=True, zero_division=0)
    r = {"dataset": name, "split": split, "featureset": fset, "seed": seed,
         "accuracy": round(accuracy_score(y[te], pred), 4), "macro_f1": round(f1_score(y[te], pred, average="macro"), 4),
         "per_class_f1": {c: round(rep[c]["f1-score"], 4) for c in classes}, "time_fit_s": round(time.time() - t0, 1)}
    out.write_text(json.dumps(r, indent=2, ensure_ascii=False))
    print(f"[abl] {name}/{split}/{fset}: acc={r['accuracy']:.4f} macroF1={r['macro_f1']:.4f} fit={r['time_fit_s']:.0f}s",
          flush=True)


if __name__ == "__main__":
    main()
