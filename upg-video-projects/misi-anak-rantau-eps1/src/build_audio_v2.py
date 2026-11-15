#!/usr/bin/env python3
"""V2: satu file per baris (dengan tag emosi) -> susun dialog + suasana. Tulis audio/narasi.wav & work/timing-v2.json.
Pakai: python3 src/build_audio_v2.py [durasi_sampel]"""
import json, subprocess, pathlib, sys
P=pathlib.Path(__file__).resolve().parents[1]; V=P/'audio/v2'
# (file, penutur, jeda sebelum baris [dtk], kata disorot)
SEQ=[('L00','N',0.5,['coto,','macet…','darah']),('L01','I',0.15,['normal,']),('L02','D',0.45,['darah.']),
     ('L03','N',1.0,['janji']),('L04','I',0.35,['sendiri!']),('L05','I',2.3,[]),('L06','N',1.0,['katanya.'])]
AMB=[('sfx-mandi',0.0,'s1',0.22),('sfx-malam','s2','s3',0.18)]  # (file, mulai, selesai, volume) — mulai/selesai = waktu/kunci adegan
t=0; lines=[]
for f,sp,gap,hl in SEQ:
    t+=gap; dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(V/f'{f}.mp3')]))
    ws=[w for w in json.load(open(V/f'{f}.json'))['words'] if w.get('type','word')=='word' and not (w['text'].startswith('[') or w['text'].endswith(']'))]
    lines.append({'f':f,'sp':sp,'at':round(t,3),'s':round(t+ws[0]['start'],3),'e':round(t+ws[-1]['end'],3),'hl':hl,
                  'w':[[w['text'].lstrip('…') or w['text'],round(t+w['start'],3),round(t+w['end'],3)] for w in ws]})
    t+=dur-0.25
L=lines; s_=lambda i:L[i]['s']; e_=lambda i:L[i]['e']
wt=lambda i,w:[x[1] for x in L[i]['w'] if x[0]==w][0]
total=float(sys.argv[1]) if len(sys.argv)>1 else round(e_(6)+1.6,2)
TL={'s1':[0,e_(2)+0.7],'s2':[e_(2)+0.7,e_(5)+0.6],'s3':[e_(5)+0.6,total+30]}
for k,v in [('s4',200),('s5',300),('s6',400),('s7',500),('s8',600)]: TL[k]=[v,v+10]
C={'i1':wt(0,'coto,'),'i2':wt(0,'macet…'),'i3':wt(0,'darah'),'zoom':wt(0,'darah'),'dnd':L[2]['at']-0.3,
   'ch1':e_(4)+0.35,'ch2':s_(5)-0.05,'t3':s_(6)+0.6}
notif=C['ch1']
args=['ffmpeg','-v','error','-y']; fl=[]; k=0
for ln in L:
    args+=['-i',str(V/f"{ln['f']}.mp3")]; d=int(ln['at']*1000)
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,aecho=0.8:0.5:22:0.12,adelay={d}|{d}[a{k}]"); k+=1
def amb(f,a,b,vol):
    global k
    args.extend(['-stream_loop','-1','-i',str(V/f'{f}.mp3')]); d=int(a*1000); du=b-a
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{du:.2f},afade=t=in:d=0.6,afade=t=out:st={max(0,du-0.6):.2f}:d=0.6,volume={vol},adelay={d}|{d}[a{k}]"); k+=1
amb('sfx-mandi',0,TL['s1'][1],0.22); amb('sfx-malam',TL['s2'][0],min(TL['s2'][1],total),0.16)
args+=['-i',str(V/'sfx-notif.mp3')]; d=int(notif*1000); fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume=0.5,adelay={d}|{d}[a{k}]"); k+=1
fl.append(''.join(f'[a{i}]' for i in range(k))+f'amix=inputs={k}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,apad=whole_dur={total},atrim=0:{total}[out]')
args+=['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2',str(P/'audio/narasi.wav')]
subprocess.run(args,check=True)
json.dump({'lines':L,'TL':{**TL,'cue':C},'total':total},open(P/'work/timing-v2.json','w'),ensure_ascii=False,indent=0)
print('total',total,'TL',{k:v for k,v in TL.items() if v[0]<100})
