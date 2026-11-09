"""Aşama 1: Veri profili ve birebir tekrar analizi.

Kullanım: python scripts/01_profile.py [ds_base ds_aug_v2 ...]
Çıktı: results/profile_<ad>.md ve results/profile_<ad>.json
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from http_parse import parse  # noqa: E402
from wamm_data import ROOT, is_normal, load  # noqa: E402

OUT = ROOT / "results"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8", "surrogatepass")).hexdigest()


def dup_stats(df: pd.DataFrame, key: str) -> dict:
    """Bir anahtar sütunu üzerinden birebir tekrar istatistikleri."""
    n = len(df)
    uniq = df[key].nunique()
    per_class = (
        df.groupby("label", observed=True)[key]
        .agg(n="size", unique="nunique")
        .assign(dup_rate=lambda t: 1 - t["unique"] / t["n"])
    )
    labels_per_key = df.groupby(key, observed=True)["label"].nunique()
    conflicting_keys = labels_per_key[labels_per_key > 1].index
    conflict_rows = int(df[key].isin(conflicting_keys).sum())
    return {
        "rows": n,
        "unique": int(uniq),
        "duplicate_rows": int(n - uniq),
        "duplicate_rate": round(1 - uniq / n, 4),
        "conflicting_keys": int(len(conflicting_keys)),
        "conflicting_rows": conflict_rows,
        "per_class": per_class.round(4).reset_index().to_dict(orient="records"),
    }


def top(series: pd.Series, k: int = 5) -> list:
    vc = series.value_counts().head(k)
    return [[str(i), int(c)] for i, c in vc.items()]


def profile(name: str) -> dict:
    df = load(name)
    parsed = df["request"].map(parse)
    df = df.assign(
        method=parsed.map(lambda p: p.method),
        host=parsed.map(lambda p: p.headers.get("host", "")),
        ua=parsed.map(lambda p: p.headers.get("user-agent", "")),
        n_headers=parsed.map(lambda p: len(p.headers)),
        has_body=parsed.map(lambda p: bool(p.body)),
        payload=parsed.map(lambda p: p.payload()),
        length=df["request"].str.len(),
    )
    df["h_raw"] = df["request"].map(sha)
    df["h_payload"] = (df["method"] + " " + df["payload"]).map(sha)
    df["is_attack"] = ~df["label"].map(is_normal).astype(bool)

    by_class = df.groupby("label", observed=True)
    info = {
        "dataset": name,
        "rows": len(df),
        "empty_requests": int((df["request"].str.strip() == "").sum()),
        "labels": {str(k): int(v) for k, v in df["label"].value_counts().items()},
        "length_by_class": by_class["length"].describe()[["mean", "50%", "max"]].round(1).reset_index().to_dict(orient="records"),
        "has_body_rate_by_class": by_class["has_body"].mean().round(3).astype(float).to_dict(),
        "n_headers_mean_by_class": by_class["n_headers"].mean().round(2).astype(float).to_dict(),
        "methods_by_class": {str(k): top(g["method"]) for k, g in by_class},
        "hosts_by_class": {str(k): top(g["host"], 3) for k, g in by_class},
        "user_agents_by_class": {str(k): top(g["ua"], 3) for k, g in by_class},
        "ua_overlap": {
            "attack_ua_unique": int(df.loc[df.is_attack, "ua"].nunique()),
            "normal_ua_unique": int(df.loc[~df.is_attack, "ua"].nunique()),
            "shared_ua": int(len(set(df.loc[df.is_attack, "ua"]) & set(df.loc[~df.is_attack, "ua"]))),
            "attack_rows_with_ua_seen_in_normal": round(
                float(df.loc[df.is_attack, "ua"].isin(set(df.loc[~df.is_attack, "ua"])).mean()), 4
            ),
        },
        "dup_raw": dup_stats(df, "h_raw"),
        "dup_payload": dup_stats(df, "h_payload"),
    }
    # Sonraki adımlar için hash'leri sakla
    df[["label", "h_raw", "h_payload"]].to_parquet(ROOT / "data" / "cache" / f"{name}_hashes.parquet")
    return info


def to_markdown(p: dict) -> str:
    L = [f"# Veri profili: {p['dataset']}", "", f"- Satır: **{p['rows']:,}**", f"- Boş istek: {p['empty_requests']}", ""]
    L += ["## Sınıf dağılımı", "", "| Sınıf | Satır | % |", "|---|---:|---:|"]
    for k, v in p["labels"].items():
        L.append(f"| {k} | {v:,} | {100 * v / p['rows']:.2f} |")
    for title, key in [("Birebir tekrar — ham istek", "dup_raw"), ("Birebir tekrar — method + payload (header'lar hariç)", "dup_payload")]:
        d = p[key]
        L += ["", f"## {title}", "",
              f"- Benzersiz: {d['unique']:,} / {d['rows']:,} → tekrar oranı **{100 * d['duplicate_rate']:.2f}%**",
              f"- Farklı etiketlerle görünen içerik: {d['conflicting_keys']:,} anahtar, {d['conflicting_rows']:,} satır", "",
              "| Sınıf | Satır | Benzersiz | Tekrar % |", "|---|---:|---:|---:|"]
        for r in d["per_class"]:
            L.append(f"| {r['label']} | {r['n']:,} | {r['unique']:,} | {100 * r['dup_rate']:.2f} |")
    L += ["", "## Uzunluk (karakter)", "", "| Sınıf | Ortalama | Medyan | Maks |", "|---|---:|---:|---:|"]
    for r in p["length_by_class"]:
        L.append(f"| {r['label']} | {r['mean']} | {r['50%']} | {r['max']} |")
    L += ["", "## Yapısal sinyaller (olası kısayollar)", "", "| Sınıf | Body oranı | Ort. header | En sık method | En sık host |", "|---|---:|---:|---|---|"]
    for k in p["labels"]:
        m = p["methods_by_class"][k][0]
        h = p["hosts_by_class"][k][0]
        L.append(f"| {k} | {p['has_body_rate_by_class'][k]} | {p['n_headers_mean_by_class'][k]} | {m[0]} ({m[1]:,}) | {h[0]} ({h[1]:,}) |")
    u = p["ua_overlap"]
    L += ["", "### User-Agent örtüşmesi", "",
          f"- Saldırı satırlarında benzersiz UA: {u['attack_ua_unique']:,}; normal satırlarda: {u['normal_ua_unique']:,}; ortak: {u['shared_ua']:,}",
          f"- UA'sı normal trafikte de görülen saldırı satırı oranı: **{100 * u['attack_rows_with_ua_seen_in_normal']:.2f}%**", "",
          "| Sınıf | En sık UA | Satır |", "|---|---|---:|"]
    for k, lst in p["user_agents_by_class"].items():
        ua, c = lst[0]
        L.append(f"| {k} | `{ua[:90]}` | {c:,} |")
    return "\n".join(L) + "\n"


def main(names: list[str]) -> None:
    OUT.mkdir(exist_ok=True)
    for name in names:
        print(f"[profile] {name} ...", flush=True)
        p = profile(name)
        (OUT / f"profile_{name}.json").write_text(json.dumps(p, indent=2, ensure_ascii=False))
        (OUT / f"profile_{name}.md").write_text(to_markdown(p))
        print(f"[profile] {name}: {p['rows']:,} satır, ham tekrar %{100 * p['dup_raw']['duplicate_rate']:.2f}, "
              f"payload tekrar %{100 * p['dup_payload']['duplicate_rate']:.2f}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["ds_base", "ds_aug_v2"])
