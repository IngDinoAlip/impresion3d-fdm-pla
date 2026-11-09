# Orientación y configuración FDM en piezas de PLA con diseño generativo

Estudio experimental del comportamiento mecánico de piezas de PLA diseñadas con el módulo de diseño generativo de Autodesk Fusion 360 y fabricadas por FDM. Seminario de Investigación, Universidad Ean (Facultad de Ingeniería, Bogotá, Colombia), 2026.

**Autora:** Alisson Dayana Navarro Rodríguez · anavarr36555@universidadean.edu.co

## Enlaces

| Recurso | Enlace |
|---|---|
| Sitio interactivo | https://ingdinoalip.github.io/impresion3d-fdm-pla/ |
| Artículo (PDF) | [`articulo/articulo.pdf`](articulo/articulo.pdf) |
| Póster A1 (PDF) | [`poster/poster.pdf`](poster/poster.pdf) |
| Datos de las 54 probetas | [`datos/resultados.csv`](datos/resultados.csv) |

## De qué trata

Se compararon tres configuraciones de impresión *combinadas* (Fina, Estándar y Fuerte), tres orientaciones (0°, 45° y 90°) y dos geometrías generativas (G1 y G2) en ensayos de tensión, compresión y flexión: 54 probetas, una por condición. Se midieron la fuerza máxima, la deformación, la masa y el modo de falla.

| Configuración | Relleno | Paredes | Altura de capa | Patrón |
|---|---|---|---|---|
| Fina | 15 % | 2 | 0,12 mm | Cúbico |
| Estándar | 15 % | 2 | 0,20 mm | Cúbico |
| Fuerte | 25 % | 5 | 0,20 mm | Giroide |

**Resultados principales** (calculados desde `datos/resultados.csv`):

- La configuración Fuerte soporta entre 64 % y 70 % más fuerza máxima que la Fina, según el ensayo.
- Pesa 109 % más (9,1 g frente a 4,3 g), por lo que rinde cerca de 20 % menos fuerza por gramo.
- La orientación horizontal resiste más: la vertical queda 42 % (tensión), 19 % (compresión) y 45 % (flexión) por debajo.

**Alcance.** Es un estudio exploratorio: una probeta por condición y carga manual con celda de carga. Como cada configuración cambia varios parámetros a la vez, los resultados comparan configuraciones completas y no permiten atribuir el efecto al relleno, las paredes o el patrón por separado. Las tendencias requieren replicación con ensayos normalizados (ASTM D638, D695 y D790).

## Materiales y equipos

PLA PolyMaster · impresora Creality Hi Combo · laminado en Creality Print · 215 °C de boquilla y 60 °C de cama · resto de parámetros del perfil predeterminado. Trabajo realizado en las instalaciones de la universidad, en especial el FabLab, sin financiación externa.

## Estructura del repositorio

```
index.html          sitio interactivo (un solo archivo, sin dependencias)
sitio/              plantilla del sitio y modelo 3D empaquetado para el visor
modelos/            las seis geometrías generativas en STL (G1 y G2 de tensión, compresión y flexión)
articulo/           artículo (LaTeX y PDF), tablas generadas, apéndice con las capturas
poster/             póster A1 (LaTeX y PDF) y código QR
datos/              resultados.csv (una fila por probeta) y resumen por condición
figuras/            figuras del artículo y del póster
referencias/        referencias verificadas contra Crossref
scripts/            programas que generan datos, figuras, tablas y el sitio
```

## Reproducir

Requiere Python 3 (con `pandas`, `matplotlib`, `numpy`, `pillow`, `qrcode`) y una distribución de LaTeX (MiKTeX o TeX Live).

```bash
cd scripts
python 01_crear_csv.py        # datos/resultados.csv
python 03_figuras.py          # figuras
python 05_fig_fuerza_masa.py  # figura de fuerza por gramo
python 06_articulo_tabla_fig.py
python 13_modelo3d.py ruta/modelo.stl "Nombre"   # empaqueta un STL para el visor 3D
python 12_sitio.py            # index.html
cd ../articulo && latexmk -pdf articulo.tex
cd ../poster   && latexmk -pdf poster.tex
```

`datos/resultados.csv` tiene las columnas: `id` (ensayo-geometría-configuración-orientación), `ensayo` (T, C, F), `diseno` (G1, G2), `config`, `orientacion` (V90, D45, H0), `infill_pct`, `paredes`, `capa_mm`, `patron`, `fmax_N`, `deform_mm`, `peso_g` y `falla`.

## Cómo citar

Navarro Rodríguez, A. D. (2026). *Influencia de la orientación y los parámetros de impresión FDM en el comportamiento mecánico de piezas de PLA con diseño generativo: estudio experimental*. Universidad Ean. https://github.com/IngDinoAlip/impresion3d-fdm-pla
