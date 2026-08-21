#!/usr/bin/env python3
"""Unilineal 220/23 kV Mantos Blancos — SVG limpio, símbolos IEC, sin gaps."""
import os

BLUE = "#2563eb"; GREEN = "#059669"; AMBER = "#d97706"
INK = "#0f172a"; MUT = "#64748b"

W, H = 960, 780
BUS220 = 250
BUS23 = 580

parts = []

def vline(x, y1, y2, c):
    parts.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{c}" stroke-width="2.5"/>')

def breaker(x, y, c):
    parts.append(f'<rect x="{x-11}" y="{y-11}" width="22" height="22" fill="white" stroke="{c}" stroke-width="2.2"/>')
    parts.append(f'<line x1="{x-11}" y1="{y-11}" x2="{x+11}" y2="{y+11}" stroke="{c}" stroke-width="1.6"/>')

def disconnect(x, y, c):
    parts.append(f'<line x1="{x}" y1="{y-8}" x2="{x}" y2="{y-2}" stroke="{c}" stroke-width="2"/>')
    parts.append(f'<line x1="{x}" y1="{y+8}" x2="{x}" y2="{y+2}" stroke="{c}" stroke-width="2"/>')
    parts.append(f'<line x1="{x-14}" y1="{y+7}" x2="{x+1}" y2="{y-1}" stroke="{c}" stroke-width="2"/>')

def ct(x, y, c):
    parts.append(f'<circle cx="{x}" cy="{y}" r="9" fill="white" stroke="{c}" stroke-width="2.2"/>')

# ===== BARRA 220 kV =====
parts.append(f'<line x1="60" y1="{BUS220}" x2="900" y2="{BUS220}" stroke="{BLUE}" stroke-width="6" stroke-linecap="round"/>')
parts.append(f'<text x="912" y="{BUS220+5}" fill="{BLUE}" font-size="15" font-weight="700">220 kV</text>')

# ===== BARRA 23 kV =====
parts.append(f'<line x1="100" y1="{BUS23}" x2="860" y2="{BUS23}" stroke="{GREEN}" stroke-width="6" stroke-linecap="round"/>')
parts.append(f'<text x="872" y="{BUS23+5}" fill="{GREEN}" font-size="15" font-weight="700">23 kV</text>')

def incoming(x, name, tc):
    y = 90
    parts.append(f'<text x="{x}" y="{y-6}" text-anchor="middle" fill="{INK}" font-size="13" font-weight="600">{name}</text>')
    vline(x, y, y+14, BLUE)
    disconnect(x, y+24, BLUE)
    vline(x, y+32, y+50, BLUE)
    breaker(x, y+61, BLUE)
    vline(x, y+72, y+94, BLUE)
    ct(x, y+106, BLUE)
    parts.append(f'<text x="{x+14}" y="{y+110}" fill="{MUT}" font-size="11">{tc}</text>')
    vline(x, y+115, BUS220, BLUE)

def trafo_branch(x, t_id, mva):
    r = 22
    cy1 = BUS220 + 195
    cy2 = cy1 + 2*r
    # 220 kV side
    vline(x, BUS220, BUS220+38, BLUE)
    breaker(x, BUS220+49, BLUE)
    vline(x, BUS220+60, BUS220+82, BLUE)
    disconnect(x, BUS220+94, BLUE)
    vline(x, BUS220+102, cy1, AMBER)
    # transformador (2 circulos)
    parts.append(f'<circle cx="{x}" cy="{cy1}" r="{r}" fill="white" stroke="{AMBER}" stroke-width="3"/>')
    vline(x, cy1+r, cy2-r, AMBER)
    parts.append(f'<circle cx="{x}" cy="{cy2}" r="{r}" fill="white" stroke="{AMBER}" stroke-width="3"/>')
    vline(x, cy2+r, cy2+r+26, GREEN)
    # 23 kV side
    breaker(x, cy2+r+37, GREEN)
    vline(x, cy2+r+48, BUS23, GREEN)
    # etiquetas
    parts.append(f'<text x="{x+32}" y="{cy1+6}" fill="{INK}" font-size="14" font-weight="700">{t_id}</text>')
    parts.append(f'<text x="{x+32}" y="{cy1+22}" fill="{MUT}" font-size="11">{mva}</text>')

incoming(150, "LÍNEA LABERINTO", "TC 1200/5")
incoming(810, "LÍNEA CHACAYA", "TC 800/5")
trafo_branch(350, "T1", "34/42/50 MVA")
trafo_branch(610, "T2", "40 MVA")

# ===== título =====
parts.append(f'<text x="30" y="36" fill="{INK}" font-size="17" font-weight="700">S/E MANTOS BLANCOS · 220/23 kV</text>')
parts.append(f'<text x="30" y="55" fill="{MUT}" font-size="11">Capstone Copper · Barra 220 kV 300 A · Barra 23 kV 2500 A / 1000 MVA</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" '
       f'font-family="Helvetica, Arial, sans-serif" style="background:white">'
       + "".join(parts) + "</svg>")

out = os.path.expanduser("~/b2b-sales-system/mantos_blancos/unilineal_limpio.svg")
open(out, "w").write(svg)
print("OK", out, len(svg), "bytes")
