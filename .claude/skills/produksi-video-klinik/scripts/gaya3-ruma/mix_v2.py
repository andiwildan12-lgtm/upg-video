"""Audio v2: suara dokter dibersihkan (mono, buang dengung ruangan 250 Hz, angkat kejelasan 3 kHz, gate ekor gema,
kompresi), suara ruangan klinik terus-menerus, whoosh tiap perpindahan, pop saat teks muncul, shimmer di penutup."""
import subprocess, sys
D, X, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
T = 40.4
VOICE = ('pan=mono|c0=0.5*c0+0.5*c1,highpass=f=100,afftdn=nf=-28:nr=12,'
         'equalizer=f=250:t=q:w=1:g=-5,equalizer=f=500:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.4:g=4,'
         'agate=threshold=0.02:ratio=2.5:attack=5:release=150:range=0.25,'
         'acompressor=threshold=-24dB:ratio=3:attack=5:release=90:makeup=2,pan=stereo|c0=c0|c1=c0')
# (detik global, klip, in, durasi, volume, rantai suara?)
P = [(0.0,'m0671',2.0,3.0,0.28,False),(3.0,'m0708',0.0,9.4,1.0,True),(12.4,'m0709',1.0,7.2,1.0,True),
     (19.6,'m0695',2.0,3.0,0.28,False),(22.6,'m0687',1.5,3.0,0.28,False),(25.6,'v125349',2.0,4.0,0.18,False),
     (25.8,'m0712',6.80,3.48,1.0,True),(29.6,'v172352',2.0,3.6,0.18,False),(29.8,'m0712',10.28,3.12,1.0,True)]
BOUND = [3.0, 12.4, 19.6, 22.6, 25.6, 29.6, 33.2, 36.4]   # ganti klip -> whoosh
PUNCH = [8.13, 17.9]                                          # punch-in kalimat dokter -> whoosh pelan
POP = [0.15, 3.4, 19.75, 22.75, 25.75, 29.75, 33.35]
CLICK = [33.55, 33.85, 34.15]                                 # centang kartu
SFX = [('whoosh', b-0.18, -13) for b in BOUND] + [('whoosh', b-0.15, -20) for b in PUNCH] + \
      [('pop', t, -15) for t in POP] + [('click', t, -17) for t in CLICK] + [('shimmer', 36.5, -14)]
a = ['ffmpeg','-nostdin','-v','error','-y']; fl = []; k = 0; lab = []
for g,c,i,d,v,vo in P:
    a += ['-i', f'{D}/{c}.mp4']; ch = (VOICE+',') if vo else ''
    fl.append(f'[{k}:a]atrim={i}:{i+d},asetpts=PTS-STARTPTS,aresample=48000,{ch}aformat=channel_layouts=stereo,volume={v},'
              f'afade=t=in:d=0.08,afade=t=out:st={d-0.1:.2f}:d=0.1,adelay={int(g*1000)}|{int(g*1000)}[s{k}]'); lab.append(f'[s{k}]'); k += 1
# suara ruangan klinik terus-menerus (klip 0700 tanpa bicara, diulang), pelan & redup
a += ['-stream_loop','-1','-i', f'{D}/m0700.mp4']
fl.append(f'[{k}:a]atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,lowpass=f=2800,volume=0.09,'
          f'afade=t=in:d=0.4,afade=t=out:st={T-2.5}:d=2.5[s{k}]'); lab.append(f'[s{k}]'); k += 1
for nm,t,db in SFX:
    a += ['-i', f'{X}/sfx_{nm}.mp3']
    fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,adelay={int(max(0,t)*1000)}|{int(max(0,t)*1000)}[s{k}]'); lab.append(f'[s{k}]'); k += 1
fl.append(''.join(lab)+f'amix=inputs={k}:normalize=0,apad=whole_dur={T},atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=11,aresample=48000[out]')
a += ['-filter_complex', ';'.join(fl), '-map', '[out]', '-c:a', 'pcm_s16le', OUT]
subprocess.run(a, check=True); print('ok', k, 'lapisan')
