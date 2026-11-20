import json,os
from PIL import Image
H=8;FPS=30;TOT=round(49.5*FPS)
segs=json.load(open('kpsegs.json'));os.makedirs('kpfinal',exist_ok=True)
noblend={0,4}
for i,(n,a,b) in enumerate(segs):
    st=round(a*FPS);nf=round(b*FPS)-st
    for k in range(nf):
        fr=Image.open(f'kpseg/{i:02d}/{min(k,len(os.listdir(f"kpseg/{i:02d}"))-1):04d}.jpg')
        if i not in noblend and k<H:
            pi=min(round(segs[i-1][2]*FPS)-round(segs[i-1][1]*FPS)+k,len(os.listdir(f"kpseg/{i-1:02d}"))-1);pv=Image.open(f"kpseg/{i-1:02d}/{pi:04d}.jpg");fr=Image.blend(pv,fr,(k+1)/(H+1))
        if st+k<TOT: fr.save(f'kpfinal/{st+k:04d}.jpg',quality=92)
print(len(os.listdir('kpfinal')),TOT)
