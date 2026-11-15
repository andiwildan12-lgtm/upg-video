#!/usr/bin/env python3
"""Jalur footage Cerita Rina (work/base.mp4). Hitam = adegan animasi."""
import subprocess, pathlib
A = pathlib.Path(__file__).resolve().parents[3] / "aset-drive"
P = pathlib.Path(__file__).resolve().parents[1]
SEGS = [("black",None,0,20.65,""),
 ("suasana/IMG_3505.MOV",3.0,20.65,22.3,""), ("suasana/IMG_3503.MOV",2.0,22.3,24.35,""),
 ("suasana/IMG_3217.MOV",3.0,24.35,27.2,""), ("suasana/IMG_3501.MOV",4.0,27.2,31.55,""),
 ("tambal/IMG_4683.MOV",1.0,31.55,34.6,""), ("tambal/IMG_3245.MOV",1.0,34.6,38.35,""),
 ("tambal/IMG_4685.MOV",1.0,38.35,44.35,""),
 ("black",None,44.35,59.7,"")]
args=["ffmpeg","-v","error","-y"]; fl=[]
for i,(f,ss,a,b,x) in enumerate(SEGS):
    d=round(b-a,3)
    args += (["-f","lavfi","-t",str(d),"-i","color=c=black:s=1080x1920:r=30"] if f=="black" else ["-ss",str(ss),"-t",str(d),"-i",str(A/f)])
    fl.append(f"[{i}:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=duration={d},setpts=PTS-STARTPTS{x}[v{i}]")
fl.append("".join(f"[v{i}]" for i in range(len(SEGS)))+f"concat=n={len(SEGS)}:v=1:a=0[out]")
(P/"work").mkdir(exist_ok=True)
args+=["-filter_complex",";".join(fl),"-map","[out]","-c:v","libx264","-crf","16","-preset","fast","-pix_fmt","yuv420p",str(P/"work/base.mp4")]
subprocess.run(args,check=True); print("base ->", P/"work/base.mp4")
