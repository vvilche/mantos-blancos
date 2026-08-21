# MANTOS BLANCOS — Inventario Técnico para análisis de Francisco
Fuente: InfoTecnica CEN (documentos descargados) + lectura con visión Kimi K3 de los unilineales.
Fecha: 2026-08-21

═══════════════════════════════════════════════════
1 · RESUMEN DE LA INSTALACIÓN
═══════════════════════════════════════════════════
- S/E MANTOS BLANCOS (SE103) — 220/23 kV, doble alimentación 220 kV
- Cliente libre: Mantos Copper S.A. (ex Anglo American / Minera Mantos Blancos)
- flag_scada = FALSE · flag_equipocom = FALSE · centro de control propio
- Central térmica propia: 10× grupos diésel (MCI) + Fuel Oil
- Completitud CEN 97.8% · Calidad CEN 54.7% (dolor de compliance)

═══════════════════════════════════════════════════
2 · INVENTARIO DE RELÉS (marca / modelo / ANSI)
═══════════════════════════════════════════════════
220 kV — Líneas (Laberinto 70 km + Chacaya 66 km):
  · ABB REL670 ×4 (2 líneas × Sistema 1 y 2)
    ANSI: 21, 79, 25, 50/51, 67N, 68, 50BF
  · ABB REB670 ×1 — Diferencial de barras (87B)

220 kV — Transformador T1 (paño 52-J1, proyecto reemplazo protecciones):
  · Schneider MiCOM P643 (Sistema 1) — 87T, 87N, 59N, 50BF
  · GE D30 (Sistema 2) — 21, 68, 59, 50/51, 50N/51N

Medición / facturación 220 kV:
  · Schneider ION 8690 (facturación)

Switchgear 23 kV (doble barra, sala eléctrica):
  · Schneider SEPAM — SEPAM 20/25 y SEPAM 100S (múltiples celdas)
    ANSI: 50/51, 50G/51G, 67/67N, 50BF, 86, 27/59, 25

═══════════════════════════════════════════════════
3 · TRANSFORMADORES DE PODER
═══════════════════════════════════════════════════
  · T1: 34/42/50 MVA — 220/23 kV — DYn11 (ONAN/ONAF/ONAF = OA/FA/FA)
    Fabricante: ABB (ASEA Brown Boveri) — tipo TMY-44, monofásico, N° 59421
    Normas: ANSI/IEEE C57.12.00-1993, C57.12.90-1993, IEC 76-1976 — ensayos 1995
  · T2: idéntico (34/42/50 MVA — 220/23 kV — ABB TMY-44, N° 59421)
  · 4130-TL-0004 / 4130-TL-0005: 37.5 MVA — 23/6.3 kV — ONAN/ONAF1/ONAF2 (molinos)
    NGR asociados: 200 A 10 s; Rn = 65.6 Ω y 18.2 Ω
  · Trafo N°5: 1000 kVA — 24/6.3 kV
  · Trafos N°3 / N°4 / N°6 / N°7: salidas 23 kV (detalle en plano 18050-01-EE-DU-001)

Fuente adicional (Auditoría V2, RAR): Protocolo TR1/TR2 ABB = informe de ensayos finales
(03/07/1995, Ing. Francisco Bloise, BRABB). Incluye calentamiento, impulso atmosférico,
ruido audible y descargas parciales. Documento Montaje TR2 (42 págs, Feb 2015) + Prueba
Aceite TR2 (17 MB).

═══════════════════════════════════════════════════
4 · INTERRUPTORES / SWITCHGEAR
═══════════════════════════════════════════════════
  · 220 kV: interruptores 52J (Laberinto -04L, Chacaya -02L, T1/acoplamiento J1)
  · 23 kV: celdas SF6 extraíbles — incoming 2500 A / 25 kA, alimentadores 1250 A / 25 kA
  · 6.3 kV (legacy): ABB NALF 6000 V · Siemens 500 MVA 33 kA · Brown Boveri 350 MVA 31.6 kA
    · BRUSH 334 MVA 30.6 kA (concentrador) · BRUSH 350 MVA (central diésel)
  · 7.2 kV: switchgear 630 A SF6
  · Tipos de interruptor en MT: SF-6 (23/7.2/6.3 kV), OCB aceite (400-2000 A), ACB vacío (630-2000 A)

═══════════════════════════════════════════════════
4.5 · CENTRAL TÉRMICA / GENERACIÓN PROPIA
═══════════════════════════════════════════════════
  · 10 grupos diésel: G-101 a G-110 — 3850 kVA c/u (~3.85 MVA) → ~38 MVA total de respaldo
  · T3: 13/16/20 MVA — 24/6.6 kV — YnD1 — Rn = 66.6 Ω
  · T4: 13/16/20 MVA — 24/6.6 kV — YnD1 — Rn = 66.6 Ω
  · Trafos SS/AA: T-1/T-2 1000 kVA · T-3/T-4 1500 kVA
  · Corrección: T2 = 40 MVA (lado 220/23 kV, alimenta barra 23 kV por 52E-4); T1 = 34/42/50 MVA
  · Resistencia de neutro: Rn = 66.6 Ω (T1, T3, T4) · Rn = 18.2 Ω (otros puntos)

═══════════════════════════════════════════════════
5 · TRANSFORMADORES DE MEDIDA (TC / TP)
═══════════════════════════════════════════════════
220 kV:
  · TC línea Laberinto: 1200/5 A
  · TC línea Chacaya: 800/5 A
  · TC 52-J1: 150-300/5-5-5 A (N1 CL0.2 FS5-30VA · N2/N3/N4 5P20-30VA)
  · TC JT1: 150-100/5-5 A (5P20 50VA · 5P20 30VA)
  · TP JT1: 230/√3 → 0.115/√3 → 0.115/√3 (3P-150VA + 0.2-100VA)

23 kV:
  · 1500/5 A (10P20-25VA · 10P20-50VA · 5P20-5VA) · 1250/5 A · 600/5 A · 400/5 A · 50/5 A
  · TP: 23000/√3 → 115/√3 → 115/√3 V (CL1 / CL0.5)

═══════════════════════════════════════════════════
6 · COMUNICACIONES / SCADA
═══════════════════════════════════════════════════
  · "RTU MANTOS BLANCOS" visible en switchgear 23 kV (RTU existente)
  · Sala de comando de la central
  · IEC 61850 / GOOSE / MMS: NO confirmado en los planos (ilegible) → probablemente
    telecontrol serial/convencional, sin bus de proceso
  · Protocolo de sincronismo: panel sincronización 220V, chequeo sincronismo (25)

═══════════════════════════════════════════════════
6.5 · SERVICIOS AUXILIARES (SS/AA)
═══════════════════════════════════════════════════
  C.A. (380/220 V) — Tablero 852-5240-010, 400 A, 10 kA:
  · Transferencia automática 52SA1 / 52SA2 (400 A) + panel 852-5240-050
  · 25 alimentadores (6-1 a 6-25) — calefacción, alumbrado, motores 89, celdas 24/6.3 kV
  · PLC-02 1 kVA 220/110 V

  C.C. (110 Vcc) — Tablero 852-5240-020, 2 barras con acople 72-ACOPL:
  · Cargadores N°1/N°2: 110 Vcc – 20 A (852-5570-040 / 050)
  · Cargadores N°1/N°2: 48 Vcc (852-5570-060 / 061)
  · Baterías N°1/N°2: plomo-ácido 110 V – 65 Ah (852-5570-010)
  · Relés: 64 (falla tierra), 27 (bajo voltaje), 59 (sobrevoltaje), 30 (anunciador/alarma)
  · Alarmas vía RTU a Casa de Fuerza N°2

═══════════════════════════════════════════════════
7 · ESTADO NORMATIVO (InfoTecnica CEN)
═══════════════════════════════════════════════════
  · Completitud: 897/917 = 97.8%
  · Calidad: 491/897 = 54.7%  ← 45% de datos sin certificar (rechazados / sin revisar)

═══════════════════════════════════════════════════
8 · DOCUMENTOS FUENTE (planos leídos)
═══════════════════════════════════════════════════
  · Unilineal General Media/Baja Tensión — MBCDP (Debottlenecking) EPC — E-0020-0000-ELE-SLD-001, Rev 0 (06-03-2020)
  · Unilineal 220 kV — Reemplazo protecciones paño 52-J1 — N° 6003-E102, Rev 2 (29-08-2019)
  · Unilineal Switchgear 23 kV — Esintel Ingenieros — 18050-01-EE-DU-002, Rev Q (01-04-2019)
  · (SSAA Vca/Vcc + unilineal central: en lectura al momento de este doc)

═══════════════════════════════════════════════════
9 · ÁNGULO CONECTA (para Francisco)
═══════════════════════════════════════════════════
  1. SCADA inexistente (flag_scada=False) → RTU + SCADA nuevo
  2. Sistema de relés MIXTO (ABB REL670/REB670 + Schneider P643/SEPAM + GE D30), sin
     IEC 61850 confirmado → modernización a bus de proceso / GOOSE / MMS
  3. Calidad de datos CEN 54.7% → EDAC + reporte normativo automático
  4. flag_equipocom=False → red de comunicaciones IEC 61850 + conmutadores industriales
  5. Expansión Fase II (USD 89.5M) → nueva automatización en concentradora

═══════════════════════════════════════════════════
10 · ÁNGULO SUPCON (DCS / control / instrumentación)
═══════════════════════════════════════════════════
  1. Concentradora con molinos (trafos 4130-TL 37.5 MVA 23/6.3 kV para molinos) →
     DCS ECS-700 para modernizar el control de proceso (hoy PLC legacy) o para la
     Expansión Fase II (USD 89.5M) → paquete Digitalización Minera (ECS-700 + TCS-500
     SIS + APC + instrumentación).
  2. PRIDE (predictivo): 10 grupos diésel G-101..G-110 + motores de molinos + bombas →
     monitoreo de vibración/estado 24/7 (1,566 tipos de falla de equipos rotativos).
  3. Instrumentación de campo: transmisores CXT/CJT (presión/caudal) + flujómetros +
     válvulas CVP2000 con positioner inteligente.
  4. APC V11.2: molienda y flotación (la planta tiene concentradora con SAG/bolas).
  5. supOS (IIoT) + sala de control OP085 para la central y la concentradora.

CROSS-SELL CONECTA↔SUPCON: el paquete completo = RTU/SCADA/PMU (NovaTech/Vizimax) en la
subestación + DCS/PRIDE/instrumentación (SUPCON) en la planta. Un solo partner (CONECTA)
vs 3 proveedores (Siemens PCS7+Siprotec, ABB 800xA+relés, Emerson DeltaV+Rosemount).

═══════════════════════════════════════════════════
11 · BRECHAS NORMATIVAS + CARTAS DEL COORDINADOR
═══════════════════════════════════════════════════
Fuente: InfoTécnica CEN (API pública, 21-08-2026) + cartas.coordinador.cl (PDF descargados).

FLAGS CEN (S/E Mantos Blancos):
  · flag_scada = FALSE      → sin SCADA certificado ante el CEN
  · flag_equipocom = FALSE  → sin equipamiento de comunicaciones declarado
  · flag_pararrayos = FALSE → sin pararrayos/descargadores declarados

GRADO DE CUMPLIMIENTO (Mantos Copper S.A., 21-08-2026):
  · Completitud: 97.8% (897/917 informados · 20 sin informar)
  · Calidad: 54.7% (491/897 certificados = 311 validados + 180 en uso)
  · RECHAZADOS: 152 · NO REVISADOS: 254  ← 406 datos con problemas

CARTAS DEL COORDINADOR (3 encontradas, PDF descargados):
  1. DE 03731-24 (23-07-2024) — RECHAZO de solicitud de desconexión/intervención
     S/E Mantos Blancos (N°2024074892 y 2024074894). Motivo: no cumplió plazo/forma
     (Art. 248 DS 327: aviso 120 h · Art. 249: suspensiones MT ≤8 h/12 meses). Afecta a CGE.
  2. Dictamen N°27-2024 (06-12-2024) — Discrepancia de Mantos Copper ante Panel de
     Expertos por el rechazo. La mantención era del Transformador de Poder T-1
     (Informe Hitachi "Capstone Copper: Mantos Blancos Mantenimiento a T-1").
  3. DE06407-25 (25-11-2025) — Plan de Trabajo Pruebas de Verificación SCADA + SITR +
     enlaces de comunicación (Central Mantos Blancos). Entrega de informe antes del
     31-12-2025 (plazo PRS vigente). Firmado por EnorChile S.A. (operador de la central).

LECTURA COMERCIAL:
  · SCADA en verificación activa (PRS) → ventana de modernización SCADA/RTU YA.
  · flag_scada / equipocom / pararrayos = FALSE → 3 brechas declaradas que el CEN ve.
  · 406 datos rechazados/no revisados → dolor de compliance InfoTécnica (EDAC/reporte).
  · Contactos: David Pérez (Encargado Titular, Mantos Copper) · Aldo Araya (EnorChile,
    Jefe de Planta Central Térmica). Operador de la central = EnorChile S.A.

NOTA DE LECTURA: los planos son raster de 2019-2020 y varias placas salen "ilegible".
Los modelos exactos de relés marcados SÍ se leyeron (REL670, REB670, MiCOM P643, GE D30,
SEPAM, ION 8690). Todo lo "ilegible" queda explícito — no se inventó nada.
