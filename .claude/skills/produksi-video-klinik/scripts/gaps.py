import sys,subprocess,numpy as np
f=sys.argv[1];raw=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
x=np.frombuffer(raw,np.int16).astype(float)/32768;w=320;n=len(x)//w
r=np.array([np.sqrt(np.mean(x[i*w:(i+1)*w]**2))+1e-9 for i in range(n)]);db=20*np.log10(r);th=np.percentile(db,95)-28
q=db<th;i=0;out=[]
while i<n:
  if q[i]:
    j=i
    while j<n and q[j]:j+=1
    if (j-i)*0.02>=0.18:out.append((round(i*0.02,2),round(j*0.02,2),round((j-i)*0.02,2)))
    i=j
  else:i+=1
print(f,len(x)/16000);[print(o) for o in out]
