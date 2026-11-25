#!/usr/bin/env python3
"""Render jalur EDUKASI DOKTER (Remotion).

  python3 render_edukasi.py <proyek> papan "t1,t2,..."   -> out/papan-gambar-V{n}.jpg (8 frame, TANPA gerbang ACC:
                                                            papan gambar diizinkan setelah naskah oke, SKILL.md C0)
  python3 render_edukasi.py <proyek> stills "t1,t2"       -> out/preview/still-*.jpg   (butuh ACC)
  python3 render_edukasi.py <proyek> preview [a-b]        -> out/preview/preview.mp4   (butuh ACC)
  python3 render_edukasi.py <proyek> final                -> out/<slug>-V{n}.mp4 + loudnorm -14 + verifikasi (butuh ACC)
Jalankan build_timeline.py dulu setiap edit.json berubah.
"""
import glob, json, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]
if len(sys.argv) < 3:
    sys.exit(__doc__)
P, mode = Path(sys.argv[1]).resolve(), sys.argv[2]
browser = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))), None)
bx = [f"--browser-executable={browser}"] if browser else []
(P / "out" / "preview").mkdir(parents=True, exist_ok=True)

def rr(args):
    if subprocess.run(["npx", "remotion", *args, *bx, "--log=error"], cwd=P).returncode:
        sys.exit("Render gagal.")

if mode == "papan":
    ver = sys.argv[4] if len(sys.argv) > 4 else "V1"
    ts = [float(x) for x in sys.argv[3].split(",")]
    tmp = P / "work" / "papan"; tmp.mkdir(parents=True, exist_ok=True)
    for f in tmp.glob("*.jpg"):
        f.unlink()
    for i, t in enumerate(ts):
        rr(["still", "src/index.jsx", "Main", str(tmp / f"p{i:02d}.jpg"), f"--frame={round(t * 30)}", "--scale=0.4"])
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp / f"p{i:02d}.jpg"), "-vf",
                        f"pad=iw:ih+56:0:56:white,drawtext=text='{i + 1}  ({t:.1f} dtk)':fontsize=34:x=14:y=12:fontcolor=black",
                        str(tmp / f"q{i:02d}.jpg")], check=True)
    cols = 4 if len(ts) <= 8 else 6
    out = P / "out" / f"papan-gambar-{ver}.jpg"
    subprocess.run(f"ffmpeg -v error -y -pattern_type glob -i '{tmp}/q*.jpg' -vf tile={cols}x{(len(ts) + cols - 1) // cols}:padding=12:color=white -frames:v 1 -q:v 3 {out}", shell=True, check=True)
    print("papan ->", out)
    sys.exit(0)

if subprocess.run(["python3", str(SKILL / "scripts" / "acc_gate.py"), "check", str(P)]).returncode:
    sys.exit(1)
acc = json.loads((P / "acc.json").read_text())
if mode == "stills":
    for t in [float(x) for x in sys.argv[3].split(",")]:
        rr(["still", "src/index.jsx", "Main", f"out/preview/still-{t:05.1f}.jpg", f"--frame={round(t * 30)}", "--scale=0.5"])
elif mode == "preview":
    extra = []
    if len(sys.argv) > 3:
        a, b = (float(x) for x in sys.argv[3].split("-"))
        extra = [f"--frames={round(a * 30)}-{round(b * 30) - 1}"]
    rr(["render", "src/index.jsx", "Main", "out/preview/preview.mp4", "--scale=0.5", "--codec=h264", *extra])
elif mode == "final":
    out = P / "out" / f"{P.name}-{acc['version']}.mp4"
    if out.exists():
        sys.exit(f"{out.name} sudah ada. Versi render tidak ditimpa.")
    raw = P / "out" / "preview" / "mentah.mp4"
    rr(["render", "src/index.jsx", "Main", str(raw), "--codec=h264", "--crf=17", "--audio-bitrate=256k", "--concurrency=4"])
    # loudnorm DUA TAHAP (ukur lalu linear): satu tahap bisa meleset di konten pelan (Video A drg. Naya: -16,7 LUFS)
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                           "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(meas[meas.rindex("{"):meas.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
          f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-c:v", "copy", "-af", ln,
                    "-ar", "48000", "-c:a", "aac", "-b:a", "256k", str(out)], check=True)
    # frame "jatuh" acak dari Remotion (video hitam 1 frame, teks tetap ada) -> ganti frame sebelumnya (temuan 25 Nov 2026)
    subprocess.run(["python3", str(Path(__file__).with_name("perbaiki_frame_hitam.py")), str(out)])
    subprocess.run(["python3", str(SKILL / "scripts" / "verify_video.py"), str(out)])
else:
    sys.exit(__doc__)
