"""Bölüm B: kaydedilmiş modellerin anlamı koruyan gizleme dönüşümlerine dayanıklılığı.

Kullanım: python scripts/09_obfuscation.py <model_dir_adı> [<sınıf başına örnek>=2000]
  örn. ds_aug_v2_random_s42
Yalnızca TEST kümesindeki saldırı satırları dönüştürülür; eğitim verisine dokunulmaz.
Her dönüşüm için yalnızca dönüşümün gerçekten değiştirdiği satırlar değerlendirilir.

Çıktı: results/obfuscation/<model>.json, results/obfuscation/examples_<model>.md
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from features import handcrafted  # noqa: E402
from obfuscate import TRANSFORMS, applicable, category, transform  # noqa: E402
from wamm_data import ROOT, load  # noqa: E402


def predict(clf, fz, requests: pd.Series) -> np.ndarray:
    requests = requests.reset_index(drop=True)
    return clf.predict(fz.transform(requests, handcrafted(requests)))


def main() -> None:
    model_name = sys.argv[1]
    per_class = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
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

    # Test kümesindeki saldırı satırlarından sınıf başına örneklem (sabit seed)
    rng = np.random.default_rng(0)
    sample = []
    for c in classes:
        if category(c) == "normal":
            continue
        rows = te[lab[te] == c]
        sample.extend(rng.choice(rows, min(per_class, len(rows)), replace=False).tolist())
    sample = np.array(sorted(sample))
    req = df["request"].iloc[sample].reset_index(drop=True)
    y = np.array([cidx[l] for l in lab[sample]])
    t0 = time.time()
    p0 = predict(clf, fz, req)
    print(f"[obf] {model_name}: {len(sample)} saldırı satırı, temel tahmin {time.time() - t0:.0f}s", flush=True)

    out = {"model": model_name, "dataset": ds, "split": res["split"], "n_sampled": int(len(sample)),
           "per_class_cap": per_class, "transforms": {}, "assumptions": {k: v["assumption"] for k, v in TRANSFORMS.items()}}
    examples = [f"# Gizleme örnekleri — {model_name}", "",
                "Her dönüşüm ve sınıf için en fazla 2 örnek (yalnızca değişen kısım çevresi).", ""]
    for t in TRANSFORMS:
        t0 = time.time()
        new = pd.Series([transform(r, t, lab[sample[k]], seed=int(sample[k])) for k, r in enumerate(req)])
        changed = (new != req).values
        if changed.sum() == 0:
            out["transforms"][t] = {"n_changed": 0}
            continue
        p1 = np.full(len(req), -1)
        p1[changed] = predict(clf, fz, new[changed])
        per_cls = {}
        for c in classes:
            if category(c) == "normal" or not applicable(t, c):
                continue
            m = (y == cidx[c])
            ch = m & changed
            n_ch = int(ch.sum())
            if n_ch == 0:
                per_cls[c] = {"n": int(m.sum()), "n_changed": 0}
                continue
            ok0 = ch & (p0 == y)
            per_cls[c] = {
                "n": int(m.sum()), "n_changed": n_ch,
                "recall_before": float((p0[ch] == y[ch]).mean()),
                "recall_after": float((p1[ch] == y[ch]).mean()),
                "detect_before": float((p0[ch] != normal).mean()),
                "detect_after": float((p1[ch] != normal).mean()),
                # önce doğru sınıflanıp sonra Normal'e kaçan / başka saldırı sınıfına kayan
                "evasion_rate": float(((p1 == normal) & ok0).sum() / max(ok0.sum(), 1)),
                "class_flip_rate": float(((p1 != normal) & (p1 != y) & ok0).sum() / max(ok0.sum(), 1)),
            }
        ch = changed
        ok0 = ch & (p0 == y)
        out["transforms"][t] = {
            "n_changed": int(ch.sum()),
            "recall_before": float((p0[ch] == y[ch]).mean()), "recall_after": float((p1[ch] == y[ch]).mean()),
            "detect_before": float((p0[ch] != normal).mean()), "detect_after": float((p1[ch] != normal).mean()),
            "evasion_rate": float(((p1 == normal) & ok0).sum() / max(ok0.sum(), 1)),
            "class_flip_rate": float(((p1 != normal) & (p1 != y) & ok0).sum() / max(ok0.sum(), 1)),
            "per_class": per_cls, "time_s": round(time.time() - t0, 1),
        }
        o = out["transforms"][t]
        print(f"[obf] {t:14s} n={o['n_changed']:6d} recall {o['recall_before']:.3f}->{o['recall_after']:.3f} "
              f"detect {o['detect_before']:.3f}->{o['detect_after']:.3f} evasion={o['evasion_rate']:.3f} "
              f"({o['time_s']:.0f}s)", flush=True)
        # Elle kontrol için örnekler
        examples += [f"## {t}", "", f"Varsayım: {TRANSFORMS[t]['assumption']}", ""]
        for c in classes:
            ks = np.flatnonzero(changed & (y == cidx.get(c, -1)))[:2]
            for k in ks:
                a, b = req[k], new[k]
                i = next((j for j in range(min(len(a), len(b))) if a[j] != b[j]), 0)
                ja, jb = len(a), len(b)
                while ja > i and jb > i and a[ja - 1] == b[jb - 1]:
                    ja, jb = ja - 1, jb - 1
                ctx = 50
                examples += [f"- **{c}** (tahmin: {classes[p0[k]]} → {classes[p1[k]]})",
                             f"  - önce: `{a[max(0, i - ctx):ja + ctx].replace(chr(10), ' ').replace(chr(13), '')[:400]}`",
                             f"  - sonra: `{b[max(0, i - ctx):jb + ctx].replace(chr(10), ' ').replace(chr(13), '')[:400]}`"]
        examples.append("")

    od = ROOT / "results" / "obfuscation"
    od.mkdir(parents=True, exist_ok=True)
    (od / f"{model_name}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    (od / f"examples_{model_name}.md").write_text("\n".join(examples) + "\n")
    print(f"[obf] yazıldı: results/obfuscation/{model_name}.json", flush=True)


if __name__ == "__main__":
    main()
