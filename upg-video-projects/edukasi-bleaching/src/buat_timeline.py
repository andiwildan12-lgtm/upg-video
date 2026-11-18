#!/usr/bin/env python3
"""Tulis src/timeline.js dari waktu kata Scribe + peta potongan (Edukasi Bleaching V1)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
words = [x for x in json.load(open(P/'work'/'words.json'))['words'] if x.get('type') == 'word']
offs = {n: float(o) for n, o, d in (l.split() for l in open(P/'work'/'offsets.txt'))}
peta = json.loads((P/'work'/'peta.json').read_text())
HL = {'noda', 'kekuningan', 'kusam', 'kuning', 'bleaching', 'kunjungan', 'berbeda-beda', 'periksakan', 'tepat.', 'cerah'}
FIX = {'mengkonsumsi': 'mengonsumsi', 'kopi,': 'kopi,', 'kita.': 'kita.'}
items = []
for s in peta['seg']:
    c = s['clip'].split('/')[-1]; o = offs[c]
    for w in [w for w in words if s['src_a'] - 0.05 <= w['start'] - o < s['src_a'] + s['dur'] - 0.05]:
        txt = FIX.get(w['text'], w['text'])
        t = round(s['out_a'] + (w['start'] - o - s['src_a']), 2)
        items.append(dict(text=txt, at=max(t, s['out_a']), hl=txt.strip(',.') in {h.strip(',.') for h in HL} and not (txt.startswith('bleaching') and s['seg'] != 2), seg=s['seg'], end=s['out_a'] + s['dur']))
groups, g = [], []
for it in items:
    if g and (len(g) >= 4 or it['seg'] != g[-1]['seg'] or it['at'] - g[-1]['at'] > 0.9 or g[-1]['text'][-1] in '.?,'):
        groups.append(g); g = []
    g.append(it)
if g: groups.append(g)
caps = []
for i, g in enumerate(groups):
    nxt = groups[i + 1][0]['at'] if i + 1 < len(groups) else 1e9
    to = min(nxt, g[-1]['at'] + 1.2, g[-1]['end'] + 0.3)
    caps.append({'from': g[0]['at'], 'to': round(to, 2), 'words': [dict(text=w['text'], at=w['at'], **({'hl': True} if w['hl'] else {})) for w in g]})
total = peta['total']; S = peta['seg']
labels = [
  {'from': 0.0, 'to': 3.6, 'text': 'Suka ngopi & ngeteh? Ini efeknya ke gigi ☕', 'pos': 'top'},
  {'from': 3.8, 'to': 7.6, 'text': 'drg. Firdha · UPG Dental Care', 'pos': 'top'},
  {'from': S[3]['out_a'] + 0.3, 'to': S[3]['out_a'] + 4.5, 'text': 'Cukup 1x kunjungan ✨', 'pos': 'top'},
]
note = {'from': S[4]['out_a'], 'to': S[4]['out_a'] + S[4]['dur'], 'text': 'Hasil tiap orang berbeda'}
logo_hide = [[l['from'] - 0.2, l['to'] + 0.2] for l in labels]
js = f"""// DIBUAT OTOMATIS oleh src/buat_timeline.py (Rancangan V1, ACC "gas render").
export const CUTS = [{{src: 0.0, dur: {total}}}];
export const CAPTIONS = {json.dumps(caps, ensure_ascii=False)};
export const PROMO = null;
export const LABELS = {json.dumps(labels, ensure_ascii=False)};
export const NOTE = {json.dumps(note, ensure_ascii=False)};
export const LOGO_HIDE = {json.dumps(logo_hide)};
export const LOGO_BUG = true;
export const END_CARD_SEC = 3.0;
export const END_TITLE = 'Konsultasi bleaching dulu yuk';
export const WA = '0896-7341-5806';
export const MUSIC = null;
export const totalSec = () => CUTS.reduce((a, c) => a + c.dur, 0) + END_CARD_SEC;
"""
(P/'src'/'timeline.js').write_text(js)
(P/'src'/'meta.js').write_text(f"export const META = {{width: 1080, height: 1920, fps: 30, durationSec: {total}}};\n")
print('\n'.join(f"{c['from']:5.2f} " + ' '.join(w['text'] + ('*' if w.get('hl') else '') for w in c['words']) for c in caps))
