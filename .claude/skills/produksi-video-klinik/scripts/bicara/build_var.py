import json,subprocess,os
B='/tmp/claude-0/-home-user-ruma-video/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/behel/mov'
F='/tmp/claude-0/-home-user/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/ft'
SFX='/home/user/ruma-video/.claude/skills/produksi-video-klinik/scripts/sfx'
import sys
EDL,STF,OVD,OUT=sys.argv[1:5]
rows=json.load(open(EDL));S=json.load(open(STF))
H=0.12;FPS=30;END=rows[-1]['t1']
GR='colorbalance=rs=.01:bs=-.01,eq=saturation=1.02:contrast=1.0:brightness=0.01'
BR={'4416':(f'{B}/4416.mov',1.0),'4420':(f'{F}/4420.mov',1.0),'4414':(f'{B}/4414.mov',1.0),'4398':(f'{B}/4398.mov',5.0),'4390':(f'{B}/4390.mov',0.8)}
ADM=('4436','4438','4454','4463','4467')
VS='vs_'+OVD;os.makedirs(VS,exist_ok=True)
run=lambda c:subprocess.run(c,check=True)
vids=[];k_adm=0
for i,r in enumerate(rows):
  d=r['t1']-r['t0'];pre=0 if i==0 else H;post=H if i<len(rows)-1 else 0;L=d+pre+post
  o=f'{VS}/{i:02d}.mp4'
  if r['v']=='kartu':
    run(['ffmpeg','-v','error','-y','-loop','1','-t',str(L),'-i','/dev/null' if False else 'st/'+sorted(os.listdir('st'))[-1],'-vf',f'fps={FPS},format=yuv420p,scale=1080:1920','-c:v','libx264','-crf','17',o])
    # card: pure white bg handled by overlay later; make white base
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=white:s=1080x1920:r={FPS}:d={L}','-c:v','libx264','-crf','17','-pix_fmt','yuv420p',o])
  elif r['v'] in BR:
    src,ss=BR[r['v']]
    z=f"scale=w='trunc(1080*(1.04+0.04*t/{L})/2)*2':h=-2:eval=frame,crop=1080:1920"
    run(['ffmpeg','-v','error','-y','-ss',str(max(0,ss-pre)),'-t',str(L),'-i',src,'-vf',f'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,{z},{GR},fps={FPS},format=yuv420p','-an','-c:v','libx264','-crf','17',o])
  else:
    p=1.0 if k_adm%2==0 else 1.08;k_adm+=1
    # face-centred punch + slow push 2%
    zf=f"scale=w='trunc(1080*{p}*(1+0.02*t/{L})/2)*2':h=-2:eval=frame,crop=1080:1920:(iw-1080)/2:(ih-1920)*0.42"
    run(['ffmpeg','-v','error','-y','-ss',str(r['ai']-pre),'-t',str(L),'-i',f"/tmp/claude-0/-home-user/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/test3d/bh/blurmov/{r['v']}.mp4",'-vf',f'scale=1080:1920,crop=720:1280:180:220,scale=1080:1920,{zf},{GR},fps={FPS},format=yuv420p','-an','-c:v','libx264','-crf','17',o])
  vids.append((o,r))
# xfade chain
inp=[];fc=[];last='0:v'
for i,(o,r) in enumerate(vids): inp+=['-i',o]
for i in range(1,len(vids)):
  T=vids[i][1]['t0'];out=f'x{i}'
  fc.append(f'[{last}][{i}:v]xfade=transition=fade:duration={2*H}:offset={T-H:.3f}[{out}]');last=out
run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(fc),'-map',f'[{last}]','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',VS+'/base.mp4'])
# overlay states as video
lst=[]
for i,s in enumerate(S): lst.append(f"file 'st/{i:03d}.png'\nduration {s['t1']-s['t0']:.3f}")
lst.append(f"file 'st/{len(S)-1:03d}.png'")
open('st.txt','w').write('\n'.join(lst))
run(['ffmpeg','-v','error','-y','-i',VS+'/base.mp4','-framerate','30','-i',OVD+'/%04d.png','-filter_complex','[1:v]format=rgba[o];[0:v][o]overlay=0:0:eof_action=repeat,format=yuv420p[v]','-map','[v]','-c:v','libx264','-crf','18',VS+'/vid.mp4'])
# audio: speech
segs=[];inp=[];fc=[]
AF='highpass=f=80,afftdn=nf=-28,aformat=sample_rates=48000:channel_layouts=stereo'
n=0
for r in rows:
  if r['v']=='kartu': continue
  d=r['t1']-r['t0'];ms=int(r['t0']*1000)
  inp+=['-ss',str(r['ai']),'-t',str(d),'-i',f"{B}/{r['a']}.mov"]
  fc.append(f'[{n}:a]{AF},afade=t=in:d=0.03,afade=t=out:st={d-0.04:.3f}:d=0.04,adelay={ms}|{ms}[s{n}]');segs.append(f'[s{n}]');n+=1
  if r['v'] in BR:
    src,ss=BR[r['v']]
    inp+=['-ss',str(ss),'-t',str(d),'-i',src]
    fc.append(f'[{n}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=0.18,afade=t=in:d=0.12,afade=t=out:st={d-0.15:.3f}:d=0.15,adelay={ms}|{ms}[s{n}]');segs.append(f'[s{n}]');n+=1
fc.append(f"{''.join(segs)}amix=inputs={len(segs)}:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=9,apad=whole_dur={END}[sp]")
# room bed from real clinic clips
for c,ss in (('4403',0),('4398',0),('4405',0)):
  inp+=['-ss',str(ss),'-i',f'{B}/{c}.mov']
fc.append(f'[{n}:a][{n+1}:a][{n+2}:a]concat=n=3:v=0:a=1,aformat=sample_rates=48000:channel_layouts=stereo,highpass=f=70,lowpass=f=6000,volume=0.09,atrim=0:{END},afade=t=in:d=0.5,afade=t=out:st={END-1}:d=1[bed]');n+=3
# sfx events
cutsBR=[]
for i in range(1,len(rows)):
  a,b=rows[i-1],rows[i]
  if (a['v'] in BR) or (b['v'] in BR) or b['v']=='kartu': cutsBR.append(b['t0'])
ev=[('notif',0.12,0.45)]+[('whoosh',t-0.22,0.32) for t in cutsBR]
p5=[r for r in rows if r['no']==5][0]['t0'];p6=[r for r in rows if r['no']==6][0]['t0']
ev+=[('pop',p5+0.02,0.45),('pop',p6+0.02,0.35),('pop',rows[-1]['t0']+0.05,0.4)]
sf=[]
for nm,t,v in ev:
  inp+=['-i',f'{SFX}/sfx_{nm}.mp3'];ms=int(max(0,t)*1000)
  fc.append(f'[{n}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={v},adelay={ms}|{ms}[f{n}]');sf.append(f'[f{n}]');n+=1
fc.append(f"[sp][bed]{''.join(sf)}amix=inputs={2+len(sf)}:normalize=0,alimiter=limit=0.95,atrim=0:{END}[a]")
run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(fc),'-map','[a]','-ar','48000','-ac','2',VS+'/track.wav'])
run(['ffmpeg','-v','error','-y','-i',VS+'/vid.mp4','-i',VS+'/track.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT])
print('ok',len(cutsBR),cutsBR)
