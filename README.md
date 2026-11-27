# upg-video

Konten video UPG Dental Care: Reels, TikTok, dan iklan Meta. Dikerjakan bersama Claude Code memakai skill **UPG Video**.

## Cara memakai
1. Buka aplikasi Claude → **Code** → pilih repo **upg-video** (environment: **Video Editing**).
2. Ketik apa yang mau dibuat, misalnya:
   - *"Pakai skill UPG Video, saya mau bikin iklan scaling pakai motion."*
   - *"Ini video saya dengan dokter, tolong edit buat iklan scaling."* (lampirkan rekaman atau link Google Drive)
   - *"Lanjut serial Misi Anak Rantau episode 3."* (serial TOFU animasi 3D)
   - *"Bikin konten edukasi drg. X dari folder Drive ini, gaya 1."* / *"Konten POV perawat, gaya 3."* (rekaman asli dokter/staf)
3. Diskusi → rancangan → **ACC** → video jadi. Produksi tidak berjalan sebelum ACC.

## Isi repo
| Folder | Isi |
|---|---|
| `.claude/skills/upg-video/` | Skill UPG Video: aturan brand, alur ACC, jalur MOTION, EDIT REKAMAN, **SERIAL CERITA 3D**, dan **EDUKASI DOKTER & POV STAF** (Gaya 1 / Gaya 3), **panduan visual terkunci UPG · Ruma · GrowWith** (dari Canva), template, skrip, catatan pembelajaran |
| `dist/skill-upg-video-lengkap.zip` | Semua skill repo ini (UPG, cabang, GrowWith via panduan, + skill bersama) dalam satu unduhan. `dist/skills/<nama>.zip` per skill. Dibuat dengan `bash .claude/scripts/skill-bersama.sh zip` |
| `dist/upg-video-skill.zip` | Paket skill `upg-video` saja (lama) |
| `upg-video-projects/<proyek>/` | Satu folder per video: rancangan, catatan ACC, sumber animasi/edit, audio, hasil video |
| `docs/` | Brief awal skill, audit Canva Panduan Visual Terpadu |

**Skill cabang:** `upg-antang-video`, `upg-hertasning-video` (pindahan dari repo ruma-video, 18 Nov 2026).


Rekaman mentah (`sumber/`, `aset-drive/`) dan file kerja besar tidak disimpan di git.

**Repo dipisah:** repo ini untuk UPG + GrowWith; Ruma + Dalam Gigi di repo `ruma-video`. Skill bersama (`produksi-video-klinik`, `motion-klinik-gigi`, `panduan-visual-terpadu`, `antislop` x3) ada utuh di kedua repo dan disamakan dengan `bash .claude/scripts/skill-bersama.sh kirim`.

**Filter antislop** (skill bersama): dipakai sambil bekerja untuk semua visual dan teks; "audit pakai antislop" menghasilkan laporan di `<proyek>/anti-slop/`.

## Video yang sudah jadi
| Proyek | Jenis | Hasil |
|---|---|---|
| `happy-hour-scaling` | Iklan BOFU (motion + footage) | `out/upg-happy-hour-scaling-V6.mp4` |
| `behel-cicilan` | Iklan BOFU | `out/upg-behel-cicilan-V3.mp4` |
| `tambal-keluarga` | Iklan BOFU | `out/upg-tambal-keluarga-V3.mp4` |
| `cerita-rina` | MOFU cerita (animasi + footage) | `out/upg-cerita-rina-V3.mp4` |
| `misi-anak-rantau-eps1` | TOFU serial 3D, Eps 1 | `out/upg-misi-anak-rantau-eps1-V4.mp4` |
| `misi-anak-rantau-eps2` | TOFU serial 3D, Eps 2 | `out/upg-misi-anak-rantau-eps2-V1.mp4` |
| `edukasi-cabut-firdha` | Edukasi dokter, Gaya 1 (drg. Firdha, pasien takut cabut gigi) | `out/edukasi-cabut-firdha-V4.mp4` |
| `pov-nur-fo-hertasning` | POV staf, Gaya 3 (Nur, Front Office Hertasning) | `out/pov-nur-fo-hertasning-V3.mp4` |
| `naya-psa-videoA` | Edukasi PSA, b-roll + teks + ucapan asli (drg. Naya, Hertasning), mosaik wajah pasien, tanpa musik, penutup standar organik | `out/naya-psa-videoA-V6.mp4` |
| `naya-psa-videoB` | Montase 1 jam perawatan saraf dengan jam rekam asli (drg. Naya, Hertasning), tanpa musik, mosaik pasien | `out/naya-psa-videoB-V1.mp4` |
| `naya-psa-videoC` | Testimoni Kak Nabil (pasien PSA drg. Naya, izin tertulis), wawancara + selingan perawatan, tanpa musik | `out/naya-psa-videoC-V3.mp4` (file >100 MB, tidak di repo) |
| `izza-scaling-A` | Scaling bareng drg. Izza (Hertasning): obrolan asli dari duduk sampai pulang, nama pasien dipotong, mosaik wajah + kertas | `out/izza-scaling-A-V3.mp4` (tidak di repo, >100 MB bila besar) |
| `izza-tambalan-B` | Tambalan lama kamu masih aman? (Hertasning): drg. Izza tunjukkan tepi tambalan menghitam/pecah, mosaik mata pasien, 31 dtk | `out/izza-tambalan-B-V2.mp4` (tidak di repo) |
| `adhila-scaling-A` | Pertama kali scaling, gusinya sering berdarah (Hertasning): interaksi drg. Adhila dari konsultasi sampai pesan sesudah scaling, mosaik mata pasien + kertas + orang di latar, 57 dtk | `out/adhila-scaling-A-V3.mp4` (tidak di repo) · **dipakai & diunggah Dir** |
| `adhila-berapa-lama` | Berapa lama sih scaling? (Hertasning, format B montase jam rekam): drg. Adhila 16.11-16.54, satu ide (kenapa lama + dicek semua sisi), klip file asli, mosaik minimal, 39 dtk | `out/adhila-berapa-lama-V4.mp4` (tidak di repo) · ok, tidak diunggah |
| `adhila-bleaching-tambal` | Mau bleaching, tapi ada gigi berlubang? (Hertasning, format E interaksi): drg. Adhila jelaskan kenapa ditambal dulu, mosaik mata, file asli, 37 dtk | `out/adhila-bleaching-tambal-V2.mp4` (tidak di repo) |
| `adhila-lubang-dalam` | Lubangnya dalam, harus rawat saraf? (Hertasning, format E): drg. Adhila jelaskan pilihan bahan pelapis + pantau, dan risikonya, mosaik profil + kertas, 58 dtk | `out/adhila-lubang-dalam-V1.mp4` (tidak di repo) |
| `arham-scaling-bercelah` | Habis scaling kok gigi terasa bercelah? (Hertasning, format E): drg. Arham, konsultasi → scaling → bercermin → kontrol 6 bulan, mosaik manual close-up gelap, 51,5 dtk | `out/arham-scaling-bercelah-V1.mp4` (tidak di repo) |
| `firdha-ngilu-sekali` | Gigi ngilu sekali, tanda apa? (Hertasning, format E): drg. Firdha, saraf vital vs nekrosis, ngilu sekali = dekat saluran akar, dicoba lapisan dulu, 50,5 dtk | `out/firdha-ngilu-sekali-V2.mp4` (tidak di repo) |
| `firdha-goyang` | Kemarin goyang, sekarang? (Hertasning, format E): drg. Firdha kontrol, gigi longgar sakit ditekan, sekarang stabil, coba mengunyah pelan-pelan, 37,3 dtk | `out/firdha-goyang-V1.mp4` (tidak di repo) |
| `arham-psa-scaling` | Habis PSA, boleh langsung scaling? (Hertasning, format E): drg. Arham menjawab pertanyaan pasien, karang dibiarkan → gusi turun, scaling + cek tiap 6 bulan, kartu ringkasan 4 butir, 45,7 dtk | `out/arham-psa-scaling-V2.mp4` (tidak di repo) |
| `arham-psa-terakhir` | Kunjungan terakhir PSA, ngapain aja? (Hertasning, format E + motion): drg. Arham, cek keluhan → motion tahap PSA → rubber dam (pengaman) + motion → obturasi di bawah rubber dam → kartu ringkasan, seri dengan video scaling, 55,4 dtk | `out/arham-psa-terakhir-V2.mp4` (tidak di repo) |
| `ainun-tambal-atau-psa` | Gigi berlubang, kapan bisa langsung ditambal? (Hertasning, format E + motion): drg. Ainun menunjukkan gigi pasien di monitor, bagian hitam = bakteri, sampai saraf → PSA, belum sampai saraf → langsung tambal, motion kedalaman lubang, kartu ringkasan, 63,8 dtk | `out/ainun-tambal-atau-psa-V1.mp4` (tidak di repo) |
