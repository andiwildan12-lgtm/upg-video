"""Suara latar non-musik GrowWith (Pak Dir 27 Nov: 'jangan yang musik'): klik kamera tiap foto beku + pop julukan, opsional suasana ruangan bersih (tanpa suara orang). Suara asli klip TIDAK dipakai.
Pakai: python3 sfx_saja.py VIDEO TL.json SFX_DIR OUT [AMBIENCE.mp3]"""
import subprocess, sys, json
V,TLF,X,O=sys.argv[1:5]; AMB=sys.argv[5] if len(sys.argv)>5 else None
tl=json.load(open(TLF)); T=tl['T']
ev=[('click',z['t']-0.02,-2) for z in tl['frz']]+[('pop',z['t']+0.4,-8) for z in tl['frz']]+[('pop',0.1,-8),('pop',36.6,-8),('pop',36.9,-8)]
a=['ffmpeg','-nostdin','-v','error','-y','-i',V]; fl=[]; lab=[]; k=1
if AMB:
    a+=['-stream_loop','-1','-i',AMB]; fl.append(f'[{k}:a]atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=4dB,afade=t=in:d=0.5,afade=t=out:st={T-1.5}:d=1.5[s{k}]'); lab.append(f'[s{k}]'); k+=1
for n,t,db in ev:
    a+=['-i',f'{X}/sfx_{n}.mp3']; fl.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,adelay={int(max(0,t)*1000)}|{int(max(0,t)*1000)}[s{k}]'); lab.append(f'[s{k}]'); k+=1
fl.append(f'anullsrc=r=48000:cl=stereo,atrim=0:{T}[z]'); lab.append('[z]')
fl.append(''.join(lab)+f'amix=inputs={len(lab)}:normalize=0,aresample=48000:async=1:first_pts=0,apad=whole_dur={T},atrim=0:{T},alimiter=limit=0.7:level=0,aresample=48000[a]')
a+=['-filter_complex',';'.join(fl),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',O]
subprocess.run(a,check=True); print('ok',O)
