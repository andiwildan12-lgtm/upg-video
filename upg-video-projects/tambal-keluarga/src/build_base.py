#!/usr/bin/env python3
"""Jalur footage Tambal + Keluarga (work/base.mp4). Hitam = adegan motion."""
import subprocess, pathlib
A = pathlib.Path(__file__).resolve().parents[3] / "aset-drive"
P = pathlib.Path(__file__).resolve().parents[1]
SEGS = [("black",None,0,15.65,""),
 ("suasana/IMG_3503.MOV",2.0,15.65,18.0,""), ("tambal/IMG_3261.MOV",1.5,18.0,19.8,""), ("tambal/IMG_3262.MOV",1.0,19.8,21.8,""), ("tambal/IMG_3253.MOV",0.5,21.8,24.15,""),
 ("black",None,24.15,25.95,""),
 ("suasana/IMG_3474.MOV",1.5,25.95,27.7,""), ("suasana/IMG_3473.MOV",0.8,27.7,29.0,""), ("suasana/IMG_3478.MOV",1.5,29.0,30.6,""), ("suasana/IMG_3479.MOV",3.0,30.6,32.5,""),
 ("suasana/IMG_3480.MOV",1.0,32.5,38.75,",boxblur=22:2,eq=brightness=-0.06:saturation=0.9"),
 ("black",None,38.75,46.9,"")]
args=["ffmpeg","-v","error","-y"]; fl=[]
for i,(f,ss,a,b,x) in enumerate(SEGS):
    d=round(b-a,3)
    args += (["-f","lavfi","-t",str(d),"-i","color=c=black:s=1080x1920:r=30"] if f=="black" else ["-ss",str(ss),"-t",str(d),"-i",str(A/f)])
    fl.append(f"[{i}:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=duration={d},setpts=PTS-STARTPTS{x}[v{i}]")
fl.append("".join(f"[v{i}]" for i in range(len(SEGS)))+f"concat=n={len(SEGS)}:v=1:a=0[out]")
(P/"work").mkdir(exist_ok=True)
args+=["-filter_complex",";".join(fl),"-map","[out]","-c:v","libx264","-crf","16","-preset","fast","-pix_fmt","yuv420p",str(P/"work/base.mp4")]
subprocess.run(args,check=True); print("base ->", P/"work/base.mp4")
