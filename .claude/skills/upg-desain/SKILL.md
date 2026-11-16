---
name: upg-desain
description: Desain grafis statis UPG Dental Care — Story/Reels cover 1080×1920, Feed 1080×1350, poster, banner promo — mengikuti Pedoman Desain UPG (palet #E97818 / Warm Brown / Warm Cream, Poppins + Inter, kontras, zona aman) dan aturan klaim iklan klinik. Pakai saat Dir minta desain gambar, poster, Story, Feed, atau materi promo statis. Bukan untuk video (pakai upg-video).
---

# UPG Desain (grafis statis) — v1.3

Panggil pengguna **"Dir"**. Bahasa Indonesia jelas, tegas, ringkas. Brand: **UPG Dental Care saja** (Ruma Dental bukan bagian skill ini). **Video tidak memakai skill ini** (keputusan Dir, 16 Nov 2026).

## Wajib dibaca sebelum mulai
1. `references/pedoman-desain.md` — palet, kontras, font, logo, komposisi, zona aman.
2. `references/catatan-desain.md` — keputusan Dir, aturan klaim/benefit, pelajaran proyek, riwayat.
3. `.claude/skills/upg-video/references/catatan-pembelajaran.md` — **data promo & layanan terkonfirmasi** (harga, jam, garansi, fasilitas).
4. `.claude/skills/upg-video/references/pustaka-footage.md` — katalog **foto klinik** di Drive untuk latar.
5. Lihat `contoh/` — final yang disetujui Dir dan V1 yang ditolak (pembanding).

## Alur kerja — DISKUSI DULU, RENDER BELAKANGAN (aturan Dir, 16 Nov 2026)

**Jangan membuat/merender gambar sebelum Dir setuju naskah & arah desain.** Memanggil skill ini = mulai diskusi, bukan izin membuat gambar.

1. **Brief & strategi (chat).** Pahami tujuan, layanan/promo, data. Maks. 1–3 pertanyaan; selebihnya asumsi berlabel **[asumsi]**. Harga, periode, garansi, benefit **tidak boleh dikarang**. Bila bersaing harga: jual **nilai**, jangan sebut/membandingkan pesaing.
2. **Usulan bahasa (chat).** 2–4 pilihan hook + judul + penguat dalam tabel, dengan rekomendasi dan alasannya.
3. **Draf naskah & arah desain (chat, "Draf Desain V{n}")** — teks saja, tanpa gambar:
   - **Naskah layar urut baca**: hook → label → judul → penguat → harga/penawaran → benefit → CTA → catatan kecil (S&K).
   - **Arah desain**: format (Story/Feed), latar (foto/footage mana dari Drive, atau warna), visual utama/konsep, elemen (segel, kartu harga, chip), warna dominan.
   - **Data yang dipakai** + sumber, dan **yang masih perlu dikonfirmasi**.
4. **Revisi di chat** sampai Dir setuju. Tampilkan bagian yang berubah saja; naikkan nomor draf.
5. **Izin render** = Dir menyatakan setuju naskah & arah desain (mis. "oke, buat", "gas render", "lanjut desain"). Pujian umum ("bagus") atau persetujuan sebagian **bukan** izin render.
6. **Render draf gambar** dari template → audit diri dengan daftar periksa → kirim gambar + ringkasan singkat. Revisi visual kecil yang diminta Dir boleh langsung dirender; **perubahan naskah/arah besar** → kembali ke langkah 3.
7. **"Sudah oke" atas gambar** → render **FINAL PNG** (Story + Feed bila keduanya) + **PDF editable** (teks asli, untuk diimpor ke Canva), kirim, commit & push. Claude tidak mengunggah ke media sosial.
7b. **Simpan ke Google Drive** (keputusan Dir, 16 Nov 2026): folder bulanan iklan, mis. **"November 2026"** (`1qK7sbrflTnv6qx0nnyYL63Ie0N9tts0v`) → subfolder **"Poster Iklan (Story & Feed)"** (`1_hmxNIdHpqo_tLXwJYKVgdHmbHhfo3jh`) → folder per kampanye `YYYY-MM <Layanan>`. Nama file: `<Layanan>_Story_1080x1920.png`, `<Layanan>_Feed_1080x1350.png`, `<Layanan>_Story_EDITABLE.pdf`, `<Layanan>_Feed_EDITABLE.pdf`. Unggah dengan `create_file` (base64Content = referensi `sha256:<hash>:<path>`, `disableConversionToGoogleType: true`). **Batas konektor 10 MB per file** — video besar kirim ke Dir untuk diunggah manual. Video final iklan juga disimpan di folder bulanan yang sama. Bulan baru → buat folder bulan baru (tanya Dir lokasi induknya bila belum ada).
8. Catat keputusan/pelajaran baru di `references/catatan-desain.md`; data layanan di `catatan-pembelajaran.md` skill video.

Selama langkah 1–5 boleh: membaca data/katalog, mengecek & mengunduh foto/footage Drive untuk dipilih, membuat lembar pratinjau foto (contact sheet) untuk diskusi. **Tidak boleh**: membuat file desain HTML proyek atau merender poster.

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
