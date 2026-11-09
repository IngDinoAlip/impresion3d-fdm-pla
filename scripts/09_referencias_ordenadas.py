"""Une las 6 referencias del articulo + 24 nuevas (ya verificadas por la autora) y las ordena alfabeticamente (APA 7).
Metadatos desde Crossref. Titulos pasados a 'sentence case' (APA 7) protegiendo siglas. Salida:
  articulo/referencias.tex   (bibliografia para \\input)
  referencias/referencias_ordenadas.md"""
import csv, json, os, re, unicodedata, urllib.request, urllib.parse, html

R = os.path.join(os.path.dirname(__file__), "..")
UA = {"User-Agent": "seminario-verificacion/1.0"}
DOIS = [r["doi"] for r in csv.DictReader(open(os.path.join(R, "referencias", "crossref_resultados.csv"), encoding="utf-8"))]
DOIS.append("10.3390/applmech6010017")
PROTEGER = {"Archimedean"}
# apellidos tal como los usa cada autor al citarse (la lista de la autora los traia asi)
AUTOR_OVERRIDE = {"10.1155/2022/5490831": "Medibew, T. M.",
                  "10.1016/j.matpr.2022.05.312": "Ambati, S. S., & Ambatipudi, R."}


def get(doi):
    req = urllib.request.Request("https://api.crossref.org/works/" + doi, headers=UA)
    return json.load(urllib.request.urlopen(req, timeout=30))["message"]


def iniciales(g):
    return " ".join(p[0].upper() + "." for p in re.split(r"[ \-]+", g.strip()) if p) if g else ""


def sentence_case(t):
    t = " ".join(html.unescape(t).split())
    pal = t.split(" ")
    if sum(1 for w in pal if w[:1].isupper() or w[:1].isdigit()) < 0.5 * len(pal):   # ya viene en sentence case
        return t
    out, inicio = [], True
    for w in pal:
        partes = re.split(r"([\-–])", w)
        nuevo = []
        for i, p in enumerate(partes):
            if p in "-–" or not p: nuevo.append(p); continue
            letras = re.sub(r"[^A-Za-z]", "", p)
            if (len(letras) >= 2 and letras.isupper()) or re.search(r"\d", p) or p.strip(",.:") in PROTEGER:
                nuevo.append(p)
            elif inicio and i == 0:
                nuevo.append(p[:1].upper() + p[1:].lower())
            else:
                nuevo.append(p.lower())
        w2 = "".join(nuevo); out.append(w2)
        inicio = w2.endswith(":") or w2.endswith("—")
    return " ".join(out)


def autores(m, doi):
    if doi in AUTOR_OVERRIDE: return AUTOR_OVERRIDE[doi]
    nombres = []
    for a in m.get("author", []):
        fam = a.get("family", "?")
        if fam.isupper(): fam = fam.title()
        nombres.append(f"{fam}, {iniciales(a.get('given', ''))}".rstrip(", "))
    if not nombres: return "[AUTORES]"
    if len(nombres) == 1: return nombres[0]
    if len(nombres) <= 20: return ", ".join(nombres[:-1]) + ", & " + nombres[-1]
    return ", ".join(nombres[:19]) + ", . . . " + nombres[-1]


def entrada(doi):
    m = get(doi)
    yr = m["issued"]["date-parts"][0][0]
    rev = html.unescape(m["container-title"][0]); vol = m.get("volume", ""); num = m.get("issue", "")
    pg = (m.get("page") or m.get("article-number") or "").replace("-", "–")
    t = sentence_case(m["title"][0]); au = autores(m, doi)
    clave_forzada = {"10.1155/2022/5490831": "medibew", "10.1016/j.matpr.2022.05.312": "ambati"}.get(doi)
    return dict(clave=clave_forzada or unicodedata.normalize("NFKD", (m["author"][0]["family"] if m.get("author") else "zzz")).encode("ascii", "ignore").decode().lower().replace(" ", "").replace("-", ""),
                anio=yr, au=au, t=t, rev=rev, vol=vol, num=num, pg=pg, doi=doi)


FIJAS = [  # las 6 que ya estaban en el articulo (cita APA ya revisada)
    dict(clave="alafaghani", anio=2017, au="Alafaghani, A., Qattawi, A., Alrawi, B., & Guzman, A.", t="Experimental optimization of fused deposition modelling processing parameters: A design-for-manufacturing approach", rev="Procedia Manufacturing", vol="10", num="", pg="791–803", doi="10.1016/j.promfg.2017.07.079"),
    dict(clave="altamimi", anio=2023, au="Al-Tamimi, A. A., Pandžić, A., & Kadrić, E.", t="Investigation and prediction of tensile, flexural, and compressive properties of tough PLA material using definitive screening design", rev="Polymers", vol="15", num="20", pg="4169", doi="10.3390/polym15204169"),
    dict(clave="chacon", anio=2017, au="Chacón, J. M., Caminero, M. A., García-Plaza, E., & Núñez, P. J.", t="Additive manufacturing of PLA structures using fused deposition modelling: Effect of process parameters on mechanical properties and their optimal selection", rev="Materials & Design", vol="124", num="", pg="143–157", doi="10.1016/j.matdes.2017.03.065"),
    dict(clave="tymrak", anio=2014, au="Tymrak, B. M., Kreiger, M., & Pearce, J. M.", t="Mechanical properties of components fabricated with open-source 3-D printers under realistic environmental conditions", rev="Materials & Design", vol="58", num="", pg="242–246", doi="10.1016/j.matdes.2014.02.038"),
]
AUTODESK = [
    dict(clave="autodesk", anio=0, sufijo="a", au="Autodesk", t="Preserve geometry", rev="Autodesk Fusion Help", url="https://help.autodesk.com/cloudhelp/ENU/Fusion-GenerativeDesign/files/GD-PRESERVE-GEOM.htm"),
    dict(clave="autodesk", anio=0, sufijo="b", au="Autodesk", t="Specify objectives in the Generative Design workspace", rev="Autodesk Fusion Help", url="https://help.autodesk.com/view/fusion360/ENU/?contextId=GD-SPECIFY-OBJECTIVES"),
]
items = list(FIJAS) + [entrada(d) for d in DOIS] + list(AUTODESK)
items.sort(key=lambda e: (e["clave"], e["anio"], e.get("sufijo", "")))


def esc(s): return s.replace("&", r"\&")


def tex(e):
    if "url" in e:
        return f"{esc(e['au'])}. (s.~f.-{e['sufijo']}). \\textit{{{esc(e['t'])}}}. {esc(e['rev'])}. \\url{{{e['url']}}}\\par"
    vn = f"\\textit{{{e['vol']}}}" + (f"({e['num']})" if e["num"] else "") if e["vol"] else ""
    return f"{esc(e['au'])} ({e['anio']}). {esc(e['t'])}. \\textit{{{esc(e['rev'])}}}, {vn}{', ' + e['pg'] if e['pg'] else ''}. \\url{{https://doi.org/{e['doi']}}}\\par"


def md(e):
    if "url" in e: return f"{e['au']}. (s. f.-{e['sufijo']}). *{e['t']}*. {e['rev']}. {e['url']}"
    vn = f"*{e['vol']}*" + (f"({e['num']})" if e["num"] else "") if e["vol"] else ""
    return f"{e['au']} ({e['anio']}). {e['t']}. *{e['rev']}*, {vn}{', ' + e['pg'] if e['pg'] else ''}. https://doi.org/{e['doi']}"


with open(os.path.join(R, "articulo", "referencias.tex"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(tex(e) for e in items) + "\n")
with open(os.path.join(R, "referencias", "referencias_ordenadas.md"), "w", encoding="utf-8") as fh:
    fh.write("# Referencias ordenadas (APA 7, orden alfabético) — %d\n\n" % len(items))
    for e in items: fh.write("- " + md(e) + "\n")
for i, e in enumerate(items, 1):
    print(f"{i:>2}. {e['au'][:34]:<34} {e['anio'] or 's.f.'} | {e['t'][:80]}")
