"""Construye index.html (sitio interactivo, un solo archivo) incrustando datos/resultados.csv en sitio/plantilla.html."""
import csv, json, os
R = os.path.join(os.path.dirname(__file__), "..")
rows = []
for r in csv.DictReader(open(os.path.join(R, "datos", "resultados.csv"), encoding="utf-8")):
    for k in ("infill_pct", "paredes"): r[k] = int(r[k])
    for k in ("capa_mm", "fmax_N", "deform_mm", "peso_g"): r[k] = float(r[k])
    for a, b in (("Delaminacion", "Delaminación"), ("fragil", "frágil"), ("ductil", "dúctil")): r["falla"] = r["falla"].replace(a, b)
    rows.append(r)
assert len(rows) == 54
tpl = open(os.path.join(R, "sitio", "plantilla.html"), encoding="utf-8").read()
assert "/*DATA*/[]" in tpl
html = tpl.replace("/*DATA*/[]", json.dumps(rows, ensure_ascii=False, separators=(",", ":")))
mp = os.path.join(R, "sitio", "modelos.json")   # generado por 13_modelo3d.py
modelos = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else []
html = html.replace("/*MODELOS*/[]", json.dumps(modelos, ensure_ascii=False, separators=(",", ":")))
open(os.path.join(R, "index.html"), "w", encoding="utf-8", newline="\n").write(html)
print("index.html", round(len(html) / 1024), "KB,", len(rows), "probetas")
