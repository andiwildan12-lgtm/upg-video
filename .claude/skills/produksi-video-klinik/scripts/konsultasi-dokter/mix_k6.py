"""Karang tebal sebelah, drg. Ainun scaling (25 Nov 2026). Audio v2: suara dokter dibersihkan (mono, buang dengung ruangan 250 Hz, angkat kejelasan 3 kHz, gate ekor gema,
kompresi), suara ruangan klinik terus-menerus, whoosh tiap perpindahan, pop saat teks muncul, shimmer di penutup."""
import subprocess, sys
D, X, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOICE = ('pan=mono|c0=0.5*c0+0.5*c1,highpass=f=100,afftdn=nf=-28:nr=12,'
         'equalizer=f=250:t=q:w=1:g=-5,equalizer=f=500:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.4:g=4,'
         'agate=threshold=0.02:ratio=2.5:attack=5:release=150:range=0.25,'
         'acompressor=threshold=-24dB:ratio=3:attack=5:release=90:makeup=2,pan=stereo|c0=c0|c1=c0')
T = 52.9
P = [(0.1,'d0035',12.90,5.05,1.0,True),(5.4,'d0035',18.85,3.35,1.0,True),(8.85,'d0035',26.05,5.70,1.0,True),
     (14.75,'d0035',35.45,3.50,1.0,True),(18.45,'d0035',40.50,1.45,1.0,True),(20.1,'d0037',4.45,1.45,1.0,True),
     (21.8,'d0040',3.0,2.2,0.30,False),(24.0,'d0048',4.0,2.4,0.30,False),
     (26.55,'d0058',7.15,10.55,1.0,True),(37.25,'d0060',0.0,4.5,1.0,True),(41.85,'d0060',7.00,4.15,1.0,True),
     (46.1,'d0050',2.5,2.8,0.20,False)]
BOUND = [5.3,8.8,14.7,18.4,20.0,21.8,24.0,26.4,30.1,37.2,41.8,46.1,48.9]
POP = [0.1,5.4,18.45,26.5,46.2]
SFX = [('whoosh', b-0.18, -13) for b in BOUND] + [('pop', t, -15) for t in POP] + [('shimmer', 49.0, -14)]
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
