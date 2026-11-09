# Cifras del artículo que NO coinciden con sus propias tablas

Recalculado con `scripts/02_verificar_cifras.py` sobre `datos/resultados.csv` (54 probetas, transcritas de las Tablas 4–9).
Antes de entregar hay que corregir el texto (o las tablas, si hubo error de transcripción). La rúbrica pide que «las cifras coincidan».

| # | Afirmación del artículo | Lo que dan las tablas | Acción |
|---|---|---|---|
| 1 | Fuerte supera a Fina en **65,8 %** (tensión) | 62,8 % (media de incrementos) / 63,7 % (incremento de medias) | Corregir |
| 2 | … **67,4 %** (compresión) | 68,7 % | Corregir |
| 3 | … **62,3 %** (flexión) | 71,3 % / 69,6 % | Corregir (error grande) |
| 4 | Estándar supera a Fina en **12–18 %** | T: 8,3–14,6 %; C: 9,9–10,8 %; F: 10,3–12,9 % | Corregir rango |
| 5 | Flexión: Fuerte +**64,2 %** sobre Fina en horizontal (nota Tabla 8) | G1: 64,2 % ✔; G2: 63,7 % | Aclarar que es solo G1 |
| 6 | Tensión, horizontal vs vertical: **64,2 %** (Fina) y **79,1 %** (Fuerte) | H sobre V: 65,5 % (Fina), 78,2 % (Fuerte) | Corregir y fijar la definición (ver nota) |
| 7 | Conclusiones: H supera a V en **64 %** (T), **22 %** (C), **73 %** (F) | T 72,2 %; C 24,0 %; F 82,2 % (H sobre V) | Corregir |
| 8 | 45° = **81,4 %** de la horizontal en todos los casos | T 79,9 %; **C 90,5 %**; F 79,6 % | Corregir; compresión es la excepción |
| 9 | G1 vs G2 «menos del 4 %» en T y C | T: 3,5–5,1 %; C: 2,2–3,5 % | Corregir T |
| 10 | G2 «ligeramente superior» solo en flexión | G2 > G1 en **T** (+4,4 %) y **F** (+5,1 %); en **C** G2 < G1 (−2,9 %) | Corregir (el signo en C se omite) |
| 11 | Nota Tabla 7: diferencia media en C de 2,3 % | 2,9 % | Corregir |

**Nota sobre «X % mayor» vs «X % menor».** Si H = 112,7 N y V = 68,4 N, H es 64,8 % mayor que V, pero V es 39,3 % menor que H. El artículo mezcla ambas lecturas sin decir cuál usa. Hay que elegir una y declararla.

## Cosas que las tablas muestran y el artículo no dice

1. **Masa.** Fuerte pesa 9,07 g frente a 4,33 g de Fina (+109 %), pero la fuerza sube ~63–71 %. La resistencia **por gramo** es *menor* en Fuerte en los tres ensayos (T 16,6 vs 21,1 N/g; C 29,5 vs 36,7; F 8,7 vs 10,7). La conclusión «Fuerte es la mejor» es cierta solo en valor absoluto. Esto está en la Figura 2 del artículo (`figuras/fig2_eficiencia.png`).
2. **Estándar pesa 25 % más que Fina** (5,43 g vs 4,33 g) con el mismo infill y las mismas paredes; solo cambia la altura de capa (0,20 vs 0,12 mm). Eso es físicamente raro: ¿se imprimió con otro flujo, soportes o parámetros no declarados? Hay que explicarlo o la comparación Fina–Estándar no es limpia.
3. **n = 1 por condición.** Cada celda es una sola probeta, sin réplicas, así que no se puede calcular desviación ni hacer ANOVA. Todo el análisis es descriptivo. Debe declararse como limitación y no hablar de «significativo» ni de «determinante estadísticamente».
4. **Factores confundidos.** «Fuerte» cambia a la vez infill (15→25 %), paredes (2→5), patrón (cúbico→giroide) y masa. No se puede atribuir el efecto a las paredes o al giroide por separado. La Discusión lo hace («las paredes y el giroide son los factores con mayor incidencia… por encima de infill y altura de capa»); esa frase no está respaldada por el diseño.
5. **«Taguchi L27».** El diseño real es 3 configuraciones × 3 orientaciones × 2 geometrías × 3 ensayos. No es un L27 de factores independientes.
6. **Deformación en tensión** medida «por celda de carga y manual»: el protocolo no dice cómo se midió el desplazamiento. Declarar la incertidumbre del método.
7. **Contradicción con el marco teórico:** dice que más paredes aporta más que más infill (23 % vs 8,7 %), y luego atribuye la mejora a ambos a la vez sin separarlos.
