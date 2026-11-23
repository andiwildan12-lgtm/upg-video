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
    if s['seg'] in (2, 12): continue
    o = offs[s['clip']]
    ws = [w for w in words if s['src_a'] - 0.05 <= w['start'] - o < s['src_a'] + s['dur'] - 0.05]
    for k, w in enumerate(ws):
        tx = w['text']; nx = ws[k + 1]['text'] if k + 1 < len(ws) else ''
        if tx in SKIP and not (tx == 'di' and nx not in ('keep', 'get')): continue
        if tx == 'ku' and items and items[-1]['text'] == 'saran': items[-1]['text'] = 'saranku'; continue
        if tx in ('ta', 'ta.', 'ta,'): tx = 'kita' + tx[2:]
        if tx == 'mengajar': tx = 'mengejar'
        if tx == 'baku,': continue
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
KEYS = [  # c='o' = blok orange, default blok hijau; teks hitam
  dict(text='BUKA LEBAR-LEBAR', **{'from': 0.74, 'to': 3.15}, size=92),
  dict(text='KEEP SILENT 🤫', **{'from': 3.9, 'to': 5.0}, c='o'),
  dict(text='TER-DEVELOP', **{'from': 7.59, 'to': 9.1}),
  dict(text='PERKEMBANGAN 📈', **{'from': 14.5, 'to': 15.75}, size=90),
  dict(text='MASIH ADA CELAH?', **{'from': 17.6, 'to': 19.75}, c='o', size=90),
  dict(text='LIHAT RAPOR 👀', **{'from': 21.1, 'to': 22.6}),
  dict(text='"OH, WAJAR" ✅', **{'from': 26.9, 'to': 28.7}),
  dict(text='MOTIVASI', **{'from': 29.78, 'to': 31.8}, c='o'),
  dict(text='TAHUN DEPAN 🔥', **{'from': 33.9, 'to': 34.85}),
  dict(text='DI BAWAH? 👇', **{'from': 37.6, 'to': 39.4}, c='o'),
  dict(text='DI ATAS? 👆', **{'from': 42.9, 'to': 43.8}, c='o'),
  dict(text='TAKUT AMBIL', **{'from': 48.2, 'to': 51.3}, c='o', size=88),
  dict(text='KASUS SULIT?', **{'from': 49.6, 'to': 51.3}, c='o', size=88, dy=130),
  dict(text='SEMANGAT NAIK 🔥', **{'from': 53.2, 'to': 55.5}, size=86),
  dict(text='DUA SISI', **{'from': 57.4, 'to': 58.6}, c='o'),
  dict(text='KEEP SILENT 🤫', **{'from': 59.35, 'to': 60.35}, c='o'),
  dict(text='GAK USAH TERBUKA', **{'from': 60.97, 'to': 62.1}, size=86),
]
ICONS = [
  dict(name='timeline', **{'from': 9.2, 'to': 13.9}, x=230, y=300, w=620, anim=2.2),
  dict(name='rapor', **{'from': 22.65, 'to': 25.4}, x=300, y=300, w=480),
  dict(name='tangga', **{'from': 39.5, 'to': 42.85}, x=300, y=300, w=480, anim=1.5),
  dict(name='timbangan', **{'from': 55.6, 'to': 57.35}, x=300, y=300, w=480),
]
CARDS = [
  dict(**{'from': 5.07, 'to': 6.47}, full=True, kicker='RAPAT DOKTER HARI INI 👀', lines=['Rapor dokter:', '<span style="background:#F28621;color:#020202;padding:0 18px;border-radius:16px">dibuka</span> atau', 'dirahasiakan?']),
  dict(**{'from': 62.97, 'to': TOTAL}, full=True, kicker='MENURUT KAMU? 🤔', lines=['Rapor dokter:', '<span style="background:#F28621;color:#020202;padding:0 18px;border-radius:16px">dibuka</span> atau', 'dirahasiakan?'], size=88, handle='Tulis di komentar · @growwithupgruma'),
]
AMAN = []  # (mulai, akhir, y kata kunci, y subtitle) diisi setelah cek wajah per potongan
def pos(tt, i):
    for a, b, ky, cy in AMAN:
        if a <= tt < b: return (ky, cy)[i]
    return (300, 1400)[i]
for c in caps: c['y'] = pos(c['from'], 1)
for k in KEYS: k['y'] = pos(k['from'], 0) + k.pop('dy', 0)
js = "// DIBUAT OTOMATIS oleh src/buat_timeline.py\n" + "".join(f"export const {n} = {json.dumps(v, ensure_ascii=False)};\n" for n, v in [('CAPTIONS', caps), ('KEYS', KEYS), ('ICONS', ICONS), ('CARDS', CARDS)]) + f"export const TOTAL = {TOTAL};\n"
(P/'src'/'timeline.js').write_text(js)
print(len(caps), 'caption,', len(KEYS), 'kunci,', len(ICONS), 'ikon')
