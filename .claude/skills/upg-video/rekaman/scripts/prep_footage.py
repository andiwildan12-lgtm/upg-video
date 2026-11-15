#!/usr/bin/env python3
"""Siapkan rekaman Dir untuk diedit.

Pemakaian: python3 prep_footage.py <file-rekaman> <folder-proyek> [--keep-res]

- Laporkan spesifikasi & loudness asli.
- Ubah ke 30 fps konstan, H.264, tetap vertikal. Default diskalakan ke lebar 1080
  (cukup untuk Reels/Meta; --keep-res untuk mempertahankan resolusi asli).
- Normalisasi suara 2-pass ke -14 LUFS, true peak -2,5 dBTP (ruang untuk musik).
- Tulis public/footage.mp4, src/meta.js, dan contact sheet work/contact.jpg (1 frame/detik).
File asli TIDAK diubah atau dihapus.
"""
import json, re, subprocess, sys
from pathlib import Path

def run(args):
    return subprocess.run(args, capture_output=True, text=True)

if len(sys.argv) < 3:
    sys.exit(__doc__)
src, P = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
keep = "--keep-res" in sys.argv
if not src.exists():
    sys.exit(f"File tidak ditemukan: {src}")

info = json.loads(run(["ffprobe", "-v", "error", "-show_entries",
    "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate:stream_side_data=rotation",
    "-of", "json", str(src)]).stdout)
v = next(s for s in info["streams"] if s["codec_type"] == "video")
has_audio = any(s["codec_type"] == "audio" for s in info["streams"])
rot = abs(int(next((sd.get("rotation", 0) for sd in v.get("side_data_list", [])), 0) or 0))
w, h = (v["height"], v["width"]) if rot in (90, 270) else (v["width"], v["height"])
dur = float(info["format"]["duration"])
print(f"ASLI  {w}x{h} @ {v['r_frame_rate']} · {dur:.2f} dtk · audio: {'ada' if has_audio else 'TIDAK ADA'}")
if h < w:
    print("PERINGATAN: rekaman horizontal. Perlu keputusan Dir: crop ke 9:16 atau pakai latar.")

af = []
if has_audio:
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", run(["ffmpeg", "-hide_banner", "-i", str(src), "-vn", "-af",
        "loudnorm=I=-14:TP=-2.5:LRA=11:print_format=json", "-f", "null", "-"]).stderr)
    j = json.loads(m.group(0))
    print(f"ASLI  loudness {j['input_i']} LUFS · true peak {j['input_tp']} dBTP")
    af = ["-af", f"loudnorm=I=-14:TP=-2.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
          f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true",
          "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "256k"]

vf = "fps=30" + ("" if keep or w <= 1080 else ",scale=1080:-2")
out = P / "public" / "footage.mp4"
out.parent.mkdir(parents=True, exist_ok=True)
r = run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", vf, "-c:v", "libx264", "-crf", "16", "-preset", "medium",
         "-pix_fmt", "yuv420p", *(af or ["-an"]), "-movflags", "+faststart", str(out)])
if r.returncode:
    sys.exit("Konversi gagal:\n" + r.stderr)

o = json.loads(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                    "-of", "json", str(out)]).stdout)
ow, oh, od = o["streams"][0]["width"], o["streams"][0]["height"], float(o["format"]["duration"])
(P / "src").mkdir(exist_ok=True)
(P / "src" / "meta.js").write_text(
    "// DITULIS OTOMATIS oleh prep_footage.py — jangan diedit manual.\n"
    f"export const META = {{width: {ow}, height: {oh}, fps: 30, durationSec: {od:.3f}}};\n")
(P / "work").mkdir(exist_ok=True)
cols, n = 8, max(1, int(od))
run(["ffmpeg", "-v", "error", "-y", "-i", str(out), "-vf", f"fps=1,scale=200:-2,tile={cols}x{(n + cols - 1) // cols}:padding=3",
     "-frames:v", "1", str(P / "work" / "contact.jpg")])
print(f"HASIL {out} · {ow}x{oh} @ 30 fps · {od:.2f} dtk\nCONTACT SHEET work/contact.jpg (1 frame/detik, kiri→kanan)")
