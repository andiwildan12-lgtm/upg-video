#!/usr/bin/env python3
"""Jalur footage Behel (work/base.mp4) dari klip Drive di aset-drive/. Hitam = adegan motion."""
import subprocess, pathlib
A = pathlib.Path(__file__).resolve().parents[3] / "aset-drive"
P = pathlib.Path(__file__).resolve().parents[1]
SEGS = [("black",None,0,19.9,""),
 ("behel/IMG_3489.MOV",1.0,19.9,22.9,""), ("suasana/IMG_3503.MOV",2.0,22.9,26.85,""), ("black",None,26.85,31.55,""),
 ("behel/IMG_3483.MOV",0.5,31.55,32.7,""), ("behel/IMG_3493.MOV",1.0,32.7,34.1,""),
 ("behel/IMG_3487.MOV",1.0,34.1,42.0,",boxblur=22:2,eq=brightness=-0.08:saturation=0.9"),
 ("behel/IMG_3496.MOV",2.0,42.0,44.7,""), ("black",None,44.7,47.7,"")]
args=["ffmpeg","-v","error","-y"]; fl=[]
for i,(f,ss,a,b,x) in enumerate(SEGS):
    d=round(b-a,3)
    args += (["-f","lavfi","-t",str(d),"-i","color=c=black:s=1080x1920:r=30"] if f=="black" else ["-ss",str(ss),"-t",str(d),"-i",str(A/f)])
    fl.append(f"[{i}:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=duration={d},setpts=PTS-STARTPTS{x}[v{i}]")
fl.append("".join(f"[v{i}]" for i in range(len(SEGS)))+f"concat=n={len(SEGS)}:v=1:a=0[out]")
(P/"work").mkdir(exist_ok=True)
args+=["-filter_complex",";".join(fl),"-map","[out]","-c:v","libx264","-crf","16","-preset","fast","-pix_fmt","yuv420p",str(P/"work/base.mp4")]
subprocess.run(args,check=True); print("base ->", P/"work/base.mp4")
