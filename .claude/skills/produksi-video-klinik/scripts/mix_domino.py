import json,subprocess
K=json.load(open('cfg.json'))['K'];DUR=K['total']
E=[]
def e(f,t,db,d=None):E.append((f,t,db,d))
W='whoosh';C='click'
e(W,0.0,-22);e('pop',K['cabut']-0.1,-16);e(W,K['cabut']+0.1,-22);e(C,K['cabut'],-18);e(C,K['cabut']+0.3,-19)
for i in range(3):e(C,K['tiga']-0.3+i*0.25,-18)
e('shimmer',K['kok']-0.3,-18);e(W,K['kok']-0.2,-20)
e(C,K['rak'],-19);e('book',K['ambil']+0.1,-12);e(W,K['ambil']-0.1,-23);e('book',K['miringb']+0.9,-15)
e('shimmer',K['gigijuga']+0.25,-19);e(W,K['gigijuga']+0.3,-20)
e(C,K['kirikanan']+0.8,-18);e(C,K['kirikanan']+1.0,-19)
e(W,K['lawan']-0.15,-22);e(C,K['turun']+0.3,-18);e(W,K['turun']+0.1,-24)
e(W,K['satucelah']-0.15,-22);e('pop',K['satucelah'],-20)
for i in range(3):e(C,K['tigageser']+i*0.2,-18)
e(W,K['masalah']-0.15,-21);e(C,K['masalah']+0.6,-18)
for i in range(4):e('pop',K['sisa']+i*0.15,-23)
e(W,K['plak']-0.15,-23)
for i in range(3):e('pop',K['plak']+i*0.15,-24)
e(W,K['gigitan']-0.15,-22);e(C,K['gigitan']+0.2,-18);e(W,K['nggak']-0.1,-21)
e('shimmer',K['good']-0.3,-13);e(W,K['good'],-22)
e('shimmer',K['s1']-0.3,-19);e(C,K['s1'],-17);e('pulse',K['s1']+0.3,-14);e(C,K['rawat'],-18)
e(W,K['psa']-0.15,-22);e('scaler',K['yaitu'],-22);e(C,K['yaitu']+0.6,-18);e('shimmer',K['yaitu']+1.6,-18);e('pop',K['pakai'],-20);e(C,K['pakai']+0.5,-18)
e('shimmer',K['s2']-0.3,-19);e(C,K['s2'],-17);e(W,K['isi']-0.1,-22);e('snap',K['isi']+1.3,-12);e(C,K['isi']+1.3,-20);e(C,K['ruang']+0.8,-18)
e('shimmer',K['s3']-0.3,-19);e(C,K['s3'],-17);e(W,K['bersih']-0.4,-22);e('floss',K['bersih']+0.2,-18);e('floss',K['bersih']+1.4,-20);e(C,K['bersih']+0.2,-18);e('shimmer',K['bersih']+2.6,-18)
e('shimmer',K['ingat']-0.3,-17);e(W,K['ingat'],-21);e('shimmer',K['hilang'],-19)
e('pop',K['card'],-18);e('shimmer',K['card']+0.1,-15)
ins=['-i','take1.mp3','-f','lavfi','-i',f'anoisesrc=color=brown:amplitude=0.6:d={DUR},lowpass=f=420,highpass=f=60,volume=0.035']
fl=['[0:a]adelay=300|300,loudnorm=I=-16:TP=-1.5:LRA=7,apad=whole_dur=%s[v]'%DUR,'[1:a]afade=t=in:d=0.6,afade=t=out:st=%s:d=0.5[amb]'%(DUR-0.5)]
lab=['[v]','[amb]']
for i,(f,t,db,d) in enumerate(E):
    ins+=['-i',f'sfx/sfx_{f}.mp3'];j=i+2;ms=int(max(0,t)*1000)
    tr=f'atrim=0:{d},afade=t=out:st={d-0.4}:d=0.4,' if d else ''
    fl.append(f'[{j}:a]{tr}aformat=channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{i}]');lab.append(f'[s{i}]')
fl.append(''.join(lab)+f'amix=inputs={len(lab)}:normalize=0:duration=first,alimiter=limit=0.89,atrim=0:{DUR}[out]')
cmd=['ffmpeg','-y','-v','error']+ins+['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2','track.wav']
subprocess.run(cmd,check=True);print(len(E),'events')
