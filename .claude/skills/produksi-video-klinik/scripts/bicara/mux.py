import json,subprocess,os
run=lambda c:subprocess.run(c,check=True)
B='/tmp/claude-0/-home-user-ruma-video/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/behel/mov'
F='/tmp/claude-0/-home-user/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/ft'
SFX='/home/user/ruma-video/.claude/skills/produksi-video-klinik/scripts/sfx'
OUT='/home/user/ruma-dental-video/iklan-behel-spil-harga-B-v2.mp4'
rows=json.load(open('edl2.json'));S=json.load(open('states.json'))
H=0.12;FPS=30;END=rows[-1]['t1']
GR='colorbalance=rs=.01:bs=-.01,eq=saturation=1.02:contrast=1.0:brightness=0.01'
BR={'4420':(f'{F}/4420.mov',1.0),'4414':(f'{B}/4414.mov',1.0),'4398':(f'{B}/4398.mov',5.0),'4390':(f'{B}/4390.mov',0.8)}
ADM=('4436','4438','4454','4463','4467')
# overlay states as video
lst=[]
for i,s in enumerate(S): lst.append(f"file 'st/{i:03d}.png'\nduration {s['t1']-s['t0']:.3f}")
lst.append(f"file 'st/{len(S)-1:03d}.png'")
open('st.txt','w').write('\n'.join(lst))
run(['ffmpeg','-v','error','-y','-i','vs/base.mp4','-framerate','30','-i','ovseq/%04d.png','-filter_complex','[1:v]format=rgba[o];[0:v][o]overlay=0:0:eof_action=repeat,format=yuv420p[v]','-map','[v]','-c:v','libx264','-crf','18','vs/vid.mp4'])
run(['ffmpeg','-v','error','-y','-i','vs/vid.mp4','-i','vs/track.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT])
