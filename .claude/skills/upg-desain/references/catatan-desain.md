# Catatan Desain UPG — keputusan Dir & pelajaran

**Versi skill: 1.3 (16 Nov 2026).** Naikkan versi setiap pembaruan, isi riwayat di bawah.

Hanya catat keputusan yang **disetujui Dir** atau pelajaran yang **terbukti** di proyek, beserta sumbernya.

## Keputusan Dir

| Topik | Keputusan | Sumber |
|---|---|---|
| **Alur kerja** | **Diskusi dulu: naskah layar + arah desain disetujui Dir di chat, baru render.** Jangan langsung membuat gambar | Dir, 16 Nov 2026 (proyek behel) |
| Penyimpanan final | **Google Drive, folder bulanan iklan** (November 2026 → "Poster Iklan (Story & Feed)" → per kampanye), PNG + PDF editable. Video iklan final di folder bulanan yang sama | Dir, 16 Nov 2026 |
| Canva | Unggah lewat konektor berhasil, tapi **konversi otomatis PDF → desain editable gagal** (2× internal_error). Impor ke Canva: tim seret PDF EDITABLE ke Canva (Uploads) — teks bisa diedit. Edit oleh Claude di Canva bisa, tapi ±2–4× lebih boros token; file sumber utama tetap HTML di repo. Folder Canva "UPG Desain Iklan" (`FAHbHXwOnJs`). Host `www.canva.com` sudah diizinkan di environment | Uji 16 Nov 2026 |
| Ruang lingkup pedoman | Pedoman desain (palet `#E97818`, Poppins + Inter) **khusus desain gambar**. Video tetap gaya `upg-video` | Dir, 16 Nov 2026 |
| Latar | **Foto klinik asli dari Drive** (contoh: lobi IMG_9163) lebih disukai daripada latar oranye polos | Story Scaling V6 |
| Benefit receh | "Dikerjakan dokter gigi" / "alat khusus" saja dianggap receh. **Tapi** saat bersaing dengan klinik lebih murah, "alat steril + dikerjakan dokter gigi" menjadi pembeda kepercayaan dan dipakai | Story Scaling V5–V7 |
| Klaim ditolak | "Biaya dijelaskan di awal", "tanpa antre lama", "durasi XX menit" (beda tiap dokter) — **jangan dipakai** | Dir, 16 Nov 2026 |
| Garansi | Tulis **"Ada garansi setelah perawatan\*"**. **Dilarang**: "garansi bersih", "pasti bersih", "dibersihkan ulang gratis" — berisiko komplain | Dir, 16 Nov 2026 |
| Layanan yang tidak konsisten | Jangan iklankan layanan yang belum dilakukan semua dokter (mis. "cek seluruh gigi") sampai jadi SOP | Dir, 16 Nov 2026 |
| Penjelasan istilah | Nama layanan medis diberi penjelasan awam: **SCALING + "Pembersihan Karang Gigi"** | Dir, 16 Nov 2026 |
| Fasilitas | "Sambil menunggu, gratis: snack…" sebagai baris tersendiri dihapus; fasilitas cukup tampil lewat foto | Dir, 16 Nov 2026 |
| Harga coret | Boleh menampilkan kisaran harga normal sebagai harga coret ("Harga normal ~~Rp250–350 rb~~") | Story Scaling V5–V9 (disetujui di final) |

## Pelajaran desain (terbukti)

1. **V1 ditolak** (lihat `contoh/story-scaling-V1-DITOLAK.jpg`): 3 kotak seukuran tersusun seperti formulir, foto dinding cokelat memakan 35% layar, logo dobel, latar krem pucat, tidak ada rasa "Happy Hour". Pelajaran: **satu titik fokus, visual yang menjelaskan promo, energi warna**.
2. **Visual konsep > dekorasi**: jam dengan irisan 10.00–14.00 langsung menjelaskan "Happy Hour" tanpa dibaca.
3. **Harga**: angka terbesar kedua setelah judul, dalam kartu putih miring sedikit + tag "CUMA" charcoal.
4. **Foto latar**: lapisan gradasi gelap (`rgba(40,22,8,.78)` → `.66` sampai ±45–55% tinggi) lalu pudar ke Warm Cream. Foto terlihat lebih terang di pratinjau daripada aslinya — cek piksel kalau ragu.
5. **Segel/stempel lingkaran** efektif untuk satu benefit utama (mis. garansi), tapi cek tabrakan dengan label harga.
6. Elemen ber-ID dengan CSS override di bawah memudahkan revisi cepat; hati-hati aturan umum yang ikut mengenai elemen baru (mis. `#when svg{44px}` mengecilkan ikon jam).
7. **Gestur tangan ilustrasi**: jangan jari tunggal terangkat (bisa disalahartikan); pakai telapak terbuka/melambai. Warna baju karakter ikut palet desain (bukan kuning video), dan kontraskan dengan latar kartu.
8. Render ulang di URL `#guide` perlu `about:blank` dulu agar overlay zona muncul (sudah ditangani `render_desain.js`).

## Strategi saat pesaing lebih murah (disetujui arah, 16 Nov 2026)
- Jangan perang harga: turun X% butuh tambahan pasien X ÷ (100 − X) hanya untuk omzet sama (turun 25% → +33% pasien), dan untung tetap turun.
- Jual **nilai**: garansi setelah perawatan, alat steril, dikerjakan dokter gigi, klinik nyaman (foto).
- Tidak menyebut atau membandingkan pesaing di iklan.

## Riwayat proyek

| Proyek | Hasil final | Catatan |
|---|---|---|
| Tambal gigi — Story & Feed A + B (16 Nov 2026) | **FINAL** `upg-video-projects/tambal-keluarga/desain/upg-{story,feed}-tambal-{A,B}-FINAL.png` (disetujui Dir) | A: "jangan ditunda", 3 tahap lubang, latar sinar pengeras 3262. B: "Tambal Gigi Sekeluarga", ilustrasi ibu+anak (tanpa mata, label Ilustrasi), latar lobi. Harga mulai Rp250 rb-an + "harga tergantung kondisi gigi" |
| Behel cicilan — Story & Feed (16 Nov 2026) | **FINAL** `upg-video-projects/behel-cicilan/desain/upg-{story,feed}-behel-FINAL.png` (V3, disetujui Dir) | Judul utama **PASANG BEHEL** (bukan "bisa dicicil"), label BISA DICICIL, "Cukup DP 50%, sisanya cicil 2×", **mulai Rp3 jt/rahang**, segel 3 pilihan, latar close-up behel 3493. Skema cicilan rinci dihapus atas permintaan Dir |
| Happy Hour Scaling — Story & Feed (16 Nov 2026) | `upg-video-projects/happy-hour-scaling/story/upg-story-scaling-FINAL.png` (Story V9) + `upg-feed-scaling-FINAL.png` (Feed V7) | V1→V9: audit, konsep jam, pedoman, latar foto lobi, harga coret, benefit nilai, garansi netral, penjelasan istilah |

## Riwayat versi skill

| Versi | Tanggal | Perubahan |
|---|---|---|
| 1.0 | 16 Nov 2026 | Skill dibuat: pedoman desain terkoreksi, template Story, render script |
| 1.1 | 16 Nov 2026 | Template Story + Feed final (latar foto, segel, harga coret, penjelasan istilah); render PNG final; aturan klaim/benefit/garansi; strategi vs pesaing murah; contoh final & V1 ditolak; katalog foto Drive |
| 1.2 | 16 Nov 2026 | **Aturan Dir: diskusi naskah & arah desain dulu, render setelah disetujui** |
| 1.3 | 16 Nov 2026 | Penyimpanan final ke Google Drive (folder bulanan) + PDF editable; hasil uji Canva |
