import sys,numpy as np
from PIL import Image
out,*subs=sys.argv[1:]
a=np.mean([np.asarray(Image.open(s),dtype=np.float32) for s in subs],axis=0)
Image.fromarray(a.clip(0,255).astype(np.uint8)).save(out,quality=92)
