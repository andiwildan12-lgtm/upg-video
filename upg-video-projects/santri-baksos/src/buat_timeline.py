#!/usr/bin/env python3
"""timeline.js Baksos Santri (tanpa ucapan): kata kunci + ikon + kartu, waktu di video hasil."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
pe = json.loads((P/'work'/'peta.json').read_text()); S = [s['out_a'] for s in pe['seg']]; TOTAL = pe['total']
KEYS = [
  dict(text='HARI INI KLINIK', **{'from': 0.3, 'to': 1.9}, style='wh', size=84, y=1180),
  dict(text='DISERBU SANTRI! 🕌', **{'from': 1.9, 'to': 4.0}, size=70, y=1180),
  dict(text='DAFTAR DULU ✍️', **{'from': S[1] + 0.3, 'to': S[2] + 2.8}, y=1300),
  dict(text='NUNGGU GILIRAN… 😬', **{'from': S[3] + 0.3, 'to': S[5]}, size=80, y=1340),
  dict(text='DIPERIKSA ✅', **{'from': S[5] + 0.3, 'to': S[6] + 1.2}, y=1050),
  dict(text='DIRAWAT DOKTER 🦷', **{'from': S[6] + 1.3, 'to': S[8]}, size=78, y=1050),
  dict(text='PULANG BAWA BINGKISAN 🎁', **{'from': S[8] + 0.3, 'to': S[10]}, size=56, y=1380),
]
ICONS = [
  dict(name='rombongan', **{'from': 0.2, 'to': 4.0}, x=520, y=240, w=480, anim=1.2),
  dict(name='formulir', **{'from': S[1] + 0.2, 'to': S[3]}, x=560, y=240, w=440, anim=2.2),
  dict(name='jam', **{'from': S[3] + 0.2, 'to': S[5]}, x=560, y=240, w=440),
  dict(name='gigi', **{'from': S[5] + 0.2, 'to': S[8]}, x=560, y=230, w=440, anim=1.4),
  dict(name='kado', **{'from': S[8] + 0.2, 'to': S[10]}, x=560, y=230, w=440),
]
CARDS = [
  dict(**{'from': S[10] + 0.6, 'to': TOTAL}, kicker='BAKTI SOSIAL UPG–RUMA 💚', lines=['Pemeriksaan &amp; perawatan', 'gigi gratis untuk santri', '<span style="color:#00691d">Ponpes Bilal Bin Robah</span>'], size=56, handle='@growwithupgruma', mt=-560),
]
js = "// DIBUAT OTOMATIS oleh src/buat_timeline.py\n" + "".join(f"export const {n} = {json.dumps(v, ensure_ascii=False)};\n" for n, v in [('CAPTIONS', []), ('KEYS', KEYS), ('ICONS', ICONS), ('CARDS', CARDS)]) + f"export const TOTAL = {TOTAL};\n"
(P/'src'/'timeline.js').write_text(js); print('ok', TOTAL)
