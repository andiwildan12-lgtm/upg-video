#!/usr/bin/env python3
"""Kunci bingkai: tiap frame diskalakan & digeser supaya jendela bingkai selalu di posisi yang sama (lebar TW, pusat CX,CY).
Tepi kosong diisi latar blur. Input work/build/pNN.mp4 (orang), output pNNs.mp4."""
import cv2, numpy as np, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); from deteksi import kotak
P = Path(__file__).resolve().parents[1]; B = P/'work'/'build'
TW, CX, CY = 800, 540, 930
for i in range(1, 19):
    src = B/f'p{i:02d}.mp4'; cap = cv2.VideoCapture(str(src)); fr = []
    while True:
        ok, f = cap.read()
        if not ok: break
        fr.append(f)
    bx = [kotak(f) for f in fr]
    idx = [k for k, b in enumerate(bx) if b]
    arr = np.array([[b[0] + b[2] / 2, b[1] + b[3] / 2, b[2]] for b in bx if b], float)
    # isi frame gagal dengan interpolasi, lalu haluskan (median + rata-rata)
    full = np.stack([np.interp(range(len(fr)), idx, arr[:, j]) for j in range(3)], 1)
    from scipy.ndimage import median_filter, uniform_filter1d
    full = uniform_filter1d(median_filter(full, size=(7, 1), mode='nearest'), 5, axis=0, mode='nearest')
    wr = cv2.VideoWriter(str(B/f'p{i:02d}s.mp4'), cv2.VideoWriter_fourcc(*'mp4v'), 30, (1080, 1920))
    for f, (cx, cy, w) in zip(fr, full):
        s = TW / w
        M = np.float32([[s, 0, CX - s * cx], [0, s, CY - s * cy]])
        bg = cv2.GaussianBlur(cv2.resize(f, (1080, 1920)), (0, 0), 35)
        out = cv2.warpAffine(f, M, (1080, 1920), borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
        mask = cv2.warpAffine(np.full(f.shape[:2], 255, np.uint8), M, (1080, 1920))
        a = (cv2.GaussianBlur(mask, (21, 21), 0).astype(np.float32) / 255)[..., None]
        wr.write((out * a + bg * (1 - a)).astype(np.uint8))
    wr.release(); print(i, len(fr), 'frame', len(idx), 'terdeteksi', 'skala %.2f-%.2f' % (TW / full[:, 2].max(), TW / full[:, 2].min()))
