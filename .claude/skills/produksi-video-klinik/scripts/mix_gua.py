import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e(W,0.0,-22);e(C,0.9,-17);e('dive',3.55,-9)
e(C,K['lapis'],-17)
for k,tg in [('enamel',0.15),('dentin',0.15),('asam',0.4)]:
    e(W,K[k]-0.25,-22);e(C,K[k]+tg,-17)
e('pop',K['asam']+0.1,-22)
drops=[K['n1']-0.6,K['n5']-0.35,K['n5']+0.1,K['n5']+0.55,K['n5']+1.0]
for d in drops:e('pop',d+0.45,-22);e('fizz',d+0.5,-13)
e(W,K['n1']-0.15,-23);e(W,K['n5']-0.15,-23);e(C,K['n1'],-17)
for i in range(1,4):e(C,K['n5']+0.45*i,-19)
e(C,K['n5'],-19)
e(W,K['bolong']-0.25,-22);e('crack',K['bolong']+0.4,-22);e(C,K['bolong']+0.6,-18)
e(W,K['tembus']-0.15,-22);e('crack',K['tembus']+0.3,-17);e(C,K['lebar'],-18)
e(W,K['gua']-0.15,-21);e(C,K['gua']+0.3,-18);e(C,K['gua']+1.0,-18)
e(W,K['kerasa']-0.15,-21);e(W,K['kerasa']+0.1,-24)
e(C,K['saraf']+0.2,-18);e(W,K['kecil']-0.15,-23);e(C,K['kecil']+0.2,-18)
e(W,K['ngilu']-0.15,-22);e(C,K['ngilu']+0.3,-18);e('fizz',K['ngilu']+0.3,-24)
e(W,K['sakit']-0.15,-22);e('pulse',K['sakit']+0.25,-11);e(C,K['sakit']+0.3,-18)
e('shimmer',K['good']-0.35,-13);e(W,K['good']-0.3,-20)
e(W,K['s1']-0.15,-21);e(C,K['s1'],-17);e('pop',K['s1']+0.25,-19);e(C,K['cari']+0.1,-18)
e(W,K['s2']-0.15,-21);e(C,K['s2'],-17);e('brush',K['s2']+0.5,-17,2.8);e('shimmer',K['mineral']-0.3,-14);e(C,K['mineral'],-18)
e(W,K['s3']-0.15,-22)
for i in range(5):e('pop',K['s3']+0.3+i*0.12,-23)
e(W,K['jangan']+0.2,-22);e('shimmer',K['jangan']+1.2,-17)
e(W,K['s4']-0.15,-21);e(C,K['s4'],-17);e('dive',K['karena']-0.1,-15);e(C,K['karena']+0.9,-18)
e(W,K['ingat']-0.15,-21);e('shimmer',K['ingat']+0.6,-17);e('shimmer',K['belum'],-18)
e('pop',K['card'],-18);e('shimmer',K['card']+0.1,-15)
ins=['-i','take2.mp3','-f','lavfi','-i',f'anoisesrc=color=brown:amplitude=0.6:d={DUR},lowpass=f=420,highpass=f=60,volume=0.035']
fl=['[0:a]adelay=300|300,loudnorm=I=-16:TP=-1.5:LRA=7,apad=whole_dur=%s[v]'%DUR,'[1:a]afade=t=in:d=0.6,afade=t=out:st=%s:d=0.5[amb]'%(DUR-0.5)]
lab=['[v]','[amb]']
for i,(f,t,db,d) in enumerate(E):
    ins+=['-i',f'sfx/sfx_{f}.mp3'];j=i+2;ms=int(max(0,t)*1000)
    tr=f'atrim=0:{d},afade=t=out:st={d-0.4}:d=0.4,' if d else ''
    fl.append(f'[{j}:a]{tr}aformat=channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{i}]');lab.append(f'[s{i}]')
fl.append(''.join(lab)+f'amix=inputs={len(lab)}:normalize=0:duration=first,alimiter=limit=0.89,atrim=0:{DUR}[out]')
cmd=['ffmpeg','-y','-v','error']+ins+['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2','track.wav']
subprocess.run(cmd,check=True);print(len(E),'events')
