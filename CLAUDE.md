# Instruksi repo upg-video

- Pengguna adalah owner/direktur UPG Dental Care. Panggil **"Dir"**. Jawab dalam Bahasa Indonesia yang jelas, praktis, dan tidak bertele-tele.
- Untuk semua pekerjaan video atau konten iklan UPG, **pakai skill `upg-video`** (`.claude/skills/upg-video/SKILL.md`) dan ikuti aturannya, terutama gerbang ACC.
- Setiap proyek disimpan di `upg-video-projects/<slug>/`.
- Setiap keputusan baru Dir atau pelajaran teknis yang terbukti dicatat di `.claude/skills/upg-video/references/catatan-pembelajaran.md`, lalu di-commit.
- Jangan mengunggah ke media sosial. Jangan menyimpan kunci API di file.
- Skill cabang: **`upg-antang-video`** (UPG Antang) dan **`upg-hertasning-video`** (UPG Hertasning) di `.claude/skills/`. Satu video = satu cabang; data dan footage tidak boleh tertukar, juga tidak dengan Ruma Dental.
- Teknik render bersama (3D, narasi, audit, poster, transkripsi, video orang bicara, caption kinetik, blur logo/data pasien) ada di skill `produksi-video-klinik` di repo `ruma-video`; skill identitas UPG hanya di repo ini.
- **Skill saling terlihat:** hook `.claude/hooks/sinkron-skill.sh` (SessionStart) menyalin skill repo `ruma-video` ke `~/.claude/skills` setiap sesi mulai. Kalau skill `produksi-video-klinik` tidak muncul di daftar skill, baca langsung `../ruma-video/.claude/skills/produksi-video-klinik/SKILL.md` atau `~/.cache/skill-repo/ruma-video/...`. Perubahan skill Ruma/teknik bersama di-commit ke repo `ruma-video`, bukan disalin ke sini.
- **Filter anti-AI-slop:** skill `antislop`, `antislop-ui`, `antislop-copywriting` disimpan di repo `ruma-video` dan ikut tersinkron lewat hook yang sama (kalau tidak muncul, baca `../ruma-video/.claude/skills/antislop/SKILL.md`). Pakai untuk semua pekerjaan visual dan teks UPG, mode default **during**; "cek/audit pakai antislop" = mode **after**. Arah desain tetap dari skill `upg-video` dan skill cabang; kalau bertentangan, identitas UPG yang menang.
