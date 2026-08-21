#!/usr/bin/env python3
"""Lee placa de transformadores TR1/TR2 + fecha energizacion con Kimi K3."""
import base64, json, os, urllib.request, yaml

CFG = yaml.safe_load(open(os.path.expanduser("~/.hermes/config.yaml")))
V = CFG["auxiliary"]["vision"]
KEY = V["api_key"]; BASE = V["base_url"]; MODEL = V["model"]

def vision(img, prompt):
    b64 = base64.b64encode(open(img, "rb").read()).decode()
    body = {"model": MODEL, "messages": [{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
        {"type": "text", "text": prompt}]}],
        "reasoning_effort": "low", "max_tokens": 4000}
    req = urllib.request.Request(BASE + "/chat/completions", data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read().decode())
    m = d["choices"][0]["message"]
    return m.get("content") or m.get("reasoning_content") or "(vacio)"

D = os.path.expanduser("~/b2b-sales-system/mantos_blancos/png_auditoria/")
P_TR = ("Extrae TODOS los datos de placa del transformador: fabricante, N de serie, potencia "
        "(MVA), relacion de tension (kV/kV), impedancia (%), grupo de conexion (Dyn, Ynd), "
        "corriente nominal primaria/secundaria, ano de fabricacion, normas, y todo dato tecnico "
        "visible. Si algo no se distingue, di 'ilegible'. No inventes.")

OUT = os.path.expanduser("~/b2b-sales-system/mantos_blancos/analisis")
os.makedirs(OUT, exist_ok=True)

jobs = [
    ("protocolo_tr1_p1-001_small.jpg", P_TR, "placa_TR1.txt"),
    ("protocolo_tr2_p1-001_small.jpg", P_TR, "placa_TR2.txt"),
    ("fecha_energ-1_small.jpg",
     "Extrae la fecha de energizacion/puesta en servicio y todo dato tecnico visible. Di 'ilegible' lo que no se distinga.",
     "fecha_energizacion.txt"),
]

for img, prompt, outname in jobs:
    print("=== " + img, flush=True)
    try:
        txt = vision(D + img, prompt)
        with open(os.path.join(OUT, outname), "w") as f:
            f.write(txt)
        print(txt[:1500])
    except Exception as e:
        print("ERROR:", e)
    print()
