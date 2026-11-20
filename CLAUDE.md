# Instruksi repo upg-video

- Pengguna adalah owner/direktur UPG Dental Care. Panggil **"Dir"**. Jawab dalam Bahasa Indonesia yang jelas, praktis, dan tidak bertele-tele.
- Untuk semua pekerjaan video atau konten iklan UPG, **pakai skill `upg-video`** (`.claude/skills/upg-video/SKILL.md`) dan ikuti aturannya, terutama gerbang ACC.
- Setiap proyek disimpan di `upg-video-projects/<slug>/`.
- Setiap keputusan baru Dir atau pelajaran teknis yang terbukti dicatat di `.claude/skills/upg-video/references/catatan-pembelajaran.md`, lalu di-commit.
- Jangan mengunggah ke media sosial. Jangan menyimpan kunci API di file.
- Skill cabang: **`upg-antang-video`** (UPG Antang) dan **`upg-hertasning-video`** (UPG Hertasning) di `.claude/skills/`. Satu video = satu cabang; data dan footage tidak boleh tertukar, juga tidak dengan Ruma Dental.
- **Pembagian repo (keputusan Dir, 20 Nov 2026):** `upg-video` = UPG (umum, Antang, Hertasning) + GrowWith. `ruma-video` = Ruma Dental + @dalamgigi. Skill identitas hanya di repo brand-nya.
- **Skill bersama** (daftar di `.claude/skill-bersama.txt`: `produksi-video-klinik`, `motion-klinik-gigi`, `panduan-visual-terpadu`, `antislop`, `antislop-ui`, `antislop-copywriting`) disimpan **utuh di kedua repo**, isinya harus identik. Setelah mengubah skill bersama: `bash .claude/scripts/skill-bersama.sh kirim`, lalu commit + push **kedua** repo. Hook SessionStart menjalankan `cek` dan memberi tanda bila salinannya beda (`tarik` untuk mengambil versi repo satunya).
- **Panduan baru dari Dir:** aturan yang berlaku untuk lebih dari satu brand masuk ke skill bersama (biasanya `panduan-visual-terpadu`) lalu disinkronkan; aturan satu brand masuk ke skill identitas brand itu saja.
- **Unduh skill:** `bash .claude/scripts/skill-bersama.sh zip` membuat `dist/skill-<repo>-lengkap.zip` (semua skill repo ini, termasuk skill bersama) dan `dist/skills/<nama>.zip` per skill.
- **Filter anti-AI-slop:** skill `antislop`, `antislop-ui`, `antislop-copywriting` (skill bersama, ada di repo ini). Pakai untuk semua pekerjaan visual dan teks UPG, mode default **during**; "cek/audit pakai antislop" = mode **after**. Arah desain tetap dari skill `upg-video` dan skill cabang; kalau bertentangan, identitas UPG yang menang.
