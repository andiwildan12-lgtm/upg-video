import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e('pulse',0.4,-13);e(C,0.9,-18);e(W,2.0,-24);e(C,2.35,-18)
e(W,K['t1']-0.15,-21);e(C,K['t1'],-17);e('crack',K['t1']+0.5,-22);e(C,K['t1']+0.6,-19)
e(W,K['t2']-0.15,-21);e(C,K['t2'],-17)
for i in range(4):e('pop',K['t2']+0.8+i*0.5,-25)
e('pulse',K['radang']+0.2,-14);e(C,K['radang']+0.2,-19)
e('shimmer',K['cincin']-0.3,-20);e(W,K['cincin'],-20);e(C,K['cincin']+0.6,-18)
e('shimmer',K['dinding']-0.3,-20);e(W,K['dinding'],-21);e(C,K['dinding']+0.4,-19)
e(C,K['tekanan']+0.1,-19);e('pulse',K['denyut']+0.1,-11);e('pulse',K['denyut']+1.6,-14);e(C,K['malam']+0.1,-19)
e(W,K['t3']-0.15,-21);e(C,K['t3'],-17);e(C,K['mati']+0.1,-19);e(C,K['sembuh'],-18)
e(W,K['padahal']-0.15,-21)
for i in range(4):e('pop',K['padahal']+0.6+i*0.7,-25)
e(C,K['t4'],-17);e('pop',K['nanah']+0.1,-16);e(C,K['nanah']+0.4,-19);e('pop',K['gusi']+0.1,-18);e(C,K['gusi']+0.3,-19)
e(W,K['gigit']-0.2,-22)
for i in range(3):e('crack',K['gigit']+0.4+i*0.52,-26)
e('shimmer',K['good']-0.3,-13);e(W,K['good'],-22)
e(W,K['s1']-0.15,-21);e(C,K['s1'],-17);e('snap',K['s1']+0.9,-13);e(C,K['s1']+1.2,-19)
e(W,K['s2']-0.15,-21);e(C,K['s2'],-17);e('pop',K['periksa'],-18)
e(W,K['s3']-0.15,-21);e(C,K['s3'],-17);e(W,K['s3']+0.1,-24);e('pop',K['s3']+1.1,-18);e(C,K['s3']+1.2,-19)
e(W,K['darurat'],-22);e(C,K['pipi'],-18);e(C,K['demam'],-18)
e('shimmer',K['ingat']-0.2,-17);e(W,K['ingat'],-22);e(C,K['ingat']+0.8,-19)
e(W,K['cta'],-21);e('pop',K['cta']+0.1,-17)
for i in range(3):e('pop',K['tulis']+0.1+i*0.45,-16)
for i in range(3):e(C,K['tulis']+1.6+i*0.7,-20)
e('pop',K['follow'],-14);e(C,K['follow']+0.5,-18)
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
