#!/usr/bin/env python3
"""Mosaik HANYA di area mata pasien (gigi & mulut tetap terlihat), mengikuti wajah per frame.

Pemakaian: python3 samarkan_mata.py <masuk.mp4> <keluar.mp4> <cari.json> [--gaya mosaik|blur] [--langkah 3]
cari.json: area pencarian wajah pasien (format samarkan.py: [{"kf": [[t,x,y,w,h], ...]}]); wajah terdekat dengan
pusat area dipilih (dokter/asisten diabaikan). Deteksi: MediaPipe FaceLandmarker (model face_landmarker.task di folder
ini; butuh `pip install mediapipe` + paket sistem libegl1), dicoba pada potongan area yang diperbesar dengan rotasi
0/90/180/270 (pasien rebahan/miring). Pita mata = persegi panjang berputar yang menutup kedua mata + alis, diberi margin.
Frame tanpa deteksi: diinterpolasi dari deteksi terdekat (<=1 dtk); bila tidak ada, dipakai kotak area pencarian penuh
(aman, seperti samarkan.py). UPG = mosaik, Ruma = blur (keputusan Dir 23-24 Nov 2026).
"""
import json, os, subprocess, sys
import cv2, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EYE = [33, 133, 159, 145, 362, 263, 386, 374, 70, 300, 105, 334, 46, 276]
ROT = {0: None, 90: cv2.ROTATE_90_CLOCKWISE, 180: cv2.ROTATE_180, 270: cv2.ROTATE_90_COUNTERCLOCKWISE}

def lerp_box(kf, t):
    kf = sorted(kf)
    if t <= kf[0][0]: return kf[0][1:]
    if t >= kf[-1][0]: return kf[-1][1:]
    for a, b in zip(kf, kf[1:]):
        if a[0] <= t <= b[0]:
            r = (t - a[0]) / max(b[0] - a[0], 1e-6); return [a[i] + (b[i] - a[i]) * r for i in range(1, 5)]

def make_detector():
    import mediapipe as mp
    from mediapipe.tasks import python as mpt
    from mediapipe.tasks.python import vision
    L = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
        base_options=mpt.BaseOptions(model_asset_path=os.path.join(HERE, "face_landmarker.task")),
        num_faces=3, min_face_detection_confidence=0.2, min_face_presence_confidence=0.2))
    def eyes(fr, box):
        x, y, w, h = box; cx, cy = x + w / 2, y + h / 2; s = max(w, h) * 1.6
        x0, y0 = int(max(0, cx - s / 2)), int(max(0, cy - s / 2))
        x1, y1 = int(min(fr.shape[1], cx + s / 2)), int(min(fr.shape[0], cy + s / 2))
        crop = fr[y0:y1, x0:x1]
        if crop.size == 0: return None
        k = 640 / max(crop.shape[:2]); crop = cv2.resize(crop, None, fx=k, fy=k)
        for ang, code in ROT.items():
            im = crop if code is None else cv2.rotate(crop, code)
            r = L.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))))
            if not r.face_landmarks: continue
            H, W = im.shape[:2]; cand = []
            for f in r.face_landmarks:
                p = np.array([[f[i].x * W, f[i].y * H] for i in EYE])
                if ang == 90: p = np.c_[p[:, 1], W - p[:, 0]]
                elif ang == 180: p = np.c_[W - p[:, 0], H - p[:, 1]]
                elif ang == 270: p = np.c_[H - p[:, 1], p[:, 0]]
                cand.append(p / k + [x0, y0])
            return min(cand, key=lambda p: np.hypot(*(p.mean(0) - [cx, cy])))
        return None
    return eyes

def band(p):
    """pita mata berputar: (cx, cy, panjang, tinggi, sudut derajat)"""
    l, r = p[[0, 1, 2, 3, 8, 10, 12]].mean(0), p[[4, 5, 6, 7, 9, 11, 13]].mean(0)
    d = r - l; L = np.hypot(*d); ang = np.degrees(np.arctan2(d[1], d[0])); c = p.mean(0)
    return np.array([c[0], c[1], L * 2.1, L * 0.95, ang])

def main():
    a = sys.argv[1:]; gaya = "mosaik"; step = 3
    if "--gaya" in a: i = a.index("--gaya"); gaya = a[i + 1]; del a[i:i + 2]
    if "--langkah" in a: i = a.index("--langkah"); step = int(a[i + 1]); del a[i:i + 2]
    src, dst, kj = a; kf = json.load(open(kj))[0]["kf"]
    cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS) or 30; n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    W, H = int(cap.get(3)), int(cap.get(4)); eyes = make_detector()
    det = {}
    for fi in range(0, n, step):
        cap.set(cv2.CAP_PROP_POS_FRAMES, fi); ok, fr = cap.read()
        if not ok: break
        p = eyes(fr, lerp_box(kf, fi / fps))
        if p is not None: det[fi] = band(p)
    keys = sorted(det); print(f"{os.path.basename(src)}: mata terdeteksi {len(keys)}/{len(range(0, n, step))} sampel", flush=True)
    def at(fi):
        if not keys: return None
        j = np.searchsorted(keys, fi)
        a_, b_ = (keys[j - 1] if j > 0 else None), (keys[j] if j < len(keys) else None)
        lim = fps * 1.0
        if a_ is not None and b_ is not None and b_ - a_ <= lim * 2:
            r = (fi - a_) / max(b_ - a_, 1); va, vb = det[a_], det[b_]
            da = (vb[4] - va[4] + 180) % 360 - 180
            return np.r_[va[:4] + (vb[:4] - va[:4]) * r, va[4] + da * r]
        near = min([k for k in (a_, b_) if k is not None], key=lambda k: abs(k - fi))
        return det[near] if abs(near - fi) <= lim else None
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                            "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "17", "-preset", "veryfast",
                            "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", dst], stdin=subprocess.PIPE)
    fb = 0
    for fi in range(n):
        ok, fr = cap.read()
        if not ok: break
        b = at(fi); mask = np.zeros((H, W), np.uint8)
        if b is not None:
            pts = cv2.boxPoints(((b[0], b[1]), (b[2], b[3]), b[4])).astype(np.int32); cv2.fillPoly(mask, [pts], 255)
        else:
            fb += 1; x, y, w, h = [int(v) for v in lerp_box(kf, fi / fps)]; cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
        ys, xs = np.where(mask > 0)
        if len(xs):
            x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1; reg = fr[y0:y1, x0:x1]; w, h = x1 - x0, y1 - y0
            if gaya == "blur":
                k = max(31, (min(w, h) // 2) | 1); eff = cv2.GaussianBlur(reg, (k, k), 0)
            else:
                cell = max(8, min(w, h) // 4)
                eff = cv2.resize(cv2.resize(reg, (max(1, w // cell), max(1, h // cell)), interpolation=cv2.INTER_AREA), (w, h), interpolation=cv2.INTER_NEAREST)
            m = mask[y0:y1, x0:x1, None] / 255.0; fr[y0:y1, x0:x1] = (eff * m + reg * (1 - m)).astype(np.uint8)
        enc.stdin.write(fr.tobytes())
    enc.stdin.close(); enc.wait()
    print(f"{dst}: {n} frame, cadangan kotak penuh {fb} frame")

if __name__ == "__main__":
    main()
