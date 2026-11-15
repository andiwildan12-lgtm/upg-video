#!/usr/bin/env python3
"""Verifikasi video hasil render UPG Motion sebelum diserahkan.

Pemakaian: python3 verify_video.py <video.mp4> [grid.jpg] [detik1,detik2,...]

Cek: spesifikasi (1080x1920, 30 fps, H.264 + AAC), decode utuh tanpa error,
loudness terintegrasi (target -14 LUFS ±1,5), true peak <= -1 dBTP.
Opsional: grid frame pada detik tertentu untuk dicek visual.
Logika diadaptasi dari skrip verify.mjs milik skill `shortform-edit`.
"""
import json, re, subprocess, sys

def run(args):
    return subprocess.run(args, capture_output=True, text=True)

if len(sys.argv) < 2:
    sys.exit(__doc__)
video = sys.argv[1]
ok = True

def report(good, msg):
    global ok
    ok &= good
    print(("OK    " if good else "GAGAL ") + msg)

info = json.loads(run(["ffprobe", "-v", "error", "-show_entries",
    "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate",
    "-of", "json", video]).stdout or "{}")
streams = {s["codec_type"]: s for s in info.get("streams", [])}
v, a = streams.get("video", {}), streams.get("audio", {})
dur = float(info.get("format", {}).get("duration", 0))
report(v.get("width") == 1080 and v.get("height") == 1920, f"resolusi {v.get('width')}x{v.get('height')} (target 1080x1920)")
report(v.get("r_frame_rate") == "30/1", f"fps {v.get('r_frame_rate')} (target 30/1)")
report(v.get("codec_name") == "h264", f"video codec {v.get('codec_name')}")
report(a.get("codec_name") == "aac", f"audio codec {a.get('codec_name')} (tanpa audio = belum ada narasi)")
print(f"INFO  durasi {dur:.2f} dtk")

dec = run(["ffmpeg", "-v", "error", "-i", video, "-f", "null", "-"])
err = dec.stderr.strip().splitlines()[:3]
report(dec.returncode == 0 and not err, "decode utuh" + ("" if not err else f": {err}"))

if a:
    out = run(["ffmpeg", "-hide_banner", "-i", video, "-vn", "-af", "loudnorm=print_format=json", "-f", "null", "-"]).stderr
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", out)
    if m:
        j = json.loads(m.group(0))
        i, tp = float(j["input_i"]), float(j["input_tp"])
        report(-15.5 <= i <= -12.5, f"loudness {i} LUFS (target -14 ±1,5)")
        report(tp <= -1.0, f"true peak {tp} dBTP (batas <= -1)")
    else:
        report(False, "loudness tidak terbaca")

if len(sys.argv) >= 4:
    grid, times = sys.argv[2], [float(x) for x in sys.argv[3].split(",") if x]
    sel = "+".join(f"eq(n\\,{round(t*30)})" for t in times)
    r = run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vf",
             f"select='{sel}',scale=270:-2,tile={len(times)}x1:padding=6:color=white",
             "-fps_mode", "vfr", "-frames:v", "1", grid])
    report(r.returncode == 0, f"grid frame -> {grid}")

print("\nHASIL: " + ("LULUS" if ok else "ADA YANG GAGAL — perbaiki sebelum diserahkan"))
sys.exit(0 if ok else 1)
