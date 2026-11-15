#!/usr/bin/env python3
"""Susun jalur footage V6 (work/base-V6.mp4) dari klip Drive di aset-drive/. Hitam = adegan motion."""
import subprocess, pathlib
A = pathlib.Path(__file__).resolve().parents[3] / "aset-drive"
P = pathlib.Path(__file__).resolve().parents[1]
SEGS = [("black",None,0,16.9,""),
 ("scaling/IMG_3236.MOV",1.0,16.9,19.0,""), ("scaling/IMG_3232.MOV",0.5,19.0,20.6,""), ("scaling/IMG_3223.MOV",1.5,20.6,22.1,""),
 ("suasana/IMG_3503.MOV",2.0,22.1,24.3,""), ("suasana/IMG_3501.MOV",4.0,24.3,26.3,""),
 ("suasana/IMG_3478.MOV",1.5,26.3,27.6,""), ("suasana/IMG_3479.MOV",3.0,27.6,28.9,""), ("suasana/IMG_3217.MOV",3.0,28.9,30.2,""),
 ("suasana/IMG_3480.MOV",1.0,30.2,38.7,",boxblur=22:2,eq=brightness=-0.06:saturation=0.9"),
 ("suasana/IMG_3502.MOV",2.0,38.7,43.7,""), ("black",None,43.7,46.7,"")]
args=["ffmpeg","-v","error","-y"]; fl=[]
for i,(f,ss,a,b,x) in enumerate(SEGS):
    d=round(b-a,3)
    args += (["-f","lavfi","-t",str(d),"-i","color=c=black:s=1080x1920:r=30"] if f=="black" else ["-ss",str(ss),"-t",str(d),"-i",str(A/f)])
    fl.append(f"[{i}:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=duration={d},setpts=PTS-STARTPTS{x}[v{i}]")
fl.append("".join(f"[v{i}]" for i in range(len(SEGS)))+f"concat=n={len(SEGS)}:v=1:a=0[out]")
(P/"work").mkdir(exist_ok=True)
args+=["-filter_complex",";".join(fl),"-map","[out]","-c:v","libx264","-crf","16","-preset","fast","-pix_fmt","yuv420p",str(P/"work/base-V6.mp4")]
subprocess.run(args,check=True); print("base ->", P/"work/base-V6.mp4")
