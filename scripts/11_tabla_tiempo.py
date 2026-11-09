"""Inserta en articulo.tex (IV.4) la Tabla de tiempo/filamento y la Figura con las dos capturas de Creality Print.
Valores leidos de las capturas: A = 48m19s, 6.77 g, 2.27 m, soportes 9m53s (20.5 %), recorrido 11m37s (23.0 %);
B = 23m22s, 5.54 g, 1.86 m, soportes 3m49s (16.3 %), recorrido 4m7s (17.7 %)."""
import os
from PIL import Image
R = os.path.join(os.path.dirname(__file__), "..")
BASE = os.path.join(os.environ["LOCALAPPDATA"], "Temp", "claude", "84beba65ce5d728b", "582edc10-6acf-46b5-a0f8-41d2bf303ad6", "images")
for n, d in (("16", "lam_a"), ("17", "lam_b")):
    Image.open(os.path.join(BASE, n + ".png")).convert("RGB").save(os.path.join(R, "articulo", "anexo", d + ".jpg"), quality=90)

BLOQUE = r"""\pendiente{Tiempo de impresión}{Escribir 2--3 frases sobre la diferencia de tiempo y filamento entre las dos vistas (Tabla~\ref{tab:tiempo}, Figura~\ref{fig:tiempo}) y confirmar a qué orientación y configuración corresponde cada una (¿misma pieza y misma configuración?). El tiempo no está en las Tablas 4--9 del documento original: si hay más capturas, se puede completar la tabla.}
\begin{table}[t]
\caption{Tiempo de impresión y consumo de filamento estimados por el laminador}\label{tab:tiempo}
\centering\small
\begin{tabular}{@{}lcc@{}}\toprule
 & Vista (a) & Vista (b)\\\midrule
Orientación & [por confirmar] & [por confirmar]\\
Tiempo de impresión & 48\,min 19\,s & 23\,min 22\,s\\
Masa de filamento (g) & 6{,}77 & 5{,}54\\
Longitud de filamento (m) & 2{,}27 & 1{,}86\\
Soportes (tiempo, \%) & 9\,min 53\,s (20{,}5) & 3\,min 49\,s (16{,}3)\\
Recorrido (tiempo, \%) & 11\,min 37\,s (23{,}0) & 4\,min 7\,s (17{,}7)\\\bottomrule
\end{tabular}\\[2pt]
\footnotesize\textit{Nota.} Elaboración propia con datos de la vista previa del código G en Creality Print (Figura~\ref{fig:tiempo}). Con los valores de la tabla, la vista (a) requiere 107\,\% más tiempo, 22\,\% más masa y 22\,\% más longitud de filamento que la (b).
\end{table}
\begin{figure*}[t]
\centering
\begin{subfigure}[t]{0.38\textwidth}\centering\includegraphics[width=\linewidth]{anexo/lam_a.jpg}\caption{}\end{subfigure}\hfill
\begin{subfigure}[t]{0.38\textwidth}\centering\includegraphics[width=\linewidth]{anexo/lam_b.jpg}\caption{}\end{subfigure}
\caption{Vista previa del código G en Creality Print para dos orientaciones de la misma pieza.}\label{fig:tiempo}
\par\footnotesize\textit{Nota.} Captura de pantalla de Creality Print (impresora Creality Hi 0.4 nozzle). Se muestran el tiempo de impresión, la masa y la longitud de filamento y el reparto del tiempo por tipo de línea.
\end{figure*}"""

p = os.path.join(R, "articulo", "articulo.tex")
L = open(p, encoding="utf-8").read().split("\n")
if not any("tab:tiempo" in l for l in L):
    i = [k for k, l in enumerate(L) if l.startswith("La comparación de masa y fuerza máxima por unidad")]
    assert len(i) == 1
    L[i[0] + 1:i[0] + 1] = BLOQUE.split("\n")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(L))
print("ok")
