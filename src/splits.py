"""Eğitim/test bölme stratejileri."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def random_stratified(labels: pd.Series, test_size: float = 0.2, seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    """WAMM'deki gibi: satır düzeyinde stratified rastgele bölme."""
    idx = np.arange(len(labels))
    tr, te = train_test_split(idx, test_size=test_size, stratify=labels.astype(str), random_state=seed)
    return np.sort(tr), np.sort(te)


def group_stratified(labels: pd.Series, groups: pd.Series, test_size: float = 0.2, seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    """Grupları bölmeden, sınıf oranlarını yaklaşık koruyan bölme.

    Her grup çoğunluk etiketine atanır. Her etiket içinde gruplar rastgele sırayla dolaşılır;
    bir grup, eklendiğinde o etiketin test hedefini (test_size × satır sayısı) aşmıyorsa teste alınır,
    aşıyorsa atlanır (eğitimde kalır). Böylece büyük gruplar test oranını şişirmez.
    Bir grubun bütün satırları her zaman aynı tarafta kalır.
    """
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({"label": labels.astype(str).values, "group": groups.values})
    # Çoğunluk etiketi: (grup, etiket) sayımlarından en büyüğü
    counts = df.groupby(["group", "label"], sort=False).size().reset_index(name="n")
    counts = counts.sort_values("n", ascending=False).drop_duplicates("group")
    sizes_all = df.groupby("group", sort=False).size()
    g = counts.set_index("group")[["label"]].assign(size=sizes_all)
    test_groups: list = []
    for _, gl in g.groupby("label", sort=False):
        order = rng.permutation(len(gl))
        sizes = gl["size"].values[order]
        ids = gl.index.values[order]
        target = test_size * sizes.sum()
        filled = 0
        for gid, s in zip(ids, sizes):
            if filled + s <= target:
                test_groups.append(gid)
                filled += s
            if filled >= target * 0.999:
                break
    is_test = df["group"].isin(set(test_groups)).values
    idx = np.arange(len(df))
    return idx[~is_test], idx[is_test]


def overlap_rate(keys: pd.Series, tr: np.ndarray, te: np.ndarray) -> float:
    """Test satırlarının ne kadarının eğitimde aynı anahtara sahip bir kopyası var."""
    train_keys = set(keys.values[tr])
    return float(np.mean([k in train_keys for k in keys.values[te]]))
