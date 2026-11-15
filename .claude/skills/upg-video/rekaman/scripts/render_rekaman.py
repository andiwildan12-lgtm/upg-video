#!/usr/bin/env python3
"""Render video Edit Rekaman (Remotion) dengan gerbang ACC.

Pemakaian:
  python3 render_rekaman.py <folder-proyek> preview [detik_mulai-detik_akhir]   -> out/preview/preview.mp4 (skala 0,5)
  python3 render_rekaman.py <folder-proyek> stills  "1,4.5,9"                    -> out/preview/still-<t>.jpg
  python3 render_rekaman.py <folder-proyek> final                               -> out/<slug>-V{n}.mp4 + verifikasi

Preview & stills tetap butuh ACC (keduanya bagian produksi). Memakai Chromium yang sudah
terpasang di lingkungan (tanpa unduhan Chrome).
"""
import glob, json, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]
if len(sys.argv) < 3:
    sys.exit(__doc__)
P, mode = Path(sys.argv[1]).resolve(), sys.argv[2]

gate = subprocess.run(["python3", str(SKILL / "scripts" / "acc_gate.py"), "check", str(P)])
if gate.returncode:
    sys.exit(1)
acc = json.loads((P / "acc.json").read_text())

browser = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))), None)
bx = [f"--browser-executable={browser}"] if browser else []
base = ["npx", "remotion"]
(P / "out" / "preview").mkdir(parents=True, exist_ok=True)

def rr(args):
    r = subprocess.run(base + args + bx + ["--log=error"], cwd=P)
    if r.returncode:
        sys.exit("Render gagal.")

if mode == "stills":
    fps = 30
    for t in [float(x) for x in sys.argv[3].split(",")]:
        rr(["still", "src/index.jsx", "Main", f"out/preview/still-{t:05.1f}.jpg", f"--frame={round(t * fps)}", "--scale=0.5"])
    print("stills -> out/preview/")
elif mode == "preview":
    extra = []
    if len(sys.argv) > 3:
        a, b = (float(x) for x in sys.argv[3].split("-"))
        extra = [f"--frames={round(a * 30)}-{round(b * 30) - 1}"]
    rr(["render", "src/index.jsx", "Main", "out/preview/preview.mp4", "--scale=0.5", "--codec=h264", *extra])
    print("preview -> out/preview/preview.mp4")
elif mode == "final":
    out = P / "out" / f"{P.name}-{acc['version']}.mp4"
    if out.exists():
        sys.exit(f"{out.name} sudah ada. Versi render tidak ditimpa: hapus manual atau naikkan versi rancangan.")
    rr(["render", "src/index.jsx", "Main", str(out), "--codec=h264", "--crf=17", "--audio-bitrate=256k"])
    subprocess.run(["python3", str(SKILL / "scripts" / "verify_video.py"), str(out)])
else:
    sys.exit(__doc__)
