#!/usr/bin/env python3
"""Siapkan klip rekaman dokter (banyak take) untuk jalur EDUKASI DOKTER.

Pemakaian: python3 prep_klip.py <folder-klip-asli> <folder-proyek> [nama1 nama2 ...] [--warna upg|ruma]
--warna: koreksi warna otomatis per klip (skill bersama produksi-video-klinik/scripts/warna/koreksi_warna.py)
Tanpa daftar nama -> semua *.mp4/*.mov di folder. Untuk tiap klip:
  public/clips/<nama>.mp4  : 1080x1920, 30 fps, H.264, suara -14 LUFS (loudnorm per klip)
  work/<nama>.wav           : 16 kHz mono untuk transkrip
  work/klip-sheet.jpg       : satu frame tengah tiap klip (cek lokasi/posisi wajah)
Rekaman horizontal tidak didukung di jalur ini (crop/latar dibahas dulu dengan Dir).
"""
import subprocess, sys
from pathlib import Path

if len(sys.argv) < 3:
    sys.exit(__doc__)
args = sys.argv[1:]
WARNA = None
if "--warna" in args:
    i = args.index("--warna"); WARNA = args[i + 1]; del args[i:i + 2]
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "produksi-video-klinik" / "scripts" / "warna"))
    import koreksi_warna
SRC, P = Path(args[0]).resolve(), Path(args[1]).resolve()
EXT = (".mp4", ".MP4", ".mov", ".MOV")
names = args[2:] or sorted(f.stem for f in SRC.iterdir() if f.suffix in EXT)
(P / "public" / "clips").mkdir(parents=True, exist_ok=True); (P / "work" / "f").mkdir(parents=True, exist_ok=True)
for n in names:
    src = next(SRC / f"{n}{e}" for e in EXT if (SRC / f"{n}{e}").exists())
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(src)]))
    out = P / "public" / "clips" / f"{n}.mp4"
    if not out.exists():
        pre = ""
        if WARNA:
            st = koreksi_warna.ukur(str(src)); pre = koreksi_warna.resep(st, WARNA) + ","
            print(f"{n}: warna {st['kelas']} (Y={st['YAVG']})" + ("  <- CEK DULU, hanya sisipan pendek" if st["kelas"] == "SANGAT_GELAP" else ""))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-map", "0:v:0", "-map", "0:a:0",
                        "-vf", pre + "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30",
                        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000",
                        "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", str(out)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vn", "-ac", "1", "-ar", "16000", str(P / "work" / f"{n}.wav")], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{dur / 2:.2f}", "-i", str(src), "-frames:v", "1",
                    "-vf", f"scale=270:-1,drawtext=text={n}:fontcolor=yellow:fontsize=28:x=8:y=8:box=1:boxcolor=black",
                    str(P / "work" / "f" / f"{n}.jpg")], check=True)
    print(f"{n}: {dur:.1f} dtk")
subprocess.run(f"ffmpeg -v error -y -pattern_type glob -i '{P}/work/f/*.jpg' -vf tile=8x{(len(names) + 7) // 8} -frames:v 1 {P}/work/klip-sheet.jpg", shell=True)
print("Berikutnya: transkrip.py", P)
