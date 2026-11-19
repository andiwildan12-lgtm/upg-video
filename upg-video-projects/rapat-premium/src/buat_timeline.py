#!/usr/bin/env python3
"""timeline.js Rapat Dokter Premium Cut: caption kecil dari Scribe + kata kunci/ikon/kartu (waktu di video hasil)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
words = [x for x in json.load(open(P/'work'/'words.json'))['words'] if x.get('type') == 'word']
offs = {n: float(o) for n, o, d in (l.split() for l in open(P/'work'/'offsets.txt'))}
pe = json.loads((P/'work'/'peta.json').read_text()); S = pe['seg']; TOTAL = pe['total']
SKIP = {'eh,', 'eh', 'ki', 'ji', 'to', 'maka', 'Di', 'di'}
items = []
for s in S:
    if s['seg'] in (2, 9): continue
    o = offs[s['clip']]
    ws = [w for w in words if s['src_a'] - 0.05 <= w['start'] - o < s['src_a'] + s['dur'] - 0.05]
    for k, w in enumerate(ws):
        tx = w['text']; nx = ws[k + 1]['text'] if k + 1 < len(ws) else ''
        if tx in SKIP and not (tx == 'di' and nx not in ('keep', 'get')): continue
        if tx == 'ku' and items and items[-1]['text'] == 'saran': items[-1]['text'] = 'saranku'; continue
        if tx in ('ta', 'ta.'): tx = 'kita' + tx[2:]
        if tx == 'delapan' and nx == 'lima': tx = '85'
        if tx == 'lima' and items and items[-1]['text'] == '85': continue
        items.append(dict(text=tx, at=round(s['out_a'] + w['start'] - o - s['src_a'], 2), seg=s['seg'], end=s['out_a'] + s['dur']))
if items: items[0]['text'] = items[0]['text']
groups, g = [], []
for it in items:
    if g and (len(g) >= 4 or it['seg'] != g[-1]['seg'] or it['at'] - g[-1]['at'] > 0.9 or g[-1]['text'][-1] in '.?,'):
        groups.append(g); g = []
    g.append(it)
if g: groups.append(g)
caps = []
for i, g in enumerate(groups):
    nxt = groups[i + 1][0]['at'] if i + 1 < len(groups) else 1e9
    caps.append({'from': g[0]['at'], 'to': round(min(nxt, g[-1]['at'] + 1.2, g[-1]['end'] + 0.2), 2), 'words': [{'text': w['text'], 'at': w['at']} for w in g]})
KEYS = [
  dict(text='BUKA LEBAR-LEBAR', **{'from': 0.74, 'to': 3.15}, size=90),
  dict(text='KEEP SILENT 🤫', **{'from': 3.9, 'to': 5.0}, bg='#fff'),
  dict(text='TER-DEVELOP', **{'from': 9.25, 'to': 10.8}, style='wh'),
  dict(text='PERKEMBANGAN', **{'from': 16.25, 'to': 17.4}),
  dict(text='LIHAT RAPOR', **{'from': 18.9, 'to': 20.2}, style='wh'),
  dict(text='WAJAR ✅', **{'from': 24.6, 'to': 26.3}),
  dict(text='DIREKTUR?', **{'from': 27.25, 'to': 28.5}, style='wh'),
  dict(text='PENDAPAT MITRA', **{'from': 28.55, 'to': 30.0}),
  dict(text='TANPA ATASAN–BAWAHAN', **{'from': 35.55, 'to': 38.8}, size=64),
  dict(text='DI BAWAH 👇', **{'from': 41.8, 'to': 43.4}, style='wh'),
  dict(text='DI ATAS 👆', **{'from': 47.25, 'to': 47.95}, style='wh'),
  dict(text='SEMANGAT NAIK 🔥', **{'from': 49.85, 'to': 51.9}, size=82),
  dict(text='DUA SISI', **{'from': 54.05, 'to': 55.3}, style='wh'),
  dict(text='KEEP SILENT 🤫', **{'from': 56.0, 'to': 57.4}, bg='#fff'),
  dict(text='GAK USAH TERBUKA', **{'from': 59.3, 'to': 60.45}),
]
ICONS = [
  dict(name='rapor', **{'from': 0.6, 'to': 3.2}, x=520, y=230, w=480),
  dict(name='timeline', **{'from': 10.9, 'to': 15.4}, x=90, y=230, w=620, anim=2.2),
  dict(name='chart', **{'from': 16.1, 'to': 17.45}, x=540, y=230, w=460, anim=0.9),
  dict(name='rapor', **{'from': 18.8, 'to': 20.4}, x=540, y=230, w=460),
  dict(name='hierarki', **{'from': 33.6, 'to': 35.5}, x=540, y=230, w=460, anim=1.4),
  dict(name='sejajar', **{'from': 35.5, 'to': 38.8}, x=540, y=230, w=460),
  dict(name='tangga', **{'from': 41.0, 'to': 47.95}, x=560, y=220, w=460, anim=1.5),
  dict(name='timbangan', **{'from': 53.9, 'to': 56.0}, x=540, y=220, w=460),
]
CARDS = [
  dict(**{'from': 5.07, 'to': 6.47}, full=True, kicker='RAPAT DOKTER HARI INI 👀', lines=['Rapor dokter', '<span style="color:#fbb03b">dibuka</span> atau', '<span style="color:#fbb03b">dirahasiakan?</span>']),
  dict(**{'from': TOTAL - 2.8, 'to': TOTAL}, kicker='MENURUT KAMU?', lines=['Rapor dokter', 'dibuka atau dirahasiakan?'], size=72, handle='@growwithupgruma', mt=-620),
]
# Posisi aman dari wajah (dicek manual per potongan, work/faces-grid.jpg): (mulai, akhir, y kata kunci, y subtitle)
AMAN = [(3.23, 5.07, 1300, 1490), (11.47, 13.97, 1060, 760), (39.03, 45.53, 1250, 1440), (45.53, 47.97, 860, 1530),
        (47.97, 56.27, 1300, 1490), (56.27, 58.27, 1250, 1440), (58.27, 60.5, 1300, 1490)]
def pos(tt, i):
    for a, b, ky, cy in AMAN:
        if a <= tt < b: return (ky, cy)[i]
    return (1060, 1440)[i]
for c in caps: c['y'] = pos(c['from'], 1)
for k in KEYS: k['y'] = pos(k['from'], 0)
js = "// DIBUAT OTOMATIS oleh src/buat_timeline.py\n" + "".join(f"export const {n} = {json.dumps(v, ensure_ascii=False)};\n" for n, v in [('CAPTIONS', caps), ('KEYS', KEYS), ('ICONS', ICONS), ('CARDS', CARDS)]) + f"export const TOTAL = {TOTAL};\n"
(P/'src'/'timeline.js').write_text(js)
print(len(caps), 'caption,', len(KEYS), 'kunci,', len(ICONS), 'ikon')
