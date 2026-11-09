"""Genera para la maqueta del articulo: articulo/tabla2.tex (tabla completa) y figuras/fig5_resultados_articulo.png."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = os.path.join(os.path.dirname(__file__), "..")
df = pd.read_csv(os.path.join(R, "datos", "resultados.csv"))
CONF = [("Fina", "Fina"), ("Estandar", "Estándar"), ("Fuerte", "Fuerte")]
ORI = [("V90", "90°"), ("D45", "45°"), ("H0", "0°")]
NL = "\n"

# ---- tabla 2 (tabular completo) ----
rows = []
for c, cl in CONF:
    for o, ol in ORI:
        s = df[(df.config == c) & (df.orientacion == o)]
        cel = [f"{s[s.ensayo == e].fmax_N.mean():.1f}" for e in "TCF"]
        cel += [f"{s[s.ensayo == e].deform_mm.mean():.1f}" for e in "TCF"]
        cel += [f"{s.peso_g.mean():.1f}"]
        rows.append((cl if o == "V90" else "") + " & " + ol + " & " + " & ".join(cel).replace(".", "{,}") + r" \\")
    if c != "Fuerte":
        rows.append(r"\midrule")
head = [
    r"\begin{tabular}{@{}llccccccc@{}}\toprule",
    r" & & \multicolumn{3}{c}{Fuerza máxima (N)} & \multicolumn{3}{c}{Deformación (mm)} & Masa \\",
    r"\cmidrule(lr){3-5}\cmidrule(lr){6-8}",
    r"Configuración & Orient. & Tensión & Compresión & Flexión & Tensión & Compresión & Flexión & (g) \\\midrule",
]
tail = [r"\bottomrule", r"\end{tabular}"]
with open(os.path.join(R, "articulo", "tabla2.tex"), "w", encoding="utf-8", newline=NL) as fh:
    fh.write(NL.join(head + rows + tail) + NL)

# ---- figura de resultados (version articulo, fuentes pequenas) ----
NAVY, ORANGE, GRAY = "#0B2A5B", "#D98A00", "#8A8F98"
col = {"Fina": GRAY, "Estandar": ORANGE, "Fuerte": NAVY}
plt.rcParams.update({"font.family": "Arial", "font.size": 8, "axes.spines.top": False, "axes.spines.right": False})
fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.5))
for ax, e, t in zip(axs, "TCF", ["Tensión", "Compresión", "Flexión"]):
    for j, (c, cl) in enumerate(CONF):
        m = [df[(df.ensayo == e) & (df.config == c) & (df.orientacion == o)].fmax_N.mean() for o, _ in ORI]
        ax.bar(np.arange(3) + (j - 1) * 0.26, m, 0.24, color=col[c], label=cl)
    ax.set_xticks(range(3)); ax.set_xticklabels([ol for _, ol in ORI]); ax.set_title(t, fontsize=9, fontweight="bold")
    ax.set_xlabel("Orientación de impresión"); ax.grid(axis="y", color="#DDD", zorder=0)
axs[0].set_ylabel("Fuerza máxima (N)"); axs[0].legend(frameon=False, fontsize=7)
fig.tight_layout(); fig.savefig(os.path.join(R, "figuras", "fig5_resultados_articulo.png"), dpi=300)
print("ok")
