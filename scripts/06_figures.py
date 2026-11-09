"""Rapor şekilleri. Tüm sayılar results/ altındaki JSON'lardan okunur.

Kullanım: python scripts/06_figures.py
Çıktı: results/figures/*.png
Birden fazla seed sonucu varsa (results/splits/*_s<seed>.json) ortalama ve min–maks aralığı çizilir.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wamm_data import ROOT, load  # noqa: E402

RES = ROOT / "results"
FIG = RES / "figures_revised"  # akademik revizyon numaralandırması (results_revised.md)
FIG.mkdir(parents=True, exist_ok=True)

# Referans palet (dataviz skill, light mod)
C_BASE = "#2a78d6"   # slot 1 mavi  -> DS-Base
C_AUG = "#eb6834"    # slot 2 turuncu -> DS-Augmented-v2
INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#e4e3df"
SURFACE = "#fcfcfb"
SEQ = LinearSegmentedColormap.from_list("seq_blue", ["#f4f8fd", "#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])

DS = {"ds_base": ("DS-Base", C_BASE), "ds_aug_v2": ("DS-Augmented-v2", C_AUG)}
SPLITS = ["random", "h_raw", "skeleton_id", "family_0.9", "family_0.8"]
SPLIT_LABEL = {
    "random": "Rastgele\n(WAMM)",
    "h_raw": "Birebir aynı\nistek",
    "skeleton_id": "Aynı\niskelet",
    "family_0.9": "Yakın-kopya\nkümesi (0.9)",
    "family_0.8": "Yakın-kopya\nkümesi (0.8)",
}

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK2, "axes.titlecolor": INK, "axes.titlesize": 12,
    "axes.titleweight": "bold", "axes.titlelocation": "left", "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "legend.frameon": False, "savefig.dpi": 200, "savefig.bbox": "tight",
})


def short(label: str) -> str:
    """'66 - SQL Injection' -> 'SQL Injection'."""
    return label.split(" - ", 1)[1] if " - " in label else label


def load_split_results() -> pd.DataFrame:
    rows = []
    for f in glob.glob(str(RES / "splits" / "*.json")):
        r = json.loads(Path(f).read_text())
        cl = r["classes"]
        cm = np.array(r["confusion_matrix"])
        ni = next(i for i, c in enumerate(cl) if "normal" in c.lower())
        att = [i for i in range(len(cl)) if i != ni]
        base = dict(dataset=r["dataset"], split=r["split"], seed=r["seed"], macro_f1=r["macro_f1"],
                    accuracy=r["accuracy"], normal_fpr=1 - cm[ni, ni] / cm[ni].sum(),
                    attack_miss=cm[att, ni].sum() / cm[att].sum())
        for c in cl:
            rows.append({**base, "cls": c, "f1": r["per_class"][c]["f1-score"]})
    return pd.DataFrame(rows)


def save(fig, name: str) -> None:
    fig.savefig(FIG / name)
    plt.close(fig)
    print("  ", FIG / name)


# ---------------------------------------------------------------- Şekil 1
def fig_macro_f1(df: pd.DataFrame) -> None:
    agg = (df.drop_duplicates(["dataset", "split", "seed"])
           .groupby(["dataset", "split"])["macro_f1"].agg(["mean", "min", "max", "count"]).reset_index())
    fig, ax = plt.subplots(figsize=(8, 4.6))
    x = np.arange(len(SPLITS))
    for ds, (name, col) in DS.items():
        a = agg[agg.dataset == ds].set_index("split").reindex(SPLITS)
        ax.plot(x, a["mean"], color=col, lw=2, marker="o", ms=8, mec=SURFACE, mew=2, label=name, zorder=3)
        if (a["count"] > 1).any():
            ax.fill_between(x, a["min"], a["max"], color=col, alpha=0.15, lw=0)
        ax.annotate(name, (x[-1], a["mean"].iloc[-1]), xytext=(10, 0), textcoords="offset points",
                    va="center", color=INK2, fontsize=9)
        for xi, (s, v) in zip(x, a["mean"].items()):
            if s in ("random", "family_0.8"):
                ax.annotate(f"{v:.3f}", (xi, v), xytext=(0, 9), textcoords="offset points",
                            ha="center", color=INK, fontsize=9)
    n_seeds = int(agg["count"].max())
    ax.set_xticks(x, [SPLIT_LABEL[s] for s in SPLITS])
    ax.set_ylabel("Macro F1")
    ax.set_ylim(0.5, 1.02)
    ax.grid(axis="x", visible=False)
    ax.set_title("Şekil 4. Bölme stratejisine göre Macro F1")
    ax.legend(loc="lower left")
    ax.text(0, -0.24, f"XGBoost (WAMM özellikleri). Seed sayısı: {n_seeds}"
            + ("; gölge = min–maks aralığı." if n_seeds > 1 else "; tek seed, ön sonuç."),
            transform=ax.transAxes, color=INK2, fontsize=8)
    save(fig, "fig4_macro_f1_by_split.png")


# ---------------------------------------------------------------- Şekil 2–3
def fig_class_heatmap(df: pd.DataFrame, ds: str, num: int) -> None:
    piv = df[df.dataset == ds].groupby(["cls", "split"])["f1"].mean().unstack()[SPLITS]
    piv = piv.sort_values("family_0.8")
    fig, ax = plt.subplots(figsize=(8, 0.42 * len(piv) + 1.6))
    ax.imshow(piv.values, cmap=SEQ, vmin=0, vmax=1, aspect="auto")
    for i in range(piv.shape[0]):
        for j in range(piv.shape[1]):
            v = piv.values[i, j]
            ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=8.5,
                    color="white" if v > 0.6 else INK)
    ax.set_xticks(range(len(SPLITS)), [SPLIT_LABEL[s] for s in SPLITS], fontsize=8.5)
    ax.set_yticks(range(len(piv)), [short(c) for c in piv.index])
    ax.tick_params(length=0)
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks(np.arange(-0.5, len(SPLITS)), minor=True)
    ax.set_yticks(np.arange(-0.5, len(piv)), minor=True)
    ax.grid(which="minor", color=SURFACE, lw=2)
    ax.tick_params(which="minor", length=0)
    ax.set_title(f"Şekil {num}. Sınıf bazında F1 — {DS[ds][0]}")
    save(fig, f"fig{num}_class_f1_{ds}.png")


# ---------------------------------------------------------------- Şekil 4
def fig_overlap() -> None:
    """Rastgele bölmede: test satırının eğitimde 'akrabası' olma oranı, benzerlik düzeyine göre."""
    levels = [("Birebir aynı\nistek", "h_raw"), ("Aynı payload\n(header hariç)", "h_payload"),
              ("Aynı\niskelet", "skeleton"), ("Yakın-kopya\nkümesi (0.9)", "0.9"), ("Yakın-kopya\nkümesi (0.8)", "0.8")]
    vals = {}
    for ds in DS:
        rnd = json.loads((RES / "splits" / f"{ds}_random_s42.json").read_text())
        fam = json.loads((RES / f"families_{ds}.json").read_text())
        vals[ds] = [rnd["test_rows_with_h_raw_in_train"], rnd["test_rows_with_h_payload_in_train"],
                    fam["random_split_test_rows_with_same_skeleton_in_train"],
                    fam["thresholds"]["0.9"]["random_split_test_rows_with_family_in_train"],
                    fam["thresholds"]["0.8"]["random_split_test_rows_with_family_in_train"]]
    fig, ax = plt.subplots(figsize=(8, 4.4))
    x = np.arange(len(levels))
    w = 0.38
    for k, (ds, (name, col)) in enumerate(DS.items()):
        xs = x + (k - 0.5) * (w + 0.02)
        bars = ax.bar(xs, np.array(vals[ds]) * 100, w, color=col, label=name, zorder=3)
        for b in bars:
            ax.annotate(f"{b.get_height():.0f}", (b.get_x() + b.get_width() / 2, b.get_height()),
                        xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8, color=INK)
    ax.set_xticks(x, [l for l, _ in levels])
    ax.set_ylabel("Test satırlarının yüzdesi")
    ax.set_ylim(0, 108)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left")
    ax.set_title("Şekil 3. Rastgele bölmede eğitim kümesinde eşi bulunan test satırları")
    save(fig, "fig3_random_split_overlap.png")


# ---------------------------------------------------------------- Şekil 5
def fig_fpr(df: pd.DataFrame) -> None:
    agg = (df.drop_duplicates(["dataset", "split", "seed"])
           .groupby(["dataset", "split"])["normal_fpr"].mean().unstack().reindex(columns=SPLITS) * 100)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    x = np.arange(len(SPLITS))
    w = 0.38
    for k, (ds, (name, col)) in enumerate(DS.items()):
        xs = x + (k - 0.5) * (w + 0.02)
        bars = ax.bar(xs, agg.loc[ds].values, w, color=col, label=name, zorder=3)
        for b in bars:
            ax.annotate(f"{b.get_height():.2f}", (b.get_x() + b.get_width() / 2, b.get_height()),
                        xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8, color=INK)
    ax.set_xticks(x, [SPLIT_LABEL[s] for s in SPLITS])
    ax.set_ylabel("Normal trafikte yanlış alarm (%)")
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left")
    ax.set_title("Şekil 7. Normal trafikte yanlış pozitif oranı (FPR)")
    save(fig, "fig7_normal_fpr.png")


# ---------------------------------------------------------------- Şekil 6
def fig_duplicates() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), gridspec_kw={"width_ratios": [12, 9]})
    for ax, (ds, (name, col)) in zip(axes, DS.items()):
        p = json.loads((RES / f"profile_{ds}.json").read_text())
        d = pd.DataFrame(p["dup_raw"]["per_class"]).assign(cls=lambda t: t["label"].map(short)).sort_values("dup_rate")
        ax.barh(d["cls"], d["dup_rate"] * 100, color=col, height=0.62, zorder=3)
        for y, v in enumerate(d["dup_rate"] * 100):
            ax.annotate(f"{v:.0f}", (v, y), xytext=(3, 0), textcoords="offset points", va="center", fontsize=8, color=INK)
        ax.set_xlim(0, 100)
        ax.grid(axis="y", visible=False)
        ax.set_xlabel("Ham istek tekrar oranı (%)")
        ax.set_title(f"{name}  (genel: %{100 * p['dup_raw']['duplicate_rate']:.1f})", fontsize=10, fontweight="normal", color=INK2)
    fig.suptitle("Şekil 1. Yayımlanan veri setlerinde birebir tekrar oranı, sınıf bazında", x=0.01, ha="left",
                 fontweight="bold", fontsize=12, color=INK)
    fig.tight_layout()
    save(fig, "fig1_duplicates_by_class.png")


# ---------------------------------------------------------------- Şekil 7
def fig_artifacts() -> None:
    df = load("ds_aug_v2")
    r = df["request"].str.lower()
    t = pd.DataFrame({"cls": df["label"].astype(str).map(short),
                      "oastify": r.str.contains("oastify.com", regex=False),
                      "deep": r.str.contains("%252525", regex=False)}).groupby("cls").mean() * 100
    t = t.sort_values("oastify")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
    for ax, col, title in [(axes[0], "oastify", "'oastify.com' (Burp Collaborator) geçen satır %"),
                           (axes[1], "deep", "7+ kat iç içe URL encoding (%252525…) %")]:
        ax.barh(t.index, t[col], color=C_AUG, height=0.62, zorder=3)
        for y, v in enumerate(t[col]):
            ax.annotate(f"{v:.1f}", (v, y), xytext=(3, 0), textcoords="offset points", va="center", fontsize=8, color=INK)
        ax.set_xlim(0, max(70, t[col].max() * 1.15))
        ax.grid(axis="y", visible=False)
        ax.set_title(title, fontsize=10, fontweight="normal", color=INK2)
    fig.suptitle("Şekil 2. DS-Augmented-v2'de araç kaynaklı ayırt edici izler", x=0.01, ha="left",
                 fontweight="bold", fontsize=12, color=INK)
    fig.tight_layout()
    save(fig, "fig2_tool_artifacts.png")


# ---------------------------------------------------------------- Şekil 8
def fig_confusion(ds: str = "ds_aug_v2", split: str = "family_0.8", seed: int = 42) -> None:
    r = json.loads((RES / "splits" / f"{ds}_{split}_s{seed}.json").read_text())
    cl = [short(c) for c in r["classes"]]
    cm = np.array(r["confusion_matrix"], dtype=float)
    cmn = cm / cm.sum(axis=1, keepdims=True)
    fig, ax = plt.subplots(figsize=(7.4, 6.2))
    ax.imshow(cmn, cmap=SEQ, vmin=0, vmax=1)
    for i in range(len(cl)):
        for j in range(len(cl)):
            v = cmn[i, j]
            if v >= 0.005:
                ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=7.5, color="white" if v > 0.6 else INK)
    ax.set_xticks(range(len(cl)), cl, rotation=40, ha="right", fontsize=8.5)
    ax.set_yticks(range(len(cl)), cl, fontsize=8.5)
    ax.set_xlabel("Tahmin edilen sınıf")
    ax.set_ylabel("Gerçek sınıf")
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    ax.set_title(f"Şekil 8. Karışıklık matrisi (satır normalize) — {DS[ds][0]}, yakın-kopya kümesi 0.8")
    save(fig, "fig8_confusion_aug_v2_family08.png")


def main() -> None:
    df = load_split_results()
    fig_macro_f1(df)
    fig_class_heatmap(df, "ds_aug_v2", 5)
    fig_class_heatmap(df, "ds_base", 6)
    fig_overlap()
    fig_fpr(df)
    fig_duplicates()
    fig_artifacts()
    fig_confusion()


if __name__ == "__main__":
    main()
