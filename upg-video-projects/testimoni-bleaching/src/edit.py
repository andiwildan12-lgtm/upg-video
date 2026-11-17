#!/usr/bin/env python3
"""Testimoni Bleaching V2: susun footage dasar (video + suara asli) dari daftar potongan.
Hasil: public/footage.mp4 (1080x1920, 30 fps) + work/peta.json (peta waktu untuk caption)."""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]; S = P; W = P/'work'/'build'; W.mkdir(parents=True, exist_ok=True)

# Segmen: suara dari (klip, a, b). Video: daftar (klip, mulai, durasi); total durasi video = durasi suara.
SEG = [  # klip testimoni: 'sumber/NNNN', klip proses: 'proses/NNNN'
  dict(aud=('sumber/0510', 1.40, 4.72), vid=[('sumber/0510', 1.40, None)]),
  dict(aud=('sumber/0510', 6.85, 11.76), vid=[('proses/0460', 1.5, None)]),
  dict(aud=('sumber/0510', 11.76, 21.45), vid=[('sumber/0510', 11.76, 3.7), ('proses/0453', 5.0, 2.9), ('proses/0466', 7.0, None)]),
  dict(aud=('sumber/0510', 21.90, 27.75), vid=[('sumber/0510', 21.90, 1.6), ('proses/0472', 3.5, 2.3), ('proses/0469', 2.5, None)]),
  dict(aud=('sumber/0507', 13.02, 17.07), vid=[('sumber/0507', 13.02, None)]),
  dict(aud=('sumber/0516', 8.88, 17.75), vid=[('sumber/0516', 8.88, None)]),
  dict(aud=('sumber/0517', 13.36, 14.65), vid=[('sumber/0517', 13.36, None)]),
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
