"""Base video Tambal Ulang drg. Ainun: potong klip, slow zoom, blur wajah pasien & kertas, cerahkan close-up.
Keluaran: base.mp4 (1080x1920, 30 fps, tanpa audio)."""
import subprocess, numpy as np, cv2, sys
D = sys.argv[1]  # folder klip
OUT = sys.argv[2]
W, H, FPS = 1080, 1920, 30

# wajah pasien 0671: (detik sumber, cx, cy) koordinat asli 1080x1920
KF671 = [(1.5,495,1344),(2.0,555,1254),(2.5,540,1074),(3.0,525,1014),(3.5,570,954),
         (4.0,585,909),(4.5,555,909),(5.0,630,1059),(5.5,750,1179)]
def kf(t):
    ts=[k[0] for k in KF671]
    x=np.interp(t,ts,[k[1] for k in KF671]); y=np.interp(t,ts,[k[2] for k in KF671]); return x,y

def blur_ell(f, cx, cy, rx, ry):
    m = np.zeros(f.shape[:2], np.float32)
    cv2.ellipse(m, (int(cx), int(cy)), (int(rx), int(ry)), 0, 0, 360, 1.0, -1)
    m = cv2.GaussianBlur(m, (0, 0), 18)[..., None]
    b = cv2.GaussianBlur(f, (0, 0), 40)
    return (f * (1 - m) + b * m).astype(np.uint8)

def blur_box(f, x0, y0, x1, y1):
    m = np.zeros(f.shape[:2], np.float32); m[y0:y1, x0:x1] = 1
    m = cv2.GaussianBlur(m, (0, 0), 12)[..., None]
    b = cv2.GaussianBlur(f, (0, 0), 22)
    return (f * (1 - m) + b * m).astype(np.uint8)

def gamma(f, g):
    lut = np.array([((i / 255.0) ** (1 / g)) * 255 for i in range(256)], np.uint8)
    return cv2.LUT(f, lut)

def zoom(f, s, cx=540, cy=960):
    if s == 1: return f
    M = cv2.getRotationMatrix2D((cx, cy), 0, s)
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

def frames(clip, t0, dur):
    n = round(dur * FPS)
    p = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', str(t0), '-i', f'{D}/{clip}.mp4', '-frames:v', str(n),
                        '-vf', f'fps={FPS},scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
    a = np.frombuffer(p, np.uint8).reshape(-1, H, W, 3)
    if len(a) < n: a = np.concatenate([a, np.repeat(a[-1:], n - len(a), 0)])
    return a, n

# (clip, in, dur, zoom awal, zoom akhir, proses)
SEG = [('m0671', 2.0, 3.0, 1.00, 1.04, 'f671'),
       ('m0708', 0.0, 9.4, 1.00, 1.03, 'kertas'),
       ('m0709', 1.0, 7.2, 1.03, 1.00, 'kertas'),
       ('m0695', 2.0, 3.0, 1.00, 1.04, None),
       ('m0687', 1.5, 3.0, 1.04, 1.00, 'f687'),
       ('v125349', 2.0, 4.0, 1.00, 1.04, 'gelap'),
       ('v172352', 2.0, 3.6, 1.00, 1.04, 'gelap_f'),
       ('kartu', 0, 3.2, 1, 1, None),
       ('akhir', 0, 4.0, 1, 1, None)]

enc = subprocess.Popen(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
                        '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
pip, _ = frames('m0712', 6.8, 3.2)
total = 0
for clip, t0, dur, z0, z1, pr in SEG:
    if clip == 'kartu':
        n = round(dur * FPS)
        for i in range(n):
            f = np.full((H, W, 3), 255, np.uint8)
            src = pip[min(i, len(pip) - 1)][460:1260, 240:840]  # wajah dokter 600x800
            src = cv2.resize(src, (300, 400), interpolation=cv2.INTER_AREA)
            x0, y0 = W - 90 - 300, 1060
            m = np.zeros((400, 300), np.uint8); cv2.rectangle(m, (0, 0), (299, 399), 255, -1)
            # sudut membulat
            r = 22; m[:r, :r] = 0; m[:r, -r:] = 0; m[-r:, :r] = 0; m[-r:, -r:] = 0
            for cx, cy in [(r, r), (299 - r, r), (r, 399 - r), (299 - r, 399 - r)]: cv2.circle(m, (cx, cy), r, 255, -1)
            reg = f[y0:y0 + 400, x0:x0 + 300]; reg[m > 0] = src[m > 0]
            enc.stdin.write(f.tobytes())
        total += n; continue
    if clip == 'akhir':
        n = round(dur * FPS); f = np.full((H, W, 3), (246, 248, 232), np.uint8)  # Mint White (BGR)
        for i in range(n): enc.stdin.write(f.tobytes())
        total += n; continue
    a, n = frames(clip, t0, dur)
    for i in range(n):
        f = a[i].copy(); t = t0 + i / FPS
        if pr == 'f671':
            cx, cy = kf(t); f = blur_ell(f, cx, cy, 230, 220)
        elif pr == 'f687':
            f = blur_ell(f, 440, 1010, 320, 280)
        elif pr == 'kertas':
            f = blur_box(f, 40, 1420, 1080, 1730)
        elif pr == 'gelap':
            f = gamma(f, 1.35)
        elif pr == 'gelap_f':  # mata/hidung pasien terlihat setelah dicerahkan -> blur
            f = blur_ell(gamma(f, 1.35), 190, 1090, 240, 200)
        f = zoom(f, z0 + (z1 - z0) * i / max(1, n - 1))
        enc.stdin.write(f.tobytes())
    total += n
    print(clip, n, flush=True)
enc.stdin.close(); enc.wait(); print('frames', total, total / FPS)
