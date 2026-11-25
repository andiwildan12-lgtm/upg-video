import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e('brush',0.4,-20,K['fol1']-2.6);e(C,K['fol1']-2.5,-18);e('fizz',K['fol1']-1.8,-21);e('pulse',K['fol1']-1.0,-17)
e('pop',K['fol1'],-15);e(C,K['fol1']+0.5,-19)
e(C,K['t1'],-17);e('brush',K['t1']+0.2,-21,3.4);e('snap',K['turun']+0.3,-21)
e(W,K['panci']-0.15,-20);e('scaler',K['panci']+0.5,-22);e('crack',K['panci']+2.6,-21)
e(W,K['t2']-0.15,-20);e(C,K['t2'],-17);e('shimmer',K['t2']+1.0,-22)
e('dive',K['saluran']-0.6,-19);e('pop',K['saluran']+0.4,-22)
e(C,K['t3'],-17);e('fizz',K['t3']+0.2,-20);e('whoosh',K['cairan'],-23);e('pulse',K['ngilu']-0.6,-17);e('pulse',K['ngilu']+0.2,-19)
e(W,K['masalah']-0.1,-21);e('brush',K['masalah']+0.3,-22,3.0);e('crack',K['ganti']+0.5,-20)
e(W,K['kabar']-0.1,-21);e('shimmer',K['kabar']+0.2,-19)
e(C,K['cara1'],-17);e('brush',K['cara1']+0.4,-27,2.0)
e(C,K['cara2'],-17);e('brush',K['cara2']+0.4,-27,2.0)
e(C,K['cara3'],-17);e('pop',K['cara3']+0.5,-19);e('snap',K['dokter']+0.4,-18);e('shimmer',K['dokter']+0.6,-17)
e(W,K['ingat']-0.1,-22);e('shimmer',K['ingat']+0.3,-20)
e(W,K['cta'],-21);e('pop',K['cta']+0.8,-17)
for i in range(3):e('pop',K['tulis']+0.1+i*0.45,-16)
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
