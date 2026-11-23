import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e('pop',0.6,-21);e('pulse',K['ngorek']+0.3,-22);e(C,K['justru'],-18);e('pop',K['fol1'],-15);e(C,K['fol1']+0.5,-19)
e(W,K['sehat']-0.1,-22);e('snap',K['papila']+0.4,-20)
e(C,K['t1'],-17);e('dive',K['c1']-0.4,-19);e('pop',K['c1']+1.0,-22);e('crack',K['c1']+2.8,-20);e('snap',K['c1']+4.2,-20)
e(W,K['c2']-0.1,-21);e(C,K['c2']+0.4,-19);e('pop',K['c2b']+0.4,-19);e('pop',K['c2b']+1.8,-21)
e(C,K['kunyah'],-17);e('snap',K['kunyah']+1.1,-19)
e(W,K['zip']-0.15,-20);e('brush',K['zip']+0.2,-24,1.6);e('crack',K['zip']+1.7,-19)
e(W,K['kuman']-0.1,-21);e(C,K['kuman'],-17)
for i in range(5):e('pop',K['kuman']+0.4+i*0.15,-24)
e('floss',K['darah']+0.2,-18);e('pop',K['darah']+0.8,-17);e('pulse',K['takut']+0.4,-20)
e('scaler',K['cungkil']+0.3,-22);e('shimmer',K['lega'],-22);e('pulse',K['luka']+0.3,-19)
e(W,K['kabar']-0.1,-21);e('shimmer',K['kabar']+0.2,-19)
e(C,K['cara'],-17);e('floss',K['cara']+0.4,-17);e('floss',K['cara']+1.6,-19)
e(C,K['rutin'],-17);e('shimmer',K['rutin']+0.3,-21)
for i in range(4):e(C,K['rutin']+0.6+i*0.5,-23)
e(C,K['tutup'],-17);e('pop',K['periksa']+0.5,-19);e('snap',K['periksa']+2.0,-17);e('shimmer',K['periksa']+2.2,-16)
e(W,K['ingat']-0.1,-22);e('shimmer',K['ingat']+0.3,-20)
e(W,K['cta'],-21);e('pop',K['cta']+0.8,-17)
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
