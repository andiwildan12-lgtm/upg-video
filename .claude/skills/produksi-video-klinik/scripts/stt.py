import sys,json,os,subprocess
import numpy as np
def load(f):
  raw=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
  return np.frombuffer(raw,np.int16).astype(np.float32)/32768
from faster_whisper import WhisperModel
m=WhisperModel(sys.argv[1],device='cpu',compute_type='int8')
out={}
for f in sys.argv[2:]:
  segs,_=m.transcribe(load(f),language='id',word_timestamps=True,vad_filter=False,beam_size=5)
  L=[]
  for s in segs:
    L.append(dict(s=round(s.start,2),e=round(s.end,2),t=s.text.strip(),w=[(round(w.start,2),round(w.end,2),w.word.strip()) for w in s.words]))
    print(f.split('/')[-1],f'{s.start:6.2f}-{s.end:6.2f}',s.text.strip(),flush=True)
  out[f]=L
json.dump(out,open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[2])),'stt.json'),'w'),ensure_ascii=False,indent=1)
