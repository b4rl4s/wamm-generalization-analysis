"""Bölüm C: SHAP ile açıklama (XGBoost yerleşik TreeSHAP, pred_contribs=True).

Kullanım: python scripts/10_shap.py <model_dir_adı> [<sınıf başına örnek>=200]

C1 (global): test kümesinden sınıf başına örneklem; her sınıfın kendi satırlarında, o sınıfın çıktısına
   en çok katkı veren özellikler ve özellik gruplarının |SHAP| payı.
C2 (yerel): gizleme sonrası doğru → yanlış tahmine dönen saldırı satırlarında, gerçek sınıf çıktısı için
   SHAP(sonra) − SHAP(önce): hangi özelliklerin desteği kayboldu?

Çıktı: results/shap/<model>.json
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from features import handcrafted  # noqa: E402
from obfuscate import TRANSFORMS, category, transform  # noqa: E402
from wamm_data import ROOT, load  # noqa: E402

LOCAL_N = 300
LENGTH_STATS = {"len", "len_decoded", "uri_len", "unique_chars", "entropy", "cnt_digit", "cnt_pct_encoded",
                "url_depth", "n_params"}


def feature_group(name: str) -> str:
    if name.startswith("tfidf["):
        return "tfidf_char_ngram"
    if name in LENGTH_STATS:
        return "length_stats"
    if name.startswith("sig_") or name in ("sql_kw_count", "has_sql_kw", "has_traversal"):
        return "signatures_keywords"
    if name.startswith("cnt_"):
        return "special_char_counts"
    return "other"


def contribs(booster, X) -> np.ndarray:
    """(n, K, F) SHAP katkıları (bias sütunu atılır)."""
    c = booster.predict(xgb.DMatrix(X), pred_contribs=True)
    return c[..., :-1]


def featurize(fz, requests: pd.Series):
    requests = requests.reset_index(drop=True)
    return fz.transform(requests, handcrafted(requests))


def main() -> None:
    model_name = sys.argv[1]
    per_class = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    mdir = ROOT / "models" / model_name
    res = json.loads((mdir / "result.json").read_text())
    ds, classes = res["dataset"], res["classes"]
    clf = xgb.XGBClassifier()
    clf.load_model(mdir / "model.json")
    booster = clf.get_booster()
    booster.set_param({"nthread": 16})
    fz = joblib.load(mdir / "featurizer.joblib")  # yalnızca 08_train_save.py'nin yerelde ürettiği dosya
    names = fz.feature_names()
    groups = np.array([feature_group(n) for n in names])
    gnames = sorted(set(groups))
    te = np.load(mdir / "split.npz")["test_idx"]
    df = load(ds)
    lab = df["label"].astype(str).values
    cidx = {c: i for i, c in enumerate(classes)}
    normal = next(i for i, c in enumerate(classes) if category(c) == "normal")

    # ---------------- C1: global
    rng = np.random.default_rng(0)
    sample = np.array(sorted(sum((rng.choice(te[lab[te] == c], min(per_class, int((lab[te] == c).sum())),
                                             replace=False).tolist() for c in classes), [])))
    t0 = time.time()
    X = featurize(fz, df["request"].iloc[sample])
    C = contribs(booster, X)
    y = np.array([cidx[l] for l in lab[sample]])
    pred = clf.predict(X)
    print(f"[shap] {model_name}: global {len(sample)} satır, {time.time() - t0:.0f}s", flush=True)

    out = {"model": model_name, "dataset": ds, "split": res["split"], "n_global": int(len(sample)),
           "global": {}, "group_share_all": {}, "local": {}}
    tot_by_group = {g: 0.0 for g in gnames}
    for c in classes:
        k = cidx[c]
        rows = y == k
        a = np.abs(C[rows, k, :])
        mean_abs = a.mean(0)
        signed = C[rows, k, :].mean(0)
        top = np.argsort(-mean_abs)[:20]
        share = {g: float(mean_abs[groups == g].sum() / max(mean_abs.sum(), 1e-12)) for g in gnames}
        for g in gnames:
            tot_by_group[g] += share[g] / len(classes)
        out["global"][c] = {
            "n": int(rows.sum()), "acc_on_sample": float((pred[rows] == k).mean()),
            "group_share": share,
            "top_features": [{"feature": names[j], "group": groups[j], "mean_abs": float(mean_abs[j]),
                              "mean_signed": float(signed[j])} for j in top],
        }
    out["group_share_all"] = tot_by_group
    # Özellik bazında genel sıralama (tüm sınıfların kendi çıktısı)
    overall = np.zeros(len(names))
    for c in classes:
        k = cidx[c]
        overall += np.abs(C[y == k, k, :]).mean(0) / len(classes)
    out["top_overall"] = [{"feature": names[j], "group": groups[j], "mean_abs": float(overall[j])}
                          for j in np.argsort(-overall)[:30]]

    # ---------------- C2: yerel — gizleme sonrası kaybolan destek
    rng = np.random.default_rng(1)
    att = np.array(sorted(sum((rng.choice(te[lab[te] == c], min(LOCAL_N, int((lab[te] == c).sum())), replace=False).tolist()
                               for c in classes if category(c) != "normal"), [])))
    req = df["request"].iloc[att].reset_index(drop=True)
    ya = np.array([cidx[l] for l in lab[att]])
    X0 = featurize(fz, req)
    p0 = clf.predict(X0)
    for t in TRANSFORMS:
        new = pd.Series([transform(r, t, lab[att[k]], seed=int(att[k])) for k, r in enumerate(req)])
        ch = np.flatnonzero((new != req).values & (p0 == ya))
        if len(ch) == 0:
            continue
        X1 = featurize(fz, new.iloc[ch])
        p1 = clf.predict(X1)
        flipped = ch[p1 != ya[ch]]
        entry = {"n_changed_correct_before": int(len(ch)), "n_flipped": int(len(flipped)),
                 "flipped_to_normal": int(((p1 != ya[ch]) & (p1 == normal)).sum())}
        if len(flipped):
            sel = flipped[:300]
            X1f = featurize(fz, new.iloc[sel])
            c0 = contribs(booster, X0[sel])
            c1 = contribs(booster, X1f)
            d = np.stack([c1[i, ya[s], :] - c0[i, ya[s], :] for i, s in enumerate(sel)])
            md = d.mean(0)
            lost = np.argsort(md)[:15]
            gained_other = {g: float(md[groups == g].sum()) for g in gnames}
            entry.update({
                "n_explained": int(len(sel)),
                "true_class_logit_delta_by_group": gained_other,
                "top_lost_support": [{"feature": names[j], "group": groups[j], "mean_delta": float(md[j])} for j in lost],
                "flipped_by_class": pd.Series([classes[ya[s]] for s in flipped]).value_counts().to_dict(),
            })
        out["local"][t] = entry
        print(f"[shap] local {t:14s} değişen&doğru={len(ch):5d} dönen={len(flipped):5d}", flush=True)

    od = ROOT / "results" / "shap"
    od.mkdir(parents=True, exist_ok=True)
    (od / f"{model_name}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"[shap] yazıldı: results/shap/{model_name}.json", flush=True)


if __name__ == "__main__":
    main()
