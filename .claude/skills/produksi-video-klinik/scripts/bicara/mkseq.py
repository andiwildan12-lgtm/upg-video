import json,os,sys
from PIL import Image
stf,sd,od=sys.argv[1:4];S=json.load(open(stf));os.makedirs(od,exist_ok=True)
for f in os.listdir(od): os.remove(f'{od}/{f}')
N=round(S[-1]['t1']*30)
for f in range(N):
  t=(f+0.5)/30;i=next(k for k,s in enumerate(S) if s['t0']<=t<s['t1'] or k==len(S)-1)
  os.symlink(os.path.abspath(f'{sd}/{i:03d}.png'),f'{od}/{f:04d}.png')
ci=next(k for k,s in enumerate(S) if s.get('card'));T0=S[ci]['t0']
prev=Image.open(f'{sd}/{ci-1:03d}.png').convert('RGBA');cur=Image.open(f'{sd}/{ci:03d}.png').convert('RGBA')
for f in range(round(T0*30)-4,round(T0*30)+9):
  t=(f+0.5)/30;k=min(1,max(0,(t-T0+0.12)/0.3));p=f'{od}/{f:04d}.png';os.remove(p);Image.blend(prev,cur,k).save(p)
print(od,N)
