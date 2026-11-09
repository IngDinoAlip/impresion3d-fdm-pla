# Esqueleto del artículo (plantilla IMRyD del seminario) — SOLO ESTRUCTURA

Este documento **no contiene párrafos del artículo**: la clase 7 prohíbe que la IA redacte el texto (Turnitin < 10 %). Aquí está qué debe lograr cada sección, qué datos suyos van allí y qué falta. Los párrafos los escriben ustedes.

Tipo de trabajo: **artículo de investigación experimental** (no revisión). Se adapta el modelo `ejemplo_articulo_modelo.pdf` manteniendo el orden, las extensiones y la forma de tablas/figuras. Todo en párrafos completos, sin viñetas.

Orden recomendado de escritura (clase 7): Metodología → Resultados + tablas y figuras → Discusión → Marco teórico → Introducción → Conclusiones → Resumen/Abstract → Título y palabras clave → Referencias → Declaraciones.

---

## Título
Una línea con: técnica/factor + material + variable de respuesta + tipo de estudio. Hoy es largo y no dice «estudio experimental». Debe incluir: *PLA*, *FDM*, *diseño generativo*, *propiedades mecánicas*.

## Autores
Navarro Rodriguez, Alisson Dayana; Roa Aparicio, Alejandro — Universidad Ean, Facultad de Ingeniería, Bogotá. Un solo correo de correspondencia.

## Resumen (150–250 palabras) y Abstract (150–250)
Cinco piezas: contexto → objetivo → metodología (n, factores, ensayos) → hallazgos **con cifras** → conclusión. Sin citas ni primera persona. Las cifras deben salir de `datos/resumen_por_condicion.csv`, ya corregidas (ver `00_discrepancias_cifras.md`). Palabras clave: 5 ES + 5 EN, coherentes entre sí.

## I. Introducción — 4 párrafos
1. **Contextualización** (80–120 palabras): manufactura aditiva FDM/PLA, con un dato actual y fuente real. Referencias disponibles en el reporte (Tymrak 2014, etc.).
2. **Vacío**: qué falta en la literatura. Candidato: la mayoría de estudios usa probetas normalizadas con máquina universal; pocos ensayan **piezas de diseño generativo** con ensayos accesibles. La frase del vacío debe poder subrayarse.
3. **Justificación**: a quién sirve (entornos académicos con recursos limitados).
4. **Objetivo**: «El objetivo del presente artículo es…». **Debe decir lo mismo que el párrafo 1 de las Conclusiones.**

## II. Marco teórico y conceptual
- **A.** Anisotropía y parámetros en FDM/PLA (orientación, paredes, infill, altura de capa, patrón). Mín. 3 fuentes. Síntesis con dirección, no «según Fulano».
- **B.** Diseño generativo en Fusion 360 y restricciones de manufactura aditiva (preservar/obstáculo, cargas, orientación de construcción).
- **C.** Variables y dimensiones: fuerza máxima, deformación, masa, **fuerza/masa**, tipo de falla, razón de anisotropía. Estas son las columnas de la Tabla 2.
- **Figura 1** (modelo conceptual): parámetros FDM + geometría generativa → porosidad/unión intercapa → respuesta. Hay un diagrama base en el reporte (mermaid).

## III. Metodología — A a E + Tabla 1 + Figura 2
- **A. Tipo de estudio**: experimental, cuantitativo, descriptivo-correlacional. Justificar por qué **no** es factorial ni L27 (o rehacerlo como tal: ver `02_propuesta_diseno_experimental.md`).
- **B. Materiales y equipos**: PLA (marca, lote, diámetro), impresora, slicer (Creality Print + versión), celda de carga, boquilla. **Hoy falta** marca/lote del PLA, modelo de impresora y de celda de carga, velocidades de ensayo.
- **C. Diseño generativo**: objetivo, cargas, restricciones, material, factor de seguridad, ángulo de voladizo, espesor mínimo. Hoy no están los valores.
- **D. Condiciones de impresión**: **Tabla 1** = configuraciones Fina/Estándar/Fuerte (ya existe como Tabla 3 del borrador). Notas: 215 °C, cama 60 °C, velocidad (¿?), flujo (¿?), ventilador (¿?).
- **E. Protocolo de ensayo**: montaje de tensión, compresión y flexión, cómo se midió fuerza y deformación, nº de probetas (54), codificación (T-G1-FIN-V90). **Figura 2** = diagrama del diseño experimental (3 ensayos × 2 geometrías × 3 configuraciones × 3 orientaciones = 54). Los números deben cuadrar.

## IV. Resultados — 3 categorías + Tabla 2
Sin interpretación («demuestra», «por lo tanto», «se recomienda» están prohibidos aquí). Cada cifra con su denominador y fuente (aquí, sus datos).
- **A. Tensión** — Tabla 2 (medias por condición, `datos/resumen_por_condicion.csv`).
- **B. Compresión.**
- **C. Flexión.**
Más una figura (la `fig1_fmax_poster.png` rehecha para columna) y `fig3_anisotropia.png`. Masa y eficiencia: `fig2_eficiencia.png`. Tipos de falla: describirlos por orientación.

## V. Discusión — 5 párrafos
1. Síntesis. 2. Primer hallazgo contrastado con la literatura (anisotropía: Chacón 2017, Rivera-López 2024, etc.). 3. Segundo hallazgo: **fuerza absoluta vs fuerza por gramo** (Fuerte es +109 % de masa). 4. **Limitaciones reales del estudio** (n = 1, factores confundidos, ensayo manual, un solo PLA, ausencia de normas ASTM; no «el tiempo»). 5. Fortalezas verificables.

## VI. Conclusiones — 3 párrafos
Responde el objetivo / aporta / líneas futuras específicas (replicar con ≥ 3 probetas, separar factores con un factorial, ensayar con máquina universal bajo ASTM D638/D790/D695, comparar TPU/PETG).

## VII. Declaraciones
CRediT por iniciales, financiación, conflicto de intereses, disponibilidad de datos (`datos/resultados.csv` en repositorio). **Si usaron IA para estilo, declararlo aquí con la herramienta y el uso exacto.**

## VIII. Referencias — mínimo 30, APA 7, DOI que resuelva
Ver `referencias/`. Las del borrador actual (MDPI 2026, Slicer Guide, EOS, etc.) no son verificables y deben reemplazarse.

## Checklist previo a subir (de la clase 7)
Plantilla oficial · sin viñetas · resumen y abstract 150–250 · 5+5 palabras clave · tablas con título arriba y nota abajo · figuras con título y nota abajo · Turnitin IA < 10 % · objetivo = conclusión 1 · cada tabla/figura mencionada antes de aparecer · Resultados sin interpretación · cifras que cuadran · ≥ 30 referencias, todas citadas, todos los DOI resuelven · limitaciones del estudio, no del equipo.
