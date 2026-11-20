#!/usr/bin/env python3
"""Transkrip per kata semua work/*.wav dengan Whisper lokal (faster-whisper, CPU) -> work/transkrip.json.

Pemakaian: python3 transkrip.py <folder-proyek> [model]   (model default 'small'; 'medium' lebih akurat, ±3x lebih lama)
Terbukti 20 Nov 2026: 54 klip / 8,7 menit selesai ±7 menit dengan 'small'. Butuh `pip install faster-whisper`
(model diunduh dari Hugging Face sekali). Ejaan nama/istilah tetap dikoreksi lewat "replace" di edit.json.
Audio dibaca sebagai array (bukan path) karena versi PyAV di lingkungan ini bentrok dengan decode_audio.
"""
import glob, json, os, sys, wave
import numpy as np
from faster_whisper import WhisperModel

if len(sys.argv) < 2:
    sys.exit(__doc__)
P = sys.argv[1]
m = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "small", device="cpu", compute_type="int8")
path = os.path.join(P, "work", "transkrip.json")
out = json.load(open(path)) if os.path.exists(path) else {}
for f in sorted(glob.glob(os.path.join(P, "work", "*.wav"))):
    n = os.path.basename(f)[:-4]
    if n in out:
        continue
    w_ = wave.open(f)
    a = np.frombuffer(w_.readframes(w_.getnframes()), np.int16).astype(np.float32) / 32768
    segs, _ = m.transcribe(a, language="id", word_timestamps=True)
    out[n] = [{"s": round(s.start, 2), "e": round(s.end, 2), "t": s.text.strip(),
               "w": [[w.word, round(w.start, 2), round(w.end, 2)] for w in s.words]} for s in segs]
    print(n, " ".join(s["t"] for s in out[n]), flush=True)
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=1)
