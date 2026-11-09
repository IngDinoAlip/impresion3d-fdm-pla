"""Empaqueta STLs binarios para el visor 3D del sitio (sitio/modelos.json) y los copia a modelos/.
Soldadura de vertices + posiciones en uint16 (cuantizadas al bbox) + indices uint16. Sin normales: el visor sombrea por faceta.
Uso: python 13_modelo3d.py [ruta.stl "Nombre visible"] ...   (por defecto: Downloads/compresion1.stl)"""
import base64, json, os, shutil, struct, sys
import numpy as np

R = os.path.join(os.path.dirname(__file__), "..")
args = sys.argv[1:] or [os.path.join(os.environ["USERPROFILE"], "Downloads", "compresion1.stl"), "Compresión · alternativa 1"]
DT = np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")])


def pad4(b): return b + b"\x00" * (-len(b) % 4)


def empaquetar(path, nombre):
    raw = open(path, "rb").read()
    n = struct.unpack("<I", raw[80:84])[0]
    assert 84 + 50 * n == len(raw), "no es un STL binario"
    t = np.frombuffer(raw, dtype=DT, count=n, offset=84)["v"].astype(np.float64)         # (n,3,3)
    v = t.reshape(-1, 3)
    clave = np.round(v * 1e4).astype(np.int64)
    uniq, inv = np.unique(clave, axis=0, return_inverse=True)
    pos = uniq / 1e4
    idx = inv.reshape(-1).reshape(-1, 3)
    assert len(pos) < 65536, "demasiados vertices para uint16"
    lo, hi = pos.min(axis=0), pos.max(axis=0)
    q = np.round((pos - lo) / (hi - lo) * 65535).astype("<u2")
    vol = abs(np.einsum("ij,ij->i", t[:, 0], np.cross(t[:, 1], t[:, 2])).sum() / 6) / 1000.0   # cm3
    cab = struct.pack("<6f2I", *lo, *hi, len(pos), n)
    blob = cab + pad4(q.tobytes()) + pad4(idx.astype("<u2").tobytes())
    base = os.path.splitext(os.path.basename(path))[0]
    os.makedirs(os.path.join(R, "modelos"), exist_ok=True)
    shutil.copyfile(path, os.path.join(R, "modelos", base + ".stl"))
    return dict(id=base, name=nombre, file=f"modelos/{base}.stl", mb=round(len(raw) / 1e6, 1),
                dims=[round(float(h - l), 1) for l, h in zip(lo, hi)], tris=int(n), verts=int(len(pos)),
                vol_cm3=round(float(vol), 1), b64=base64.b64encode(blob).decode())


out = [empaquetar(args[i], args[i + 1]) for i in range(0, len(args), 2)]
json.dump(out, open(os.path.join(R, "sitio", "modelos.json"), "w", encoding="utf-8"), ensure_ascii=False)
for m in out:
    print(m["id"], m["dims"], "mm |", m["tris"], "triángulos |", m["verts"], "vértices | volumen", m["vol_cm3"], "cm3 | b64", round(len(m["b64"]) / 1024), "KB")
