import json,os
from PIL import Image
FPS=30;H=5
jobs=json.load(open('jobs.json'))
os.makedirs('final',exist_ok=True)
hard={'c2','c3','c4','c5','c6','c7'}  # quick cuts, no crossfade
TOT=round(jobs[-1]['b']*FPS)
for i,j in enumerate(jobs):
    st=round(j['a']*FPS);nf=round(j['b']*FPS)-st
    for k in range(nf):
        fr=Image.open(f"seg/{j['seg']}/{k:04d}.jpg")
        if i>0 and j['seg'] not in hard and k<H:
            p=jobs[i-1];pn=round(p['b']*FPS)-round(p['a']*FPS)
            pf=f"seg/{p['seg']}/{min(pn+k,p['n']-1):04d}.jpg"
            fr=Image.blend(Image.open(pf),fr,(k+1)/(H+1))
        fr.save(f"final/{st+k:04d}.jpg",quality=92)
print(len(os.listdir('final')),TOT)
