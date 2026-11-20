# Produksi (hanya setelah ACC sah)

## 0. Gerbang
Jalankan `python3 .claude/skills/upg-video/scripts/acc_gate.py check upg-video-projects/<slug>`.
Jika gagal, **berhenti** dan kembali ke mode peninjauan. Jangan mengisi catatan ACC sendiri agar lolos.

## 1. Struktur proyek
```
upg-video-projects/<slug>/
  rancangan-V{n}.md      # versi yang di-ACC (tidak diubah setelah ACC)
  acc.json               # catatan ACC (dibuat oleh acc_gate.py record)
  naskah-tts.txt         # naskah narasi persis dari rancangan (+ ejaan fonetis)
  sumber.md              # catatan sumber klaim medis
  audio/narasi.wav
  src/                   # salin dari templates/komposisi-contoh.html (→ index.html) + templates/render.js
  assets/                # ilustrasi & logo yang dipakai
  out/<slug>-V{n}.mp4
  out/preview/           # contact sheet / frame cek
```

## 2. Kesiapan alat (diperiksa 15 Nov 2026, sesi cloud Claude Code)
| Kebutuhan | Status | Catatan |
|---|---|---|
| Renderer animasi | ✅ Siap | Node 22, Playwright + Chromium, ffmpeg 6.1. Animasi HTML/SVG/Canvas dirender per frame lalu digabung ke MP4. Remotion bisa dipasang via npm (registry terjangkau) |
| Ekspor MP4 | ✅ Siap | ffmpeg (H.264, yuv420p, 30 fps, AAC) |
| Pemrosesan gambar | ✅ Siap | Python Pillow, numpy |
| **Suara AI (TTS)** | ✅ Siap | Konektor ElevenLabs, **paket Creator (lisensi komersial)**. Narator Denas + suara tokoh serial (lihat `serial-3d.md`). Environment **Video Editing** mengizinkan host `elevenlabsusercontent.com` |
| Animasi 3D | ✅ Siap (17 Nov 2026) | three.js r149 di Chromium headless (`--use-gl=swiftshader`), ±0,4 dtk/frame. Lihat `serial-3d.md` |
| SFX suasana | ✅ Siap | ElevenLabs node `sfx` (bukan musik) |
| Ilustrasi | ⚠️ Terbatas | Ilustrasi vektor (SVG) bisa dibuat dengan kode. Generator gambar AI tidak tersedia di sini. Canva terhubung tapi asetnya perlu diekspor manual |
| Logo | ✅ Siap | `assets/logo-upg-transparan.png` (berwarna) dan `logo-upg-putih.png` (latar gelap), dari logo resmi Drive |

### Opsi suara AI (Dir yang memutuskan, jangan berlangganan otomatis)
- **ElevenLabs:** kualitas tinggi, ada suara pria berbahasa Indonesia. Butuh akun dan biaya bulanan.
- **Google Cloud TTS / Azure Speech:** suara pria `id-ID` resmi, bayar per pemakaian (biasanya murah untuk video pendek). Butuh akun cloud dan kunci API.
- **Rekam manual:** Dir/tim merekam sendiri lalu file diunggah. Ini tidak termasuk "suara AI" dan perlu persetujuan perubahan.

Kunci API **tidak boleh** ditempel di chat, naskah, atau file skill. Simpan lewat pengaturan kredensial environment (network secret) Claude Code.

## 3. Langkah produksi
1. Baca rancangan yang di-ACC, aset, dan cek alat.
2. Buat narasi TTS dari naskah yang di-ACC, kata per kata.
3. Susun adegan (ilustrasi, karakter tanpa mata, teks, gerakan) sesuai storyboard.
4. Sesuaikan durasi adegan dengan audio nyata tanpa mengubah pesan.
5. Render pratinjau → QA → perbaiki masalah teknis → ekspor final.
6. Serahkan: MP4, folder `src/` + aset, serta naskah/storyboard final.

Perbaikan teknis (teks terpotong, sinkronisasi, volume) termasuk lingkup ACC. Perubahan pesan, klaim, narasi, arah visual, atau CTA harus dibahas ulang. Video tidak diunggah ke media sosial.

## 4. Daftar periksa sebelum penyerahan
- [ ] Naskah, hook, CTA, dan storyboard sesuai versi ACC
- [ ] Fakta medis dan data promo sudah diperiksa (lihat `sumber.md`)
- [ ] Narasi laki-laki jelas, **tanpa musik**, tanpa audio di luar ACC
- [ ] **Tidak ada mata** pada karakter atau ikon di frame mana pun
- [ ] Logo asli UPG utuh, tidak berubah bentuk, tidak tertukar dengan Ruma
- [ ] WA tepat: 089673415806 / https://wa.me/6289673415806
- [ ] Teks terbaca di ukuran HP, tidak terpotong/bertumpuk, tampil cukup lama, berada di area aman
- [ ] Sesuai skill `panduan-visual-terpadu`: kontras (teks gelap di atas oranye), area aman 250/400/120 px, hook 3 dtk, 5 dtk terakhir logo + 1 CTA sesuai funnel, cover maks 6 kata
- [ ] Konten klinis sudah direview dokter; testimoni/before-after punya izin tertulis
- [ ] Audio dan gerakan sinkron, tidak ada bagian kosong mendadak, narasi akhir tidak terpotong
- [ ] Jalankan `python3 scripts/verify_video.py out/<file>.mp4`. Wajib **LULUS**: 1080×1920, 30 fps, decode utuh, loudness −14 ±1,5 LUFS, true peak ≤ −1 dBTP
- [ ] File proyek dan aset ikut diserahkan. Versi lama tidak dihapus atau ditimpa (simpan V1, V2, …)
- [ ] Cek frame saja tidak cukup untuk menilai tempo. Tinjau pemutaran hasil. Bila tidak bisa, nyatakan batasnya
