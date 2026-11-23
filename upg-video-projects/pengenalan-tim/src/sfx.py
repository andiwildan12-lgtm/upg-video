#!/usr/bin/env python3
"""SFX: whoosh di tiap pergantian orang + pop saat label/kartu muncul. Tanpa musik (lagu trending ditambah saat unggah)."""
import json, re, subprocess
W = 'work/sfx/'; sub = lambda c: subprocess.run(c, check=True)
seg = json.loads(re.search(r'export const SEG = (\[.*?\]);', open('src/timeline.js').read(), re.S).group(1))
T = seg[-1]['start'] + seg[-1]['dur']
ev = []
for i, s in enumerate(seg[1:], 1):
    ev.append(('wa.wav' if i % 2 else 'wb.wav', max(0, s['start'] - 0.27), 0.55))
    if s['name']: ev.append(('pop.wav', s['start'] + 0.05, 0.5))
ev += [('pop.wav', 0.15, 0.6), ('pop.wav', 0.75, 0.6), ('pop.wav', seg[-1]['start'] + 0.2, 0.6), ('pop.wav', seg[-1]['start'] + 0.9, 0.7)]
ins, fc = ['-f', 'lavfi', '-t', str(T), '-i', 'anullsrc=r=48000:cl=stereo'], []
for k, (f, t, v) in enumerate(ev):
    ins += ['-i', W + f]; ms = int(t * 1000); fc.append(f'[{k+2}:a]adelay={ms}|{ms},volume={v}[s{k}]')
fc.append('[1:a]' + ''.join(f'[s{k}]' for k in range(len(ev))) + f'amix=inputs={len(ev)+1}:normalize=0:duration=first,loudnorm=I=-14:TP=-2,alimiter=limit=0.8:level=false,aresample=48000[a]')
sub(['ffmpeg','-nostdin','-v','error','-y','-i','out/pengenalan-tim-V1b.mp4',*ins,'-filter_complex',';'.join(fc),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','out/pengenalan-tim-V1b-sfx.mp4'])
print(len(ev), 'sfx')
