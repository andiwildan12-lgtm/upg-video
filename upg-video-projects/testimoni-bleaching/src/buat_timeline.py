#!/usr/bin/env python3
"""Tulis src/timeline.js dari waktu kata Scribe + peta potongan (Testimoni Bleaching V2)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
words = [x for x in json.load(open(P/'work'/'words.json'))['words'] if x.get('type') == 'word']
offs = {n: float(o) for n, o, d in (l.split() for l in open(P/'work'/'offsets.txt'))}
peta = json.loads((P/'work'/'peta.json').read_text())
HL = {'takut', 'scaling.', 'nyaman.', 'ramah', 'edukatif.', 'nyamannya.', 'profesional,', 'putih', 'tersenyum.', 'berfoto.'}
FIX = {'scaling': 'scaling.', 'ndak': 'nggak', 'Alhamdulillah': 'Alhamdulillah,', 'nyaman': 'nyaman.', 'berfoto': 'berfoto.', 'dan': 'dan'}
items = []
for s in peta['seg']:
    c = s['clip'].split('/')[-1]; o = offs[c]
    ws = [w for w in words if s['src_a'] - 0.05 <= w['start'] - o < s['src_a'] + s['dur'] - 0.05]
    for w in ws:
        txt = w['text']
        if txt.lower().strip(',.') in ('ehm', 'eh', 'itu', 'tuh') and not (txt == 'itu' and False): 
            if txt.lower().startswith('itu'): continue
            continue
        if c == '0510' and txt == 'scaling': txt = 'scaling.'
        if txt == 'ndak': txt = 'nggak'
        if txt == 'awalnya': txt = 'Awalnya'
        if txt == 'nah': txt = 'Nah'
        if c == '0507' and txt == 'nyaman': txt = 'nyaman.'
        if txt == 'berfoto': txt = 'berfoto.'
        if c == '0517' and txt == 'dan': txt = 'Dan'
        t = round(s['out_a'] + (w['start'] - o - s['src_a']), 2)
        items.append(dict(text=txt, at=max(t, s['out_a']), hl=txt in HL, seg=s['seg'], end=s['out_a'] + s['dur']))
for k in range(len(items) - 1):   # 'di' + kata kerja -> 'di-scaling.', 'di-bleaching'
    if items[k]['text'] == 'di' and items[k+1]['text'].startswith(('scaling', 'bleaching')):
        items[k+1]['text'] = 'di-' + items[k+1]['text']; items[k]['drop'] = True
items = [i for i in items if not i.get('drop')]
for i in items: i['hl'] = i['hl'] or i['text'] in ('di-scaling.',)
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
  {'from': 0.0, 'to': 3.3, 'text': 'Takut bleaching? Dengar cerita Kak Tika dulu', 'pos': 'top'},
  {'from': S[5]['out_a'] + 5.6, 'to': S[6]['out_a'] + S[6]['dur'], 'text': 'Lebih pede senyum 😁', 'pos': 'top'},
]
note = {'from': S[5]['out_a'], 'to': total, 'text': 'Hasil tiap orang berbeda'}
logo_hide = [[S[4]['out_a'] - 0.1, S[4]['out_a'] + S[4]['dur'] + 0.1]] + [[l['from'] - 0.2, l['to'] + 0.2] for l in labels]
js = f"""// DIBUAT OTOMATIS oleh src/buat_timeline.py (Rancangan V2, ACC "Gas").
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
for c in caps: print(f"{c['from']:5.2f}-{c['to']:5.2f}", ' '.join(w['text'] + ('*' if w.get('hl') else '') for w in c['words']))
