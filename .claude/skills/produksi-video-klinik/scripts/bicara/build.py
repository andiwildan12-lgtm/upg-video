import json,subprocess,os
B='/tmp/claude-0/-home-user-ruma-video/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/behel/mov'
F='/tmp/claude-0/-home-user/a9206803-5d8e-5be7-be23-40a6dfe89f1c/scratchpad/ft'
rows=json.load(open('edl2.json'));os.makedirs('seg',exist_ok=True)
GR='colorbalance=rs=.03:bs=-.04:rm=.02:bm=-.02,eq=saturation=1.04:contrast=1.02'
CROP='scale=1080:1920,crop=720:1280:180:220,scale=1080:1920'
FILL='scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920'
BR={'4420':(f'{F}/4420.mov',1.0),'4414':(f'{B}/4414.mov',1.0),'4398':(f'{B}/4398.mov',5.0),'4390':(f'{B}/4390.mov',0.8)}
AF='highpass=f=80,afftdn=nf=-28,aformat=sample_rates=48000:channel_layouts=stereo'
lst=[]
for r in rows:
  n=r['no'];o=f'seg/{n:02d}.mp4';ov=f'ov{n:02d}.png'
  if r['v']=='kartu':
    cmd=['ffmpeg','-v','error','-y','-loop','1','-t','3','-i',ov,'-f','lavfi','-t','3','-i','anoisesrc=color=brown:amplitude=0.6,lowpass=f=420,highpass=f=60,volume=0.03,aformat=sample_rates=48000:channel_layouts=stereo',
      '-vf','fps=30,format=yuv420p','-af','afade=t=out:st=2.2:d=0.8','-c:v','libx264','-crf','18','-c:a','aac','-b:a','192k','-shortest',o]
  else:
    d=r['ao']-r['ai']
    if r['v'] in BR:
      vs,ss=BR[r['v']]
      cmd=['ffmpeg','-v','error','-y','-ss',str(ss),'-t',str(d),'-i',vs,'-ss',str(r['ai']),'-t',str(d),'-i',f"{B}/{r['a']}.mov",'-i',ov,
        '-filter_complex',f'[0:v]{FILL},{GR},fps=30[b];[b][2:v]overlay=0:0,format=yuv420p[v];[1:a]{AF},afade=t=in:d=0.015,afade=t=out:st={d-0.02:.3f}:d=0.02[a]',
        '-map','[v]','-map','[a]','-t',str(d),'-c:v','libx264','-crf','18','-c:a','aac','-b:a','192k',o]
    else:
      cr=CROP
      cmd=['ffmpeg','-v','error','-y','-ss',str(r['ai']),'-t',str(d),'-i',f"{B}/{r['v']}.mov",'-i',ov,
        '-filter_complex',f'[0:v]{cr},{GR},fps=30[b];[b][1:v]overlay=0:0,format=yuv420p[v];[0:a]{AF},afade=t=in:d=0.015,afade=t=out:st={d-0.02:.3f}:d=0.02[a]',
        '-map','[v]','-map','[a]','-t',str(d),'-c:v','libx264','-crf','18','-c:a','aac','-b:a','192k',o]
  subprocess.run(cmd,check=True);lst.append(f"file '{o}'")
open('list.txt','w').write('\n'.join(lst))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','list.txt','-af','loudnorm=I=-16:TP=-1.5:LRA=9','-c:v','libx264','-crf','19','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','160k','-movflags','+faststart','/home/user/ruma-dental-video/iklan-behel-spil-harga-B-v1.mp4'],check=True)
