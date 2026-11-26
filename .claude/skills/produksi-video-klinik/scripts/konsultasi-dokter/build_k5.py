"""Video 2 drg. Ainun (25 Nov 2026) "Masih bisa ditambal, atau harus dicabut?": base video dengan standar natural Pak Dir
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
# wajah pasien (organik -> blur): titik kunci (t sumber, cx, cy, rx, ry)
KF={'p82':[(2.5,691,1145,165,190),(3,691,1145,165,190),(4.5,713,1166,165,190),(6,648,1274,175,205),(6.6,640,1290,180,210)],
    'p78':[(9.8,1015,1728,130,170),(10,1015,1728,130,170),(12,1037,1685,130,170),(13.5,1015,1663,130,170),(14.3,1015,1663,130,170)]}
def proc(pr,f,t):
    if pr in KF: f=blur_ell(f,*kf(KF[pr],t))
    elif pr=='g13': f=cv2.LUT(f,lut(1.3))
    return f
def reader(clip,t0,n):
    pre=0
    if t0<0: pre=round(-t0*FPS); t0=0
    p=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-ss',f'{t0:.3f}','-i',f'{D}/{clip}.mov','-vf',f'fps={FPS},scale={W}:{H}',
                        '-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    last=None; k=0
    while k<n:
        b=p.stdout.read(W*H*3)
        if len(b)==W*H*3: last=np.frombuffer(b,np.uint8).reshape(H,W,3)
        if last is None: continue
        for _ in range(pre+1 if k==0 else 1):
            if k<n: yield last; k+=1
    p.kill()
FACE=(560,950)
SEG=[('m0092',21.3,2.8,1.00,1.04,None,FACE),
     ('m0092',24.0,4.4,1.08,1.10,None,FACE),
     ('m0082',2.6,3.8,1.00,1.04,'p82',None),
     ('m0078',10.0,4.2,1.00,1.04,'p78',None),
     ('m0092',36.5,5.4,1.00,1.04,None,FACE),
     ('m0092',41.9,2.1,1.08,1.10,None,FACE),
     ('m0086',2.5,2.8,1.00,1.04,None,(540,760)),
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
