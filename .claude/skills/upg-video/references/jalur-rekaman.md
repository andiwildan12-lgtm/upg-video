# Jalur EDIT REKAMAN

Untuk video yang sudah direkam Dir/tim (mis. dokter menjelaskan scaling ke kamera). Claude mengedit:
potongan, caption per kata, label/poin, kartu promo, logo, end card WA, dan musik latar opsional.
Perangkat diadaptasi dari skill `shortform-edit` dan sudah diuji di Claude Code (15 Nov 2026).

## 1. Terima rekaman
- **Cara kirim:**
  - File kecil: unggah langsung di chat Claude Code.
  - File besar dari HP: taruh di **Google Drive**, kirim link, lalu ambil lewat konektor Google Drive.
  - Batas ukuran unggah dan Drive belum diuji. Catat hasilnya di `catatan-pembelajaran.md` saat pertama kali dipakai.
- Simpan rekaman asli di `upg-video-projects/<slug>/sumber/`. Folder ini tidak masuk git. **File asli tidak diubah atau dihapus.**
- Tanyakan sekali saja bila belum jelas:
  1. Untuk apa: iklan Meta atau Reels organik?
  2. Siapa yang tampil? Sudah setuju dipakai untuk iklan? Kalau ada pasien: sudah ada **izin tertulis**?
  3. Ada musik? Kalau ya, file dan sumber lisensinya dari Dir.

## 2. Siapkan proyek (boleh sebelum ACC, karena hanya analisis)
```
python3 .claude/skills/upg-video/rekaman/scripts/setup_proyek.py upg-video-projects/<slug>
python3 .claude/skills/upg-video/rekaman/scripts/prep_footage.py <rekaman> upg-video-projects/<slug>
```
`prep_footage.py` mengubah rekaman ke 30 fps, lebar 1080, dan suara −14 LUFS. Ia juga membuat `work/contact.jpg` (1 frame/detik). **Lihat contact sheet itu** untuk mencatat:
- posisi wajah (supaya kartu dan teks tidak menutupi wajah),
- bagian yang goyang, gelap, atau salah ucap,
- area kosong untuk teks.

Rekaman horizontal: tanyakan ke Dir mau di-crop ke 9:16 atau diberi latar.

## 3. Transkrip (untuk caption dan potongan)
1. **ElevenLabs Scribe** lewat konektor (`creative_transcribe_audio`). Ekstrak audio dulu (`ffmpeg -i public/footage.mp4 -vn work/audio.mp3`), unggah ke flow, lalu transkrip. Hasilnya waktu per kata. Kalau antrean akun gratis penuh, tunggu, jangan diulang terus.
2. Kalau gagal: Dir atau Claude menulis transkrip manual, lalu waktunya diukur dari jeda (`silencedetect`) seperti di jalur Motion.

**Selalu koreksi ejaan:** nama dokter (tanyakan Dir), "UPG", "scaling", angka, dan harga. Transkrip otomatis sering salah di bagian ini.

## 4. Rancangan (tahap C) → ACC
Pakai `templates/rancangan-rekaman.md`. Isinya:
- **Potongan:** detik mana yang dipakai dan dibuang. Usulkan pemangkasan ucapan yang berulang, salah ucap, atau jeda panjang.
- **Hook 3 detik pertama:** potongan terkuat dipindah ke depan, bila perlu ditambah label judul.
- **Caption:** kata yang disorot, dan teks label/poin.
- **Kartu promo:** isi persis dari data terkonfirmasi, kapan muncul, dan posisinya (`top`/`center`, jangan menutupi wajah).
- **Musik:** file, sumber lisensi, dan volume. Atau "tanpa musik".
- **End card** dan **draf caption per platform** (`caption-platform.md`).
- Perkiraan durasi akhir (dihitung dari potongan + 3 dtk end card).

## 5. Produksi (setelah ACC sah)
1. Catat ACC: `python3 .claude/skills/upg-video/scripts/acc_gate.py record upg-video-projects/<slug> --version V{n} --message "<kutipan persis>"`.
2. Isi `src/timeline.js`. **Hanya file ini yang diisi.** Semua waktu caption, label, dan promo dihitung di **video hasil**, bukan di rekaman asli.
3. Musik: salin file Dir ke `public/` dan isi `MUSIC`. Buat `LISENSI-MUSIK.md` di folder proyek (sumber, jenis lisensi, tanggal).
4. Cek tampilan: `python3 .claude/skills/upg-video/rekaman/scripts/render_rekaman.py upg-video-projects/<slug> stills "1,5,10,…"`. Lihat apakah wajah tertutup, teks terpotong, atau caption telat.
5. Render final: `… render_rekaman.py upg-video-projects/<slug> final`. Hasilnya `out/<slug>-V{n}.mp4` dan verifikasi otomatis jalan. Versi lama tidak ditimpa.
6. Serahkan: video, ringkasan potongan, catatan yang perlu Dir dengar (suara, musik, ejaan), dan caption per platform.

## 6. Aturan visual rekaman
- Caption: putih tebal dengan bayangan gelap. Kata kunci diberi **kotak oranye + teks putih** (teks oranye tipis sulit dibaca di atas video).
- Kata yang ditekankan tampil minimal ±0,4 dtk.
- Area aman: teks di antara y 250–1520 dan tidak di kanan ±120 px (tombol platform).
- Logo kecil di pojok kanan atas, otomatis hilang saat kartu promo tampil.
- Kartu promo dan label jangan menutupi wajah. Cek di stills.
- Jangan mempercantik wajah atau mengubah tampilan orang (filter kulit dll.) tanpa permintaan Dir.

## 7. Batas yang perlu disampaikan ke Dir
- Claude **tidak bisa mendengar**. Kejelasan suara, keseimbangan musik dengan suara, dan salah ucap harus Dir cek.
- Suara rekaman yang berisik atau bergema hanya bisa dibantu sedikit. Sarankan rekam ulang kalau parah.
- Iklan Meta: musik populer yang berhak cipta bisa membuat iklan ditolak atau suaranya dibisukan. Pakai hanya musik berlisensi dari Dir.

## Kesiapan alat (diuji 15 Nov 2026, Claude Code cloud, rekaman uji buatan)
| Komponen | Status |
|---|---|
| Setup Remotion (npm) | ✅ ±10 dtk |
| Prep footage (fps, skala, loudness, contact sheet) | ✅ |
| Stills dan render final memakai Chromium yang sudah terpasang | ✅ 11,7 dtk video ±37 dtk render |
| Verifikasi akhir | ✅ LULUS (−15,3 LUFS, TP −5,4) |
| Transkrip ElevenLabs Scribe | ⚠️ Belum teruji (antrean gratis penuh saat dicoba) |
| Rekaman asli dari HP + unggah/Drive | ⚠️ Belum teruji |
