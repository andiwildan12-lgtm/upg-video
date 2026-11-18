#!/usr/bin/env python3
"""Testimoni Bleaching V2: susun footage dasar (video + suara asli) dari daftar potongan.
Hasil: public/footage.mp4 (1080x1920, 30 fps) + work/peta.json (peta waktu untuk caption)."""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]; S = P; W = P/'work'/'build'; W.mkdir(parents=True, exist_ok=True)

# Segmen: suara dari (klip, a, b). Video: daftar (klip, mulai, durasi); total durasi video = durasi suara.
SEG = [
  dict(aud=('sumber/9529', 4.30, 8.66), vid=[('sumber/9529', 4.30, None)]),
  dict(aud=('sumber/9530', 0.15, 3.75), vid=[('sumber/9530', 0.15, None)]),
  dict(aud=('sumber/9532', 3.60, 10.15), vid=[('sumber/9532', 3.60, None)]),
  dict(aud=('sumber/9537', 6.80, 13.80), vid=[('sumber/9537', 6.80, None)]),
  dict(aud=('sumber/9538', 9.40, 12.55), vid=[('sumber/9538', 9.40, None)]),
  dict(aud=('sumber/9539', 0.35, 8.90), vid=[('sumber/9539', 0.35, 4.3), ('sumber/9543', 3.0, None)]),
  dict(aud=('sumber/9563', 7.00, 13.00), vid=[('sumber/9563', 3.0, 3.0), ('sumber/9563', 10.0, None)]),
  dict(aud=('sumber/9563', 27.00, 29.00), vid=[('sumber/9563', 27.0, None)]),
  dict(aud=('sumber/9551', 14.00, 19.50), vol=0.9, vid=[('sumber/9542', 0.3, None)]),
]
FPS = 30
def run(c): subprocess.run(c, check=True)
vparts, aparts, peta, t = [], [], [], 0.0
for i, s in enumerate(SEG):
    c, a, b = s['aud']; dur = round((b - a) * FPS) / FPS
    used = 0.0
    for j, (vc, vs, vd) in enumerate(s['vid']):
        vd = dur - used if vd is None else vd
        out = W/f'v{i:02d}{j}.mp4'
        run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(vs),'-i',str(S/f'{vc}.mp4'),'-t',f'{vd:.4f}','-an',
             '-vf',f'fps={FPS},scale=1080:1920,setsar=1','-c:v','libx264','-crf','14','-preset','fast',str(out)])
        vparts.append((str(out), vc, vs, vd)); used += vd
    ao = W/f'a{i:02d}.wav'
    fade = 0.04
    run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(a),'-i',str(S/f'{c}.mp4'),'-t',f'{dur:.4f}','-vn','-ac','2','-ar','48000',
         '-af',f"volume={s.get('vol',1)},afade=t=in:d={fade},afade=t=out:st={dur-fade:.3f}:d={fade}",str(ao)])
    aparts.append(str(ao)); peta.append(dict(seg=i, clip=c, src_a=a, out_a=t, dur=dur)); t += dur
(W/'vlist.txt').write_text(''.join(f"file '{p[0]}'\n" for p in vparts))
(W/'alist.txt').write_text(''.join(f"file '{p}'\n" for p in aparts))
(P/'work'/'peta.json').write_text(json.dumps(dict(total=t, seg=peta, vparts=vparts), indent=1))
print('total', round(t, 2))
