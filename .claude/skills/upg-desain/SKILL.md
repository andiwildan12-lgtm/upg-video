---
name: upg-desain
description: Desain grafis statis UPG Dental Care — Story/Reels cover 1080×1920, Feed 1080×1350, poster, banner promo — mengikuti Pedoman Desain UPG (palet #E97818 / Warm Brown / Warm Cream, Poppins + Inter, kontras, zona aman) dan aturan klaim iklan klinik. Pakai saat Dir minta desain gambar, poster, Story, Feed, atau materi promo statis. Bukan untuk video (pakai upg-video).
---

# UPG Desain (grafis statis) — v1.1

Panggil pengguna **"Dir"**. Bahasa Indonesia jelas, tegas, ringkas. Brand: **UPG Dental Care saja** (Ruma Dental bukan bagian skill ini). **Video tidak memakai skill ini** (keputusan Dir, 16 Nov 2026).

## Wajib dibaca sebelum mulai
1. `references/pedoman-desain.md` — palet, kontras, font, logo, komposisi, zona aman.
2. `references/catatan-desain.md` — keputusan Dir, aturan klaim/benefit, pelajaran proyek, riwayat.
3. `.claude/skills/upg-video/references/catatan-pembelajaran.md` — **data promo & layanan terkonfirmasi** (harga, jam, garansi, fasilitas).
4. `.claude/skills/upg-video/references/pustaka-footage.md` — katalog **foto klinik** di Drive untuk latar.
5. Lihat `contoh/` — final yang disetujui Dir dan V1 yang ditolak (pembanding).

## Alur kerja
1. **Brief singkat.** Format (Story/Feed/keduanya), layanan/promo, data. Maks. 1–3 pertanyaan; selebihnya asumsi berlabel **[asumsi]**. Harga, periode, garansi, benefit **tidak boleh dikarang**.
2. **Strategi pesan dulu** (bila promo bersaing harga): jual **nilai**, bukan perang harga; jangan menyebut/membandingkan pesaing (etika PDGI). Lihat `catatan-desain.md`.
3. **Draf V1** langsung dibuat dari template (`templates/`). Kirim gambar + ringkasan 3–5 poin.
4. **Audit diri** dengan daftar periksa di bawah *sebelum* kirim. Kalau Dir minta "audit/nilai", jawab jujur dalam tabel *masalah → dampak*, lalu perbaiki di versi berikutnya.
5. **Revisi** → naikkan versi (V2, V3…), simpan semua versi, jangan timpa. Tampilkan bagian yang berubah saja.
6. **Benefit/klaim baru** → tanyakan fakta ke Dir (apakah dijalankan *semua* dokter/admin?). Yang belum konsisten di lapangan **tidak diiklankan**.
7. **"Sudah oke" dari Dir** → render **FINAL PNG** (Story + Feed bila keduanya dibuat), kirim, commit & push. Claude tidak mengunggah ke media sosial.
8. Catat keputusan/pelajaran baru di `references/catatan-desain.md`; data layanan di `catatan-pembelajaran.md` skill video.

## Produksi teknis
- Folder proyek: `upg-video-projects/<slug>/desain/` (atau subfolder proyek terkait).
- Salin ke folder proyek: `templates/story-promo.html` / `templates/feed-promo.html`, `assets/fonts/*.woff2` → `fonts/`, logo dari `.claude/skills/upg-video/assets/` (`logo-upg-putih.png` untuk latar gelap/oranye), dan foto latar. Foto lobi siap pakai (IMG_9163, sudah di-crop): `assets/foto/foto-9163-story.jpg` & `foto-9163-feed.jpg`.
- **Foto latar dari Drive**: unduh hanya yang dipilih ke `aset-drive/foto/` (di-.gitignore), crop + resize dengan PIL ke ukuran blok latar, simpan hasil kecil (±300 KB) di folder proyek.
- Template disusun dari elemen ber-ID (`#bg #shade #logo #q #title #sub #expl #seal #price #when #ben #cta`); ganti isi, lalu atur posisi lewat blok CSS paling bawah.
- Render:
  - Draf: `node .claude/skills/upg-desain/scripts/render_desain.js <file.html> <out.jpg> [lebar tinggi]` → JPG + `<out>-zona.jpg`.
  - Final: sama, dengan keluaran `.png`.
  - Feed: tambahkan `1080 1350`.
- **Selalu lihat hasil render** (dan versi zona) sebelum kirim; untuk detail kecil, crop area dan periksa.

## Daftar periksa sebelum kirim
**Brand & teknis**
- [ ] Warna hanya dari palet; tidak ada turquoise. Font hanya Poppins + Inter.
- [ ] Teks kecil tidak oranye; tombol CTA oranye pakai teks charcoal.
- [ ] Logo resmi satu kali, tanpa kotak, tidak menimpa/tertimpa konten.
- [ ] Story: info penting di luar 250 px atas & 340 px bawah. Tidak ada teks saling menimpa (cek segel/label vs kartu harga).
- [ ] Judul di atas foto terbaca (lapisan gelap ±70% di area judul).

**Pesan & klaim**
- [ ] Satu titik fokus; urutan baca: hook → judul → nama layanan + penjelasan awam → harga → jadwal → benefit → CTA.
- [ ] Istilah medis dijelaskan bahasa awam (mis. **SCALING → "Pembersihan Karang Gigi"**).
- [ ] Harga & jadwal sesuai data terkonfirmasi; "S&K berlaku" bila ada syarat. Harga coret hanya dari harga normal yang diberikan Dir.
- [ ] Benefit = fakta yang dijalankan semua tim, bukan basa-basi; **tanpa janji hasil** ("pasti", "dijamin", "pasti bersih", "diulang gratis", "tanpa antre", "tanpa sakit").
- [ ] Garansi ditulis netral: **"Ada garansi setelah perawatan\*"**.
- [ ] WA 089673415806 benar. Ilustrasi manusia/gigi tanpa mata.
