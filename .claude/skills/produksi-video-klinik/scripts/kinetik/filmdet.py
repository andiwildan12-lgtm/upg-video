import sys,subprocess,numpy as np,cv2
def detect(f):
  hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
  m=((hsv[...,2]<75)&(hsv[...,1]<70)).astype(np.uint8)
  m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((25,25),np.uint8))
  cs,_=cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  best=None
  for c in cs:
    x,y,w,h=cv2.boundingRect(c);a=cv2.contourArea(c)
    if a>60000 and 1.0<w/h<2.4 and 700<y+h/2<1400 and (best is None or a>best[4]): best=(x,y,w,h,a)
  return best
def run(src,dst):
  W,H=1080,1920
  rd=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
  wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-i',src,'-map','0:v','-map','1:a?','-c:v','libx264','-crf','14','-pix_fmt','yuv420p','-c:a','aac',dst],stdin=subprocess.PIPE)
  last=None;miss=0;n=0
  while True:
    b=rd.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    f=np.frombuffer(b,np.uint8).reshape(H,W,3).copy();d=detect(f)
    if d: last=d if last is None else tuple(int(0.5*a+0.5*b_) for a,b_ in zip(d,last))
    else: miss+=1
    if last:
      x,y,w,h,_=last
      a,bb,c,dd=max(0,x-15),max(0,y-15),min(W,x+int(w*0.42)),min(H,y+int(h*0.30))
      f[bb:dd,a:c]=cv2.GaussianBlur(f[bb:dd,a:c],(0,0),16)
    wr.stdin.write(f.tobytes());n+=1
  wr.stdin.close();wr.wait();print(dst,n,'miss',miss)
if __name__=='__main__': run(sys.argv[1],sys.argv[2])
