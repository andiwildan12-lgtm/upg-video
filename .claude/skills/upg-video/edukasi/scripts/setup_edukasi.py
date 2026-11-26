#!/usr/bin/env python3
"""Siapkan folder proyek EDUKASI DOKTER (Remotion) dari template skill.

Pemakaian: python3 setup_edukasi.py <folder-proyek>
Aman dijalankan ulang: tidak menimpa edit.json / src/timeline.js yang sudah ada.
"""
import json, shutil, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]
TPL = SKILL / "edukasi" / "template" / "src"
ASSETS = SKILL / "assets"
PKGS = ["remotion@4.0.300", "@remotion/cli@4.0.300", "react@18.3.1", "react-dom@18.3.1"]

if len(sys.argv) < 2:
    sys.exit(__doc__)
P = Path(sys.argv[1]).resolve()
for d in ["public/fonts", "public/clips", "public/sfx", "src", "out/preview", "work", "sumber"]:
    (P / d).mkdir(parents=True, exist_ok=True)
for f in TPL.iterdir():
    dst = P / "src" / f.name
    if f.name == "timeline.js" and dst.exists():
        continue
    shutil.copy2(f, dst)
for f in [*ASSETS.glob("nunito-latin-*-normal.woff2"), *ASSETS.glob("*-latin-*-normal.woff2")]:
    shutil.copy2(f, P / "public" / "fonts" / f.name)
shutil.copy2(ASSETS / "logo-upg-resmi.png", P / "public" / "logo-upg-resmi.png")
for _l in ("logo-upg-mendatar.png", "logo-upg-mendatar-putih.png"):  # logo pojok + penutup standar organik (versi mendatar resmi, Dir 23 Nov 2026)
    shutil.copy2(ASSETS / _l, P / "public" / _l)
# pustaka SFX bersama (dibuat sekali, dipakai ulang semua proyek edukasi)
for f in (ASSETS / "sfx").glob("*.mp3") if (ASSETS / "sfx").exists() else []:
    shutil.copy2(f, P / "public" / "sfx" / f.name)
if not (P / "edit.json").exists():
    shutil.copy2(SKILL / "edukasi" / "contoh-edit.json", P / "edit.json")
gi = P / ".gitignore"
if not gi.exists():
    gi.write_text("node_modules/\nsumber/\npublic/clips/\nout/preview/\nwork/*.wav\nwork/*.mp4\nwork/clips-tanpa-mosaik/\nout/*.mp4\n")
pkg = P / "package.json"
if not pkg.exists():
    pkg.write_text(json.dumps({"name": P.name.lower(), "private": True, "type": "module"}, indent=2))
if not (P / "node_modules" / "remotion").exists():
    if subprocess.run(["npm", "install", "--no-audit", "--no-fund", *PKGS], cwd=P).returncode:
        sys.exit("npm install gagal — cek koneksi ke registry npm.")
print(f"Siap: {P}\nBerikutnya: prep_klip.py <folder-klip-asli> {P} [nomor klip ...]")
