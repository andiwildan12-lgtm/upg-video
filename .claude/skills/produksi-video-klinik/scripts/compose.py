import json,os,shutil
from PIL import Image
H=8;FPS=30;TOT=round(51.0*FPS)
segs=json.load(open('segs.json'))
os.makedirs('final2',exist_ok=True)
# hook resample 0..7.6s from old final (0..269)
nh=round(7.6*FPS)
for i in range(nh):
    src=round(i*269/(nh-1));shutil.copy(f'final/{src:04d}.jpg',f'final2/{i:04d}.jpg')
blend_into={1,2,3,4,6,7,8,9,10}  # segment indices that crossfade in from previous
for i,(n,a,b) in enumerate(segs):
    st=round(a*FPS);nf=round((b-a)*FPS);d=f'seg/{i:02d}'
    for k in range(nf):
        fr=Image.open(f'{d}/{k:04d}.jpg')
        if i in blend_into and k<H:
            pv=Image.open(f'seg/{i-1:02d}/{round((segs[i-1][2]-segs[i-1][1])*FPS)+k:04d}.jpg')
            fr=Image.blend(pv,fr,(k+1)/(H+1))
        if st+k<TOT: fr.save(f'final2/{st+k:04d}.jpg',quality=92)
print(len(os.listdir('final2')),TOT)
