# Jalur EDUKASI DOKTER (Gaya 1) — konten edukasi UPG dari rekaman dokter

Dibuat atas permintaan Dir (20 Nov 2026): *"jadikan skill untuk konten khusus edukasi UPG"*. Proyek pertama: `edukasi-cabut-firdha`.
Pakai jalur ini saat Dir mengirim **rekaman dokter yang berbicara ke kamera** (biasanya banyak take dari DJI Mimo/HP) dan
ingin dijadikan **Reels edukasi bergaya "Gaya 1"**. Untuk iklan promo dengan kartu harga, tetap pakai EDIT REKAMAN.

## 1. Tata bahasa visual "Gaya 1" (dari referensi Dir, folder Drive `1PvuEOaWdiV6EmG_Oc9-Xi2ms2UNIFJu0`)
| Unsur | Cara di UPG | Kapan |
|---|---|---|
| **Hook judul** | Teks putih besar berbayang di atas kepala (`titles.kind:"hook"`), pop-in | 0–5 dtk pertama; boleh juga di kalimat penutup |
| **Caption per kata** | Putih tebal di dada, 1–3 kata per grup, **kata kunci = kotak oranye** (`hl`) yang memantul | Sepanjang video, otomatis dari transkrip |
| **Stiker emoji** | Lingkaran putih + emoji, pop + mengambang, label oranye opsional | Tiap 3–6 dtk, diikat ke kata yang relevan |
| **Pill** | Kapsul putih + emoji + teks; bisa **dicoret merah** (mitos/anggapan salah) | Kontras "bukan X, tapi Y" |
| **Zoom punch-in** | Wajah digeser ke sepertiga atas dan diperbesar (`zooms`), "settle" kecil di tiap pergantian take | Kata penting, kalimat inti |
| **Kartu ilustrasi** | Latar krem berpola titik, video dokter mengecil jadi **polaroid miring** di kiri bawah (tetap bicara), isi: `chat` (bubble keluhan pasien), `checklist` (langkah bercentang), `judul` (teks besar) | 1–2 kartu per video untuk bagian yang paling "abstrak" |
| **Name tag** | **Cukup "drg. Nama"**, tanpa "UPG Dental Care" (koreksi Dir papan V1) | Awal kalimat kedua |
| **SFX padat** | pop, whoosh, ding, ketik, notifikasi pesan, swish, scratch (coret), zoom, sparkle, klik | **Otomatis** dari event (lihat §4) |
| **Backsound** | Musik ringan ceria, volume rendah di bawah suara dokter | Seluruh video (keputusan Dir: dibuat dengan ElevenLabs Music) |
| **End card** | Logo resmi UPG + 1 kalimat penutup + "Bersama drg. …" | 3 dtk |

Logo kecil di kiri atas **otomatis hilang** saat judul/pill/kartu tampil (pelajaran papan V1: logo kanan atas bertabrakan dengan judul).

## 1b. Gaya 3 (retro) — `"gaya": 3` di edit.json (proyek pertama: pov-nur-fo-hertasning, 20 Nov 2026)
Dari panel "Gaya 3" referensi yang sama. Unsur:
- Judul `kind:"retro"`: huruf slab krem (Alfa Slab One) bergaris cokelat `#5B3216`, **diketik huruf per huruf** + SFX ketik; `sub` = pill cokelat font mesin ketik (Courier Prime). Maks. ±14 huruf per baris di ukuran 86.
- Caption: kotak putih, teks gelap; kata sorot = pill cokelat.
- `notes`: coretan tangan (Caveat) + panah melengkung yang tergambar (`arrow:[x1,y1,x2,y2]`, `bend`).
- `counter`: lencana krem "label + angka + emoji" yang bertambah di tiap jangkar `hits` (+ding+sparkle). Disembunyikan saat kartu.
- Kartu checklist bergaya **jendela aplikasi** (titik merah-kuning-hijau + `window`), item lebih rapat (maks. 5 item).
- End card `komen:true` = tombol 💬 Komen.
Font OFL di `assets/` (GAYA3-FONTS-OFL-LICENSE), disalin otomatis oleh setup.

**Konten POV staf (bukan dokter):** pola sama; teks ucapan ditulis manual per potongan (`say` + `speech_from/to`) karena logat Makassar sering salah ditangkap Whisper ("weatmin"=WA admin, "kitansi"=kuitansi, "kiris"=QRIS). Wajah profil samping tidak terdeteksi Haar → ukur `fx,fy` manual dari frame bergrid (`drawgrid=w=120:h=120`).
**Privasi meja FO:** buang nominal tagihan, nama pasien, jawaban kesehatan pasien, nama dokter; formulir di meja diberi `blur:[[x,y,w,h]]` per potongan (koordinat rekaman, ikut zoom).

## 2. Keputusan Dir untuk jalur ini
- Tujuan default: **Reels organik** (tanpa harga/promo, tanpa nomor WA di end card) kecuali Dir bilang iklan.
- Nama tampil: **"drg. Firdha"** (tanpa nama lengkap) — ikuti pola ini untuk dokter lain, tanyakan namanya sekali.
- Pilih take/lokasi bebas, prioritas **"asal orang singgah nonton"**: hook terkuat di depan, take paling ekspresif.
- Backsound: **dibuat dengan ElevenLabs Music** (paket Creator aktif = hak komersial). Catat di `LISENSI-MUSIK.md` proyek.
- **Emoji stiker harus cocok dengan ekspresi dokter saat itu** (koreksi Dir: dokter tersenyum tapi stiker 😰 = janggal). Emosi pasien (takut/cemas) ditampilkan lewat judul atau kartu chat, bukan stiker di samping wajah dokter yang tersenyum.
- Aturan "tanpa mata" tidak berlaku untuk dokter asli. Stiker emoji bukan karakter ilustrasi.
- Tetap: ACC sebelum produksi, papan gambar boleh setelah naskah/keputusan oke, klaim medis aman.

## 3. Alur kerja
1. **Ambil klip dari Drive** (folder per dokter, mis. "Cabut Gigi / dr. firdha / Video Edukasi"). Daftar file dengan Drive `search_files parentId=…` (bisa 2 halaman; **folder sering berisi unggahan ganda dari 2 akun → buang duplikat berdasarkan nama file**). Unduh paralel:
   `xargs -P 6 … curl -sL -o <nomor>.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"` ke `aset-drive/<slug>/` (gitignored).
2. **Transkrip semua take** (Whisper lokal, tidak memakai kredit): ekstrak wav 16 kHz lalu `edukasi/scripts/transkrip.py`. 54 klip / 8,7 mnt ≈ 7 mnt.
3. **Pilih take terbaik per kalimat** dari transkrip: buang hitungan "tiga, dua, satu", "sorry", take terpotong. Cek gambar (frame tengah) untuk lokasi & ekspresi. Cari titik potong presisi dengan `silencedetect` (−35 dB/0,25 s, lalu −40 dB/0,08 s) atau profil loudness per 50 ms. **Awal kata pertama dari Whisper sering terlalu dini** (kata "Ada@0.0–1.6") → percayai jeda, bukan Whisper.
4. Draf di chat: hook, urutan potongan (tabel ucapan + visual + SFX), keputusan yang perlu Dir.
5. Setelah keputusan Dir: `setup_edukasi.py` → `prep_klip.py <folder-asli> <proyek> <nomor…>` → salin transkrip ke `work/transkrip.json` → posisi wajah (OpenCV Haar, `opencv-python-headless==4.10.*`; versi 5 tidak punya CascadeClassifier) → tulis `edit.json` → `build_timeline.py` → `render_edukasi.py papan "t1,…" V1` → kirim papan ke Dir.
6. "**gas render**" → catat ACC → buat backsound (ElevenLabs Music) + lengkapi SFX library bila belum ada → `build_timeline.py` → `render_edukasi.py final` (loudnorm −14 otomatis + verifikasi).

## 4. `edit.json` (satu-satunya file yang diisi per proyek)
Contoh lengkap: `edukasi/contoh-edit.json` (proyek cabut gigi drg. Firdha).
- `cuts`: `{clip, in, out, fx, fy, scale, flash}` — `fx,fy` = pusat wajah di 1080×1920 (dari deteksi wajah), `scale` ±1.42 untuk rekaman duduk berjarak (wajah lalu digeser ke y≈780 tanpa tepi hitam). `flash:false` untuk potongan yang masuk ke kartu.
- `replace`: koreksi ejaan Whisper (`"engan":"enggan"`, `"pencagutan":"pencabutan"`); nilai `""` = buang token.
- `hl`: kata yang disorot oranye.
- `titles`, `stickers`, `zooms`, `cards`, `nametag`, `end`, `music`.
- **Jangkar waktu** (jangan menghitung detik manual): `"c3:tenang"` awal kata, `"c3:tenang>"` akhir kata, `"c3:tenang#2"` kemunculan ke-2, `"c3@1.5"`, `"c3@end"`, `"end"`, plus `+0.2/-0.3`. Daftar kata per potongan ditulis ke `work/kata-per-potongan.txt`.
- **SFX otomatis** (`sfx_auto` default true): pop tiap stiker, sparkle untuk burst, swish tiap judul/pill, scratch saat coret, whoosh kartu masuk/keluar + end card, ketik + notifikasi tiap bubble, ding tiap centang, zoom tiap punch-in, klik name tag. SFX manual tambahan di `sfx: [{at, file, vol}]`.

## 5. Pustaka SFX bersama (`assets/sfx/`, disalin otomatis oleh `setup_edukasi.py`)
Nama file wajib: `pop, whoosh, swish, ding, typing, message, scratch, zoom, sparkle, click` (`.mp3`). Dibuat sekali dengan ElevenLabs SFX (`creative_generate_in_flow` node `sfx`), pendek (0,3–1,5 dtk), dipangkas sunyi depan, dinormalisasi. **Sudah tersedia (20 Nov 2026, ±190 kredit):** 10 file di `assets/sfx/`, dipangkas sunyi depan + loudnorm −16 (lihat prompt di `LISENSI-MUSIK.md` proyek edukasi-cabut-firdha). Tidak perlu dibuat ulang untuk proyek berikutnya.

**Backsound per proyek:** `creative_generate_in_flow` node `music`, model `eleven_music_v2_5`, `generations_count:1` (±1.000 kredit/80 dtk). Prompt terbukti: *"Instrumental only, no vocals. Light, warm, cheerful background music for a friendly educational social media video by a dentist. Soft plucked ukulele and gentle marimba, light finger snaps, soft bass, relaxed bouncy tempo around 100 BPM… Steady and unobtrusive so speech sits clearly on top… Duration 80 seconds, ends gently."* Normalisasi −16 LUFS → `public/backsound.mp3`, `music.volume` 0,14. Pengaturan node menampilkan "Instrumental: False" walau prompt minta instrumental → Dir cek tidak ada vokal.

## 6. Pelajaran teknis (terbukti)
- Rekaman DJI Mimo: 1080×1920 29,97 fps + stream data/thumbnail → `prep_klip.py` memetakan hanya `0:v:0` & `0:a:0`, 30 fps, loudnorm −14 per klip.
- faster-whisper di lingkungan ini: kirim audio sebagai **array numpy** (PyAV terpasang tidak menerima argumen `metadata_errors`).
- Papan gambar 10 frame ±30 dtk. Render final ±3–5 mnt untuk ±80 dtk video.
- Kartu chat: maks. 3 bubble pendek (≤45 karakter) agar tidak tertimpa polaroid.
- Durasi hasil ≈ jumlah potongan + 3 dtk end card; monolog dokter ±8–10 kalimat ≈ 80 dtk.

## 7. Daftar periksa sebelum kirim papan / final
**Audit papan (pelajaran V2→V3, diminta Dir "audit dlu papan gambarnya"):** render juga frame di momen transisi (stiker muncul, coret, centang, burst) + 1 still resolusi penuh, lalu cek:
- Efek burst/kilau **tidak boleh jatuh di wajah** → taruh di sekitar pill/judul.
- Emoji yang tampil jelek/gelap di Noto (mis. 🗣️ jadi kepala biru) → ganti (💬).
- Kutipan pasien di kartu chat = karangan → wajib label kecil **"ilustrasi"** (`note`).
- Teks kartu harus sama dengan ucapan dokter (mis. "selama pencabutan", bukan "perawatan").
- Kalimat yang sama jangan tampil 3x (judul + caption + end card): pakai `nocap:true` di judul, end card diisi ajakan komentar.
- Zoom dasar **±1,3×** (1,42× terlihat lembut di resolusi penuh).
- Wajah tidak tertutup judul/pill/stiker; stiker di kiri/kanan kepala (x≈220 / 860).
- Teks di area aman (y 250–1570, tidak di kanan ±120 px).
- Ejaan istilah & nama dokter benar; tidak ada klaim "pasti tidak sakit".
- Claude tidak bisa mendengar: Dir cek salah ucap, potongan kata, dan keseimbangan musik/SFX.
