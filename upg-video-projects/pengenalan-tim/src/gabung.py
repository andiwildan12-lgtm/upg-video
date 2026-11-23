#!/usr/bin/env python3
"""Gabung hook + klip orang yang bingkainya dikunci + latar penutup -> public/footage.mp4."""
import subprocess
from pathlib import Path
P = Path(__file__).resolve().parents[1]; B = P/'work'/'build'
parts = [B/'p00.mp4'] + [B/f'p{i:02d}s.mp4' for i in range(1, 19)] + [B/'p19.mp4']
ins = sum([['-i', str(p)] for p in parts], [])
fc = ''.join(f'[{i}:v]fps=30,format=yuv420p,setsar=1[v{i}];' for i in range(len(parts))) + ''.join(f'[v{i}]' for i in range(len(parts))) + f'concat=n={len(parts)}:v=1:a=0[v]'
subprocess.run(['ffmpeg','-nostdin','-v','error','-y',*ins,'-filter_complex',fc,'-map','[v]','-c:v','libx264','-crf','16','-preset','medium',str(P/'public'/'footage.mp4')], check=True)
print('ok')
