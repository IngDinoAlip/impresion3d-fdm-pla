"""Genera articulo/anexo_figuras.tex: Apendice A con TODAS las imagenes del documento original (32).
Agrupadas por tipo de ensayo segun lo confirmado por la autora (p13-p15 = compresion; p16-p20 = tension y flexion)."""
import os
R = os.path.join(os.path.dirname(__file__), "..")
# (titulo, imagenes, nota, alto maximo por imagen como fraccion de \textheight)
G = [
 ("Diseño generativo de la pieza de compresión en Fusion 360: definición de geometrías y cargas, espacio de diseño inicial, alternativas generadas y comparación de resultados.",
  ["p13_0", "p13_1", "p14_0", "p14_1", "p15_0", "p15_1"], "Documento original, páginas 13 a 15.", 0.20),
 ("Diseño generativo de la pieza de flexión en Fusion 360: definición de geometrías y cargas, forma inicial y alternativas generadas.",
  ["p18_1", "p16_0", "p16_1", "p17_0", "p17_1"], "Documento original, páginas 16 a 18.", 0.20),
 ("Diseño generativo de la pieza de tensión en Fusion 360: definición de geometrías y cargas, forma inicial y alternativas generadas.",
  ["p18_0", "p19_0", "p19_1", "p20_0", "p20_1"], "Documento original, páginas 18 a 20.", 0.20),
 ("Vistas de laminado en Creality Print con distintas orientaciones (1 de 3).", ["p21_0", "p22_0", "p23_0", "p24_0"], "Documento original, páginas 21 a 24.", 0.28),
 ("Vistas de laminado en Creality Print con distintas orientaciones (2 de 3).", ["p25_0", "p26_0", "p27_0", "p28_0"], "Documento original, páginas 25 a 28.", 0.28),
 ("Vistas de laminado en Creality Print con distintas orientaciones (3 de 3).", ["p29_0", "p30_0", "p31_0", "p32_0"], "Documento original, páginas 29 a 32.", 0.28),
 ("Distribución de las piezas en la cama de impresión y piezas fabricadas.", ["p33_0", "p33_1", "p34_0", "p34_1"], "Documento original, páginas 33 y 34.", 0.28),
]
L = [
 r"% ---------------- APENDICE A ----------------",
 r"\clearpage",
 r"\onecolumn",
 r"\section*{Apéndice A. Evidencia gráfica del proceso experimental}",
 r"\pendiente{Mencionar en el texto}{Citar el Apéndice A en III.3 y III.4 (p.~ej. «véanse las Figuras A1 a A7») y precisar en qué consisten los «puntos de tensión» definidos en Fusion 360 (¿carga, apoyo o ambos?).}",
 r"\begingroup\setcounter{figure}{0}\renewcommand{\thefigure}{A\arabic{figure}}",
]
for tit, ims, nota, alto in G:
    L.append(r"\begin{figure}[!htbp]\centering")
    for i, k in enumerate(ims):
        sep = r"\hfill" if i % 2 == 0 else r"\par\smallskip"
        L.append(r"\begin{subfigure}[t]{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=%.2f\textheight,keepaspectratio]{anexo/" % alto + k + r".jpg}\end{subfigure}" + sep)
    L.append(r"\caption{" + tit + "}")
    L.append(r"\par\footnotesize\textit{Nota.} Elaboración propia. " + nota)
    L.append(r"\end{figure}")
L.append(r"\endgroup")
with open(os.path.join(R, "articulo", "anexo_figuras.tex"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(L) + "\n")
print("ok")
