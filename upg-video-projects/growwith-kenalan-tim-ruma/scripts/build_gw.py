"""GrowWith 'Kenalan sama tim Ruma Dental' (27 Nov 2026): base video (klip hidup 1,5 dtk + foto beku 1,6 dtk per orang) + audio.
Overlay (kartu, foto miring, latar blur) dari ov.html per frame. Pakai: python3 build_gw.py RAW OUT_DIR"""
import subprocess, sys, json
RAW, OUT = sys.argv[1], sys.argv[2]
ORD = ['e101547','v102119','m0010','v102351','v102204','e101715','e101614','m0024','e101647','m0027','m0019']
HOOK, LIVE, FRZ, END = 2.5, 1.5, 1.6, 3.0
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
segs=[('live','e101547',0.0,HOOK)]; tl=[]; t=HOOK
for i,n in enumerate(ORD):
    d=dur(f'{RAW}/{n}.mp4'); fz=round(d*0.82,2); a=max(0,fz-LIVE)
    segs.append(('live',n,a,fz-a)); t+=fz-a
    segs.append(('frz',n,fz,FRZ)); tl.append({'i':i+1,'t':round(t,3)}); t+=FRZ
segs.append(('end',None,0,END)); T=t+END
a=['ffmpeg','-nostdin','-v','error','-y']; fv=[]; fa=[]; k=0
for kind,n,s,d in segs:
    if kind=='live':
        a+=['-ss',str(s),'-t',str(d),'-i',f'{RAW}/{n}.mp4']
        fv.append(f'[{k}:v]scale=1080:1920,fps=30,setsar=1,trim=0:{d},setpts=PTS-STARTPTS[v{k}]')
        fa.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{d},asetpts=PTS-STARTPTS,volume=0.8,afade=t=in:d=0.04,afade=t=out:st={max(0,d-0.05):.2f}:d=0.05[a{k}]')
    else:
        a+=['-f','lavfi','-t',str(d),'-i','color=c=black:s=1080x1920:r=30']
        fv.append(f'[{k}:v]setsar=1[v{k}]')
        a+=['-f','lavfi','-t',str(d),'-i','anullsrc=r=48000:cl=stereo']; k+=1
        fa.append(f'[{k}:a]atrim=0:{d}[a{k-1}]')
    k+=1
nv=len(segs); lab=''.join(f'[v{j}]' for j in [i for i in range(k) if f'[v{i}]' in ';'.join(fv)])
labs=[x.split('[')[-1][:-1] for x in fv]; labsa=[x.split('[')[-1][:-1] for x in fa]
fl=fv+fa+[''.join(f'[{x}]' for x in labs)+f'concat=n={len(labs)}:v=1:a=0[vo]',''.join(f'[{x}]' for x in labsa)+f'concat=n={len(labsa)}:v=0:a=1[ao]']
a+=['-filter_complex',';'.join(fl),'-map','[vo]','-map','[ao]','-c:v','libx264','-crf','17','-pix_fmt','yuv420p','-c:a','pcm_s16le',f'{OUT}/base.mkv']
subprocess.run(a,check=True)
json.dump({'T':round(T,3),'frz':tl,'hook':HOOK,'frzdur':FRZ},open(f'{OUT}/tl.json','w'))
print('T',round(T,2),tl)
