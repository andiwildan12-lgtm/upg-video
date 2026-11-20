# Indeks skrip produksi

| File | Fungsi |
|---|---|
| `gusi.html` (+ `gusi_cfg.json`) | **Geraham realistis** (`sculpt()`), plak/karang mengikuti kontur (clipping), sisa makanan, kuman, mineral, teko kerak, sikat miring, benang, scaling, kalender, panel CTA |
| `sakit.html` (+ `sakit_cfg.json`) | Penampang gigi 4 tahap (lubang → saraf radang → mati → nanah/gusi bengkak), jari bercincin, panel tanda bahaya, panel CTA |
| `gua.html`, `domino.html`, `arch3.html` (+ `*_cfg.json`) | Template scene 3D satu halaman (#02, #03, #01). Kamera = array `shots`; subtitle via `kinetic.js` |
| `kinetic.js` | Subtitle/teks kinetik per kata (`kineticSub`) |
| `render_frames.js` + `blend_blur.py` | Render frame deterministik (all / range / probe) + motion blur dari `cfg.blur` |
| `gaps.py` | Cadangan deteksi jeda narasi (kalau Scribe tidak tersedia) |
| `mix_gua.py`, `mix_domino.py` | Contoh mix: narasi + suara latar + daftar event SFX → `track.wav` |
| `qc.sh` | Cek kualitas file MP4 jadi (wajib LULUS) |
| `cover.html` + `cover_make.js` | Sampul seragam @dalamgigi dari frame bersih scene |
| `scene.html`, `extra.js`, `smile.js`, `render2.js`, `compose.py` | Pipeline iklan Ruma (bleaching v2): segmen 3D + footage + wipe atap + kartu harga |
| `arch.html`, `render3.js`, `render4.js`, `render_gua.js`, `clean.js`, `cover.js` | Versi lama (#01 v1/v3, #02); simpan sebagai arsip/acuan |
| `sfx/` | Pustaka SFX (lihat SKILL.md bagian 7a) |

Alur cepat konten 3D:
```bash
npm i three@0.160.0 && cp <skill-brand>/assets/* . && cp <scripts>/{kinetic.js,cover.html} . && python3 -m http.server 8765 &
node render_frames.js scene.html cfg.json p 1 5 10      # probe
node render_frames.js scene.html cfg.json all           # render penuh (latar)
python3 mix.py                                          # track.wav
ffmpeg -framerate 30 -i frames/%04d.jpg -i track.wav -map 0:v -map 1:a -frames:v <dur*30> -t <dur> -r 30 -c:v libx264 -pix_fmt yuv420p -crf 19 -c:a aac -b:a 160k -movflags +faststart out.mp4
bash qc.sh out.mp4 <dur> <detik_kartu>
node cover_make.js scene.html cfg.json <detik> "Baris satu" "BARIS DUA?" cover.png
```


## Tambahan 18 Nov 2026
- `stt.py` — transkripsi lokal faster-whisper (waktu per kata).
- `bicara/` — video orang bicara: `blurlogo.py`, `ov2.html`, `shot_states*.js`, `mkseq.py`, `build2.py`, `build_var.py`, `mux.py`, font Montserrat.
- `kinetik/` — iklan caption kinetik + stiker: `kin.html`, `mkstates.py`, `shotu.js`, `build_k.py`, `plan.json` (contoh behel), `filmdet.py` (blur label rontgen), `filmblur.py`.
- `kp.js`, `compose_kp*.py` — iklan Kunjungan Pertama (3D meja/HP + footage).
- `poster/` — poster foto lama (Outfit); untuk desain baru pakai skill `desain-grafis-ruma`.
- `sfx/sfx_notif.mp3` — ting notifikasi HP.
