# Impresión 3D — Parámetros FDM y diseño generativo en PLA (Seminario de Investigación, Universidad Ean)

Autora: Alisson Dayana Navarro Rodriguez (única autora). Formato objetivo: plantilla IMRyD del seminario (clase 7) + póster A1.

```
datos/        resultados.csv (54 probetas, Tablas 4-9), resumen_por_condicion.csv
scripts/      01_crear_csv.py -> 02_verificar_cifras.py -> 03_figuras.py
figuras/      fig1_fmax_poster.png (protagonista), fig2_eficiencia.png, fig3_anisotropia.png
articulo/     00_discrepancias_cifras.md  <- leer primero
              01_esqueleto_articulo.md    (estructura; los párrafos los escriben ustedes)
              02_propuesta_diseno_experimental.md
              articulo.tex / articulo.pdf  <- MAQUETA con recuadros \pendiente{} para los parrafos; tabla2.tex generada
poster/       poster.tex / poster.pdf (A1 vertical, compilar con latexmk -pdf)
referencias/  referencias_verificadas.md
fuentes/      (no copiadas) PDFs en Descargas: annotated-articulo_seminario_final, deep-research-report, clase6/7, modelos
```

Reproducir: `cd scripts && python 01_crear_csv.py && python 02_verificar_cifras.py && python 03_figuras.py` y luego `cd ../poster && latexmk -pdf poster.tex`.

Pendiente: plantillas oficiales (.docx / .tex) de Canvas, URL para el QR, 28+ referencias verificadas, texto del póster en sus propias palabras (800–1000 palabras; hoy ~430), medir Turnitin antes de entregar.
