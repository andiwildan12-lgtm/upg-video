"""Audio GrowWith: suara asli lokasi dari base + suara ruangan klinik Ruma (m0700) menyambung + klik kamera saat foto beku + pop saat julukan; tanpa musik (belum ada musik berlisensi). Pakai: python3 mix_gw.py BASE TL.json SFX_DIR OUT"""
import subprocess, sys, json
B, TLF, X, OUT = sys.argv[1:5]; GAIN=float(sys.argv[5]) if len(sys.argv)>5 else 0.0; tl=json.load(open(TLF)); T=tl['T']
ev=[('click',z['t']-0.02,-8) for z in tl['frz']]+[('pop',z['t']+0.4,-15) for z in tl['frz']]+[('pop',0.1,-15),('pop',36.6,-15),('pop',36.9,-15)]
a=['ffmpeg','-nostdin','-v','error','-y','-i',B,'-stream_loop','-1','-i',f'{X}/m0700.mp4']; fl=['[0:a]volume=1.0[s0]',f'[1:a]atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,lowpass=f=2800,volume=0.35,afade=t=in:d=0.3,afade=t=out:st={T-1.5}:d=1.5[rt]']; lab=['[s0]','[rt]']
for k,(n,t,db) in enumerate(ev,2):
    a+=['-i',f'{X}/sfx_{n}.mp3']; fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,adelay={int(max(0,t)*1000)}|{int(max(0,t)*1000)}[s{k}]'); lab.append(f'[s{k}]')
fl.append(''.join(lab)+f'amix=inputs={len(lab)}:normalize=0,aresample=48000:async=1:first_pts=0,apad=whole_dur={T},atrim=0:{T},volume={GAIN}dB,alimiter=limit=0.7:attack=3:release=60:level=0,aresample=48000[out]')
a+=['-filter_complex',';'.join(fl),'-map','[out]','-c:a','pcm_s16le',OUT]; subprocess.run(a,check=True); print('ok',len(lab))
