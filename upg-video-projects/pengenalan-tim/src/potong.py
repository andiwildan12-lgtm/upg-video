#!/usr/bin/env python3
"""Potong momen terbaik tiap orang (tanpa suara) -> public/footage.mp4 + src/timeline.js."""
import json, subprocess
from pathlib import Path
P = Path(__file__).resolve().parents[1]; W = P/'work'/'build'
D = 1.35
SEG = [  # (klip, mulai, durasi, nama, peran)
  ('9387', 9.8, 3.0, None, None),
  ('9421', 0.9, D, 'drg. Ayu', 'Dokter Gigi & Kepala Klinik'),
  ('9419', 10.3, D, 'drg. Adan', 'Dokter Gigi'),
  ('9422', 0.8, D, 'drg. Arham', 'Dokter Gigi'),
  ('9403', 5.8, D, 'Kak Rahma', 'Perawat Gigi'),
  ('9426', 0.6, D, 'Kak Suci', 'Perawat Gigi'),
  ('9431', 0.2, D, 'Kak Saldi', 'Perawat Gigi'),
  ('9395', 0.4, D, 'Kak Uswa', 'Admin Rekam Medis'),
  ('9396', 7.4, D, 'Kak Inna', 'Admin Rekam Medis'),
  ('9397', 0.4, D, 'Kak Ain', 'Admin Rekam Medis'),
  ('9450', 0.2, D, 'Kak Niar', 'Admin Online'),
  ('9454', 0.6, D, 'Pak Indra', 'Manajer Operasional'),
  ('9452', 1.6, D, 'Pak Bayu', 'Manajer Marketing'),
  ('9441', 5.2, D, 'Kak Fiska', 'Staf Keuangan'),
  ('9429', 0.8, D, 'Pak Eko', 'Staf Purchasing'),
  ('9457', 0.9, D, 'Kak Egi', 'Staf HR'),
  ('9456', 5.9, D, 'Kak Tika', 'Desain Grafis'),
  ('9461', 1.3, D, 'Kak Dwi', 'Spesialis Media Sosial'),
  ('9390', 0.5, 2.2, 'Kak Abdur', 'Helper'),
  ('9389', 10.0, 3.0, None, None),   # latar kartu penutup
]
run = lambda c: subprocess.run(c, check=True)
parts, tl, t = [], [], 0.0
for i, (c, s, d, nm, rl) in enumerate(SEG):
    o = W/f'p{i:02d}.mp4'
    run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(s),'-i',str(P/'sumber'/f'{c}.mov'),'-t',str(d),'-an',
         '-vf','fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p',
         '-c:v','libx264','-crf','16','-preset','medium',str(o)])
    parts.append(o); tl.append(dict(clip=c, start=round(t, 3), dur=d, name=nm, role=rl)); t += d
ins = sum([['-i', str(p)] for p in parts], [])
fc = ''.join(f'[{i}:v]' for i in range(len(parts))) + f'concat=n={len(parts)}:v=1:a=0[v]'
run(['ffmpeg','-nostdin','-v','error','-y',*ins,'-filter_complex',fc,'-map','[v]','-c:v','libx264','-crf','16','-preset','medium',str(P/'public'/'footage.mp4')])
(P/'src'/'timeline.js').write_text(f"// DIBUAT OTOMATIS oleh src/potong.py\nexport const SEG = {json.dumps(tl, ensure_ascii=False)};\nexport const TOTAL = {round(t, 3)};\n")
print('total', round(t, 2))
