"""Arma citas APA 7 desde los metadatos de Crossref (no desde la lista de la IA). Salida: referencias/referencias_apa_candidatas.md"""
import csv, json, os, re, urllib.request, html
R = os.path.join(os.path.dirname(__file__), "..")
def ini(g):
    return " ".join((p[0] + ".") for p in re.split(r"[ \-]+", g.strip()) if p) if g else ""
def apa(m, doi):
    au = m.get("author", [])
    names = [f"{a.get('family','?').title() if a.get('family','').isupper() else a.get('family','?')}, {ini(a.get('given',''))}".strip().rstrip(",") for a in au]
    if len(names) == 1: s = names[0]
    elif len(names) <= 20: s = ", ".join(names[:-1]) + ", & " + names[-1]
    else: s = ", ".join(names[:19]) + ", . . . " + names[-1]
    yr = m["issued"]["date-parts"][0][0]; rev = html.unescape(m["container-title"][0])
    t = " ".join(html.unescape(m["title"][0]).split()); vol = m.get("volume", ""); num = m.get("issue", ""); pg = m.get("page", m.get("article-number", ""))
    vn = f"*{vol}*" + (f"({num})" if num else "") if vol else ""
    pg = pg.replace("-", "–") if pg else ""
    return f"{s} ({yr}). {t}. *{rev}*, {vn}{', ' + pg if pg else ''}. https://doi.org/{doi}"
rows = list(csv.DictReader(open(os.path.join(R, "referencias", "crossref_resultados.csv"), encoding="utf-8")))
out = []
for r in rows:
    m = json.load(urllib.request.urlopen(urllib.request.Request("https://api.crossref.org/works/" + r["doi"], headers={"User-Agent": "seminario-verificacion/1.0"}), timeout=30))["message"]
    out.append((apa(m, r["doi"]), len(m.get("author", []))))
# estudio sin DOI en la lista (mdpi.com/2673-3161/6/1/17)
try:
    q = "Sensitivity analysis of 3D printing parameters on mechanical properties of fused deposition modeling-printed polylactic acid parts"
    it = json.load(urllib.request.urlopen(urllib.request.Request("https://api.crossref.org/works?rows=2&query.bibliographic=" + urllib.parse.quote(q), headers={"User-Agent": "seminario-verificacion/1.0"}), timeout=30))["message"]["items"]
    for m in it: print("CANDIDATO sin DOI:", m["DOI"], "|", m["title"][0][:90], "|", m["issued"]["date-parts"][0][0], "|", m.get("container-title", ["?"])[0])
except Exception as e:
    print("sin DOI:", e)
with open(os.path.join(R, "referencias", "referencias_apa_candidatas.md"), "w", encoding="utf-8") as fh:
    fh.write("# Referencias candidatas (APA 7, datos tomados de Crossref el 2026-11-09)\n\nTodas: el DOI resuelve y el titulo coincide con la lista propuesta. **No agregar al articulo hasta citarlas en el texto y abrir el PDF** (clase 6, pasos 2 y 3). Orden alfabetico por primer apellido al incorporarlas.\n\n")
    for a, n in sorted(out, key=lambda x: x[0].lower()):
        fh.write(f"- {a}\n")
print("ok", len(out))
