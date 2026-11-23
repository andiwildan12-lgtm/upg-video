#!/usr/bin/env python3
"""Cek kotak tulisan yang bertumpuk (judul, pill, teks, jam, name tag, logo, kartu) dari src/timeline.js.

Pemakaian: python3 cek_tumpang.py <folder-proyek> [--jarak 16]
Mengambil setiap elemen + rentang waktunya, memperkirakan kotaknya (ukuran huruf Nunito 900 ±0,58 x ukuran per huruf),
lalu melaporkan pasangan yang tampil BERSAMAAN dan kotaknya bersentuhan/bertumpuk (jarak < --jarak px).
Hasil = daftar detik + elemen; kosong = aman. Tetap cek visual frame yang dilaporkan.
"""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1]); gap = float(sys.argv[sys.argv.index("--jarak") + 1]) if "--jarak" in sys.argv else 16
src = (P / "src" / "timeline.js").read_text()
def get(name):
    m = re.search(rf"export const {name} = (.*?);\n", src, re.S)
    return json.loads(m.group(1)) if m else None
TITLES, NAMETAG, CARDS, LOGO, cuts_end = get("TITLES") or [], get("NAMETAG"), get("CARDS") or [], get("LOGO"), float(get("cutsEnd"))
W = 1080
def tw(t, size): return max(len(l) for l in t.split("\n")) * size * 0.58
els = []
for k in TITLES:
    kind, txt, y = k.get("kind", "pill"), k.get("text", ""), k.get("y", 330)
    n = len(txt.split("\n"))
    if kind == "hook":
        s = k.get("size", 96); w = min(W - 120, tw(txt, s)); h = n * s * 1.08
    elif kind == "teks":
        s = k.get("size", 54); w = min(W - 140, tw(txt.replace("*", ""), s) + 52); h = n * (s * 1.15 + 20) + (n - 1) * 10
    elif kind == "jam":
        y = k.get("y", 270); els.append((f"jam {txt}", k["from"], k["to"], (W - 140 - 300, y, W - 140, y + 78))); continue
    else:  # pill / retro
        s = k.get("size", 56); w = tw(txt, s) + 68 + (70 if k.get("emoji") else 0); h = s * 1.2 + 28
    x0 = (W - w) / 2
    els.append((f"{kind} \"{txt[:28]}\"", k["from"], k["to"], (x0, y, x0 + w, y + h)))
if NAMETAG:
    els.append((f"nametag {NAMETAG['name']}", NAMETAG["from"], NAMETAG["to"], (70, 1080, 70 + tw(NAMETAG["name"], 46) + 68, 1080 + 46 * 1.35 + 24)))
for c in CARDS:
    els.append((f"kartu {c.get('type')}", c["from"], c["to"], (70, 230, W - 70, 1500)))
if LOGO:
    busy = [(k["from"], k["to"]) for k in TITLES if k.get("kind") not in ("teks", "jam")]
    t, free = 0.0, []
    while t < cuts_end:
        if not any(a - 0.3 < t < b + 0.3 for a, b in busy) and not any(c["from"] <= t <= c["to"] for c in CARDS): free.append(t)
        t += 0.1
    if free:  # gabungkan rentang bebas
        segs, s0, prev = [], free[0], free[0]
        for t in free[1:]:
            if t - prev > 0.15: segs.append((s0, prev)); s0 = t
            prev = t
        segs.append((s0, prev))
        for a, b in segs: els.append(("logo pojok", a, b, (60, 250, 330, 327)))
bad = []
for i in range(len(els)):
    for j in range(i + 1, len(els)):
        n1, a1, b1, r1 = els[i]; n2, a2, b2, r2 = els[j]
        t0, t1 = max(a1, a2), min(b1, b2)
        if t1 - t0 < 0.05: continue
        dx = max(r1[0] - r2[2], r2[0] - r1[2]); dy = max(r1[1] - r2[3], r2[1] - r1[3])
        if max(dx, dy) < gap:
            bad.append((round(t0, 2), round(t1, 2), n1, n2, round(max(dx, dy))))
for b in sorted(bad): print(f"{b[0]}–{b[1]} dtk: {b[2]}  ×  {b[3]}  (jarak {b[4]} px)")
print("AMAN: tidak ada kotak tulisan bertumpuk" if not bad else f"PERLU DICEK: {len(bad)} pasangan")
