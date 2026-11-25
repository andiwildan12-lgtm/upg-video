"""Jangan berhenti di tambal sementara, drg. Ainun (25 Nov 2026 sore), footage HP 1080x1920 60fps; blur wajah pasien + layar HP pasien: base video dengan standar natural Pak Dir
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
KF={'m48':[(3,945,1002,150,170),(4,945,1002,150,170),(7,960,1002,150,170),(10,979,1020,150,170),(12,979,1020,150,170),
           (33,956,1040,150,170),(35,956,1040,150,170),(39,952,1040,150,170),(41,952,1040,150,170),(43,892,1077,150,170),(46,892,1077,150,170)],
    'm11':[(6.5,533,1304,130,145),(7.5,533,1304,130,145),(8.5,567,1293,130,145),(9.5,567,1293,130,145),(12,640,1150,160,180),(16,640,1150,160,180)],
    'hp55':[(0,918,1500,175,100),(0.5,918,1500,175,100),(4,858,1444,175,100),(8,816,1482,175,100),(11,816,1482,175,100)]}
def proc(pr,f,t):
    if pr in KF: f=blur_ell(f,*kf(KF[pr],t))
    elif pr=='g13': f=cv2.LUT(f,lut(1.3))
    return f
def reader(clip,t0,n):
    pre=0
    if t0<0: pre=round(-t0*FPS); t0=0
    p=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-ss',f'{t0:.3f}','-i',f'{D}/VID_20261125_{clip}.mp4','-vf',f'fps={FPS},scale={W}:{H}',
                        '-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    last=None; k=0
    while k<n:
        b=p.stdout.read(W*H*3)
        if len(b)==W*H*3: last=np.frombuffer(b,np.uint8).reshape(H,W,3)
        if last is None: continue
        for _ in range(pre+1 if k==0 else 1):
            if k<n: yield last; k+=1
    p.kill()
DK=(380,620)
SEG=[('153055',0.0,3.0,1.00,1.04,'hp55',(450,1100)),
     ('152148',3.34,5.8,1.00,1.04,'m48',DK),
     ('152148',9.14,2.6,1.10,1.13,'m48',DK),
     ('152148',36.8,2.0,1.00,1.03,'m48',DK),
     ('152148',43.4,2.0,1.10,1.13,'m48',DK),
     ('152411',6.95,2.1,1.00,1.04,'m11',None),
     ('152559',0.0,3.4,1.00,1.04,None,(560,700)),
     ('153055',2.6,4.0,1.00,1.04,'hp55',(450,1100)),
     ('153055',6.6,3.85,1.08,1.11,'hp55',(450,1100)),
     ('152411',12.4,2.6,1.00,1.04,'m11',None),
     ('akhir',0,4.0,1,1,None,None)]
# v1 revisi 25 Nov: 152148 33,9-36,8 dibuang (nama obat + ucapan tidak jelas), 38,7-41 dibuang (bengkak: dua model berbeda)
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
