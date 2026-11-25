#!/usr/bin/env python3
"""Cari & perbaiki frame "jatuh" hasil render Remotion (video kosong/hitam 1-2 frame, overlay teks tetap ada).

Pemakaian: python3 perbaiki_frame_hitam.py <video.mp4> [--cek]
  --cek : hanya melapor (exit 1 bila ada frame jatuh)
Tanpa --cek: frame jatuh diganti frame sebelumnya, video di-encode ulang (CRF 16), audio disalin apa adanya.
Kriteria: terang rata-rata frame < 35% dari median 4 tetangganya (±2 frame) dan tetangganya cukup terang (>60),
jadi pergantian adegan/fade ke penutup tidak ikut terdeteksi.
Temuan 25 Nov 2026 (Adhila-A V2 dtk 48,9 & V3 dtk 10,5): gangguan acak, bukan dari klip sumber.
"""
import subprocess, sys, os
import numpy as np

if len(sys.argv) < 2:
    sys.exit(__doc__)
src = sys.argv[1]; cek = "--cek" in sys.argv
W, H = 108, 192
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
                     capture_output=True, check=True).stdout
m = np.frombuffer(raw, np.uint8).reshape(-1, H, W).mean((1, 2))
bad = []
for i in range(len(m)):
    nb = [m[j] for j in (i - 2, i - 1, i + 1, i + 2) if 0 <= j < len(m) and j not in bad]
    if len(nb) >= 2 and np.median(nb) > 60 and m[i] < 0.35 * np.median(nb):
        bad.append(i)
fps = 30
print("frame jatuh:", [(i, round(i / fps, 2)) for i in bad] or "tidak ada")
if cek or not bad:
    sys.exit(1 if bad else 0)

info = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate",
                       "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip().split(",")
w, h, rate = int(info[0]), int(info[1]), info[2]
tmp = src + ".perbaikan.mp4"
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", rate, "-i", "-",
                        "-i", src, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "16", "-preset", "medium",
                        "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", tmp], stdin=subprocess.PIPE)
sz = w * h * 3; prev = None; n = 0; badset = set(bad)
while True:
    buf = dec.stdout.read(sz)
    if len(buf) < sz:
        break
    if n in badset and prev is not None:
        buf = prev
    enc.stdin.write(buf); prev = buf; n += 1
enc.stdin.close(); enc.wait(); dec.wait()
if enc.returncode != 0:
    sys.exit("encode gagal")
os.replace(tmp, src)
print(f"diperbaiki {len(bad)} frame -> {src}")
