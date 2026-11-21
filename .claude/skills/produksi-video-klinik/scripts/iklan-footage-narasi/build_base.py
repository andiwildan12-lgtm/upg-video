"""Iklan scaling Ruma v3: base video dengan standar natural Pak Dir
(crossfade 8 frame di semua potongan, punch-in 1,08 antar-kalimat, zoom pelan), blur wajah pasien (titik kunci)
dan nama pasien di monitor rontgen. Keluaran base_k1.mp4."""
import subprocess, numpy as np, cv2, sys, json
D, OUT = sys.argv[1], sys.argv[2]
W, H, FPS, HF = 1080, 1920, 30, 4
def blur_ell(f,cx,cy,rx,ry):
    m=np.zeros(f.shape[:2],np.float32); cv2.ellipse(m,(int(cx),int(cy)),(int(rx),int(ry)),0,0,360,1.0,-1)
    m=cv2.GaussianBlur(m,(0,0),18)[...,None]; b=cv2.GaussianBlur(f,(0,0),40); return (f*(1-m)+b*m).astype(np.uint8)
def blur_box(f,x0,y0,x1,y1):
    m=np.zeros(f.shape[:2],np.float32); m[y0:y1,x0:x1]=1; m=cv2.GaussianBlur(m,(0,0),8)[...,None]
    b=cv2.GaussianBlur(f,(0,0),16); return (f*(1-m)+b*m).astype(np.uint8)
def lut(g): return np.array([((i/255.0)**(1/g))*255 for i in range(256)],np.uint8)
L125,L135=lut(1.25),lut(1.35)
def zoom(f,s,cx=540,cy=960):
    if abs(s-1)<1e-4: return f
    return cv2.warpAffine(f,cv2.getRotationMatrix2D((cx,cy),0,s),(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
def kf(KF,t):  # KF: [(t,cx,cy,rx,ry)]
    ts=[k[0] for k in KF]; return [np.interp(t,ts,[k[j] for k in KF]) for j in range(1,5)]
FACE644=[(26.0,750,1700,310,200),(28.0,560,1715,280,190),(30.3,370,1730,250,180),(34.6,520,1735,280,180)]
FACE645=[(20.3,818,1482,240,180),(24.0,760,1490,240,180),(27.7,750,1490,240,180)]
FACE651=[(4.4,160,1850,240,120),(9.4,160,1850,240,120)]
def proc(pr,f,t):
    if pr=='f644': f=blur_ell(f,*kf(FACE644,t))
    elif pr=='f645': f=blur_ell(f,*kf(FACE645,t))
    elif pr=='f651': f=blur_ell(f,*kf(FACE651,t))
    elif pr=='mon650': f=blur_box(f,790,925,1005,1025)
    elif pr=='mon680': f=blur_box(f,835,600,1015,710)
    elif pr=='g125': f=cv2.LUT(f,L125)
    elif pr=='g135': f=cv2.LUT(f,L135)
    elif pr=='sinar': f=blur_ell(cv2.LUT(f,L135),190,1090,240,200)
    return f
def reader(clip,t0,n):
    pre=0
    if t0<0: pre=round(-t0*FPS); t0=0
    p=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-ss',f'{t0:.3f}','-i',f'{D}/{clip}','-vf',f'fps={FPS},scale={W}:{H}',
                        '-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    last=None; k=0
    while k<n:
        b=p.stdout.read(W*H*3)
        if len(b)==W*H*3: last=np.frombuffer(b,np.uint8).reshape(H,W,3)
        if last is None: continue
        for _ in range(pre+1 if k==0 else 1):
            if k<n: yield last; k+=1
    p.kill()
# iklan: wajah pasien TIDAK di-blur (keputusan Pak Dir). (clip, in, dur, z0, z1, proses, pusat zoom)
SEG=[('dl2/9741.mov',2.0,4.02,1.00,1.06,None,None),
     ('dl2/9743.mov',3.0,6.66,1.00,1.04,None,(540,900)),
     ('dl2/9744.mov',0.5,6.08,1.04,1.00,None,None),
     ('dl2/9740.mov',1.0,5.96,1.00,1.06,None,None),
     ('dl2/9742.mov',7.0,4.28,1.00,1.05,None,None),
     ('dl2/9732.mov',6.0,3.44,1.00,1.04,None,None),
     ('dl2/9747.mov',2.5,2.14,1.00,1.04,None,(540,800)),
     ('dl2/9737.mov',0.5,1.80,1.04,1.08,None,None),
     ('dl2/9739.mov',0.3,4.68,1.00,1.04,None,None),
     ('dl3/9648.mov',1.0,1.80,1.00,1.04,None,None),
     ('dl3/9650.mov',1.4,2.70,1.00,1.04,None,(540,800)),
     ('dl/4420.mov',1.0,4.04,1.00,1.06,None,None),
     ('akhir',0,4.0,1,1,None,None)]
MINT=np.full((H,W,3),(246,248,232),np.uint8)
def seg_frames(s):
    clip,t0,dur,z0,z1,pr,zc=s; n=round(dur*FPS); tot=n+2*HF
    if clip=='akhir':
        for i in range(tot): yield MINT
        return
    for i,f in enumerate(reader(clip,t0-HF/FPS,tot)):
        t=t0+(i-HF)/FPS; f=proc(pr,f.copy(),t)
        prog=min(1,max(0,(i-HF)/max(1,n-1))); cx,cy=zc if zc else (540,960)
        yield zoom(f,z0+(z1-z0)*prog,cx,cy)
enc=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
                      '-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
keep=None; written=0; bounds=[]
for s in SEG:
    n=round(s[2]*FPS); buf=[]
    for idx,f in enumerate(seg_frames(s)):
        if idx<2*HF:
            buf.append(f)
            if idx==2*HF-1:
                if keep is None:
                    for x in buf[HF:]: enc.stdin.write(x.tobytes()); written+=1
                else:
                    bounds.append(written+HF)
                    for k in range(2*HF):
                        a=(k+0.5)/(2*HF); enc.stdin.write(((1-a)*keep[k]+a*buf[k]).astype(np.uint8).tobytes()); written+=1
                buf=[]
            continue
        if idx<n: enc.stdin.write(f.tobytes()); written+=1
        else: buf.append(f)
    keep=buf
for x in keep[:HF]: enc.stdin.write(x.tobytes()); written+=1
enc.stdin.close(); enc.wait()
json.dump({'frames':written,'batas':[round(b/FPS,3) for b in bounds]},open(OUT.replace('.mp4','.json'),'w'))
print('frames',written,written/FPS,[round(b/FPS,2) for b in bounds])
