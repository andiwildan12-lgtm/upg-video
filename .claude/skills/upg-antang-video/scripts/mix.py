import subprocess
SFX='/home/user/ruma-video/.claude/skills/produksi-video-klinik/scripts/sfx/'
DUR=53.6
ev=[ # file, time, dur, dB
 ('pop',0.25,0.6,-20),('brush',1.9,1.8,-21),
 ('whoosh',5.45,1.0,-21),('notif',7.8,1.2,-25),
 ('whoosh',9.8,1.0,-21),('pop',10.85,0.5,-25),('pop',11.2,0.5,-26),('pop',11.55,0.5,-26),('pop',13.35,0.6,-22),
 ('whoosh',16.45,1.0,-21),('brush',17.4,1.6,-22),('whoosh',19.95,1.0,-22),('brush',21.15,1.7,-23),
 ('whoosh',22.95,1.0,-20),
 ('pop',26.9,0.5,-20),('pop',27.2,0.5,-19),('pop',28.45,0.5,-20),
 ('whoosh',31.55,0.9,-23),('pop',32.38,0.4,-22),('pop',33.4,0.4,-22),('pop',34.1,0.4,-22),
 ('pop',34.85,0.4,-23),('pop',35.75,0.4,-23),('pop',37.2,0.4,-23),
 ('whoosh',42.6,0.9,-22),('pop',42.93,0.4,-22),('pop',45.73,0.4,-22),('pop',48.91,0.4,-22),
 ('whoosh',50.5,0.9,-21),('pop',50.75,0.6,-19),
]
inp=['-i','narasi.mp3','-f','lavfi','-i',f'anoisesrc=color=brown:amplitude=0.6:d={DUR},lowpass=f=420,highpass=f=60,volume=0.035']
fl=['[0:a]adelay=300|300,loudnorm=I=-16:TP=-1.5:LRA=7,apad=whole_dur=%s[v]'%DUR,'[1:a]afade=t=in:d=0.6,afade=t=out:st=%s:d=1.2[amb]'%(DUR-1.4)]
labs=['[v]','[amb]']
for i,(f,t,d,db) in enumerate(ev):
    inp+=['-i',SFX+f'sfx_{f}.mp3'];idx=i+2;ms=int(t*1000)
    fl.append(f'[{idx}:a]atrim=0:{d},afade=t=out:st={max(0,d-0.25)}:d=0.25,volume={db}dB,adelay={ms}|{ms},apad=whole_dur={DUR}[s{i}]');labs.append(f'[s{i}]')
fl.append(''.join(labs)+f'amix=inputs={len(labs)}:normalize=0,alimiter=limit=0.95,atrim=0:{DUR}[out]')
cmd=['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2','track.wav']
subprocess.run(cmd,check=True);print('ok')
