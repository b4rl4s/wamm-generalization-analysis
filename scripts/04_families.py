"""Bölüm A, Adım A1–A4: payload ailesi (yakın kopya) gruplama ve eşik analizi.

Kullanım: python scripts/04_families.py <dataset>
Çıktılar:
  data/cache/<dataset>_families.parquet  — satır başına: skeleton id + her eşik için aile id
  results/families_<dataset>.md / .json   — eşik bazında aile istatistikleri ve rastgele bölmedeki aile sızıntısı
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from families import lsh_families, minhash_signatures, skeleton  # noqa: E402
from http_parse import parse  # noqa: E402
from splits import overlap_rate, random_stratified  # noqa: E402
from wamm_data import CACHE, ROOT, load  # noqa: E402

THRESHOLDS = [0.5, 0.6, 0.7, 0.8, 0.9]
SEED = 42


def main(name: str) -> None:
    df = load(name)
    y = df["label"].astype(str)
    t = time.time()
    surf = df["request"].map(lambda r: parse(r).attack_surface())
    sk = surf.map(skeleton)
    sk_codes, sk_uniques = pd.factorize(sk)
    print(f"[fam] {name}: {len(df):,} satır, {len(sk_uniques):,} benzersiz iskelet ({time.time() - t:.0f}s)", flush=True)

    t = time.time()
    sig = minhash_signatures(list(sk_uniques))
    print(f"[fam] MinHash: {time.time() - t:.0f}s", flush=True)

    out = pd.DataFrame({"skeleton_id": sk_codes})
    tr, te = random_stratified(y, seed=SEED)
    report = {"dataset": name, "rows": len(df), "unique_skeletons": int(len(sk_uniques)),
              "random_split_test_rows_with_same_skeleton_in_train": round(overlap_rate(out["skeleton_id"], tr, te), 4),
              "thresholds": {}}
    for th in THRESHOLDS:
        t = time.time()
        fam_u = lsh_families(sig, th)
        fam = fam_u[sk_codes]
        out[f"family_{th}"] = fam
        sizes = pd.Series(fam).value_counts()
        per_class = (
            pd.DataFrame({"label": y, "fam": fam})
            .groupby("label")
            .agg(rows=("fam", "size"), families=("fam", "nunique"),
                 largest=("fam", lambda s: int(s.value_counts().iat[0])))
        )
        per_class["largest_share"] = (per_class["largest"] / per_class["rows"]).round(3)
        # Bir aile birden fazla sınıfın satırlarını içeriyor mu?
        mixed = pd.DataFrame({"label": y, "fam": fam}).groupby("fam")["label"].nunique()
        mixed_rows = int(pd.Series(fam).isin(mixed[mixed > 1].index).sum())
        report["thresholds"][str(th)] = {
            "families": int(sizes.size),
            "largest_family_rows": int(sizes.iat[0]),
            "largest_family_share": round(float(sizes.iat[0] / len(df)), 4),
            "singleton_families": int((sizes == 1).sum()),
            "rows_in_mixed_label_families": mixed_rows,
            "random_split_test_rows_with_family_in_train": round(overlap_rate(pd.Series(fam), tr, te), 4),
            "per_class": per_class.reset_index().to_dict(orient="records"),
        }
        print(f"[fam] eşik {th}: {sizes.size:,} aile, en büyük {sizes.iat[0]:,} satır, "
              f"rastgele bölmede ailesi eğitimde olan test oranı "
              f"{report['thresholds'][str(th)]['random_split_test_rows_with_family_in_train']:.3f} ({time.time() - t:.0f}s)", flush=True)

    out.to_parquet(CACHE / f"{name}_families.parquet")
    (ROOT / "results" / f"families_{name}.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
    (ROOT / "results" / f"families_{name}.md").write_text(to_md(report))


def to_md(r: dict) -> str:
    L = [f"# Payload aileleri: {r['dataset']}", "",
         f"- Satır: {r['rows']:,}; benzersiz iskelet: {r['unique_skeletons']:,}",
         f"- Rastgele bölmede iskeleti eğitimde birebir bulunan test satırı: **{100 * r['random_split_test_rows_with_same_skeleton_in_train']:.1f}%**", "",
         "## Eşik bazında özet", "",
         "| Eşik | Aile | En büyük aile (satır, %) | Tekil aile | Karışık etiketli ailelerdeki satır | Rastgele bölmede ailesi eğitimde olan test % |",
         "|---|---:|---:|---:|---:|---:|"]
    for th, d in r["thresholds"].items():
        L.append(f"| {th} | {d['families']:,} | {d['largest_family_rows']:,} ({100 * d['largest_family_share']:.1f}%) | "
                 f"{d['singleton_families']:,} | {d['rows_in_mixed_label_families']:,} | {100 * d['random_split_test_rows_with_family_in_train']:.1f} |")
    for th, d in r["thresholds"].items():
        L += ["", f"## Sınıf bazında (eşik {th})", "", "| Sınıf | Satır | Aile | En büyük aile payı |", "|---|---:|---:|---:|"]
        for c in d["per_class"]:
            L.append(f"| {c['label']} | {c['rows']:,} | {c['families']:,} | {c['largest_share']} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main(sys.argv[1])
