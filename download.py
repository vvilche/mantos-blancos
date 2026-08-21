#!/usr/bin/env python3
"""Descarga TODOS los documentos de Mantos Blancos desde InfoTecnica CEN."""
import json, os, re, urllib.request

BASE = "https://api-infotecnica.coordinador.cl/v1"
OUT = os.path.expanduser("~/b2b-sales-system/mantos_blancos/docs")
os.makedirs(OUT, exist_ok=True)

TARGETS = [
    ("subestaciones", 1899, "SE"),
    ("centrales", 391, "TER"),
]

def get_json(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.loads(r.read().decode())

def sanitize(name):
    name = re.sub(r"[^\w\-]+", "_", name, flags=re.UNICODE)
    return name.strip("_")

manifest = []
for tipo, iid, pref in TARGETS:
    docs = get_json(f"{BASE}/{tipo}/{iid}/documentos/?format=json")
    docs = docs.get("results", docs) if isinstance(docs, dict) else docs
    for d in docs:
        doc_id = d.get("id")
        nombre = d.get("nombre") or f"doc_{doc_id}"
        ext = (d.get("extension") or "").lstrip(".").lower()
        if not doc_id:
            continue
        fname = f"{pref}_{sanitize(nombre)}.{ext}"
        path = os.path.join(OUT, fname)
        url = f"{BASE}/{tipo}/{iid}/documentos/{doc_id}/"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if len(data) == 0:
                print(f"  [VACIO] {fname}")
                continue
            with open(path, "wb") as f:
                f.write(data)
            print(f"  [OK {len(data)//1024}KB] {fname}")
            manifest.append({"file": fname, "bytes": len(data), "ext": ext, "tipo": tipo})
        except Exception as e:
            print(f"  [ERROR] {fname}: {e}")

with open(os.path.join(OUT, "_manifest.json"), "w") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\nDescargados: {len(manifest)} archivos en {OUT}")
