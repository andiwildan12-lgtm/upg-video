#!/usr/bin/env python3
"""Siapkan folder proyek Edit Rekaman (Remotion) dari template UPG Video.

Pemakaian: python3 setup_proyek.py <folder-proyek>
Aman dijalankan ulang: tidak menimpa src/timeline.js yang sudah diisi.
Butuh internet ke registry npm (diizinkan default di environment Claude Code).
"""
import json, shutil, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]          # .../upg-video
TPL = SKILL / "rekaman" / "template" / "src"
ASSETS = SKILL / "assets"
PKGS = ["remotion@4.0.300", "@remotion/cli@4.0.300", "react@18.3.1", "react-dom@18.3.1"]

if len(sys.argv) < 2:
    sys.exit(__doc__)
P = Path(sys.argv[1]).resolve()
for d in ["public/fonts", "src", "out/preview", "work", "sumber"]:
    (P / d).mkdir(parents=True, exist_ok=True)

for f in TPL.iterdir():
    dst = P / "src" / f.name
    if f.name in ("timeline.js", "meta.js") and dst.exists():
        continue                                       # jangan timpa isi proyek
    shutil.copy2(f, dst)
for f in ASSETS.glob("nunito-latin-*-normal.woff2"):
    shutil.copy2(f, P / "public" / "fonts" / f.name)
shutil.copy2(ASSETS / "logo-upg-dental-care.jpg", P / "public" / "logo-upg-dental-care.jpg")

gi = P / ".gitignore"
if not gi.exists():
    gi.write_text("node_modules/\nsumber/\npublic/footage.mp4\nout/preview/\nwork/\n")

pkg = P / "package.json"
if not pkg.exists():
    pkg.write_text(json.dumps({"name": P.name.lower(), "private": True, "type": "module"}, indent=2))
if not (P / "node_modules" / "remotion").exists():
    r = subprocess.run(["npm", "install", "--no-audit", "--no-fund", *PKGS], cwd=P)
    if r.returncode:
        sys.exit("npm install gagal — cek koneksi ke registry npm.")
print(f"Siap: {P}\nBerikutnya: python3 {SKILL}/rekaman/scripts/prep_footage.py <file-rekaman> {P}")
