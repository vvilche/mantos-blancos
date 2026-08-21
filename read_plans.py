#!/usr/bin/env python3
"""Lee los unilineales de Mantos Blancos con Kimi K3 (Moonshot) via API directa."""
import base64, json, os, urllib.request, yaml

CFG = yaml.safe_load(open(os.path.expanduser("~/.hermes/config.yaml")))
VISION = CFG["auxiliary"]["vision"]
KEY = VISION["api_key"]
BASE = VISION.get("base_url", "https://api.moonshot.ai/v1")
MODEL = VISION.get("model", "kimi-k3")

PNG_DIR = os.path.expanduser("~/b2b-sales-system/mantos_blancos/png")
OUT_DIR = os.path.expanduser("~/b2b-sales-system/mantos_blancos/analisis")
os.makedirs(OUT_DIR, exist_ok=True)

PLANS = [
    "SE_Anexo_1_Diagrama_Unilineal_General_SE_Mantos_Blancos-1.png",
    "SE_Anexo_1_Diagrama_Unilineal_SE_Mantos_Blancos_220_kV-1.png",
    "SE_Anexo_1_Diagrama_Unilineal_SE_Mantos_Blancos_Switchgear_23kV-1.png",
    "SE_Anexo_4_Diagrama_Unilineal_SSAA_Vca-1.png",
    "SE_Anexo_4_Diagrama_Unilineal_SSAA_Vcc-1.png",
    "TER_Unilineal_Mantos_Blancos_-_Esquematico_Rev1-1.png",
    "TER_Unifilar_Mantos_Blancos-1.png",
]

PROMPT = (
    "Eres ingeniero de protecciones y automatización de subestaciones. Extrae del diagrama "
    "unilineal TODOS los datos técnicos legibles, en español, estructurado:\n"
    "1) Niveles de tensión y barras (kV).\n"
    "2) Relés de protección: código ANSI (50/51/87/21/59/27/81/63/86...), marca y modelo EXACTO "
    "(SEL, ABB REL/REB/REC, Siemens 7SJ/7UT/7SA/7SL, GE/Multilin, Schneider MiCOM, etc.).\n"
    "3) Transformadores de poder: potencia MVA, relación (kV/kV), grupo de conexión.\n"
    "4) Interruptores: marca, modelo, tensión, corriente.\n"
    "5) Transformadores de medida TC/TP: relación y clase de precisión.\n"
    "6) Comunicaciones: IEC 61850, GOOSE, MMS, protocolos.\n"
    "7) Seccionadores, pararrayos, bancos de condensadores, reactores si aparecen.\n"
    "8) Número de plano y revisión.\n"
    "Regla: si algo NO se distingue con claridad, escribe 'ilegible' para ese dato. NO inventes "
    "marcas, modelos ni relaciones. Sé exhaustivo con los códigos y valores que sí leas."
)

def call_vision(png_path):
    b64 = base64.b64encode(open(png_path, "rb").read()).decode()
    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            {"type": "text", "text": PROMPT},
        ]}],
        "reasoning_effort": "low",
        "max_tokens": 6000,
    }
    req = urllib.request.Request(
        BASE + "/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode())

for name in PLANS:
    path = os.path.join(PNG_DIR, name)
    out = os.path.join(OUT_DIR, name.replace(".png", ".txt"))
    if os.path.exists(out) and os.path.getsize(out) > 200:
        print(f"=== skip (ya existe) {name}", flush=True)
        continue
    print(f"=== Leyendo {name} ...", flush=True)
    try:
        d = call_vision(path)
        msg = d["choices"][0]["message"]
        content = msg.get("content") or ""
        if not content.strip():
            content = msg.get("reasoning_content") or "(sin contenido)"
        with open(out, "w") as f:
            f.write(content)
        print(f"    -> OK ({len(content)} chars) -> {out}")
    except Exception as e:
        print(f"    -> ERROR: {e}")

print("\nListo.")
