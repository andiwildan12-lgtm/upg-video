#!/usr/bin/env python3
"""Deteksi kotak jendela bingkai (garis tinta hijau) di frame 1080x1920: ambil garis panjang horizontal & vertikal."""
import cv2, numpy as np
def kotak(f):
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    m = cv2.inRange(hsv, (55, 40, 40), (100, 255, 230))
    blob = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((31, 31), np.uint8))
    m = cv2.subtract(m, cv2.dilate(blob, np.ones((15, 15), np.uint8)))
    m = cv2.dilate(m, np.ones((7, 7), np.uint8))
    h = cv2.morphologyEx(m, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (220, 1)))
    v = cv2.morphologyEx(m, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 220)))
    ys, xs = np.nonzero(v)
    if len(xs) < 200: return None
    # dua garis vertikal: kiri & kanan
    xl, xr = np.percentile(xs, 2), np.percentile(xs, 98)
    yt, yb = np.percentile(ys, 2), np.percentile(ys, 98)
    hy, hx = np.nonzero(h)
    if len(hy):
        sel = (hx > xl - 40) & (hx < xr + 40)
        if sel.sum() > 100:
            yy = hy[sel]; top = yy[yy < (yt + yb) / 2]; bot = yy[yy > (yt + yb) / 2]
            if len(top): yt = min(yt, np.median(top))
            if len(bot): yb = max(yb, np.median(bot))
    if xr - xl < 300 or yb - yt < 250: return None
    return (int(xl), int(yt), int(xr - xl), int(yb - yt))
if __name__ == '__main__':
    import sys
    for p in sys.argv[1:]:
        f = cv2.imread(p); b = kotak(f); print(p, b)
        if b: x, y, w, h = b; cv2.rectangle(f, (x, y), (x + w, y + h), (0, 0, 255), 8)
        cv2.imwrite(p.replace('.png', '-k.jpg'), cv2.resize(f, (270, 480)))
