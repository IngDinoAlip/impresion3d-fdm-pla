"""Transcribe las Tablas 4-9 del articulo (seminario_final) a un CSV tidy.
Fuente: annotated-articulo_seminario_final.pdf, pags. 7-10. 54 probetas = 3 ensayos x 2 disenos x 3 configs x 3 orientaciones.
Cada fila es UNA probeta (n = 1 por condicion)."""
import csv, os

OUT = os.path.join(os.path.dirname(__file__), "..", "datos", "resultados.csv")

CONF = ["Fina", "Estandar", "Fuerte"]
ORI = ["V90", "H0", "D45"]  # orden de las tablas: vertical, horizontal, 45

# (Fmax N, deformacion mm, peso g) en orden Fina(V,H,45), Estandar(V,H,45), Fuerte(V,H,45)
D = {
    ("T", "G1"): [(68.4, 1.2, 4.1), (112.7, 2.8, 4.3), (89.3, 2.1, 4.2),
                  (74.1, 1.4, 5.2), (128.5, 3.1, 5.4), (101.9, 2.5, 5.3),
                  (104.6, 2.0, 8.7), (187.3, 4.6, 9.1), (152.4, 3.8, 8.9)],
    ("T", "G2"): [(71.2, 1.3, 4.4), (118.4, 2.9, 4.6), (93.1, 2.2, 4.5),
                  (77.8, 1.5, 5.5), (134.2, 3.3, 5.7), (106.7, 2.7, 5.6),
                  (109.3, 2.2, 9.0), (193.8, 4.8, 9.4), (158.1, 4.0, 9.2)],
    ("C", "G1"): [(143.6, 3.1, 4.2), (178.2, 3.8, 4.3), (161.4, 3.4, 4.2),
                  (158.7, 3.5, 5.3), (196.5, 4.2, 5.4), (177.3, 3.8, 5.3),
                  (241.8, 5.7, 8.8), (298.4, 6.9, 9.1), (271.2, 6.3, 9.0)],
    ("C", "G2"): [(138.9, 2.9, 4.3), (172.5, 3.6, 4.5), (155.8, 3.2, 4.4),
                  (153.4, 3.3, 5.4), (191.2, 4.0, 5.6), (172.6, 3.7, 5.5),
                  (235.3, 5.5, 9.0), (291.7, 6.7, 9.3), (264.9, 6.1, 9.2)],
    ("F", "G1"): [(31.4, 4.2, 4.1), (58.7, 8.6, 4.3), (46.2, 6.8, 4.2),
                  (34.8, 4.7, 5.2), (66.3, 9.4, 5.4), (52.1, 7.5, 5.3),
                  (56.9, 7.8, 8.8), (96.4, 14.2, 9.1), (78.3, 11.6, 8.9)],
    ("F", "G2"): [(33.1, 4.4, 4.3), (61.8, 8.9, 4.6), (48.7, 7.1, 4.5),
                  (36.5, 4.9, 5.4), (69.4, 9.8, 5.7), (54.8, 7.8, 5.5),
                  (59.7, 8.1, 9.1), (101.2, 14.8, 9.4), (82.1, 12.0, 9.2)],
}


def falla(ens, conf, ori):
    if ens == "T":
        return {"V90": "Delaminacion parcial" if conf == "Fuerte" else "Delaminacion fragil",
                "H0": "Fractura ductil", "D45": "Fractura diagonal"}[ori]
    if ens == "C":
        if conf == "Fuerte":
            return "Aplastamiento progresivo"
        return {"V90": "Colapso por pandeo", "H0": "Fractura transversal", "D45": "Fractura diagonal"}[ori]
    return {"V90": "Delaminacion parcial" if conf == "Fuerte" else "Delaminacion intercapa",
            "H0": "Fractura en fibra inferior", "D45": "Fractura oblicua"}[ori]


PARAM = {"Fina": (15, 2, 0.12, "Cubico"), "Estandar": (15, 2, 0.20, "Cubico"), "Fuerte": (25, 5, 0.20, "Giroide")}

rows = []
for (ens, dis), vals in D.items():
    i = 0
    for c in CONF:
        for o in ORI:
            f, d, p = vals[i]; i += 1
            infill, paredes, capa, patron = PARAM[c]
            rows.append(dict(id=f"{ens}-{dis}-{c[:3].upper()}-{o}", ensayo=ens, diseno=dis, config=c,
                             orientacion=o, infill_pct=infill, paredes=paredes, capa_mm=capa, patron=patron,
                             fmax_N=f, deform_mm=d, peso_g=p, falla=falla(ens, c, o)))
assert len(rows) == 54
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print("filas:", len(rows), "->", os.path.abspath(OUT))
