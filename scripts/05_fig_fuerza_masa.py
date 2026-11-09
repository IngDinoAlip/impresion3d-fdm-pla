"""fig4_fuerza_masa.png : fuerza maxima por gramo (N/g) por ensayo y configuracion (poster)."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
R = os.path.join(os.path.dirname(__file__), "..")
df = pd.read_csv(os.path.join(R, "datos", "resultados.csv")); df["npg"] = df.fmax_N / df.peso_g
NAVY, ORANGE, GRAY = "#0B2A5B", "#D98A00", "#8A8F98"
COL = {"Fina": GRAY, "Estandar": ORANGE, "Fuerte": NAVY}; LAB = {"Fina": "Fina", "Estandar": "Estándar", "Fuerte": "Fuerte"}
plt.rcParams.update({"font.family": "Arial", "axes.spines.top": False, "axes.spines.right": False})
fs = 26
fig, ax = plt.subplots(figsize=(10, 3.3))
w = 0.26; res = {}
for j, c in enumerate(["Fina", "Estandar", "Fuerte"]):
    v = [df[(df.ensayo == e) & (df.config == c)].npg.mean() for e in "TCF"]; res[c] = v
    b = ax.bar(np.arange(3) + (j - 1) * w, v, w * 0.92, color=COL[c], label=LAB[c], zorder=2)
    for x, y in zip(np.arange(3) + (j - 1) * w, v): ax.text(x, y + 0.6, f"{y:.0f}", ha="center", fontsize=fs - 5)
ax.set_xticks(range(3)); ax.set_xticklabels(["Tensión", "Compresión", "Flexión"], fontsize=fs - 2)
ax.set_ylabel("Fuerza / masa (N/g)", fontsize=fs - 4); ax.tick_params(axis="y", labelsize=fs - 3)
ax.grid(axis="y", color="#DDDDDD", zorder=0); ax.set_ylim(0, 44)
ax.legend(frameon=False, fontsize=fs - 4, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.12))
fig.tight_layout(); fig.savefig(os.path.join(R, "figuras", "fig4_fuerza_masa.png"), dpi=300)
for e, i in zip("TCF", range(3)):
    print(e, {c: round(res[c][i], 1) for c in res}, "Fuerte vs Fina %:", round((res["Fuerte"][i] / res["Fina"][i] - 1) * 100, 1))
# por orientacion
print(df.pivot_table(index="orientacion", columns="config", values="npg").round(1))
