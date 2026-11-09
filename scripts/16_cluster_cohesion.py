"""Yakın-kopya kümelerinin iç tutarlılığı: zincirleme bağlantının etkisi.

Kullanım: python scripts/16_cluster_cohesion.py <dataset> [<eşik>=0.8] [<küme sayısı>=300]
En az 3 üyeli kümelerden rastgele örneklem alınır (seed 0); her kümeden en fazla 25 üye seçilir ve
üyeler arasındaki TÜM çiftler için gerçek Jaccard benzerliği (5 karakterlik shingle kümeleri üzerinde,
MinHash tahmini değil) hesaplanır.
Çıktı: results/cluster_cohesion_<dataset>_<eşik>.json
"""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from families import shingles  # noqa: E402
from wamm_data import CACHE, ROOT, load  # noqa: E402

def jac(a, b):
    return len(a & b) / len(a | b) if (a or b) else 1.0

def main():
    name = sys.argv[1]; thr = sys.argv[2] if len(sys.argv) > 2 else "0.8"; k = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    sk = pd.read_parquet(CACHE / f"{name}_skeleton.parquet")["sk"].values
    fam = pd.read_parquet(CACHE / f"{name}_families.parquet")[f"family_{thr}"].astype(str).values
    lab = load(name)["label"].astype(str).values
    key = pd.Series(fam + "|" + lab)
    sizes = key.value_counts(); cand = sizes[sizes >= 3].index.values
    rng = np.random.default_rng(0)
    pick = rng.choice(cand, min(k, len(cand)), replace=False)
    groups = key.groupby(key).indices
    per = []
    allpairs = []
    for c in pick:
        idx = groups[c]; idx = rng.choice(idx, min(25, len(idx)), replace=False)
        S = [shingles(sk[i], 5) for i in idx]
        sims = [jac(S[a], S[b]) for a, b in itertools.combinations(range(len(S)), 2)]
        allpairs += sims
        per.append(dict(size=int(sizes[c]), min=float(min(sims)), mean=float(np.mean(sims)),
                        below=float(np.mean(np.array(sims) < float(thr)))))
    p = pd.DataFrame(per); a = np.array(allpairs)
    out = {"dataset": name, "threshold": float(thr), "n_clusters": len(p), "n_pairs": int(len(a)),
           "pair_jaccard_mean": float(a.mean()), "pair_jaccard_median": float(np.median(a)),
           "pairs_below_threshold": float((a < float(thr)).mean()), "pairs_below_0.5": float((a < 0.5).mean()),
           "cluster_min_jaccard_median": float(p["min"].median()),
           "clusters_with_any_pair_below_threshold": float((p["min"] < float(thr)).mean()),
           "clusters_min_below_0.5": float((p["min"] < 0.5).mean()),
           "by_size": p.assign(sz=pd.cut(p["size"], [2, 5, 20, 100, 10**9], labels=["3-5", "6-20", "21-100", ">100"]))
                       .groupby("sz", observed=True).agg(n=("min", "size"), min_med=("min", "median"),
                                                          mean_med=("mean", "median"), below=("below", "mean")).round(3).reset_index().to_dict("records")}
    (ROOT / "results" / f"cluster_cohesion_{name}_{thr}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(json.dumps({k: v for k, v in out.items() if k != "by_size"}, indent=1)); print(pd.DataFrame(out["by_size"]).to_string(index=False))

if __name__ == "__main__":
    main()
