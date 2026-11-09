"""Bölüm B ve C şekilleri (stil 06_figures.py ile aynı).

Kullanım: python scripts/12_figures_bc.py
Girdi: results/obfuscation/*.json, results/shap/*.json
Çıktı: results/figures/fig9..fig12_*.png
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

_spec = importlib.util.spec_from_file_location("figs", Path(__file__).with_name("06_figures.py"))
F = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(F)
plt, RES, SEQ, INK, INK2, GRID, SURFACE, short, save = F.plt, F.RES, F.SEQ, F.INK, F.INK2, F.GRID, F.SURFACE, F.short, F.save

TRANSFORMS = ["case", "whitespace", "sql_comment", "html_slash", "cmd_quote", "path_dot", "artifact", "encoding_norm", "combo"]
T_LABEL = {"case": "harf\nbüyüklüğü", "whitespace": "boşluk→\nsekme", "sql_comment": "SQL\n/**/", "html_slash": "HTML\n'/'",
           "cmd_quote": 'komut\n""', "path_dot": "./../", "artifact": "oastify\ndeğişimi", "encoding_norm": "encoding\ntek kat*",
           "combo": "hepsi\nbirlikte"}
MIN_N = 10


def obf(model: str) -> dict:
    return json.loads((RES / "obfuscation" / f"{model}.json").read_text())


def drop_matrix(model: str):
    r = obf(model)
    classes = sorted({c for t in r["transforms"].values() for c in t.get("per_class", {})}, key=short)
    M = np.full((len(classes), len(TRANSFORMS)), np.nan)
    N = np.zeros_like(M)
    for j, t in enumerate(TRANSFORMS):
        for i, c in enumerate(classes):
            v = r["transforms"].get(t, {}).get("per_class", {}).get(c)
            if v and v.get("n_changed", 0) >= MIN_N:
                M[i, j] = 100 * (v["recall_before"] - v["recall_after"])
                N[i, j] = v["n_changed"]
    return classes, M, N


def fig_obf_heatmap(ds: str, title: str, num: int) -> None:
    pairs = [(f"{ds}_random_s42", "Rastgele bölme modeli"), (f"{ds}_family_0.8_s42", "Yakın-kopya kümesi (0.8) bölme modeli")]
    data = [drop_matrix(m) for m, _ in pairs]
    classes = data[0][0]
    vmax = max(30, np.nanmax([np.nanmax(d[1]) for d in data]))
    fig, axes = plt.subplots(1, 2, figsize=(15, 0.5 * len(classes) + 2.4), sharey=True)
    for ax, (cls, M, N), (_, sub) in zip(axes, data, pairs):
        assert cls == classes
        ax.imshow(np.where(np.isnan(M), 0, np.clip(M, 0, None)), cmap=SEQ, vmin=0, vmax=vmax, aspect="auto")
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if np.isnan(M[i, j]):
                    ax.text(j, i, "·", ha="center", va="center", color=GRID, fontsize=12)
                    continue
                v = M[i, j]
                ax.text(j, i, f"{-v:+.0f}" if abs(v) >= 0.5 else "0", ha="center", va="center", fontsize=8.5,
                        color="white" if v > vmax * 0.5 else INK)
        ax.set_xticks(range(len(TRANSFORMS)), [T_LABEL[t] for t in TRANSFORMS], fontsize=8)
        ax.set_yticks(range(len(classes)), [short(c) for c in classes])
        ax.set_title(sub, fontsize=10.5)
        ax.grid(False)
        ax.set_xticks(np.arange(-.5, len(TRANSFORMS), 1), minor=True)
        ax.set_yticks(np.arange(-.5, len(classes), 1), minor=True)
        ax.grid(which="minor", color=SURFACE, linewidth=2)
        ax.tick_params(which="minor", length=0)
    fig.suptitle(f"Şekil {num}. Gizleme sonrası sınıf recall değişimi (puan) — {title}", x=0.01, ha="left",
                 fontweight="bold", fontsize=12)
    fig.text(0.01, -0.04, f"Hücre: dönüşümün değiştirdiği test saldırılarında recall farkı (sonra − önce). "
                          f"'·' = dönüşüm bu sınıfa uygulanamıyor ya da {MIN_N}'dan az satırı değiştiriyor. "
                          "* çözücüye bağlı dönüşüm.", fontsize=8.5, color=INK2)
    fig.tight_layout()
    save(fig, f"fig{num}_obfuscation_{ds}.png")


def fig_artifact() -> None:
    models = [("ds_aug_v2_random_s42", "Rastgele bölme"), ("ds_aug_v2_family_0.8_s42", "Yakın-kopya kümesi (0.8) bölme")]
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.6), sharey=True)
    for ax, (m, sub) in zip(axes, models):
        pc = obf(m)["transforms"]["artifact"]["per_class"]
        rows = [(short(c), v) for c, v in pc.items() if v.get("n_changed", 0) >= MIN_N]
        rows.sort(key=lambda x: x[0])
        for i, (c, v) in enumerate(rows):
            b, a = 100 * v["recall_before"], 100 * v["recall_after"]
            ax.plot([b, a], [i, i], color=GRID, linewidth=2, zorder=1)
            ax.scatter([b], [i], s=60, color=INK2, zorder=2, edgecolor=SURFACE, linewidth=1.5)
            ax.scatter([a], [i], s=60, color=F.C_AUG, zorder=3, edgecolor=SURFACE, linewidth=1.5)
            ax.text(101, i, f"{b:.0f} → {a:.0f}  (n={v['n_changed']})", va="center", fontsize=8.5, color=INK2)
        ax.set_yticks(range(len(rows)), [r[0] for r in rows])
        ax.set_xlim(0, 100)
        ax.set_xlabel("Doğru sınıf recall (%)")
        ax.set_title(sub, fontsize=10.5)
        ax.grid(axis="y", visible=False)
    h1 = axes[0].scatter([], [], s=60, color=INK2)
    h2 = axes[0].scatter([], [], s=60, color=F.C_AUG)
    fig.legend([h1, h2], ["önce", "oastify.com değiştirildikten sonra"], loc="lower left", ncol=2, fontsize=9,
               bbox_to_anchor=(0.01, -0.08))
    fig.suptitle("Şekil 11. Yalnızca Burp Collaborator alan adı değiştirildiğinde (DS-Augmented-v2)", x=0.01,
                 ha="left", fontweight="bold", fontsize=12)
    fig.tight_layout()
    save(fig, "fig11_artifact_counterfactual.png")


def fig_shap_lost() -> None:
    cases = [("ds_aug_v2_family_0.8_s42", "artifact", "DS-Aug-v2 (küme 0.8): oastify değişimi"),
             ("ds_base_family_0.8_s42", "cmd_quote", 'DS-Base (küme 0.8): komut adına ""')]
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    for ax, (m, t, sub) in zip(axes, cases):
        e = json.loads((RES / "shap" / f"{m}.json").read_text())["local"][t]
        top = e["top_lost_support"][:8][::-1]
        names = [f["feature"].replace("tfidf[", "n-gram ").replace("]", "") for f in top]
        vals = [f["mean_delta"] for f in top]
        ax.barh(range(len(top)), vals, color=F.C_BASE, height=0.6)
        ax.set_yticks(range(len(top)), names, fontsize=9)
        ax.axvline(0, color=INK2, linewidth=0.8)
        ax.set_xlabel("Doğru sınıfın ham skoruna (raw margin) katkı değişimi")
        ax.set_title(f"{sub}\n(yanlışa dönen {e['n_flipped']} satır)", fontsize=10)
        ax.grid(axis="y", visible=False)
    fig.suptitle("Şekil 12. Gizleme sonrası en çok destek kaybeden özellikler (SHAP)", x=0.01, ha="left",
                 fontweight="bold", fontsize=12)
    fig.tight_layout()
    save(fig, "fig12_shap_lost_support.png")


def main() -> None:
    fig_obf_heatmap("ds_aug_v2", "DS-Augmented-v2", 9)
    fig_obf_heatmap("ds_base", "DS-Base", 10)
    fig_artifact()
    fig_shap_lost()


if __name__ == "__main__":
    main()
