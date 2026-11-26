"""Gigi bungsu drg. Ainun (25 Nov 2026). Audio v2: suara dokter dibersihkan (mono, buang dengung ruangan 250 Hz, angkat kejelasan 3 kHz, gate ekor gema,
kompresi), suara ruangan klinik terus-menerus, whoosh tiap perpindahan, pop saat teks muncul, shimmer di penutup."""
import subprocess, sys
D, X, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOICE = ('pan=mono|c0=0.5*c0+0.5*c1,highpass=f=100,afftdn=nf=-28:nr=12,'
         'equalizer=f=250:t=q:w=1:g=-5,equalizer=f=500:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.4:g=4,'
         'agate=threshold=0.02:ratio=2.5:attack=5:release=150:range=0.25,'
         'acompressor=threshold=-24dB:ratio=3:attack=5:release=90:makeup=2,pan=stereo|c0=c0|c1=c0')
T = 55.3
P = [(0.15,'m0074',4.74,3.21,1.0,True),(3.45,'m0073',0.0,1.30,1.0,True),(4.9,'m0073',10.85,1.50,1.0,True),
     (6.6,'m0073',30.5,4.9,1.0,True),(11.6,'m0073',13.55,1.25,1.0,True),(13.0,'m0074',20.4,5.3,1.0,True),
     (20.4,'m0083',0.0,3.5,1.0,True),(24.1,'m0084',2.80,9.0,1.0,True),(33.3,'m0084',14.25,11.15,1.0,True),
     (44.6,'m0084',45.5,3.8,1.0,True)]
BOUND = [3.4,4.8,6.5,11.5,12.9,18.4,20.4,24.0,27.7,33.2,39.1,44.5,48.5,51.3]
POP = [0.1,6.6,13.0,18.5,24.1,33.3,44.6,48.6]
SFX = [('whoosh', b-0.18, -13) for b in BOUND] + [('pop', t, -15) for t in POP] + [('shimmer', 51.4, -14)]
a = ['ffmpeg','-nostdin','-v','error','-y']; fl = []; k = 0; lab = []
for g,c,i,d,v,vo in P:
    a += ['-i', f'{D}/{c}.mov']; ch = (VOICE+',') if vo else ''
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
