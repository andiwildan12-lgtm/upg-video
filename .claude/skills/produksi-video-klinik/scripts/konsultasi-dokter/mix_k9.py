"""Gigi bungsu dicabut, drg. Akbar (25 Nov 2026). Audio v2: suara dokter dibersihkan (mono, buang dengung ruangan 250 Hz, angkat kejelasan 3 kHz, gate ekor gema,
kompresi), suara ruangan klinik terus-menerus, whoosh tiap perpindahan, pop saat teks muncul, shimmer di penutup."""
import subprocess, sys
D, X, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOICE = ('pan=mono|c0=0.5*c0+0.5*c1,highpass=f=100,afftdn=nf=-28:nr=12,'
         'equalizer=f=250:t=q:w=1:g=-5,equalizer=f=500:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.4:g=4,'
         'agate=threshold=0.02:ratio=2.5:attack=5:release=150:range=0.25,'
         'acompressor=threshold=-24dB:ratio=3:attack=5:release=90:makeup=2,pan=stereo|c0=c0|c1=c0')
T = 56.6
P = [(0.1,'a0099',0.0,1.2,1.0,True),(3.0,'a0099',7.80,5.15,1.0,True),(8.35,'a0106',0.0,4.4,1.0,True),(12.95,'a0106',7.5,3.8,1.0,True),
     (16.95,'a0102',0.0,6.25,1.0,True),(23.4,'a0102',13.2,6.95,1.0,True),(30.6,'a0102',21.15,3.53,1.0,True),(34.35,'a0112',0.0,2.15,1.0,True),
     (36.5,'a0131',13.0,4.0,0.25,False),(40.6,'a0149',0.0,6.3,1.0,True),(47.05,'a0153',0.0,2.9,1.0,True),(50.0,'a0131',24.0,2.6,0.20,False)]
BOUND = [2.9,8.3,16.9,34.3,36.5,40.5,47.0,50.0,52.6]
PUNCH = [12.9,23.3,30.5]
POP = [0.1,3.0,8.4,17.0,34.4,40.6,50.1]
SFX = [('whoosh', b-0.18, -13) for b in BOUND] + [('whoosh', b-0.18, -20) for b in PUNCH] + [('pop', t, -15) for t in POP] + [('shimmer', 52.7, -14)]
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
