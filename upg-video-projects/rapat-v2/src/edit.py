#!/usr/bin/env python3
"""Rapat Dokter V2: susun footage dasar (video + suara asli) dari daftar potongan.
Hasil: public/footage.mp4 (1080x1920, 30 fps) + work/peta.json (peta waktu untuk caption)."""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]; S = P/'sumber'; W = P/'work'/'build'; W.mkdir(parents=True, exist_ok=True)

# Segmen: suara dari (klip, a, b). Video: daftar (klip, mulai, durasi); total durasi video = durasi suara.
SEG = [  # Rapat Dokter V2 rekonstruksi (adu pendapat, tanpa bahasa direktur/mitra)
  dict(aud=('0584', 33.62, 36.85), vid=[('0584', 33.62, None)]),                                   # 0 buka lebar-lebar
  dict(aud=('0599', 34.95, 36.80), vid=[('0599', 34.95, None)]),                                   # 1 saranku keep silent
  dict(aud=('0591', 2.0, 3.4), vol=0.6, vid=[('0591', 0.2, None)]),                                # 2 kartu judul (tawa)
  dict(aud=('0543', 8.15, 17.45), vid=[('0543', 8.15, 4.0), ('0544', 1.0, 2.3), ('0543', 14.45, None)]),  # 3 perkembangan
  dict(aud=('0551', 0.65, 4.70), vid=[('0551', 0.65, None)]),                                      # 4 masih ada celah
  dict(aud=('0584', 5.0, 13.95), vid=[('0584', 5.0, 4.5), ('0549', 2.0, 2.0), ('0584', 11.5, None)]),     # 5 lihat rapor, wajar
  dict(aud=('0584', 20.9, 27.0), vid=[('0584', 20.9, 3.5), ('0553', 0.7, None)]),                  # 6 motivasi tahun depan
  dict(aud=('0588', 0.0, 8.95), vid=[('0588', 0.0, 4.0), ('0592', 1.5, 2.5), ('0588', 6.5, None)]),      # 7 di bawah / di atas
  dict(aud=('0599', 4.6, 12.1), vid=[('0599', 4.6, 4.5), ('0579', 3.5, None)]),                    # 8 takut kasus sulit
  dict(aud=('0599', 27.6, 36.6), vid=[('0599', 27.6, 4.0), ('0544', 5.5, 2.0), ('0599', 33.6, None)]),    # 9 dua sisi, keep silent
  dict(aud=('0599', 38.3, 40.15), vid=[('0553', 3.0, None)]),                                      # 10 gak usah terbuka
  dict(aud=('0599', 45.8, 46.6), vid=[('0599', 45.8, None)]),                                      # 11 setuju
  dict(aud=('0591', 3.4, 6.2), vol=0.7, vid=[('0549', 18.5, None)]),                               # 12 penutup tawa
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
