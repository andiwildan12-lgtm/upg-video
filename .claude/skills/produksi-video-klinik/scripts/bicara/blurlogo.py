import sys,subprocess,numpy as np,cv2
src,dst=sys.argv[1],sys.argv[2]
W,H=1080,1920
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
rd=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf',f'scale={W}:{H},fps=30','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
fps=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip()
wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-i',src,'-map','0:v','-map','1:a','-c:v','libx264','-crf','14','-pix_fmt','yuv420p','-c:a','copy',dst],stdin=subprocess.PIPE)
pos=None;n=0;log=[]
while True:
  buf=rd.stdout.read(W*H*3)
  if len(buf)<W*H*3: break
  f=np.frombuffer(buf,np.uint8).reshape(H,W,3).copy()
  x0,y0,x1,y1=280,1150,820,1750
  g=cv2.cvtColor(f[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY)
  m=(g<55).astype(np.uint8)
  k,lab,st,cen=cv2.connectedComponentsWithStats(m)
  best=None
  for i in range(1,k):
    a=st[i,cv2.CC_STAT_AREA];w_=st[i,cv2.CC_STAT_WIDTH];h_=st[i,cv2.CC_STAT_HEIGHT]
    if 250<a<6000 and 0.6<w_/max(h_,1)<1.6 and (best is None or a>best[0]): best=(a,cen[i][0]+x0,cen[i][1]+y0)
  if best:
    c=np.array(best[1:])
    if pos is None:
      if c[1]>1280: pos=c
    elif np.linalg.norm(c-pos)<90: pos=0.6*pos+0.4*c
  if pos is not None:
    cx,cy=pos[0]-150,pos[1]+45
    mask=np.zeros((H,W),np.float32)
    cv2.ellipse(mask,(int(cx),int(cy)),(215,175),0,0,360,1,-1)
    mask=cv2.GaussianBlur(mask,(0,0),22)[...,None]
    bl=cv2.GaussianBlur(f,(0,0),16)
    f=(f*(1-mask)+bl*mask).astype(np.uint8)
  log.append(None if pos is None else (round(pos[0]),round(pos[1])))
  wr.stdin.write(f.tobytes());n+=1
wr.stdin.close();wr.wait()
miss=sum(1 for p in log if p is None)
print(src.split('/')[-1],n,'frames, no-mic',miss, 'first',log[0],'last',log[-1])
