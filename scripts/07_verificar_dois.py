"""Consulta Crossref por cada DOI propuesto y guarda los metadatos reales (no confia en lo que diga la lista)."""
import csv, json, os, urllib.request, urllib.error, html
R = os.path.join(os.path.dirname(__file__), "..")
DOIS = """10.3390/polym14050886 10.1155/2022/5490831 10.3390/machines11121086 10.1007/s00339-022-05579-w 10.3390/ma17246076
10.3390/polym17223069 10.1016/j.rinma.2026.100987 10.3390/jmmp10010021 10.20528/cjsmec.2025.04.003 10.3390/polym15122585
10.1007/s40964-023-00487-8 10.1016/j.matpr.2022.05.312 10.3390/ma15155142 10.3390/chemengineering7030046 10.3390/polym18131619
10.3390/app16178538 10.3390/polym16111562 10.3390/ma12233859 10.3390/polym13081239 10.1016/j.cja.2020.09.020
10.1089/3dp.2021.0189 10.1016/j.ifacol.2023.10.307 10.1016/j.procir.2022.02.114""".split()
rows = []
for d in DOIS:
    try:
        req = urllib.request.Request("https://api.crossref.org/works/" + d, headers={"User-Agent": "seminario-verificacion/1.0"})
        m = json.load(urllib.request.urlopen(req, timeout=30))["message"]
        au = "; ".join(f"{a.get('family','?')}, {a.get('given','')}" for a in m.get("author", []))
        yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
        rows.append(dict(doi=d, ok="SI", anio=yr, revista=html.unescape((m.get("container-title") or ["?"])[0]),
                         volumen=m.get("volume", ""), numero=m.get("issue", ""), paginas=m.get("page", m.get("article-number", "")),
                         titulo=html.unescape(" ".join((m.get("title") or ["?"])[0].split())), autores=au))
    except urllib.error.HTTPError as e:
        rows.append(dict(doi=d, ok=f"NO ({e.code})", anio="", revista="", volumen="", numero="", paginas="", titulo="", autores=""))
    except Exception as e:
        rows.append(dict(doi=d, ok="ERR " + str(e)[:40], anio="", revista="", volumen="", numero="", paginas="", titulo="", autores=""))
with open(os.path.join(R, "referencias", "crossref_resultados.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for i, r in enumerate(rows, 1):
    a = r["autores"].split(";")
    print(f"{i:>2} {r['ok']:<6} {r['doi']}\n    {r['anio']} | {r['revista'][:42]} {r['volumen']}({r['numero']}) {r['paginas']}\n    {r['titulo'][:110]}\n    autores({len(a)}): {a[0].strip()}{' ...' if len(a)>1 else ''}")
