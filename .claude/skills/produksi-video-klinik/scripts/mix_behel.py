import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e('shimmer',0.4,-22);e(C,1.2,-19);e('snap',3.0,-22)
e(C,K['t1'],-18);e(C,K['s1t'],-17);e('pulse',K['s1t']+0.8,-21);e('pulse',K['s1t']+2.0,-22)
e(W,K['t2']-0.15,-20);e('dive',K['t2'],-21);e(C,K['t2']+0.6,-19)
e('shimmer',K['bantal']+0.3,-21);e(C,K['bantal']+0.6,-19)
e(C,K['tekan']+0.6,-19);e('fizz',K['tekan']+0.6,-23,2.5);e(W,K['tekan']+1.6,-24)
e(C,K['tarik']+0.6,-19)
for i in range(4):e('pop',K['tarik']+1.2+i*0.6,-23)
e(W,K['rumah']-0.15,-20);e('book',K['rumah']+0.05,-20)
for i in range(4):e('pop',K['depan']+0.3+i*0.4,-22)
for i in range(4):e('snap',K['belakang']+0.3+i*0.4,-23)
e(W,K['geser'],-23);e(C,K['mm']+0.2,-18)
e(W,K['t3']-0.15,-20);e(C,K['t3'],-18);e('pulse',K['t3']+1.0,-22);e(C,K['per'],-19)
e(W,K['kontrol']-0.1,-21);e('shimmer',K['kontrol']+0.4,-21)
for i in range(5):e('pop',K['kontrol']+0.5+i*0.4,-23)
e(C,K['s1'],-17);e('shimmer',K['s1']+1.0,-17);e(C,K['s1']+1.6,-18)
e(C,K['s2'],-17);e('crack',K['s2']+0.5,-20);e('snap',K['s2']+2.5,-17)
e(C,K['s3'],-17);e(C,K['s3']+0.6,-19);e('pulse',K['kencang'],-19)
e(W,K['telat']-0.1,-21);e('pulse',K['telat']+0.8,-21);e(C,K['telat']+2.8,-19)
e(W,K['cta'],-21);e('pop',K['cta']+1.5,-17)
for i in range(3):e('pop',K['tulis']+0.1+i*0.45,-16)
for i in range(3):e(C,K['tulis']+1.6+i*0.7,-20)
e('pop',K['follow'],-14);e(C,K['follow']+0.5,-18)
e('pop',K['card'],-18);e('shimmer',K['card']+0.1,-15)
ins=['-i','take.mp3','-f','lavfi','-i',f'anoisesrc=color=brown:amplitude=0.6:d={DUR},lowpass=f=420,highpass=f=60,volume=0.035']
fl=['[0:a]adelay=300|300,loudnorm=I=-16:TP=-1.5:LRA=7,apad=whole_dur=%s[v]'%DUR,'[1:a]afade=t=in:d=0.6,afade=t=out:st=%s:d=0.5[amb]'%(DUR-0.5)]
lab=['[v]','[amb]']
for i,(f,t,db,d) in enumerate(E):
    ins+=['-i',f'sfx/sfx_{f}.mp3'];j=i+2;ms=int(max(0,t)*1000)
    tr=f'atrim=0:{d},afade=t=out:st={d-0.4}:d=0.4,' if d else ''
    fl.append(f'[{j}:a]{tr}aformat=channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{i}]');lab.append(f'[s{i}]')
fl.append(''.join(lab)+f'amix=inputs={len(lab)}:normalize=0:duration=first,alimiter=limit=0.89,atrim=0:{DUR}[out]')
subprocess.run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2','track.wav'],check=True);print(len(E),'events')
