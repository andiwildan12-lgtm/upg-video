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
| `naya-psa-videoA` | Edukasi PSA, b-roll + teks + ucapan asli (drg. Naya, Hertasning), mosaik wajah pasien, penutup standar organik | `out/naya-psa-videoA-V2.mp4` |
