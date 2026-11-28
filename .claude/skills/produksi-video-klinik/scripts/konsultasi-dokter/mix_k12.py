"""Testimoni Kak Canon (28 Nov 2026). Audio v2: suara dokter dibersihkan (mono, buang dengung ruangan 250 Hz, angkat kejelasan 3 kHz, gate ekor gema,
kompresi), suara ruangan klinik terus-menerus, whoosh tiap perpindahan, pop saat teks muncul, shimmer di penutup."""
import subprocess, sys
D, X, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOICE = ('pan=mono|c0=0.5*c0+0.5*c1,highpass=f=100,afftdn=nf=-28:nr=12,'
         'equalizer=f=250:t=q:w=1:g=-5,equalizer=f=500:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.4:g=4,'
         'agate=threshold=0.02:ratio=2.5:attack=5:release=150:range=0.25,'
         'acompressor=threshold=-24dB:ratio=3:attack=5:release=90:makeup=2,pan=stereo|c0=c0|c1=c0')
T = 32.9
P = [(0.1,'t_canon',52.55,5.95,1.0,True),(6.25,'t_canon',8.85,3.4,1.0,True),(9.75,'t_canon',19.05,2.35,1.0,True),(12.3,'t_canon',62.35,7.95,1.0,True),
     (20.2,'t_canon',74.95,2.95,1.0,True),(24.1,'t_canon',88.85,1.1,1.0,True)]
BOUND = [6.2,12.2,16.2,20.1,23.7,26.1,28.9]
PUNCH = [9.6]
POP = [0.1,0.4,6.3,12.35,23.75,26.2]
SFX = [('book', b-0.18, -12) for b in BOUND] + [('book', b-0.18, -19) for b in PUNCH] + [('pop', t, -15) for t in POP] + [('shimmer', 29.0, -14)]
a = ['ffmpeg','-nostdin','-v','error','-y']; fl = []; k = 0; lab = []
for g,c,i,d,v,vo in P:
    a += ['-i', f'{D}/{c}.mp4']; ch = (VOICE+',') if vo else ''
    fl.append(f'[{k}:a]atrim={i}:{i+d},asetpts=PTS-STARTPTS,aresample=48000,{ch}aformat=channel_layouts=stereo,volume={v},'
              f'afade=t=in:d=0.08,afade=t=out:st={d-0.1:.2f}:d=0.1,adelay={int(g*1000)}|{int(g*1000)}[s{k}]'); lab.append(f'[s{k}]'); k += 1
# suara ruangan klinik terus-menerus (klip 0700 tanpa bicara, diulang), pelan & redup
a += ['-stream_loop','-1','-i', f'{X}/m0700.mp4']
fl.append(f'[{k}:a]atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,lowpass=f=2800,volume=0.09,'
          f'afade=t=in:d=0.4,afade=t=out:st={T-2.5}:d=2.5[s{k}]'); lab.append(f'[s{k}]'); k += 1
for nm,t,db in SFX:
    a += ['-i', f'{X}/sfx_{nm}.mp3']
    fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,adelay={int(max(0,t)*1000)}|{int(max(0,t)*1000)}[s{k}]'); lab.append(f'[s{k}]'); k += 1
fl.append(f'anullsrc=r=48000:cl=stereo,atrim=0:{T}[z0]'); lab.append('[z0]'); k += 1  # jangkar waktu: lapisan hening mulai detik 0
fl.append(''.join(lab)+f'amix=inputs={k}:normalize=0,aresample=48000:async=1:first_pts=0,apad=whole_dur={T},atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=11,aresample=48000[out]')
a += ['-filter_complex', ';'.join(fl), '-map', '[out]', '-c:a', 'pcm_s16le', OUT]
subprocess.run(a, check=True); print('ok', k, 'lapisan')
