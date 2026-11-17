#!/usr/bin/env python3
"""Testimoni Bleaching V2b: tambah SFX transisi (whoosh ElevenLabs) + pop teks ke video final V2, remux tanpa render ulang.
SFX mentah di work/sfx/ (w2, w3 = whoosh; p1 = pop) dari flow ElevenLabs proyek ini."""
import subprocess
W = 'work/sfx/'
sub = lambda c: subprocess.run(c, check=True)
sub(['ffmpeg','-nostdin','-v','error','-y','-i',W+'w3.mp3','-ss','0.05','-t','0.95','-af','afade=t=out:st=0.7:d=0.25,loudnorm=I=-20:TP=-6','-ar','48000','-ac','2',W+'wa.wav'])
sub(['ffmpeg','-nostdin','-v','error','-y','-i',W+'w2.mp3','-ss','0.15','-t','0.95','-af','afade=t=out:st=0.7:d=0.25,loudnorm=I=-20:TP=-6','-ar','48000','-ac','2',W+'wb.wav'])
sub(['ffmpeg','-nostdin','-v','error','-y','-i',W+'p1.mp3','-t','0.35','-af','afade=t=out:st=0.2:d=0.15,loudnorm=I=-20:TP=-8','-ar','48000','-ac','2',W+'pop.wav'])
CUT = [3.33, 8.23, 17.93, 23.8, 27.87, 36.73, 38.03]      # batas segmen + awal end card (work/peta.json)
PEAK = {'wa.wav': 0.25, 'wb.wav': 0.30}                          # puncak whoosh jatuh tepat di potongan
ev = [('wa.wav' if i % 2 == 0 else 'wb.wav', c, 0.55) for i, c in enumerate(CUT)]
ev = [(f, max(0, c - PEAK[f]), v) for f, c, v in ev] + [('pop.wav', t, 0.5) for t in (0.05, 33.47, 38.23)]
ins, fc = ['-i', 'out/testimoni-bleaching-V2.mp4'], []
for k, (f, t, v) in enumerate(ev):
    ins += ['-i', W + f]; ms = int(t * 1000)
    fc.append(f'[{k+1}:a]adelay={ms}|{ms},volume={v}[s{k}]')
fc.append('[0:a]' + ''.join(f'[s{k}]' for k in range(len(ev))) + f'amix=inputs={len(ev)+1}:normalize=0:duration=first,alimiter=limit=0.85:level=false[a]')
sub(['ffmpeg','-nostdin','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','256k','out/testimoni-bleaching-V2b-transisi.mp4'])
