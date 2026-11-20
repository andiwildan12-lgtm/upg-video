import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e('brush',0.1,-19,2.8);e('shimmer',1.0,-21);e(C,1.3,-19)
e(W,K['cari']-0.1,-20);e('dive',K['cari']+0.2,-22);e(C,K['cari']+1.0,-19)
e(C,K['l1'],-17);e(C,K['l1']+0.6,-19)
for i in range(4):e('pop',K['karpet']+0.6+i*0.12,-24)
e(C,K['karpet']+0.6,-19)
e(W,K['tidur']-0.1,-23);e('pop',K['tidur']+0.1,-19);e(C,K['tidur']+0.9,-19)
e('fizz',K['gas']+0.3,-20,3.0);e(C,K['gas']+0.7,-19)
e('shimmer',K['pagi'],-20);e(C,K['pagi']+0.1,-18)
e(C,K['cara1'],-17);e('scaler',K['cara1']+0.4,-21);e('brush',K['cara1']+0.5,-20,2.4);e('shimmer',K['cara1']+3.0,-21)
e(W,K['l2q']-0.15,-21);e(C,K['l2q'],-18)
e(C,K['l2'],-17);e(C,K['l2']+0.4,-19)
for i in range(3):e('pop',K['sarang']+i*0.12,-21)
e('pop',K['sarang']+0.8,-19);e(C,K['sarang']+1.0,-19);e('pulse',K['sarang']+2.4,-18)
e(C,K['cara2'],-17);e('floss',K['cara2']+0.5,-17);e('floss',K['cara2']+1.3,-19)
e('scaler',K['cara2']+2.6,-19);e('crack',K['cara2']+3.0,-21);e('scaler',K['cara2']+3.6,-20);e('shimmer',K['cara2']+4.4,-20)
e(W,K['l3q']-0.15,-21);e('book',K['l3q']+0.05,-19)
for i in range(3):e('pop',K['l3']+0.6+i*0.6,-18)
e('pop',K['dokter'],-15);e(C,K['dokter']+0.1,-18)
e(W,K['jadi']-0.1,-21);e('shimmer',K['jadi']+0.2,-15)
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
