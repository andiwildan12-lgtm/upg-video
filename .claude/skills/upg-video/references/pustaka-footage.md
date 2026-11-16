# Pustaka Footage & Foto UPG (Google Drive)

Drive adalah **perpustakaan footage** milik Dir, dan isinya bisa diperbarui kapan saja (keputusan Dir, 15 Nov 2026).

**Cara pakai:**
1. Jangan mengunduh semuanya di awal.
2. Setiap proyek, baca isi folder terbaru lewat konektor Google Drive (`search_files` dengan `parentId = '<id>'`).
3. Pilih klip yang relevan, lalu **unduh hanya klip terpilih** ke `aset-drive/`. Folder ini sudah di-.gitignore dan tidak masuk repo.
4. Perintah unduh (environment **Video Editing** sudah mengizinkan host Drive):
   ```
   curl -sS -L -f -o "aset-drive/<sub>/<nama>" "https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t"
   ```
5. Klip di bawah ini terakhir dicek 15 Nov 2026. Bila ada klip baru di Drive, tinjau dan tambahkan ke katalog ini.

## Folder
| Folder | Link / ID | Isi |
|---|---|---|
| Foto klinik | `1EOvmc4i-jqA0OnYiZINYRn8E89RbvGkC` | ±59 foto (IMG_9154–9212) + **`Logo UPG.png` resmi** (10.000 px, transparan, id `1rmT3rJ9pfRcF86A--yPgBVKhRlPjFWvR`) |
| Footage iklan A | `1PzkgDi_4MjtgTdDU8y9EP-TqUd-QDH6k` | Subfolder: Bleaching, Gigi Palsu, Tambal Gigi |
| Footage iklan B | `1IoNwfaYyKP0HaOSmVDAgZIzgd1cFfSTT` | Subfolder: **Scalling** (`1zY_xRIKdMUMNMhqjuQ5EWAabQc9z8GRR`), Bleaching, Behel/Ortho, Tambal Gigi, **Suasana Klinik** (`1tjD4iBPaU1k47UXqMSRcMZxayycwawl_`) |

**Spesifikasi klip:** iPhone, vertikal 1080×1920 (rotasi metadata −90), 60 fps, 2–20 dtk, dengan suara ambient (biasanya dibisukan dan diganti narasi).

## Katalog — Scalling
| Klip | Isi | Catatan |
|---|---|---|
| 3236, 3223, 3235, 3220 | Close-up alat scaling / kaca mulut di gigi | Pas untuk "solusinya scaling" |
| 3219, 3237, 3239 | Pemeriksaan dengan kaca mulut | |
| 3226, 3232, 3233, 3230, 3238, 3227, 3231 | Dokter + asisten bekerja, APD lengkap | Kesan profesional & steril |
| 3218, 3224, 3225, 3234 | Ruang tindakan lebar, pasien di kursi | |
| 3221, 3222 | Dokter menunjukkan foto gigi di HP ke pasien | Kesan "dijelaskan dengan jelas" |

**Izin tampil:** pasien di footage scaling sudah setuju tampil di iklan (dikonfirmasi Dir, 15 Nov 2026).

## Katalog — Suasana Klinik
| Klip | Isi |
|---|---|
| 3482, 3503, 3504 | **Dinding logo UPG** di resepsionis |
| 3501, 3502 | Resepsionis melayani pasien |
| 3217, 3480, 3216, 3481 | Ruang tunggu sofa abu-abu |
| 3215, 3477, 3478 | Meja "IT'S FREE! Snacks, drinks & ice cream" |
| 3475, 3476, 3479 | Freezer es krim / snack |
| 3474 | Area bermain anak |
| 3469, 3473 | Pojok baca ("READ ME! Enjoy reading") |
| 3500, 3505, 3506, 3507 | Pasien berjalan, lorong, ruang tunggu lantai atas |

**Fasilitas terkonfirmasi masih berlaku (Dir, 15 Nov 2026):** snack, minuman, dan es krim gratis; area bermain anak; pojok baca.

## Katalog — Tambal Gigi (dicek 15 Nov 2026)
Folder B `1vqgJqSfA-x9icTXqZdBcvcOK9JIBAbf5` (3240–3271) dan folder A `1YpKc-VbnHarj3HPx8NLGPV7XCNUy4tN6` (4683–4702).
| Klip | Isi |
|---|---|
| 3262 | **Sinar biru pengeras tambalan** (ikon tambal gigi) |
| 3247–3249, 3252, 3254–3255, 3259–3261, 3263, 3266, 3269 | Close-up bor/alat di gigi |
| 3253, 3267, 4696, 4697 | Nampan alat steril |
| 3245, 3270, 4684–4687, 4702 | Dokter menunjukkan foto gigi di HP/tablet ke pasien |
| 3240–3244, 3256–3258, 3264–3265, 4689–4694 | Dokter + asisten bekerja |
| 4683 | Dokter menjelaskan ke pasien dengan tablet |

## Katalog — Behel/Ortho (`1sVGv_szB3nWFQPzPgG90S8qNNLEcdJYi`)
| Klip | Isi |
|---|---|
| 3483, 3486 | Nampan alat steril |
| 3484 | Konsultasi |
| 3485, 3488, 3489, 3497, 3498 | Dokter dengan pasien |
| 3487, 3490–3495, 3499 | Close-up pemasangan bracket/kawat |
| 3496 | **Pasien melihat behelnya di cermin** |

## Katalog — Foto klinik (dicek 16 Nov 2026, untuk desain gambar)
Unduh ke `aset-drive/foto/<nomor>.jpg` (iPhone 4032×3024, sebagian portrait).
| Foto | Isi |
|---|---|
| **9163**, 9162 | **Lobi: dinding logo UPG + resepsionis + sofa ruang tunggu**. Terang, paling kuat untuk latar promo (dipakai Story/Feed Scaling V6) |
| 9166–9170 | Resepsionis & dinding logo dari depan (9168 ada pasien duduk) |
| 9171, 9173–9175 | Close-up papan nama "UPG Dental Care" (9173–9175 dengan bunga) |
| 9157 (P), 9158 | Dinding logo lengkung, sudut bawah |
| 9154, 9155 | Freezer es krim + rak tanaman |
| 9159–9161, 9156, 9164 | Rak hias, pojok baca |
| 9187 (P) | Meja "IT'S FREE" snack |
| 9178–9181 | Pintu kaca depan, papan klinik di jalan (9180 P) |
| 9182–9185 | Mushola |
| 9188–9191, 9198–9207 | **Ruang tindakan** dengan dental unit (9191 close-up kursi biru + nampan alat). Cocok untuk promo tindakan |
| 9192–9194, 9208–9212 | Ruang tunggu kecil/VIP dengan sofa & lampu gigi |
