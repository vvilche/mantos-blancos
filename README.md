# S/E Mantos Blancos — Dossier Técnico (Capstone Copper)

Dossier de ingeniería de la subestación Mantos Blancos (220/23 kV), Región de Antofagasta,
Chile. Datos extraídos de InfoTecnica CEN (API pública) y documentos del expediente,
leídos con visión (Kimi K3). Generado el 21-08-2026.

## Archivos clave

| Archivo | Qué es |
|---|---|
| `inventario_tecnico.md` | **Dossier principal**: relés, transformadores, switchgear, TC/TP, SSAA, estado normativo |
| `unilineal_limpio.svg` | Unilineal 220/23 kV (T1/T2 + líneas Laberinto/Chacaya) |
| `unilineal_23kv.svg` | Switchgear 23 kV (alimentadores, relés SEPAM) |
| `unilineal_63kv.svg` | MT 6.3 kV + central diésel (10 gensets + molinos) |
| `topo_*.json` / `topologia.json` | Topologías para regenerar los unilineales |
| `diagrama_unilineal.txt` | Texto completo del unilineal oficial (capa de texto del PDF) |
| `analisis/` | Lecturas de visión completas de los planos (Kimi K3) |

## Resumen técnico

### Relés de protección
- 220 kV: ABB REL670 ×4 (líneas) · ABB REB670 (diferencial de barras 87B) ·
  Schneider MiCOM P643 (T1, sist 1) · GE D30 (T1, sist 2) · ION 8690 (facturación)
- 23 kV: Schneider SEPAM 20/25 y 100S (celdas)
- MT 6.3 kV: switchgear legacy (ABB NALF, Brush, Brown Boveri, Siemens) — OCB/ACB/SF6

### Transformadores
- T1: 34/42/50 MVA · 220/23 kV · DYn1 · ABB TMY-44 (ensayos 1995)
- T2: 40 MVA · 220/23 kV · ABB TMY-44
- T3/T4: 13/16/20 MVA · 24/6.6 kV · YnD1 · Rn=66.6 Ω
- Molinos: 37.5 MVA ×2 · 23/6.3 kV
- Trafos menores: 1000–1600 kVA varios

### Generación propia
- 10 grupos diésel G-101..110 de 3850 kVA c/u (~38 MVA de respaldo)

### Estado normativo (InfoTecnica CEN)
- flag_scada = **FALSE** · flag_equipocom = FALSE · centro de control propio
- Completitud 97.8% · **Calidad 54.7%** (45% de datos sin certificar)

### Ángulo CONECTA (por impacto)
1. SCADA inexistente (flag_scada=False) → SCADA + RTU
2. Calidad de datos CEN al 54.7% → EDAC + reporte normativo automático
3. Sin equipo de comunicaciones → red IEC 61850 + conmutadores
4. Expansión Fase II (USD ~89.5M) → automatización nueva

## Cómo regenerar todo

```bash
# 1. Re-descargar documentos del CEN
python3 download.py

# 2. Leer planos con visión (Kimi K3)
python3 read_plans.py

# 3. Regenerar unilineales (skill sld-generator v3)
python3 ~/.hermes/skills/creative/sld-generator/scripts/sld_generator.py \
  --input topo_23kv.json --output unilineal_23kv.svg
```

## Fuentes
- InfoTecnica CEN (API pública): api-infotecnica.coordinador.cl/v1 — subestaciones/1899, centrales/391
- Capstone Copper: capstonecopper.com/operations/mantos-blancos/
- SEA (DIA Fase II): infofirma.sea.gob.cl
- Protocolos ABB TR1/TR2 (ensayos 1995, tipo TMY-44, N° 59421)

## Nota
Los planos son raster de 2019-2020; todo lo "ilegible" quedó marcado explícitamente, nada se inventó.
