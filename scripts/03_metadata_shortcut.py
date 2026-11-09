"""Kısayol kontrolü: payload içeriği olmadan yalnızca meta verilerle sınıflandırma.

Özellikler: method, Host, header sayısı, header adları kümesi, istek uzunluğu, body var/yok.
URI, parametreler, body içeriği ve header DEĞERLERİ (Host hariç) kullanılmaz.
Çıktı: results/metadata_shortcut_<dataset>.json
"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from http_parse import parse
from splits import random_stratified
from wamm_data import ROOT, load

name = sys.argv[1]
df = load(name)
p = df["request"].map(parse)
meta = pd.DataFrame({
    "method": p.map(lambda r: r.method),
    "host": p.map(lambda r: r.headers.get("host", "")),
    "header_names": p.map(lambda r: ",".join(sorted(r.headers))),
})
X = pd.DataFrame({
    "n_headers": p.map(lambda r: len(r.headers)),
    "length": df["request"].str.len(),
    "has_body": p.map(lambda r: int(bool(r.body))),
})
for c in meta:
    codes = meta[c].astype("category").cat.codes
    X[c] = codes
y = df["label"].astype(str)
tr, te = random_stratified(y)
res = {}
for feats in [["host"], ["n_headers"], ["length"], ["header_names"], list(X.columns)]:
    clf = DecisionTreeClassifier(max_depth=12, class_weight="balanced", random_state=0)
    clf.fit(X.iloc[tr][feats], y.iloc[tr])
    pr = clf.predict(X.iloc[te][feats])
    key = "+".join(feats) if len(feats) < len(X.columns) else "ALL_METADATA"
    res[key] = {"accuracy": round(accuracy_score(y.iloc[te], pr), 4), "macro_f1": round(f1_score(y.iloc[te], pr, average="macro"), 4)}
    if key == "ALL_METADATA":
        rep = classification_report(y.iloc[te], pr, output_dict=True, zero_division=0)
        res["ALL_METADATA_per_class_f1"] = {k: round(v["f1-score"], 3) for k, v in rep.items() if isinstance(v, dict) and k not in ("macro avg", "weighted avg")}
    print(key, res[key], flush=True)
(ROOT / "results" / f"metadata_shortcut_{name}.json").write_text(json.dumps(res, indent=2, ensure_ascii=False))
print(json.dumps(res.get("ALL_METADATA_per_class_f1"), indent=1, ensure_ascii=False))
