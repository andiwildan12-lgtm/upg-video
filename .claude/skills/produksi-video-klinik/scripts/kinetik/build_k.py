import json,subprocess,os
P=json.load(open('plan.json'))
PP='/tmp/claude-0/-home-user-ruma-video/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/pp/mov'
B='/tmp/claude-0/-home-user-ruma-video/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/behel/mov'
SFX='/home/user/ruma-video/.claude/skills/produksi-video-klinik/scripts/sfx'
NAR='/tmp/claude-0/-home-user/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/vo/bk_b.mp3'
OUT='/home/user/ruma-dental-video/iklan-behel-mofu-kinetik-v1.mp4'
H=0.12;F=30;END=P['end'];os.makedirs('vk',exist_ok=True)
run=lambda c:subprocess.run(c,check=True)
GR='colorbalance=rs=.01:bs=-.01,eq=saturation=1.03:contrast=1.01:brightness=0.01'
segs=P['edl'];vids=[]
for i,(src,ss,a,b) in enumerate(segs):
  d=b-a;pre=0 if i==0 else H;post=H if i<len(segs)-1 else 0;L=d+pre+post;o=f'vk/{i:02d}.mp4'
  if src=='CARD':
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=white:s=1080x1920:r={F}:d={L}','-c:v','libx264','-crf','17','-pix_fmt','yuv420p',o])
  else:
    s=src.replace('PP',PP);p=1.0 if i%2==0 else 1.06
    z=f"scale=w='trunc(1080*{p}*(1+0.03*t/{L})/2)*2':h=-2:eval=frame,crop=1080:1920"
    run(['ffmpeg','-v','error','-y','-ss',str(max(0,ss-pre)),'-t',str(L),'-i',s,'-vf',f'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,{z},{GR},fps={F},format=yuv420p','-an','-c:v','libx264','-crf','17',o])
  vids.append(o)
inp=[];fc=[];last='0:v'
for o in vids: inp+=['-i',o]
for i in range(1,len(vids)):
  T=segs[i][2];fc.append(f'[{last}][{i}:v]xfade=transition=fade:duration={2*H}:offset={T-H:.3f}[x{i}]');last=f'x{i}'
run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(fc),'-map',f'[{last}]','-c:v','libx264','-crf','16','-pix_fmt','yuv420p','vk/base.mp4'])
run(['ffmpeg','-v','error','-y','-i','vk/base.mp4','-framerate','30','-i','kseq/%04d.png','-filter_complex','[1:v]format=rgba[o];[0:v][o]overlay=0:0:eof_action=repeat,format=yuv420p[v]','-map','[v]','-c:v','libx264','-crf','18','vk/vid.mp4'])
# audio
inp=['-i',NAR];fc=[f'[0:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay=300|300,loudnorm=I=-16:TP=-1.5:LRA=7,apad=whole_dur={END}[n]']
for c in ('4403','4398','4405'): inp+=['-i',f'{B}/{c}.mov']
fc.append(f'[1:a][2:a][3:a]concat=n=3:v=0:a=1,aformat=sample_rates=48000:channel_layouts=stereo,highpass=f=70,lowpass=f=6000,volume=0.07,atrim=0:{END},afade=t=in:d=0.5,afade=t=out:st={END-1}:d=1[bed]')
n=4;sf=[]
ev=[('whoosh',segs[i][2]-0.2,0.22) for i in range(1,len(segs))]
ev+=[('pop',e[0],0.32) for e in P['ev']]+[('pop',c[0],0.35) for c in P['ch']]+[('pop',P['btn'][0],0.35),('pop',P['card']+0.05,0.38)]
for nm,t,v in ev:
  inp+=['-i',f'{SFX}/sfx_{nm}.mp3'];ms=int(max(0,t)*1000)
  fc.append(f'[{n}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={v},adelay={ms}|{ms}[f{n}]');sf.append(f'[f{n}]');n+=1
fc.append(f"[n][bed]{''.join(sf)}amix=inputs={2+len(sf)}:normalize=0,alimiter=limit=0.95,atrim=0:{END}[a]")
run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(fc),'-map','[a]','-ar','48000','-ac','2','vk/track.wav'])
run(['ffmpeg','-v','error','-y','-i','vk/vid.mp4','-i','vk/track.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',OUT])
print('ok')
