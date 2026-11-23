#!/usr/bin/env python3
"""Samarkan wajah/data pasien di klip video, kotak bisa bergerak mengikuti keyframe.

Pemakaian: python3 samarkan.py <masuk.mp4> <keluar.mp4> <kotak.json> [--gaya mosaik|blur]
kotak.json: [ {"kf": [[t, x, y, w, h], [t, x, y, w, h], ...]}, ... ]   (detik klip, piksel frame klip)
  - satu objek = satu area; posisi di antara keyframe diinterpolasi linear; di luar rentang = keyframe terdekat.
Gaya: "mosaik" = kotak-kotak bersudut bulat (ciri UPG, keputusan Dir 23 Nov 2026)
      "blur"   = kabur halus (dipakai Ruma).
Audio disalin apa adanya. Butuh opencv-python-headless (cv2) + ffmpeg.
"""
import json, subprocess, sys
import cv2, numpy as np

def lerp_box(kf, t):
    kf = sorted(kf)
    if t <= kf[0][0]: return kf[0][1:]
    if t >= kf[-1][0]: return kf[-1][1:]
    for a, b in zip(kf, kf[1:]):
        if a[0] <= t <= b[0]:
            r = (t - a[0]) / max(b[0] - a[0], 1e-6)
            return [a[i] + (b[i] - a[i]) * r for i in range(1, 5)]

def rounded_mask(w, h, rad):
    m = np.zeros((h, w), np.uint8)
    cv2.rectangle(m, (rad, 0), (w - rad, h), 255, -1); cv2.rectangle(m, (0, rad), (w, h - rad), 255, -1)
    for cx, cy in ((rad, rad), (w - rad, rad), (rad, h - rad), (w - rad, h - rad)):
        cv2.circle(m, (cx, cy), rad, 255, -1)
    return m

def main():
    a = sys.argv[1:]
    gaya = "mosaik"
    if "--gaya" in a: i = a.index("--gaya"); gaya = a[i + 1]; del a[i:i + 2]
    src, dst, kj = a
    areas = json.load(open(kj))
    cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS) or 30
    W, H = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                            "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "17", "-preset", "veryfast",
                            "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", dst], stdin=subprocess.PIPE)
    n = 0
    while True:
        ok, fr = cap.read()
        if not ok: break
        t = n / fps
        for ar in areas:
            x, y, w, h = [int(round(v)) for v in lerp_box(ar["kf"], t)]
            x, y = max(0, x), max(0, y); w, h = min(w, W - x), min(h, H - y)
            if w < 8 or h < 8: continue
            reg = fr[y:y + h, x:x + w]
            if gaya == "blur":
                k = max(31, (min(w, h) // 3) | 1); eff = cv2.GaussianBlur(reg, (k, k), 0)
            else:
                cell = max(10, min(w, h) // 7)
                eff = cv2.resize(cv2.resize(reg, (max(1, w // cell), max(1, h // cell)), interpolation=cv2.INTER_AREA), (w, h), interpolation=cv2.INTER_NEAREST)
            m = rounded_mask(w, h, max(6, min(w, h) // 6))[:, :, None] / 255.0
            fr[y:y + h, x:x + w] = (eff * m + reg * (1 - m)).astype(np.uint8)
        enc.stdin.write(fr.tobytes()); n += 1
    enc.stdin.close(); enc.wait(); cap.release()
    print(f"{dst}: {n} frame, {len(areas)} area, gaya {gaya}")

if __name__ == "__main__":
    main()
