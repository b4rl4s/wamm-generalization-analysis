"""Ortak deney hattı: bölme → özellik çıkarımı (yalnızca eğitimde fit) → XGBoost → metrikler."""
from __future__ import annotations

import time

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.utils.class_weight import compute_sample_weight

from features import ASSUMPTIONS, WammFeaturizer, handcrafted
from splits import group_stratified, overlap_rate, random_stratified
from wamm_data import CACHE, load

XGB_PARAMS = dict(n_estimators=300, max_depth=8, learning_rate=0.1, tree_method="hist",
                  subsample=1.0, colsample_bytree=1.0, n_jobs=16)


def hand_features(name: str, df: pd.DataFrame) -> pd.DataFrame:
    p = CACHE / f"{name}_hand.parquet"
    if p.exists():
        return pd.read_parquet(p)
    h = handcrafted(df["request"])
    h.to_parquet(p)
    return h


def group_keys(name: str) -> pd.DataFrame:
    """Bölmede kullanılabilecek grup anahtarları (satır sırası veriyle aynı)."""
    keys = pd.read_parquet(CACHE / f"{name}_hashes.parquet")[["h_raw", "h_payload"]]
    fam_path = CACHE / f"{name}_families.parquet"
    if fam_path.exists():
        fam = pd.read_parquet(fam_path)
        # Aileler sınıf içi tanımlanır: (aile, etiket). Bir aile farklı sınıfların satırlarını içerebilir
        # (ör. normal istek ve aynı isteğin Cookie'sine enjekte edilmiş saldırı); sınıflar arası paylaşım
        # sızıntı sayılmaz, sınıf içi benzer payload'lar ise aynı tarafta tutulur.
        lab = load(name)["label"].astype(str).values
        fam = fam.apply(lambda col: col.astype(str) + "|" + lab)
        keys = pd.concat([keys, fam], axis=1)
    return keys


def make_split(split: str, y_str: pd.Series, keys: pd.DataFrame, seed: int):
    """split: 'random' ya da group_keys() sütun adlarından biri (örn. 'h_raw', 'family_0.8')."""
    if split == "random":
        return random_stratified(y_str, seed=seed)
    return group_stratified(y_str, keys[split], seed=seed)


def run(name: str, split: str, seed: int = 42, return_model: bool = False):
    df = load(name)
    keys = group_keys(name)
    hand = hand_features(name, df)
    y_str = df["label"].astype(str)
    classes = sorted(y_str.unique())
    y = y_str.map({c: i for i, c in enumerate(classes)}).values
    tr, te = make_split(split, y_str, keys, seed)

    t0 = time.time()
    fz = WammFeaturizer()
    X_tr = fz.fit_transform(df["request"].iloc[tr], hand.iloc[tr])
    X_te = fz.transform(df["request"].iloc[te], hand.iloc[te])
    t_feat = time.time() - t0

    clf = xgb.XGBClassifier(objective="multi:softprob", num_class=len(classes), random_state=seed, **XGB_PARAMS)
    t0 = time.time()
    clf.fit(X_tr, y[tr], sample_weight=compute_sample_weight("balanced", y[tr]))
    t_fit = time.time() - t0
    pred = clf.predict(X_te)

    rep = classification_report(y[te], pred, labels=range(len(classes)), target_names=classes,
                                output_dict=True, zero_division=0)
    overlaps = {f"test_rows_with_{k}_in_train": round(overlap_rate(keys[k], tr, te), 4) for k in keys.columns
                if k in ("h_raw", "h_payload", "skeleton_id", "family_0.8")}
    train_frac = pd.Series(y[te]).value_counts() / pd.Series(y).value_counts()
    res = {
        "dataset": name, "split": split, "seed": seed,
        "n_train": int(len(tr)), "n_test": int(len(te)),
        "test_fraction_per_class": {classes[i]: round(float(v), 3) for i, v in train_frac.sort_index().items()},
        **overlaps,
        "accuracy": round(accuracy_score(y[te], pred), 4),
        "macro_f1": round(f1_score(y[te], pred, average="macro"), 4),
        "weighted_f1": round(f1_score(y[te], pred, average="weighted"), 4),
        "per_class": {c: {k: round(v, 4) for k, v in rep[c].items()} for c in classes},
        "confusion_matrix": confusion_matrix(y[te], pred, labels=range(len(classes))).tolist(),
        "classes": classes,
        "time_features_s": round(t_feat, 1), "time_fit_s": round(t_fit, 1),
        "xgb_params": XGB_PARAMS, "assumptions": ASSUMPTIONS,
    }
    if return_model:
        return res, dict(clf=clf, featurizer=fz, train_idx=tr, test_idx=te, X_te=X_te, y=y, pred=pred)
    return res
