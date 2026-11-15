#!/usr/bin/env python3
"""Jalur footage Cerita Rina (work/base.mp4). Hitam = adegan animasi."""
import subprocess, pathlib
A = pathlib.Path(__file__).resolve().parents[3] / "aset-drive"
P = pathlib.Path(__file__).resolve().parents[1]
SEGS = [("black",None,0,20.5,""),
 ("suasana/IMG_3505.MOV",3.0,20.5,21.8,""), ("suasana/IMG_3503.MOV",2.0,21.8,23.15,""),
 ("suasana/IMG_3217.MOV",3.0,23.15,26.6,""), ("suasana/IMG_3501.MOV",4.0,26.6,30.1,""),
 ("tambal/IMG_4683.MOV",1.0,30.1,33.5,""), ("tambal/IMG_3245.MOV",1.0,33.5,37.2,""),
 ("tambal/IMG_4685.MOV",1.0,37.2,42.9,""),
 ("black",None,42.9,57.1,"")]
args=["ffmpeg","-v","error","-y"]; fl=[]
for i,(f,ss,a,b,x) in enumerate(SEGS):
    d=round(b-a,3)
    args += (["-f","lavfi","-t",str(d),"-i","color=c=black:s=1080x1920:r=30"] if f=="black" else ["-ss",str(ss),"-t",str(d),"-i",str(A/f)])
    fl.append(f"[{i}:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=duration={d},setpts=PTS-STARTPTS{x}[v{i}]")
fl.append("".join(f"[v{i}]" for i in range(len(SEGS)))+f"concat=n={len(SEGS)}:v=1:a=0[out]")
(P/"work").mkdir(exist_ok=True)
args+=["-filter_complex",";".join(fl),"-map","[out]","-c:v","libx264","-crf","16","-preset","fast","-pix_fmt","yuv420p",str(P/"work/base.mp4")]
subprocess.run(args,check=True); print("base ->", P/"work/base.mp4")
