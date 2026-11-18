#!/usr/bin/env python3
"""timeline.js GrowWith Onboarding V1 dari waktu kata Scribe + peta potongan."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
words = [x for x in json.load(open(P/'work'/'words.json'))['words'] if x.get('type') == 'word']
offs = {n: float(o) for n, o, d in (l.split() for l in open(P/'work'/'offsets.txt'))}
peta = json.loads((P/'work'/'peta.json').read_text())
FIX = {'OPG': 'UPG', 'rumah': 'Ruma', 'dental.': 'Dental?', 'Eh': None, 'eh': None, 'Kau': 'Kau', 'Tidak': 'Tidak'}
HL = {'kakak.', 'E.', 'Tika.', 'integritas.', 'integritas,', 'excellence', 'excellence,', 'humanity.', 'kecuali.', 'tiga.'}
items = []
for s in peta['seg']:
    c = s['clip'].split('/')[-1]; o = offs[c]
    for w in [w for w in words if s['src_a'] - 0.05 <= w['start'] - o < s['src_a'] + s['dur'] - 0.05]:
        txt = FIX.get(w['text'], w['text'])
        if txt is None: continue
        t = round(s['out_a'] + (w['start'] - o - s['src_a']), 2)
        items.append(dict(text=txt, at=max(t, s['out_a']), hl=txt in HL, seg=s['seg'], end=s['out_a'] + s['dur']))
if items: items[0]['text'] = items[0]['text'].capitalize()
for k, it in enumerate(items):   # chant awal terpotong: 'tukar shift.' pertama di segmen kuis -> tambah 'Tidak pernah'
    if it['seg'] == 6 and it['text'] == 'tukar':
        items.insert(k, dict(it, text='Tidak pernah', at=max(S0 := it['at'] - 0.6, it['at'] - 0.6))); break
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
  {'from': 0.0, 'to': 4.2, 'text': 'POV: hari pertama kamu jadi tim UPG–Ruma', 'pos': 'top'},
  {'from': S[2]['out_a'], 'to': S[2]['out_a'] + 3.2, 'text': 'Step 1: kenalan dulu', 'pos': 'top'},
  {'from': S[3]['out_a'], 'to': S[3]['out_a'] + 3.4, 'text': 'Step 2: kenalan sama budayanya', 'pos': 'top'},
  {'from': S[6]['out_a'], 'to': S[6]['out_a'] + 3.2, 'text': 'Step 3: langsung dikuis 😆', 'pos': 'top'},
]
js = f"""// DIBUAT OTOMATIS oleh src/buat_timeline.py (Rancangan V1, ACC "ok").
export const CUTS = [{{src: 0.0, dur: {total}}}];
export const CAPTIONS = {json.dumps(caps, ensure_ascii=False)};
export const PROMO = null;
export const LABELS = {json.dumps(labels, ensure_ascii=False)};
export const OUTRO = {{from: {S[8]['out_a']}, to: {total}, q: 'Hari pertama: kenalan, belajar budaya,', q2: 'langsung kuis. Siap? 😆', handle: '@growwithupgruma'}};
export const LOGO_BUG = false;
export const END_CARD_SEC = 0;
export const WA = '';
export const MUSIC = null;
export const totalSec = () => CUTS.reduce((a, c) => a + c.dur, 0) + END_CARD_SEC;
"""
(P/'src'/'timeline.js').write_text(js)
(P/'src'/'meta.js').write_text(f"export const META = {{width: 1080, height: 1920, fps: 30, durationSec: {total}}};\n")
print('\n'.join(f"{c['from']:5.2f} " + ' '.join(w['text'] + ('*' if w.get('hl') else '') for w in c['words']) for c in caps))
