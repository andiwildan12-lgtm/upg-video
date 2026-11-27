import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
for i in range(8):e(C,0.8+i*0.55,-25)
e('pop',K['fol1'],-15);e(C,K['fol1']+0.5,-19)
e(W,K['t1']-0.15,-20);e('dive',K['t1']-0.3,-21);e('shimmer',K['t1']+0.6,-23)
for i in range(5):e('pop',K['zat']+0.2+i*0.18,-24)
e(C,K['t2'],-17);e('fizz',K['resap']+0.3,-22)
e(C,K['t3'],-17);e('snap',K['t3']+0.7,-21);e('snap',K['t3']+1.3,-21)
e(W,K['cangkir']-0.15,-20);e('pour' if False else 'fizz',K['cangkir']+0.4,-23);e('shimmer',K['coklat']+0.3,-22)
e(W,K['masalah']-0.15,-21);e('pulse',K['masalah']+0.5,-22)
e(W,K['kabar']-0.1,-21);e('shimmer',K['kabar']+0.2,-19)
e(C,K['cara1'],-17);e('fizz',K['cara1']+0.4,-20)
e(C,K['cara2'],-17);e('pop',K['cara2']+0.6,-20)
e(C,K['cara3'],-17);e('brush',K['cara3']+1.7,-27,1.8);e('snap',K['dokter']+0.4,-18);e('shimmer',K['dokter']+0.6,-17)
e(W,K['ingat']-0.1,-22);e('shimmer',K['ingat']+0.3,-20)
e(W,K['cta'],-21);e('pop',K['cta']+0.7,-17)
for i in range(3):e('pop',K['tulis']+0.1+i*0.35,-16)
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
