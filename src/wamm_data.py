"""WAMM veri setlerini tek tip bir DataFrame (request, label) olarak yükler."""
from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
CACHE = ROOT / "data" / "cache"

SOURCES = {
    "ds_base": RAW / "ds_base" / "cleaned_with_full_request_and_class_columns.csv",
    "ds_aug_v1": RAW / "ds_aug_v1.db",
    "ds_aug_v2": RAW / "ds_aug_v2.db",
}


def _load_uncached(name: str) -> pd.DataFrame:
    path = SOURCES[name]
    if path.suffix == ".csv":
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
        df = df.rename(columns={"Full_request": "request", "class": "label"})
    else:
        with sqlite3.connect(path) as con:
            df = pd.read_sql("SELECT col1 AS request, col2 AS label FROM combined_data", con)
    df = df[["request", "label"]].astype({"request": "string", "label": "category"})
    return df.reset_index(drop=True)


def load(name: str) -> pd.DataFrame:
    """Veri setini yükler; ilk yüklemeden sonra parquet önbelleği kullanır.

    Satır sırası kaynak dosyadaki sırayla aynıdır; satır indeksi kayıt kimliği olarak kullanılabilir.
    """
    CACHE.mkdir(parents=True, exist_ok=True)
    cached = CACHE / f"{name}.parquet"
    if cached.exists():
        return pd.read_parquet(cached)
    df = _load_uncached(name)
    df.to_parquet(cached, index=False)
    return df


def is_normal(label: str) -> bool:
    return "normal" in str(label).lower()
