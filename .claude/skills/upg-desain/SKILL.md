---
name: upg-desain
description: Desain grafis statis UPG Dental Care — poster, Story, Feed, banner promo — mengikuti Pedoman Desain UPG (palet #E97818/Warm Brown/Warm Cream, Poppins + Inter, aturan kontras dan zona aman). Pakai saat Dir minta desain gambar/poster/Story/Feed. Bukan untuk video (pakai upg-video).
---

# UPG Desain (grafis statis)

Panggil pengguna **"Dir"**. Bahasa Indonesia jelas dan ringkas. Brand: **UPG Dental Care saja** (Ruma Dental bukan bagian skill ini).

## Wajib dibaca dulu
- `references/pedoman-desain.md` — palet, kontras, font, logo, komposisi, zona aman.
- `.claude/skills/upg-video/references/catatan-pembelajaran.md` — data promo terkonfirmasi, aturan harga, fasilitas, karakter tanpa mata.
- `.claude/skills/upg-video/references/brand.md` — WA, logo.

**Video tidak memakai pedoman ini** (keputusan Dir, 16 Nov 2026).

## Alur kerja
1. **Brief singkat**: format (Story/Feed/poster), promo/pesan, data. Pakai data terkonfirmasi; harga & periode tidak boleh dikarang. Maks. 1–3 pertanyaan; selebihnya asumsi berlabel.
2. **Draf V1** langsung dibuat (gambar murah direvisi). Kirim gambar + ringkasan singkat.
3. **Audit diri sebelum kirim** pakai daftar periksa di bawah. Kalau Dir minta "audit", nilai jujur dalam tabel *masalah → dampak*, lalu perbaiki di versi berikutnya.
4. Revisi → naikkan versi (V2, V3…). Simpan setiap versi, jangan timpa.
5. Desain final tidak diunggah ke media sosial oleh Claude.

## Produksi teknis
- Proyek: `upg-video-projects/<slug>/desain/` (atau subfolder proyek terkait, mis. `story/`).
- Salin `templates/story-promo.html` + folder `assets/fonts/` (sebagai `fonts/`) + logo yang dipakai ke folder proyek, ubah isi.
- Render: `node .claude/skills/upg-desain/scripts/render_desain.js <file.html> <out.jpg> [lebar tinggi]` → menghasilkan JPG + `<out>-zona.jpg` (overlay zona aman, untuk cek).
- Selalu lihat hasil render (dan versi zona) sebelum dikirim.

## Daftar periksa sebelum kirim
- [ ] Warna hanya dari palet; tidak ada turquoise.
- [ ] Font hanya Poppins + Inter.
- [ ] Teks kecil tidak oranye; tombol CTA oranye pakai teks charcoal.
- [ ] Satu titik fokus; harga terbaca dalam 1 detik.
- [ ] Logo resmi satu kali, tanpa kotak, tidak menimpa konten.
- [ ] Info penting di luar zona aman (Story: 250 atas / 340 bawah).
- [ ] Data promo sesuai konfirmasi Dir; "S&K berlaku" bila ada syarat.
- [ ] WA 089673415806 benar.
- [ ] Ilustrasi tanpa mata; tidak ada klaim medis berlebihan.

## Memperbarui skill
Keputusan baru Dir dicatat di `references/pedoman-desain.md` (aturan desain) atau `catatan-pembelajaran.md` skill video (data promo), lalu di-commit.
