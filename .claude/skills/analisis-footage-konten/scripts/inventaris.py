#!/usr/bin/env python3
"""Inventaris footage mentah -> bahan analisis konten (skill analisis-footage-konten).

Pemakaian: python3 inventaris.py <folder-footage> [--tanpa-suara] [--model medium]
Hasil di <folder-footage>/inventaris/:
  inventaris.md / .json : per klip: jam rekam, durasi, orientasi, kelas terang (NORMAL/GELAP/SANGAT_GELAP),
                          ucapan yang LOLOS saringan (+ tanda "ragu"), urut jam rekam
  lembar/<klip>.jpg     : 6 frame per klip;  lembar-NN.jpg : 10 klip per lembar untuk dilihat sekaligus
Ucapan dicek dengan faster-whisper (default medium) + VAD; segmen no_speech > 0,6 dan kalimat halusinasi umum
("terima kasih kerana/telah menonton", teks prompt, dsb.) DIBUANG. Ucapan pendek tetap harus dicek ulang sebelum dipakai
(pelajaran 23 Nov 2026: "Oke, manis" ternyata "Scaler…").
"""
import datetime, json, os, re, subprocess, sys, wave
from pathlib import Path

EXT = {".mp4", ".mov", ".m4v"}
HALU = re.compile(r"terima kasih (kerana|karena|telah|sudah|banyak)? ?(menonton|nonton)|thank(s| you) for watching|subscribe|"
                  r"percakapan dokter|sampai jumpa di video|selamat tinggal", re.I)

def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    suara = "--tanpa-suara" not in a
    model = a[a.index("--model") + 1] if "--model" in a else "medium"
    src = Path(a[0]).resolve(); out = src / "inventaris"; (out / "lembar").mkdir(parents=True, exist_ok=True); (out / "wav").mkdir(exist_ok=True)
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "produksi-video-klinik" / "scripts" / "warna"))
    import koreksi_warna
    W = None
    if suara:
        import numpy as np
        from faster_whisper import WhisperModel
        W = WhisperModel(model, device="cpu", compute_type="int8")
    rows = []
    for f in sorted(p for p in src.iterdir() if p.suffix.lower() in EXT):
        n = f.stem
        info = json.loads(sh("ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(f)))
        fmt = info["format"]; tags = fmt.get("tags", {})
        raw = tags.get("com.apple.quicktime.creationdate") or tags.get("creation_time", "")
        try:   # samakan ke jam lokal WITA (+08:00): DJI menulis UTC "Z", iPhone menulis jam lokal + zona
            jam = datetime.datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
        except ValueError:
            jam = raw
        v = next(s for s in info["streams"] if s["codec_type"] == "video")
        rot = next((int(sd.get("rotation", 0)) for sd in v.get("side_data_list", []) if "rotation" in sd), 0)
        w, h = (v["height"], v["width"]) if abs(rot) == 90 else (v["width"], v["height"])
        dur = float(fmt["duration"]); st = koreksi_warna.ukur(str(f))
        lb = out / "lembar" / f"{n}.jpg"
        if not lb.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(f), "-vf", f"fps={6 / max(dur, 0.5):.4f},scale=-2:220,tile=6x1",
                            "-frames:v", "1", str(lb)])
        ucap = []
        if W:
            wv = out / "wav" / f"{n}.wav"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(f), "-vn", "-ac", "1", "-ar", "16000", str(wv)])
            r = wave.open(str(wv)); x = np.frombuffer(r.readframes(r.getnframes()), np.int16).astype(np.float32) / 32768
            segs, _ = W.transcribe(x, language="id", vad_filter=True)
            for s in segs:
                t = s.text.strip()
                if s.no_speech_prob > 0.6 or HALU.search(t) or len(t) < 2: continue
                ucap.append({"dari": round(s.start, 1), "sampai": round(s.end, 1), "teks": t, "ragu": s.avg_logprob < -0.8 or len(t.split()) <= 2})
        rows.append({"klip": f.name, "jam": jam, "durasi": round(dur, 1), "orientasi": "tegak" if h > w else "mendatar",
                     "kelas": st["kelas"], "terang": st["YAVG"], "ucapan": ucap})
        print(n, st["kelas"], len(ucap), "ucapan", flush=True)
    rows.sort(key=lambda r: r["jam"])
    json.dump(rows, open(out / "inventaris.json", "w"), ensure_ascii=False, indent=1)
    L = ["# Inventaris footage", "", f"Total {len(rows)} klip, {sum(r['durasi'] for r in rows) / 60:.1f} menit. "
         f"GELAP/SANGAT_GELAP: {sum(r['kelas'] != 'NORMAL' for r in rows)}. Klip berucapan: {sum(bool(r['ucapan']) for r in rows)}.", "",
         "| Jam | Klip | Dtk | Orientasi | Terang | Ucapan (lolos saringan; ⚠ = ragu, cek ulang) |", "|---|---|---|---|---|---|"]
    for r in rows:
        u = " · ".join(f"{'⚠ ' if x['ragu'] else ''}{x['dari']}–{x['sampai']} \"{x['teks']}\"" for x in r["ucapan"]) or "-"
        L.append(f"| {r['jam'][11:19]} | {r['klip']} | {r['durasi']} | {r['orientasi']} | {r['kelas']} ({r['terang']}) | {u} |")
    (out / "inventaris.md").write_text("\n".join(L) + "\n")
    # lembar gabungan 10 klip
    from PIL import Image, ImageDraw
    for k in range(0, len(rows), 10):
        ims = []
        for r in rows[k:k + 10]:
            im = Image.open(out / "lembar" / f"{Path(r['klip']).stem}.jpg"); im = im.resize((1500, int(im.height * 1500 / im.width)))
            c = Image.new("RGB", (1500, im.height + 28), "white"); c.paste(im, (0, 28))
            ImageDraw.Draw(c).text((6, 6), f"{r['jam'][11:19]}  {r['klip'][:40]}  {r['durasi']}s  {r['kelas']}", fill="black"); ims.append(c)
        g = Image.new("RGB", (1500, sum(i.height for i in ims)), "white"); y = 0
        for i in ims: g.paste(i, (0, y)); y += i.height
        g.save(out / f"lembar-{k // 10 + 1:02d}.jpg", quality=80)
    print("->", out / "inventaris.md")

if __name__ == "__main__":
    main()
