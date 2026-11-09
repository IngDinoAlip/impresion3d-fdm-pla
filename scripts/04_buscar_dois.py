"""Busca candidatos en Crossref y los imprime para verificacion humana (no escribe nada en el poster)."""
import sys, json, urllib.parse, urllib.request
qs = [
 "Alafaghani Qattawi Alrawi Guzman experimental optimization of fused deposition modelling processing parameters 2017",
 "Al-Tamimi definitive screening design tough PLA tensile flexural compressive layer height wall infill 2023",
 "Rivera-Lopez PLA extrusion temperature mechanical properties 180 260 fused filament fabrication 2024",
 "Fekiac infill density gyroid cubic rectilinear PLA tensile DMA SEM 2025",
 "Chokshi Shah Patel PLA layer height infill geometry perimeters tensile flexural",
]
for q in qs:
    u = "https://api.crossref.org/works?rows=3&select=DOI,title,author,issued,container-title,volume,page&query.bibliographic=" + urllib.parse.quote(q)
    d = json.load(urllib.request.urlopen(u, timeout=30))["message"]["items"]
    print("##", q[:70])
    for m in d:
        a = ", ".join(x.get("family", "?") for x in m.get("author", [])[:4])
        print("  ", m["DOI"], "|", (m.get("title") or ["?"])[0][:95], "|", a, "|", m["issued"]["date-parts"][0][0], "|", (m.get("container-title") or ["?"])[0][:40])
