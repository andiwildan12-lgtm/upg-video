"""Pantangan setelah cabut gigi, drg. Akbar (25 Nov 2026). Audio v2: suara dokter dibersihkan (mono, buang dengung ruangan 250 Hz, angkat kejelasan 3 kHz, gate ekor gema,
kompresi), suara ruangan klinik terus-menerus, whoosh tiap perpindahan, pop saat teks muncul, shimmer di penutup."""
import subprocess, sys
D, X, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOICE = ('pan=mono|c0=0.5*c0+0.5*c1,highpass=f=100,afftdn=nf=-28:nr=12,'
         'equalizer=f=250:t=q:w=1:g=-5,equalizer=f=500:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.4:g=4,'
         'agate=threshold=0.02:ratio=2.5:attack=5:release=150:range=0.25,'
         'acompressor=threshold=-24dB:ratio=3:attack=5:release=90:makeup=2,pan=stereo|c0=c0|c1=c0')
T = 54.35
P = [(0.05,'a0150',0.0,3.65,1.0,True),(3.8,'a0150',6.55,8.0,1.0,True),(11.95,'a0150',16.10,3.45,1.0,True),(15.5,'a0150',78.25,7.15,1.0,True),
     (22.85,'a0150',90.6,7.35,1.0,True),(30.45,'a0150',102.25,5.1,1.0,True),(35.7,'a0152',0.0,4.7,1.0,True),(40.45,'a0152',18.2,7.35,1.0,True)]
BOUND = [3.7,15.45,18.05,22.75,35.65,47.85,50.35]
PUNCH = [11.85,30.35,39.95]
POP = [0.1,3.75,16.8,18.92,21.5,36.08,42.63,47.95]
# Uji coba Pak Dir 26 Nov: suara transisi 'kertas dibalik' (sfx_book) menggantikan whoosh
SFX = [('book', b-0.18, -12) for b in BOUND] + [('book', b-0.18, -19) for b in PUNCH] + [('pop', t, -15) for t in POP] + [('shimmer', 50.45, -14)]
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
