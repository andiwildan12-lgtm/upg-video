---
name: upg-antang-video
description: Identitas dan data resmi KHUSUS cabang UPG Dental Care ANTANG (Lt. 2 Apotek Wahdah Antang, Makassar) untuk iklan video: alamat, WA, harga, footage Antang, naskah. Gunakan setiap kali konten untuk UPG Antang, bersama skill produksi-video-klinik. Jangan tertukar dengan UPG Hertasning (skill upg-hertasning-video) atau Ruma Dental (skill ruma-dental-video).
---

# Pedoman Video UPG Dental Care ANTANG

## 0. Pemisahan Cabang [WAJIB]
UPG Antang, UPG Hertasning, dan Ruma Dental adalah **tiga identitas terpisah**. Satu video = satu cabang.

| | **UPG Antang** (skill ini) | UPG Hertasning | Ruma Dental |
|---|---|---|---|
| Skill | `upg-antang-video` | `upg-hertasning-video` | `ruma-dental-video` |
| Alamat | Lt. 2 Apotek Wahdah Antang | Jl. Letjen Hertasning No.50 | (lihat skill Ruma) |
| WA | **0895-1013-2102** | 0896-7341-5806 | (lihat skill Ruma) |
| Nama di iklan | UPG Dental Care **Antang** | UPG Dental Care **Hertasning** | Klinik Gigi Ruma Dental |
| Logo | Logo UPG (sama) + label ANTANG | Logo UPG | Logo Ruma |
| Footage | Hanya folder milik upgdentalcareantang | Hanya folder Hertasning | Hanya folder Ruma |
| Ciri interior | Panel kayu, rak lampu kuning (ruang konsultasi), kursi unit biru navy, gorden abu | (cek di skill Hertasning) | Dinding sage + garis daun |

Aturan:
- Jangan pakai footage, WA, alamat, atau isi paket Hertasning di iklan Antang, dan sebaliknya. Harga boleh sama **hanya bila Pak Dir menyatakan sama**.
- Iklan Hertasning boleh dijadikan **acuan gaya**, bukan sumber footage/data.
- Sebelum render: cek kartu penutup menyebut **Antang** + WA Antang; cek tidak ada papan/atribut cabang lain.

Versi 0.1 (18 Nov 2026). Status: [USULAN] kecuali ditandai lain.

## 1. Data resmi cabang Antang [DISEPAKATI]
- Nama di iklan: **UPG Dental Care Antang**
- Alamat: **Lantai 2 Apotek Wahdah Antang**, Makassar
- WA admin: **0895-1013-2102**
- Jam buka: **setiap hari 10.00–22.00 WITA**
- Dokter: drg umum → di iklan tulis **"dokter gigi"** (jangan "spesialis"/"ortodontis").

## 1a. Logo & warna [DISEPAKATI 18 Nov 2026]
- **Logo UPG Antang = sama dengan Hertasning** (gigi garis + "UPG Dental Care"). File: `assets/logo_upg_putih.png` (putih transparan, untuk latar gelap), `assets/logo_upg_oranye.png`. Diekstrak dari Behel_Story Hertasning (resolusi sedang; minta file vektor bila perlu cetak besar).
- **Pembeda cabang di video**: label **ANTANG** di bawah logo + WA & alamat Antang. Jangan pakai frame story Hertasning (ada alamat Jl. Letjen Hertasning No.50).
- Warna UPG: oranye `#E8771E`, gelap `#262626`, krem `#F7EEE3`, putih.

## 1b. Suara narator Antang [DISEPAKATI 18 Nov 2026]
- **Tio – Persuasive & Convincing** (voice_id `5U7QzveIXT8fIoBXaoUC`), model eleven_v4. Ciri khas Antang: lugas, energik, meyakinkan (beda dari Ricky/Ruma yang lembut).
- Pengucapan **UPG = "U-Pe-Ge"** (huruf Indonesia). Di teks narasi tulis fonetik `U-Pe-Ge`, jangan "UPG" (dibaca salah). Versi final A/B menunggu pilihan Pak Dir.
- Kandidat ditolak: Macazzart (logat Makassar), Zulsyifah (wanita).
- Catatan: cek supaya tidak sama dengan suara iklan Hertasning.

## 2. Harga behel (Pak Dir: sama dengan Hertasning) [DISEPAKATI]
- Mulai **Rp3 juta per rahang** (metal), **DP 50%, sisanya cicil 2x**.
- 3 pilihan: metal, keramik, self-ligating.
- Isi paket **Antang**: sudah termasuk **konsultasi, cetak gigi, scaling**.
- **Jangan bahas rontgen** di iklan (arahan Pak Dir 18 Nov 2026).
- Kontrol Rp200–350 rb: tidak ditulis di iklan, dijelaskan admin.
- Rating Google Maps: tidak dipakai di iklan.

## 3. Aturan khusus
- Desain feed Hertasning memuat "Alat steril" → **jangan dipakai di video** (klaim terlarang, lihat produksi-video-klinik bagian 3).

## 4. Footage Antang
Induk: Drive folder `1H4xtXSoBlPJ-F_4rzD5sXLGH4qGDQSqR` (Footage UPG Antang - Agustus): subfolder Tambal Gigi, PSA, Behel/Ortho (`1YyzB4rOVtB5nlQZvjhsKvvttdpMLf_-H`, 24 klip .MOV).
Konektor Drive hanya bisa mengunduh file < 10 MB. Klip > 10 MB perlu dikompres/diunggah ulang.

| Klip | Isi | Catatan |
|---|---|---|
| 4738–4740 | Dokter (jas hitam) menjelaskan foto panoramik ke pasien, ruang konsultasi panel kayu + rak lampu kuning | 4740 detik ±4,9 (foto sudah diturunkan) dipakai; rontgen jangan disebut |
| 4741 | Pasien (blazer putih) duduk di meja konsultasi, tangan dokter menjelaskan | **Pakai** (ketukan "itu saya") |
| 4743 | Tangan bersarung memegang model cetakan gigi | **Pakai** (cetak gigi) |
| 4752 / 4756 | Dokter + asisten di kursi unit, pasien rebah | Cadangan |
| 4754 | Close-up dokter bermasker bekerja | Cadangan |
| 9263 / 9274 | Staf berlanyard UPG bicara ke kamera | Cek audio; kandidat konten lain |

### Folder "Footage Konten UPG Antang" (Jul 2026, `1fb1aTkFMUy-TZ0MbekcMWZVO4cwJbtyW`) — dicek 18 Nov 2026
Subfolder: Behel/Ortho (`1_Rjzxz8MfZtX-53ldrGA35gWVXzwCFl6`, 21 klip), Suasana Klinik (8), Scalling, Tambal Gigi, Bleaching, + folder Agustus di atas.
Satu pasien behel yang sama (jilbab mauve). Seragam UPG = jas hitam logo oranye.

| Klip | Isi | Status |
|---|---|---|
| 3726 | Baki alat ortho + model cetakan | Pakai; **nama pasien tertulis di model → crop/blur** |
| 3735 / 3737 / 3738 / 3739 | Dokter + asisten memasang behel, pasien pegang cermin | **Pakai** (dikerjakan dokter gigi) |
| 3740 / 3741 | Dokter berdiri pakai alat, cek gigi | Pakai |
| 3742 | Model cetakan dipegang di samping pasien | Pakai (cetak gigi), 1,1 dtk |
| 3744 | Pasien **tersenyum lihat behel di cermin** | **Pakai** (ketukan hasil) |
| 3745 | Close-up senyum pasien dengan bracket | Pakai singkat (hindari close-up klinis lama) |
| 3746 | Dokter memasang kawat, logo UPG di jas jelas | **Pakai** |
| 3517 | Pintu "This clinic is OPEN" → resepsionis menyapa | **Pakai** (penutup/sambutan) |
| 3525 | Ruang perawatan luas, dental unit | Pakai (bukti ruang) |
Belum ada: tangga lt. 2.

### Folder "Footage antang" (milik Pak Dir, `1Rdnyvy44TSXJeT_jtVwxoz3_tfShUMh5`, 18 Nov 2026)
- 2 klip MP4 (±12 dtk): **tampak depan Apotek Wahdah Antang** sore hari (papan nama jelas di detik ±1 dan ±11). Resolusi rendah 464×832 → pakai singkat.

### Folder Scalling Antang (`1A3M2bbN9dKU5uoT1_n1IsRSgbUd0yeU0`, 25 klip)
| Klip | Isi |
|---|---|
| 3690 | Dokter + asisten scaling, scaler & suction jelas (9:16 bagus) |
| 3703 | Close-up scaler bekerja |
| 3707 | Dokter bermasker menjelaskan di meja konsultasi ("dicek dulu") |
| 3693 / 3696 / 3697 / 3700 / 3701 / 3704 / 3706 | Variasi sudut scaling, pasien jilbab krem |

## 4b. Produksi behel v1 (18 Nov 2026) — status: **ACC Pak Dir** (pelafalan OK, klip rontgen dibiarkan, siap tayang)
- Skrip render di `scripts/`: `upg.html` (3D senyum berjejal, sela+karang, rapi + overlay teks UPG + kartu), `jobs.py` (timeline per adegan dari jeda suara), `render.js` (Playwright, port 8766), `compose.py` (crossfade 5 frame, potongan cepat tanpa crossfade), `mix.py` (narasi -16 LUFS + ambience + SFX), `cover.html/js`.
- Narasi dipakai: versi B (jeda paling rapi), `scripts/narasi-behel-antang-v1.mp3`.
- Pelajaran audit: adegan sela pakai zoom ke senyum yang sama (bukan gigi kapsul besar); klip konsultasi 4740 diambil setelah foto rontgen diturunkan; teks "Self‑ligating" pakai tanda hubung tak-putus; 3517 di-crop agar papan Pepsodent tidak tampil; blur nama pasien di 3726 (kotak 500x620 @ 410,1000).
- Kredit ElevenLabs: tes suara ±1.250 + narasi 2 versi ±1.850 + transkrip ±310 = ±3.400.

## 4c. Poster [DISUKAI Pak Dir 18 Nov 2026]
- Konsep poster behel Antang disukai → jadikan acuan poster layanan Antang lain.
- Template: `scripts/poster/poster.html` + `shot.js` (Story 1080x1920 & Feed 1080x1350 dari satu HTML, variabel CSS per ukuran).
- Rumus: foto asli Antang di atas (gradasi ke krem #F7EEE3) → logo UPG + label oranye ANTANG → judul putih tebal + pita gelap → pil oranye syarat cicilan → kartu harga putih miring "MULAI" → lencana pilihan → 2 pil centang (isi paket, dikerjakan dokter gigi) → tombol WA oranye → lokasi & jam.
- Tanpa "alat steril", tanpa hook pertanyaan, tanpa rontgen/biaya kontrol.

## 5. Naskah
- Scaling Antang: `references/naskah-scaling-antang-01.md` (v2 fokus konversi), papan gambar `references/papan-gambar-scaling-antang-v1.png`, render 3D `scripts/sc.html`
- Behel Antang: `references/naskah-behel-antang-01.md`, papan gambar `references/papan-gambar-behel-antang-v1.png`
- Pengucapan dipilih: **Versi A "U-Pe-Ge Dental Care"** (menyambung).
