#!/usr/bin/env python3
"""Tulis src/timeline.js dari waktu kata Scribe (work/words.json) + peta potongan (work/peta.json)."""
import json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1]
words = [x for x in json.load(open(P/'work'/'words.json'))['words'] if x.get('type') == 'word']
offs = {n: float(o) for n, o, d in (l.split() for l in open(P/'work'/'offsets.txt'))}
peta = json.loads((P/'work'/'peta.json').read_text())
DROP = {'eh', 'eh,', 'ki', 'ki,', 'ji', 'ji,', 'ji.', 'maka', 'to', 'di', 'Di'}   # 'di' hanya dibuang sebelum keep/get (lihat bawah)
FIX = {'ta': 'kita', 'ta.': 'kita.', 'ta,': 'kita,', 'ku': '', 'Mi': '', 'KPI-nya.': 'KPI-nya.'}
HL = {'lebar-lebar', 'perkembangannya', 'rapor.', 'mitra.', 'sisi', 'keep', 'silent.', 'Setuju.', 'semangat', 'wajar'}
items = []
for s in peta['seg']:
    if s['clip'] in ('0558', '0624'): continue
    o = offs[s['clip']]
    ws = [w for w in words if s['src_a'] - 0.05 <= w['start'] - o < s['src_a'] + s['dur'] - 0.05]
    prev = None
    for k, w in enumerate(ws):
        txt = w['text']; nxt = ws[k + 1]['text'] if k + 1 < len(ws) else ''
        if txt in ('di', 'Di') and nxt.lower() in ('keep', 'get'): continue
        if txt.lower().rstrip(',.') in ('eh', 'ki', 'ji', 'maka') : 
            if txt[-1] in '.' and items: items[-1]['text'] = items[-1]['text'].rstrip(',') + '.'
            continue
        if txt == 'ku' and prev == 'saran': items[-1]['text'] = 'saranku'; continue
        if txt in ('ta', 'ta.', 'ta,', 'ta.'): txt = 'kita' + txt[2:]
        if txt in ('ku,', 'to'): continue
        if txt == 'lima' and prev == 'delapan': continue
        if txt == 'delapan' and nxt == 'lima': txt = '85'
        if txt == 'dua' and nxt.startswith('sisi'): pass
        t = round(s['out_a'] + (w['start'] - o - s['src_a']), 2)
        items.append(dict(text=txt, at=max(t, s['out_a']), hl=txt in HL or (txt == 'dua' and nxt.startswith('sisi')), seg=s['seg'], end=s['out_a'] + s['dur']))
        prev = txt
# kelompokkan maks 4 kata, putus di akhir kalimat / jeda > 0.6 dtk / ganti segmen
groups, g = [], []
for i, it in enumerate(items):
    if g and (len(g) >= 4 or it['seg'] != g[-1]['seg'] or it['at'] - g[-1]['at'] > 0.9 or g[-1]['text'][-1] in '.?,'):
        groups.append(g); g = []
    g.append(it)
if g: groups.append(g)
caps = []
for i, g in enumerate(groups):
    nxt = groups[i + 1][0]['at'] if i + 1 < len(groups) else 1e9
    to = min(nxt, g[-1]['at'] + 1.2, g[-1]['end'])
    caps.append(dict(**{'from': g[0]['at'], 'to': round(to, 2)}, words=[dict(text=w['text'], at=w['at'], **({'hl': True} if w['hl'] else {})) for w in g]))
total = peta['total']
s4 = next(s for s in peta['seg'] if s['clip'] == '0572')['out_a']
s7 = peta['seg'][-1]['out_a']
labels = [
  dict(**{'from': 0.0, 'to': 3.6}, text='Rapat dokter hari ini: rapor semua dokter mau dibuka?', pos='top'),
  dict(**{'from': s4, 'to': s4 + 3.4}, text='Tapi direkturnya tanya dulu ke dokter mitra', pos='top'),
]
js = f"""// DIBUAT OTOMATIS oleh src/buat_timeline.py (Rancangan V2, ACC "Render gaskan").
export const CUTS = [{{src: 0.0, dur: {total}}}];
export const CAPTIONS = {json.dumps(caps, ensure_ascii=False)};
export const PROMO = null;
export const LABELS = {json.dumps(labels, ensure_ascii=False)};
export const OUTRO = {{from: {s7}, to: {total}, q: 'Kalau kamu dokternya:', q2: 'rapor dibuka atau dirahasiakan?', handle: '@growwithupgruma'}};
export const LOGO_BUG = false;
export const END_CARD_SEC = 0;
export const WA = '';
export const MUSIC = null;
export const totalSec = () => CUTS.reduce((a, c) => a + c.dur, 0) + END_CARD_SEC;
"""
(P/'src'/'timeline.js').write_text(js)
(P/'src'/'meta.js').write_text(f"// footage dasar dari src/edit.py\nexport const META = {{width: 1080, height: 1920, fps: 30, durationSec: {total}}};\n")
for c in caps: print(f"{c['from']:5.2f}-{c['to']:5.2f}", ' '.join(w['text'] + ('*' if w.get('hl') else '') for w in c['words']))
