# Naskah Iklan Behel — UPG Dental Care Antang (v2, 18 Nov 2026)

Status: **draf lengkap, menunggu OK Pak Dir.**
Format: 9:16, ±52 dtk (narasi ±49 dtk + kartu penutup 3 dtk). MOFU/BOFU. Rumus 8 ketukan.
Gaya: **Opsi 2 — motion 3D (±30%) untuk masalah/edukasi + footage asli Antang (±70%) untuk bukti/ajakan.** Tempo lebih cepat dari Ruma; potongan footage 1,5–3 dtk.
Audio: narator AI (ElevenLabs eleven_v4, satu generasi mengalir), tanpa musik, SFX tiap gerakan, suara latar ruangan pelan.
Warna kartu/teks: hitam + oranye UPG (asumsi dari jas staf, menunggu file logo resmi).

---

## A. Narasi lengkap (teks untuk ElevenLabs)

```
[conversational] Gigi berjejal itu bukan cuma soal penampilan. Selanya lebih susah dibersihkan.
Banyak yang pengin rapi dari dulu... tapi kepikiran biayanya.
Di sela yang rapat, sisa makanan gampang nyelip. Lama-lama jadi karang, dan lebih rawan berlubang.
Kalau dibiarkan, tiap hari tetap susah dibersihkan. Kalau dirapikan, sikat gigi jadi lebih gampang.
[cheerfully] Solusinya, perawatan behel di U-Pe-Ge Dental Care Antang. Mulai tiga juta per rahang. Cukup DP lima puluh persen, sisanya cicil dua kali.
Sudah termasuk konsultasi, cetak gigi, dan skeling. Dicek dulu, dikerjakan dokter gigi. Pilihannya ada tiga jenis behel.
[warmly] Tujuannya, gigi lebih rapi dan lebih gampang dirawat.
Lokasinya di lantai dua Apotek Wahdah Antang. Buka setiap hari, jam sepuluh pagi sampai sepuluh malam. Chat admin, konsultasi dulu, ya.
```
±118 kata. "skeling" = ejaan fonetik "scaling" agar dibaca benar.

---

## B. Skrip per adegan

| # | Detik | Ketukan | Narasi | Visual | Teks layar | SFX / transisi |
|---|---|---|---|---|---|---|
| 1 | 0,0–4,5 | Hook fakta | Gigi berjejal itu bukan cuma soal penampilan. Selanya lebih susah dibersihkan. | 🎨 3D: senyum (bibir + deretan gigi, tanpa wajah), gigi depan bawah tumpang tindih. Sikat gigi masuk dari kanan, bulunya mentok di sela. Kamera dorong pelan ke sela. | Label: *Fakta gigi* · Utama: **Gigi berjejal = susah dibersihkan** | sikat (brush) saat sikat bergerak; pop saat teks muncul |
| 2 | 4,5–8,5 | Itu saya | Banyak yang pengin rapi dari dulu… tapi kepikiran biayanya. | 🎥 4741: pasien (blazer putih) duduk di ruang konsultasi, menatap ke depan. Zoom pelan 3%. | *Pengin rapi, tapi…* lalu ikon 💸 | wipe 3D → footage; notif HP kecil saat ikon 💸 |
| 3 | 8,5–15 | Yang terjadi | Di sela yang rapat, sisa makanan gampang nyelip. Lama-lama jadi karang, dan lebih rawan berlubang. | 🎨 3D: kamera masuk "lorong" sela gigi. Butir sisa makanan krem menyelip → lapisan karang kekuningan menumpuk di pangkal. Suasana sedikit redup/dingin. | Label: *Di sela yang rapat* · Utama: **Sisa makanan nyelip → karang** | whoosh masuk lorong; pop tiap butir |
| 4 | 15–20 | Dua jalan | Kalau dibiarkan, tiap hari tetap susah dibersihkan. Kalau dirapikan, sikat gigi jadi lebih gampang. | 🎨 3D: kamera naik ke senyum. Gigi berjejal bergeser pelan jadi rapi; cahaya berubah hangat. Sikat gigi lewat mulus. (Ilustrasi, **bukan** foto sebelum-sesudah.) | Kiri: *Dibiarkan* (abu) → Kanan: **Dirapikan** (oranye) | whoosh naik; sikat mulus |
| 5 | 20–30 | Solusi + brand + harga | Solusinya, perawatan behel di UPG Dental Care Antang. Mulai tiga juta per rahang. Cukup DP lima puluh persen, sisanya cicil dua kali. | 🎥 3746 (20–24): dokter memasang kawat, logo UPG di jas terlihat. → 🎨 kartu harga (24–30) di atas footage 3746 yang diburamkan. | 20–24: **Behel di UPG Dental Care Antang** · 24–30: *MULAI* **Rp3 jt/rahang** · DP 50% · cicil 2x | wipe footage; pop tiap baris harga |
| 6 | 30–39 | Alasan percaya | Sudah termasuk konsultasi, cetak gigi, dan skeling. Dicek dulu, dikerjakan dokter gigi. Pilihannya ada tiga jenis behel. | 🎥 potongan cepat: 4740 dokter menjelaskan (30–32) → 4743 cetakan gigi (32–33,5) → 3726 baki alat, **nama pasien di model diblur** (33,5–35) → 3737/3739 dokter + asisten memasang (35–37,5) → 3745 senyum bracket sekilas ≤1 dtk (37,5–39). | Centang muncul satu per satu: ✅ Konsultasi ✅ Cetak gigi ✅ Scaling · lalu **Dikerjakan dokter gigi** · lalu chip: *Metal · Keramik · Self-ligating* | pop tiap centang; whoosh kecil tiap potongan |
| 7 | 39–43 | Hasil | Tujuannya, gigi lebih rapi dan lebih gampang dirawat. | 🎥 3744: pasien tersenyum melihat behel barunya di cermin. Warna hangat. | **Rapi & gampang dirawat** | tanpa SFX (biarkan momen) |
| 8 | 43–49 | Ajakan + lokasi | Lokasinya di lantai dua Apotek Wahdah Antang. Buka setiap hari, jam sepuluh pagi sampai sepuluh malam. Chat admin, konsultasi dulu, ya. | 🎥 3517: pintu "OPEN" → resepsionis menyapa & tersenyum (43–46) → 3525 ruang perawatan luas (46–49). | 📍 **Lt. 2 Apotek Wahdah Antang** · ⏰ Setiap hari 10.00–22.00 · 💬 **Chat admin, konsultasi dulu** | pintu geser (opsional); pop |
| 9 | 49–52 | Kartu penutup | — | 🎨 Kartu hitam-oranye: logo UPG Dental Care, "Antang", WA, alamat, harga ringkas. | **UPG Dental Care Antang** · Behel mulai Rp3 jt/rahang, cicil · 💬 0895-1013-2102 · Lt. 2 Apotek Wahdah Antang | pop logo; suara latar memudar |

---

## C. Hasil checklist 3a (dijalankan sendiri)

| Draf awal | Masalah | Diganti jadi |
|---|---|---|
| Hook "Gigi berjejal, renggang, atau maju?" (Hertasning) | Pertanyaan pribadi, menyiratkan kondisi penonton | Hook fakta "Gigi berjejal itu bukan cuma soal penampilan…" |
| "Alat steril" (Hertasning) | Klaim terlarang | Dihapus; diganti "Dicek dulu, dikerjakan dokter gigi" |
| Narasi "metal, keramik, dan self-ligating" | Istilah asing berat diucapkan AI, memperpanjang durasi | Narasi "tiga jenis behel", nama jenis tampil di teks layar |
| "Dibiarkan, susahnya terus" | Kaku diucapkan | "Kalau dibiarkan, tiap hari tetap susah dibersihkan" |
| Foto rontgen di footage 4738–4741 | Pak Dir: rontgen tidak dibahas | Narasi tidak menyebut rontgen; 4740 hanya sekilas sebagai "konsultasi" |

- [x] Hook fakta ≤3 dtk · [x] Momen "itu saya" · [x] Dua jalan, nada tenang · [x] Solusi + "UPG Dental Care Antang" di tengah (dtk 20)
- [x] Bukti nyata (footage Antang asli) · [x] Hasil positif tanpa janji ("tujuannya…") · [x] Ajakan ringan "konsultasi dulu"
- [x] Tanpa klaim terlarang (steril, tanpa sakit, permanen, terbaik, gratis) · [x] Data resmi Antang sesuai skill (alamat, WA, jam, harga)
- [x] ±118 kata ≈ 49 dtk + kartu 3 dtk

## D. Perlu validasi Pak Dir
1. **Logo UPG** (file PNG/JPG) dan warna resmi. Sementara: hitam + oranye.
2. **Izin wajah pasien** behel (klip 3744, 3745, 3737) untuk iklan berbayar.
3. **Pelafalan**: "skeling", "Apotek Wahdah" — dicek saat dengar suara.
