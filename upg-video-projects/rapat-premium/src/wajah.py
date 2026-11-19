#!/usr/bin/env python3
"""Deteksi pita wajah (y min–max) per potongan video, disimpan ke work/wajah.json untuk penempatan subtitle."""
import json, cv2
from pathlib import Path
P = Path(__file__).resolve().parents[1]
fc = cv2.CascadeClassifier(str(P/'work'/'haarcascade_frontalface_default.xml'))
pc = cv2.CascadeClassifier(str(P/'work'/'haarcascade_profileface.xml'))
pe = json.loads((P/'work'/'peta.json').read_text())
res, t0 = [], 0.0
for path, clip, vs, vd in pe['vparts']:
    p2 = path.replace('.mp4', '-b.mp4'); p2 = p2 if Path(p2).exists() else path
    cap = cv2.VideoCapture(p2); fps = cap.get(5) or 30; n = int(cap.get(7)); ys = []
    for i in range(0, n, max(1, int(fps * 0.4))):
        cap.set(1, i); ok, f = cap.read()
        if not ok: break
        g = cv2.cvtColor(cv2.resize(f, (540, 960)), cv2.COLOR_BGR2GRAY)
        boxes = list(fc.detectMultiScale(g, 1.1, 4, minSize=(40, 40))) + list(pc.detectMultiScale(g, 1.1, 4, minSize=(40, 40)))
        fl = cv2.flip(g, 1); boxes += list(pc.detectMultiScale(fl, 1.1, 4, minSize=(40, 40)))
        for (x, y, w, h) in boxes:
            if w * 2 < 90: continue   # abaikan wajah sangat kecil di latar
            ys.append((y * 2 - int(.35 * h * 2), (y + h) * 2 + int(.25 * h * 2)))
    band = [int(min(a for a, b in ys)), int(max(b for a, b in ys))] if ys else None
    res.append(dict(start=round(t0, 2), end=round(t0 + vd, 2), clip=clip, band=band)); t0 += vd
(P/'work'/'wajah.json').write_text(json.dumps(res, indent=1))
for r in res: print(r)
