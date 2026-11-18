import sys,subprocess,numpy as np
f=sys.argv[1]
raw=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
x=np.frombuffer(raw,np.int16).astype(float)/32768
hop=320;n=len(x)//hop
rms=np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2))+1e-9 for i in range(n)])
db=20*np.log10(rms);thr=np.percentile(db,95)-28
sil=db<thr;out=[];i=0
while i<n:
  if sil[i]:
    j=i
    while j<n and sil[j]:j+=1
    if (j-i)*0.02>=0.18:out.append((round(i*0.02,2),round(j*0.02,2)))
    i=j
  else:i+=1
print(f, 'dur',round(n*0.02,2));print(out)
