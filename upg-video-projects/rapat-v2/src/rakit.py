#!/usr/bin/env python3
"""Rakit public/footage.mp4: potongan (edit.py) + blur layar (blur.py) + level suara per segmen -16 LUFS lalu loudnorm -14."""
import json, subprocess
from pathlib import Path
P = Path(__file__).resolve().parents[1]; W = P/'work'/'build'
run = lambda c: subprocess.run(c, check=True)
pe = json.loads((P/'work'/'peta.json').read_text())
vs = [p[0].replace('.mp4', '-b.mp4') if Path(p[0].replace('.mp4', '-b.mp4')).exists() else p[0] for p in pe['vparts']]
ins = sum([['-i', v] for v in vs], [])
fc = ''.join(f'[{i}:v]fps=30,format=yuv420p,setsar=1[v{i}];' for i in range(len(vs))) + ''.join(f'[v{i}]' for i in range(len(vs))) + f'concat=n={len(vs)}:v=1:a=0[v]'
run(['ffmpeg','-nostdin','-v','error','-y',*ins,'-filter_complex',fc,'-map','[v]','-c:v','libx264','-crf','16','-preset','medium',str(W/'video.mp4')])
aw = []
for i in range(len(pe['seg'])):
    o = W/f'a{i:02d}n.wav'
    run(['ffmpeg','-nostdin','-v','error','-y','-i',str(W/f'a{i:02d}.wav'),'-af','loudnorm=I=-16:TP=-2:LRA=11','-ar','48000','-ac','2',str(o)]); aw.append(o)
ins = sum([['-i', str(a)] for a in aw], [])
fc = ''.join(f'[{i+1}:a]' for i in range(len(aw))) + f'concat=n={len(aw)}:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]'
run(['ffmpeg','-nostdin','-v','error','-y','-i',str(W/'video.mp4'),*ins,'-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','256k','-shortest',str(P/'public'/'footage.mp4')])
print('ok', P/'public'/'footage.mp4')
