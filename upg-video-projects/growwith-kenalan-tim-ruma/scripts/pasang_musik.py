"""Pasang musik latar ke video GrowWith (video v3 hening). Musik dipotong ke durasi video, fade-in 0,3 dtk, fade-out 1,5 dtk, loudnorm -16 LUFS.
Pakai: python3 pasang_musik.py VIDEO MUSIK OUT"""
import subprocess, sys
V, M, O = sys.argv[1:4]
T=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V],capture_output=True,text=True).stdout)
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',V,'-i',M,'-filter_complex',
 f'[1:a]atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.3,afade=t=out:st={T-1.5:.2f}:d=1.5,loudnorm=I=-16:TP=-2:LRA=11,aresample=48000[a]',
 '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',O],check=True)
print('ok',O)
