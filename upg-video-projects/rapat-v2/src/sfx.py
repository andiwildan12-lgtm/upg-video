#!/usr/bin/env python3
"""Rapat V2: whoosh di pergantian segmen + pop tipis saat kata kunci/ikon/kartu muncul; remux tanpa render ulang."""
import json, re, subprocess
W = 'work/sfx/'
sub = lambda c: subprocess.run(c, check=True)
sub(['ffmpeg','-nostdin','-v','error','-y','-i',W+'w3.mp3','-ss','0.05','-t','0.95','-af','afade=t=out:st=0.7:d=0.25,loudnorm=I=-20:TP=-6','-ar','48000','-ac','2',W+'wa.wav'])
sub(['ffmpeg','-nostdin','-v','error','-y','-i',W+'w2.mp3','-ss','0.15','-t','0.95','-af','afade=t=out:st=0.7:d=0.25,loudnorm=I=-20:TP=-6','-ar','48000','-ac','2',W+'wb.wav'])
sub(['ffmpeg','-nostdin','-v','error','-y','-i',W+'p1.mp3','-t','0.35','-af','afade=t=out:st=0.2:d=0.15,loudnorm=I=-20:TP=-8','-ar','48000','-ac','2',W+'pop.wav'])
pe = json.load(open('work/peta.json')); S = pe['seg']
tl = open('src/timeline.js').read()
def starts(name):
    arr = json.loads(re.search(rf'export const {name} = (\[.*?\]);\n', tl, re.S).group(1)); return [x['from'] for x in arr]
cuts = [s['out_a'] for s in S[1:]]
pops = sorted(set(round(x, 2) for x in starts('KEYS') + starts('ICONS') + starts('CARDS')))
PEAK = {'wa.wav': 0.25, 'wb.wav': 0.30}
ev = [(('wa.wav' if i % 2 == 0 else 'wb.wav'), c, 0.5) for i, c in enumerate(cuts)]
ev = [(f, max(0, c - PEAK[f]), v) for f, c, v in ev] + [('pop.wav', t, 0.35) for t in pops]
ins, fc = ['-i', 'out/rapat-v2-V2.mp4'], []
for k, (f, t, v) in enumerate(ev):
    ins += ['-i', W + f]; ms = int(t * 1000)
    fc.append(f'[{k+1}:a]adelay={ms}|{ms},volume={v}[s{k}]')
fc.append('[0:a]' + ''.join(f'[s{k}]' for k in range(len(ev))) + f'amix=inputs={len(ev)+1}:normalize=0:duration=first,alimiter=limit=0.85:level=false[a]')
sub(['ffmpeg','-nostdin','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','256k','out/rapat-v2-V2-transisi.mp4'])
print(len(cuts), 'whoosh,', len(pops), 'pop')
