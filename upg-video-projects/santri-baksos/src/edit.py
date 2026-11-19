#!/usr/bin/env python3
"""Rapat Dokter V2: susun footage dasar (video + suara asli) dari daftar potongan.
Hasil: public/footage.mp4 (1080x1920, 30 fps) + work/peta.json (peta waktu untuk caption)."""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]; S = P/'sumber'; W = P/'work'/'build'; W.mkdir(parents=True, exist_ok=True)

# Segmen: suara dari (klip, a, b). Video: daftar (klip, mulai, durasi); total durasi video = durasi suara.
SEG = [  # Baksos santri Ponpes Bilal Bin Robah (tanpa ucapan; suara suasana)
  dict(aud=('131045111', 2.0, 6.0), vid=[('131045111', 2.0, None)]),     # rombongan datang
  dict(aud=('131202244', 7.0, 10.5), vid=[('131202244', 7.0, None)]),    # registrasi
  dict(aud=('131321932', 4.0, 7.0), vid=[('131321932', 4.0, None)]),     # isi formulir
  dict(aud=('131601532', 2.0, 5.0), vid=[('131601532', 2.0, None)]),     # ruang tunggu
  dict(aud=('131722676', 3.0, 6.0), vid=[('131722676', 3.0, None)]),
  dict(aud=('131454045', 4.0, 7.5), vid=[('131454045', 4.0, None)]),     # perawatan
  dict(aud=('132429847', 2.0, 5.0), vid=[('132429847', 2.0, None)]),
  dict(aud=('132506729', 5.0, 8.5), vid=[('132506729', 5.0, None)]),
  dict(aud=('132224426', 12.0, 16.5), vid=[('132224426', 12.0, None)]),  # bingkisan
  dict(aud=('131845153', 0.5, 3.5), vid=[('131845153', 0.5, None)]),
  dict(aud=('131755407', 3.0, 9.5), vid=[('131755407', 3.0, None)]),     # penutup: ngobrol & senyum
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
