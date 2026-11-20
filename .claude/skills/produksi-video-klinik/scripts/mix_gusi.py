import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e('brush',0.1,-19,1.2);e('pop',0.9,-20);e(C,0.95,-18)
e(W,K['t1']-0.15,-21);e(C,K['t1'],-17)
for i in range(5):e('pop',K['t1']+0.6+i*0.12,-24)
e(C,K['t1']+1.2,-19);e(C,K['kuman']+0.3,-19)
for i in range(4):e('pop',K['kuman']+0.2+i*0.2,-25)
e('pop',K['plak'],-18);e(C,K['plak']+0.6,-18)
e('pop',K['jam'],-17);e(C,K['jam']+0.3,-20)
e(W,K['t2']-0.15,-21);e(C,K['t2'],-17);e('shimmer',K['menyerap']+0.1,-19);e(C,K['menyerap']+0.3,-19)
e('crack',K['karang']+0.3,-16);e(C,K['karang']+0.6,-18)
e('shimmer',K['teko']-0.3,-20);e(W,K['teko'],-20);e('pop',K['teko']+0.6,-21);e(C,K['teko']+1.6,-19)
e('shimmer',K['sikatkarang']-0.3,-21);e(W,K['sikatkarang'],-21);e('brush',K['sikatkarang']+0.1,-17,2.0);e(C,K['sikatkarang']+1.0,-19)
e(W,K['t3']-0.15,-21);e(C,K['t3'],-17);e(C,K['kasar'],-19)
for i in range(4):e('pop',K['kasar']+0.4+i*0.3,-24)
e('pulse',K['radang']+0.1,-15);e(C,K['radang']+0.4,-19);e(C,K['rapuh'],-19)
e('brush',K['darah'],-19,0.6);e('pop',K['darah']+0.5,-16);e('pop',K['darah']+0.65,-18);e(C,K['darah']+0.6,-19)
e(W,K['masalah']-0.1,-21);e('brush',K['masalah']+0.3,-24,2.2);e(C,K['masalah']+1.2,-19)
e('shimmer',K['good']-0.3,-13);e(W,K['good'],-22)
e(W,K['s1']-0.15,-21);e(C,K['s1'],-17);e('brush',K['s1']+0.2,-17,2.6);e(C,K['s1']+0.8,-19)
e(W,K['s2']-0.15,-21);e(C,K['s2'],-17);e('floss',K['s2']+0.6,-17);e('floss',K['s2']+1.5,-19);e(C,K['s2']+0.8,-19)
e(W,K['s3']-0.15,-21);e(C,K['s3'],-17);e('scaler',K['s3']+0.6,-19);e('scaler',K['s3']+1.6,-20);e('crack',K['s3']+1.0,-20);e(C,K['s3']+0.8,-19)
e(W,K['rutin']-0.1,-22);e('pop',K['rutin']+0.1,-18)
for i in range(5):e(C,K['rutin']+0.6+i*0.55,-22)
e('shimmer',K['ingat']-0.2,-17);e(W,K['ingat'],-22)
e(W,K['cta'],-21);e('pop',K['cta']+0.1,-17)
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
cmd=['ffmpeg','-y','-v','error']+ins+['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2','track.wav']
subprocess.run(cmd,check=True);print(len(E),'events')
