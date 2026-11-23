"""v2 base: standar video bicara natural Pak Dir (skill produksi-video-klinik): crossfade 0,24 dtk di semua potongan
(handle per sisi), zoom bergantian 1,00/1,08 antar-kalimat dokter (punch-in), dorong pelan, footage zoom pelan 4%.
Blur wajah pasien / kertas meja tetap. Keluaran: base_v2.mp4 + segmen.json (batas potongan untuk SFX)."""
import subprocess, numpy as np, cv2, sys, json
D, OUT = sys.argv[1], sys.argv[2]
W, H, FPS, HF = 1080, 1920, 30, 4   # HF = frame handle per sisi -> crossfade 8 frame (0,27 dtk)
KF671 = [(1.5,495,1344),(2.0,555,1254),(2.5,540,1074),(3.0,525,1014),(3.5,570,954),
         (4.0,585,909),(4.5,555,909),(5.0,630,1059),(5.5,750,1179)]
def kf(t):
    ts=[k[0] for k in KF671]; return np.interp(t,ts,[k[1] for k in KF671]), np.interp(t,ts,[k[2] for k in KF671])
def blur_ell(f,cx,cy,rx,ry):
    m=np.zeros(f.shape[:2],np.float32); cv2.ellipse(m,(int(cx),int(cy)),(int(rx),int(ry)),0,0,360,1.0,-1)
    m=cv2.GaussianBlur(m,(0,0),18)[...,None]; b=cv2.GaussianBlur(f,(0,0),40); return (f*(1-m)+b*m).astype(np.uint8)
def blur_box(f,x0,y0,x1,y1):
    m=np.zeros(f.shape[:2],np.float32); m[y0:y1,x0:x1]=1; m=cv2.GaussianBlur(m,(0,0),12)[...,None]
    b=cv2.GaussianBlur(f,(0,0),22); return (f*(1-m)+b*m).astype(np.uint8)
LUT=np.array([((i/255.0)**(1/1.35))*255 for i in range(256)],np.uint8)
def zoom(f,s,cx=540,cy=960):
    if abs(s-1)<1e-4: return f
    return cv2.warpAffine(f,cv2.getRotationMatrix2D((cx,cy),0,s),(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)

def reader(clip,t0,n):
    """n frame mulai t0 (t0 boleh negatif -> frame pertama diulang)."""
    pre=0
    if t0<0: pre=round(-t0*FPS); t0=0
    p=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-ss',f'{t0:.3f}','-i',f'{D}/{clip}.mp4','-vf',f'fps={FPS},scale={W}:{H}',
                        '-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    last=None; k=0
    while k<n:
        b=p.stdout.read(W*H*3)
        if len(b)==W*H*3: last=np.frombuffer(b,np.uint8).reshape(H,W,3)
        if last is None: continue
        reps = pre+1 if k==0 else 1
        for _ in range(reps):
            if k<n: yield last; k+=1
    p.kill()

# (clip, in, dur, z0, z1, proses, pusat zoom)
FACE=(540,900)
SEG=[('m0671',2.0,3.0,1.00,1.04,'f671',None),
     ('m0708',0.0,5.15,1.00,1.02,'kertas',FACE),
     ('m0708',5.15,4.25,1.08,1.10,'kertas',FACE),
     ('m0709',1.0,5.5,1.00,1.02,'kertas',FACE),
     ('m0709',6.5,1.7,1.08,1.10,'kertas',FACE),
     ('m0695',2.0,3.0,1.00,1.04,None,None),
     ('m0687',1.5,3.0,1.04,1.00,'f687',None),
     ('v125349',2.0,4.0,1.00,1.04,'gelap',None),
     ('v172352',2.0,3.6,1.00,1.04,'gelap_f',None),
     ('kartu',0,3.2,1,1,None,None),
     ('akhir',0,4.0,1,1,None,None)]

pip=list(reader('m0712',6.8-HF/FPS,round(3.2*FPS)+2*HF))
def mk_card(i):
    f=np.full((H,W,3),255,np.uint8); src=pip[min(i,len(pip)-1)][460:1260,240:840]
    src=cv2.resize(src,(300,400),interpolation=cv2.INTER_AREA); x0,y0=W-90-300,1060
    m=np.zeros((400,300),np.uint8); r=22; cv2.rectangle(m,(r,0),(299-r,399),255,-1); cv2.rectangle(m,(0,r),(299,399-r),255,-1)
    for cx,cy in [(r,r),(299-r,r),(r,399-r),(299-r,399-r)]: cv2.circle(m,(cx,cy),r,255,-1)
    reg=f[y0:y0+400,x0:x0+300]; reg[m>0]=src[m>0]; return f
MINT=np.full((H,W,3),(246,248,232),np.uint8)

def seg_frames(s):
    clip,t0,dur,z0,z1,pr,zc=s; n=round(dur*FPS); tot=n+2*HF
    if clip=='kartu':
        for i in range(tot): yield mk_card(i)
        return
    if clip=='akhir':
        for i in range(tot): yield MINT
        return
    for i,f in enumerate(reader(clip,t0-HF/FPS,tot)):
        f=f.copy(); t=t0+(i-HF)/FPS
        if pr=='f671': cx,cy=kf(t); f=blur_ell(f,cx,cy,230,220)
        elif pr=='f687': f=blur_ell(f,440,1010,320,280)
        elif pr=='kertas': f=blur_box(f,40,1420,1080,1730)
        elif pr=='gelap': f=cv2.LUT(f,LUT)
        elif pr=='gelap_f': f=blur_ell(cv2.LUT(f,LUT),190,1090,240,200)
        prog=min(1,max(0,(i-HF)/max(1,n-1)))
        cx,cy=zc if zc else (540,960)
        yield zoom(f,z0+(z1-z0)*prog,cx,cy)

enc=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
                      '-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
keep=None; written=0; bounds=[]
for si,s in enumerate(SEG):
    n=round(s[2]*FPS); g=seg_frames(s); buf=[]
    for idx,f in enumerate(g):
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
json.dump({'frames':written,'batas_dtk':[b/FPS for b in bounds]},open(OUT.replace('.mp4','.json'),'w'))
print('frames',written,written/FPS,[round(b/FPS,2) for b in bounds])
