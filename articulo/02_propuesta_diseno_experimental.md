# Propuesta de diseño experimental (de `deep-research-report.md`) — para la Metodología y las líneas futuras

Lo que hay hoy: 3 configuraciones agrupadas × 3 orientaciones × 2 geometrías × 3 ensayos = 54 probetas, **n = 1** por celda. Ese diseño no es un Taguchi L27 y confunde cuatro parámetros dentro de «Fina/Estándar/Fuerte». Dos caminos:

**A. Declarar lo que es** (si no hay tiempo de reimprimir): estudio descriptivo comparativo de tres «paquetes» de parámetros. Quitar «Taguchi L27» del título, resumen y metodología; no atribuir efectos a paredes/giroide por separado; declarar n = 1 y ensayo manual como limitaciones.

**B. Rediseñar** (líneas futuras o segunda fase), en este orden:
1. Cribado con 7 factores a 3 niveles (L27 real, columnas asignadas antes de imprimir y alias verificado): densidad 20/50/80 %, patrón (rectilíneo/giroide/cúbico), paredes 2/4/6, capa 0,12/0,20/0,28 mm, velocidad 30/50/70 mm/s, temperatura 200/215/230 °C, orientación 0/45/90°. n = 3 réplicas por corrida.
2. Factorial completo 3³ sobre los 3 factores dominantes, n = 3.
3. Probetas ASTM D638 / D790 / D695 aparte de las piezas generativas; en las generativas reportar fuerza de falla, rigidez y fuerza/masa, no «MPa».
4. Aleatorizar el orden y bloquear por cama de impresión.

Análisis: ANOVA multifactorial (α = 0,05, η² parcial, IC 95 %), regresión de 2.º orden, Tukey, función de deseabilidad. Con n = 1 nada de esto es posible hoy.
