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
