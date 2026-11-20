import numpy as np,cv2
def film_box(f):
  g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
  m=(g<45).astype(np.uint8)
  m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
  k,lab,st,cen=cv2.connectedComponentsWithStats(m)
  best=None
  for i in range(1,k):
    x,y,w,h,a=st[i]
    if a>40000 and 0.9<w/max(h,1)<2.2 and y<1500 and (best is None or a>best[4]): best=(x,y,w,h,a)
  return best
def blur_label(f,box):
  x,y,w,h,_=box
  x1,y1=max(0,x-10),max(0,y-10);x2,y2=min(f.shape[1],x+int(w*0.55)),min(f.shape[0],y+int(h*0.36))
  roi=f[y1:y2,x1:x2];f[y1:y2,x1:x2]=cv2.GaussianBlur(roi,(0,0),14)
  return f
if __name__=='__main__':
  import sys
  for p in sys.argv[1:]:
    f=cv2.imread(p);b=film_box(f);print(p,b)
    if b: cv2.imwrite(p,blur_label(f,b))
