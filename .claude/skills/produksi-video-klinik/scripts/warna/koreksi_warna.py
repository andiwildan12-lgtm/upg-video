#!/usr/bin/env python3
"""Koreksi warna otomatis per klip (UPG & Ruma), hanya ffmpeg, tanpa dependensi lain.

Alur: UKUR (signalstats beberapa frame) -> pilih RESEP per kelas -> TERAPKAN -> BANDING (cek visual).
  python3 koreksi_warna.py ukur <klip...>                       tabel kelas + angka, simpan warna.json di folder klip
  python3 koreksi_warna.py filter <klip> [--brand upg|ruma]    cetak string -vf (untuk dipakai skrip lain)
  python3 koreksi_warna.py terapkan <masuk> <keluar> [--brand upg|ruma]   render ulang (audio disalin)
  python3 koreksi_warna.py banding <klip...> --out sheet.jpg [--brand ..]  frame tengah sebelum|sesudah

Kelas (rata-rata luma Y, skala 0-255):
  NORMAL        Y >= 70 : regang kontras ringan (persentil 10/90), terang dijaga natural, buang sebagian warna
                          cast, saturasi naik bila pucat, tajam ringan. Brand: UPG hangat-dekat, Ruma clean-tenang.
  GELAP         25-70   : kurangi bintik (hqdn3d) lalu angkat bayangan dengan gamma ke target terang, saturasi ringan.
  SANGAT_GELAP  Y < 25  : resep GELAP dengan batas angkat; tandai "cek dulu", pakai hanya sebagai sisipan pendek.
Panduan brand (skill panduan-visual-terpadu): UPG warm natural sedikit glow, kulit natural; Ruma clean, soft,
low contrast. Batas dijaga kecil supaya warna kulit tidak berubah.
"""
import json, math, os, re, subprocess, sys

def ukur(path, n=10):
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))
    fps = n / max(dur, 0.5)
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps:.4f},scale=320:-2,signalstats,metadata=print:file=-",
                          "-an", "-f", "null", "-"], capture_output=True, text=True).stdout
    k = {}
    for key in ("YAVG", "YLOW", "YHIGH", "SATAVG", "UAVG", "VAVG"):
        v = [float(x) for x in re.findall(rf"signalstats\.{key}=([\d.]+)", out)]
        k[key] = round(sum(v) / len(v), 1) if v else None
    k["dur"] = round(dur, 1)
    y = k["YAVG"] or 0
    k["kelas"] = "NORMAL" if y >= 70 else ("GELAP" if y >= 25 else "SANGAT_GELAP")
    return k

clamp = lambda x, a, b: max(a, min(b, x))

def resep(s, brand="upg"):
    y, lo, hi, sat, u, v = s["YAVG"], s["YLOW"], s["YHIGH"], s["SATAVG"], s["UAVG"], s["VAVG"]
    # buang 40% warna cast (maks 6 level), lalu nada brand
    du, dv = clamp((128 - u) * 0.4, -6, 6), clamp((128 - v) * 0.4, -6, 6)
    if brand == "upg":
        du, dv, cmax, ssat = du - 0.5, dv + 1.5, 1.30, 1.22   # hangat, sedikit lebih kontras
    else:
        du, dv, cmax, ssat = du + 1.0, dv - 0.5, 1.15, 1.12   # bersih, lembut
    f = []
    if s["kelas"] == "NORMAL":
        a = clamp((200 - 30) / max(hi - lo, 1), 1.0, cmax)
        mid = clamp(y + 6, 122, 140) if brand == "upg" else clamp(y, 122, 145)
        b = mid - a * y
        f.append(f"lutyuv=y='clip({a:.3f}*val+{b:.1f},16,235)':u='clip(val+{du:.1f},16,240)':v='clip(val+{dv:.1f},16,240)'")
        # vibrance: menaikkan warna yang pucat saja (kulit, latar), baju hijau yang sudah jenuh tidak makin norak
        f.append(f"vibrance=intensity={clamp((20 - sat) / 40, 0.05, ssat - 1):.2f}")
        f.append("unsharp=5:5:0.35")
    else:
        dark = s["kelas"] == "SANGAT_GELAP"
        f.append("hqdn3d=4:3:8:6" if dark else "hqdn3d=2.5:2:5:4")
        m = clamp((y - 16) / 219, 0.01, 0.9)
        t = clamp((min(95, 2 * y + 20) - 16) / 219, m, 0.9)
        g = clamp(math.log(m) / math.log(t), 1.0, 1.9 if dark else 2.2)
        f.append(f"lutyuv=y='clip(16+219*pow(clip((val-16)/219,0,1),{1/g:.3f}),16,235)':u='clip(val+{du:.1f},16,240)':v='clip(val+{dv:.1f},16,240)'")
        f.append("eq=saturation=1.12")
        f.append("unsharp=5:5:0.25")
    return ",".join(f)

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    brand = "upg"
    if "--brand" in a: i = a.index("--brand"); brand = a[i + 1]; del a[i:i + 2]
    out = None
    if "--out" in a: i = a.index("--out"); out = a[i + 1]; del a[i:i + 2]
    cmd, files = a[0], a[1:]
    if cmd == "ukur":
        res = {}
        for p in files:
            s = ukur(p); res[os.path.basename(p)] = s
            print(f"{os.path.basename(p)[:34]:34} {s['kelas']:12} Y={s['YAVG']:5} p10={s['YLOW']:5} p90={s['YHIGH']:5} sat={s['SATAVG']:5} U={s['UAVG']} V={s['VAVG']}", flush=True)
        json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(files[0])), "warna.json"), "w"), indent=1)
    elif cmd == "filter":
        print(resep(ukur(files[0]), brand))
    elif cmd == "terapkan":
        src, dst = files
        s = ukur(src); vf = resep(s, brand)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", vf, "-c:v", "libx264", "-crf", "17", "-preset", "veryfast",
                        "-pix_fmt", "yuv420p", "-c:a", "copy", dst], check=True)
        print(f"{os.path.basename(src)} {s['kelas']} -> {dst}")
    elif cmd == "banding":
        import tempfile
        d = tempfile.mkdtemp(); rows = []
        for i, p in enumerate(files):
            s = ukur(p); t = s["dur"] / 2
            for tag, vf in (("a", "scale=-2:480"), ("b", resep(s, brand) + ",scale=-2:480")):
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", p, "-frames:v", "1", "-vf", vf, f"{d}/{i}{tag}.png"], check=True)
            rows.append(f"{d}/{i}")
        inp, fc = [], []
        for i, r in enumerate(rows):
            inp += ["-i", r + "a.png", "-i", r + "b.png"]; fc.append(f"[{2*i}][{2*i+1}]hstack=2,scale=720:-2[r{i}]")
        fc.append("".join(f"[r{i}]" for i in range(len(rows))) + f"vstack={len(rows)}" if len(rows) > 1 else "[r0]null")
        subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fc), out or "banding-warna.jpg"], check=True)
        print("banding:", out or "banding-warna.jpg")
    else:
        sys.exit(__doc__)

if __name__ == "__main__":
    main()
