"""Figuras del articulo y del poster desde datos/resultados.csv.
fig1_fmax_poster.png : protagonista del poster (escala A1: texto >= 24 pt, 300 ppp a tamano final).
fig2_eficiencia.png  : Fmax por gramo y masa por configuracion (articulo).
fig3_anisotropia.png : razon V/H y 45/H por ensayo (articulo)."""
import os, numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = os.path.join(os.path.dirname(__file__), "..")
df = pd.read_csv(os.path.join(R, "datos", "resultados.csv"))
OUT = os.path.join(R, "figuras")

NAVY, ORANGE, GRAY = "#0B2A5B", "#D98A00", "#8A8F98"
COL = {"Fina": GRAY, "Estandar": ORANGE, "Fuerte": NAVY}
LAB = {"Fina": "Fina", "Estandar": "Estándar", "Fuerte": "Fuerte"}
ORI = ["V90", "D45", "H0"]
ORI_LAB = {"V90": "Vertical\n(90°)", "D45": "Inclinada\n(45°)", "H0": "Horizontal\n(0°)"}
TIT = {"T": "Tensión", "C": "Compresión", "F": "Flexión"}
plt.rcParams.update({"font.family": "Arial", "axes.spines.top": False, "axes.spines.right": False})


def fig1(fs=26, size=(21, 4.3)):
    fig, axs = plt.subplots(1, 3, figsize=size, sharey=False)
    w = 0.26
    for ax, e in zip(axs, "TCF"):
        for j, c in enumerate(["Fina", "Estandar", "Fuerte"]):
            means, g1, g2 = [], [], []
            for o in ORI:
                s = df[(df.ensayo == e) & (df.config == c) & (df.orientacion == o)].set_index("diseno").fmax_N
                means.append(s.mean()); g1.append(s["G1"]); g2.append(s["G2"])
            x = np.arange(3) + (j - 1) * w
            ax.bar(x, means, w * 0.92, color=COL[c], label=LAB[c], zorder=2)
            ax.scatter(x, g1, s=130, marker="o", facecolor="white", edgecolor="black", linewidth=2, zorder=3,
                       label="G1" if (e == "T" and j == 0) else None)
            ax.scatter(x, g2, s=130, marker="s", facecolor="black", edgecolor="black", zorder=3,
                       label="G2" if (e == "T" and j == 0) else None)
        ax.set_xticks(range(3)); ax.set_xticklabels([ORI_LAB[o] for o in ORI], fontsize=fs - 4)
        ax.set_title(TIT[e], fontsize=fs + 4, fontweight="bold", pad=14)
        ax.tick_params(axis="y", labelsize=fs - 4)
        ax.grid(axis="y", color="#DDDDDD", zorder=0)
        ax.set_ylim(0, {"T": 230, "C": 340, "F": 125}[e])
    axs[0].set_ylabel("Fuerza máxima (N)", fontsize=fs)
    h, l = axs[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=5, fontsize=fs - 2, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.12, 1, 1))
    fig.savefig(os.path.join(OUT, "fig1_fmax_poster.png"), dpi=300)
    plt.close(fig)


def fig2(fs=12):
    df["f_por_g"] = df.fmax_N / df.peso_g
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.1))
    m = df.groupby("config").peso_g.agg(["mean", "std"]).loc[["Fina", "Estandar", "Fuerte"]]
    axs[0].bar([LAB[c] for c in m.index], m["mean"], color=[COL[c] for c in m.index], yerr=m["std"], capsize=3)
    axs[0].set_ylabel("Masa (g)"); axs[0].set_title("(a) Masa por configuración", fontsize=9)
    w = 0.26
    for j, c in enumerate(["Fina", "Estandar", "Fuerte"]):
        v = [df[(df.ensayo == e) & (df.config == c)].f_por_g.mean() for e in "TCF"]
        axs[1].bar(np.arange(3) + (j - 1) * w, v, w * 0.92, color=COL[c], label=LAB[c])
    axs[1].set_xticks(range(3)); axs[1].set_xticklabels([TIT[e] for e in "TCF"])
    axs[1].set_ylabel("Fuerza máxima / masa (N/g)"); axs[1].set_title("(b) Eficiencia específica", fontsize=9)
    axs[1].legend(frameon=False, fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig2_eficiencia.png"), dpi=300); plt.close(fig)


def fig3():
    fig, ax = plt.subplots(figsize=(3.4, 2.9))
    w = 0.34
    for k, (o, lab, col) in enumerate([("V90", "Vertical / Horizontal", NAVY), ("D45", "45° / Horizontal", ORANGE)]):
        v = []
        for e in "TCF":
            s = df[df.ensayo == e].groupby(["diseno", "config", "orientacion"]).fmax_N.mean().unstack()
            v.append((s[o] / s["H0"]).mean())
        ax.bar(np.arange(3) + (k - 0.5) * w, v, w * 0.92, color=col, label=lab)
    ax.axhline(1, color="black", lw=0.8, ls="--")
    ax.set_xticks(range(3)); ax.set_xticklabels([TIT[e] for e in "TCF"])
    ax.set_ylabel("Razón de fuerza máxima"); ax.set_ylim(0, 1.1); ax.legend(frameon=False, fontsize=7, loc="lower right")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig3_anisotropia.png"), dpi=300); plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    # tabla resumen para el articulo
    t = (df.groupby(["ensayo", "config", "orientacion"]).agg(fmax_media=("fmax_N", "mean"), deform_media=("deform_mm", "mean"),
         peso_medio=("peso_g", "mean")).round(2).reset_index())
    t.to_csv(os.path.join(R, "datos", "resumen_por_condicion.csv"), index=False)
    print("figuras y resumen listos")
