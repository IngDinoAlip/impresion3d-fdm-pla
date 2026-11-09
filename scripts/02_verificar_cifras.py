"""Recalcula desde datos/resultados.csv las cifras que el articulo afirma en Discusion y Conclusiones."""
import os, pandas as pd, numpy as np

R = os.path.join(os.path.dirname(__file__), "..")
df = pd.read_csv(os.path.join(R, "datos", "resultados.csv"))
pd.set_option("display.width", 160)

def pct(a, b):  # incremento de a respecto de b
    return (a / b - 1) * 100

print("== Fuerte vs Fina (incremento % en Fmax, media sobre 2 disenos x 3 orientaciones) ==")
print("   articulo afirma: T 65.8 | C 67.4 | F 62.3")
for e in "TCF":
    s = df[df.ensayo == e].groupby(["diseno", "orientacion", "config"]).fmax_N.mean().unstack()
    inc = pct(s["Fuerte"], s["Fina"])
    print(f"   {e}: media de incrementos = {inc.mean():.1f}  | incremento de medias = {pct(s['Fuerte'].mean(), s['Fina'].mean()):.1f}")

print("\n== Estandar vs Fina (articulo: 12-18 %) ==")
for e in "TCF":
    s = df[df.ensayo == e].groupby(["diseno", "orientacion", "config"]).fmax_N.mean().unstack()
    inc = pct(s["Estandar"], s["Fina"])
    print(f"   {e}: min {inc.min():.1f}  max {inc.max():.1f}  media {inc.mean():.1f}")

print("\n== Horizontal vs Vertical ==")
print("   articulo: tension Fina 64.2, Fuerte 79.1; conclusiones T 64 | C 22 | F 73")
for e in "TCF":
    s = df[df.ensayo == e].groupby(["diseno", "config", "orientacion"]).fmax_N.mean().unstack()
    a = pct(s["H0"], s["V90"])          # H es X % mayor que V
    b = (1 - s["V90"] / s["H0"]) * 100  # V es X % menor que H
    print(f"   {e}: H sobre V = {a.mean():.1f} %  | V por debajo de H = {b.mean():.1f} %")
    if e == "T":
        for c in ["Fina", "Estandar", "Fuerte"]:
            print(f"       {c}: H sobre V = {a.xs(c, level='config').mean():.1f} %, V bajo H = {b.xs(c, level='config').mean():.1f} %")

print("\n== 45 grados como % de horizontal (articulo: 81.4 / 81) ==")
for e in "TCF":
    s = df[df.ensayo == e].groupby(["diseno", "config", "orientacion"]).fmax_N.mean().unstack()
    print(f"   {e}: {(s['D45'] / s['H0'] * 100).mean():.1f} %")

print("\n== G2 vs G1 (articulo: <4 % T y C; <6 % F; C medio 2.3 %) ==")
for e in "TCF":
    s = df[df.ensayo == e].pivot_table(index=["config", "orientacion"], columns="diseno", values="fmax_N")
    d = pct(s["G2"], s["G1"])
    print(f"   {e}: min {d.min():.1f}  max {d.max():.1f}  media(|d|) {d.abs().mean():.1f}  signo medio {d.mean():.1f}")

print("\n== Masa (g): media por configuracion ==")
print(df.groupby("config").peso_g.agg(["mean", "min", "max"]).round(2))
m = df.pivot_table(index=["ensayo", "diseno", "orientacion"], columns="config", values="peso_g")
print("   Estandar vs Fina (masa): ", f"{pct(m['Estandar'], m['Fina']).mean():.1f} % en promedio")
print("   Fuerte vs Fina (masa):   ", f"{pct(m['Fuerte'], m['Fina']).mean():.1f} % en promedio")

print("\n== Eficiencia Fmax/masa (N/g), media por ensayo y config ==")
df["f_por_g"] = df.fmax_N / df.peso_g
print(df.pivot_table(index="ensayo", columns="config", values="f_por_g").round(1))
