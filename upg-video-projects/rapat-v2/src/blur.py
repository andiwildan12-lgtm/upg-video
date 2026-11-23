#!/usr/bin/env python3
"""Blur area layar proyektor per klip, kecuali area orang (dilindungi lewat deteksi wajah + badan)."""
import json, sys, cv2, numpy as np
from pathlib import Path
P = Path(__file__).resolve().parents[1]
WIDE = {'0584': 1.4, '0572': 1.4, '0588': 1.2, '0543': 0.55}
BAND = {'0543': [(300, 850, 1080, 970)], '0588': [(0, 400, 880, 640)]}  # baris URL/judul: selalu blur, hanya wajah dilindungi
RECT = {  # x0,y0,x1,y1 di kanvas 1080x1920
  '0588': [(0, 400, 870, 1250)],
  '0543': [],
  '0584': [(0, 680, 420, 1460)],
  '0572': [(0, 680, 200, 1300)],
}
fc = cv2.CascadeClassifier(str(P/'work')+'/haarcascade_frontalface_default.xml')
pc = cv2.CascadeClassifier(str(P/'work')+'/haarcascade_profileface.xml')
def faces(g):
    out = []
    for c in (fc, pc):
        out += list(c.detectMultiScale(g, 1.15, 5, minSize=(60, 60)))
    fl = cv2.flip(g, 1)
    for (x, y, w, h) in pc.detectMultiScale(fl, 1.15, 5, minSize=(60, 60)):
        out.append((g.shape[1] - x - w, y, w, h))
    return out
peta = json.loads((P/'work'/'peta.json').read_text())
for path, clip, vs, vd in peta['vparts']:
    if clip not in RECT: continue
    cap = cv2.VideoCapture(path); fps = cap.get(5)
    out = path.replace('.mp4', '-b.mp4')
    wr = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*'mp4v'), fps, (1080, 1920))
    last, hold, n = None, 0, 0
    while True:
        ok, f = cap.read()
        if not ok: break
        g = cv2.cvtColor(cv2.resize(f, (540, 960)), cv2.COLOR_BGR2GRAY)
        fs = [(x*2, y*2, w*2, h*2) for (x, y, w, h) in faces(g)]
        if fs: last, hold = fs, 20
        elif hold > 0: hold -= 1
        else: last = None
        mask = np.zeros(f.shape[:2], np.uint8)
        for (x0, y0, x1, y1) in RECT[clip]: mask[y0:y1, x0:x1] = 255
        for (x, y, w, h) in (last or []):   # lindungi kepala + badan di bawahnya
            k = WIDE[clip]; mask[max(0, y - int(.45*h)):, max(0, x - int(k*w)):x + w + int(k*w)] = 0
        for (x0, y0, x1, y1) in BAND.get(clip, []):
            band = np.zeros_like(mask); band[y0:y1, x0:x1] = 255
            for (x, y, w, h) in (last or []):
                band[max(0, y - int(.6*h)):y + int(1.4*h), max(0, x - int(.2*w)):x + w + int(.2*w)] = 0
            mask = np.maximum(mask, band)
        mask = cv2.GaussianBlur(mask, (41, 41), 0)
        bl = cv2.GaussianBlur(f, (0, 0), 18)
        a = (mask.astype(np.float32) / 255)[..., None]
        wr.write((bl * a + f * (1 - a)).astype(np.uint8)); n += 1
    wr.release()
    print(clip, vs, n, 'frame', 'wajah' if last else '')
