---
name: analisis-footage-konten
description: Menonton footage mentah klinik (folder Drive berisi banyak klip HP/DJI) lalu menyimpulkan dengan cepat dan jujur bisa jadi konten apa saja dan berapa banyak, seperti content creator / social media specialist. Inventaris otomatis (jam rekam, terang, ucapan terverifikasi, lembar cuplikan), saring aturan (rontgen, jumlah asisten, privasi), hitung kapasitas video tanpa terasa berulang, lalu usulan ide per pilar & funnel yang diperingkat. Pakai SETIAP KALI Dir/Pak Dir mengirim folder footage dan bertanya "bisa jadi konten apa", "berapa konten", atau "modelnya gimana", untuk UPG maupun Ruma, sebelum menulis rancangan.
---

# Analisis Footage → Konten

Skill bersama UPG + Ruma (salinan identik di repo `upg-video` dan `ruma-video`). Dibangun dari kerja nyata footage drg. Naya (23 Nov 2026). Struktur video pendek & daftar "pemicu proaktif" diadaptasi dari skill `video-content-strategist` (alirezarezvani/claude-skills, MIT).

**Tugasnya satu:** dari footage yang ADA (tanpa syuting ulang, kecuali Dir minta), jawab cepat & jujur: *bisa jadi konten apa, berapa, dan mana yang paling kuat.* Arah brand tetap dari skill identitas (`upg-video`/cabang, `ruma-dental-video`) dan `panduan-visual-terpadu`.

## Langkah

0. **Jatah disk sesi terbatas (aturan Dir 25 Nov 2026, semua brand):** di `aset-drive/` (dan klip olahan `public/clips` proyek) hanya disimpan **footage yang sedang dikerjakan + 1 footage sebelumnya**. Salinan yang lebih lama dihapus (aslinya tetap di Drive, unduh ulang bila perlu revisi). Folder referensi gaya/foto klinik tidak termasuk. Untuk analisis, unduh lalu kecilkan (540p) per klip; file asli diunduh ulang hanya untuk klip terpilih saat render.
1. **Unduh** daftar folder Drive (`search_files` dengan `'<id>' in ancestors`, ikuti `nextPageToken`), unduh semua klip ke `aset-drive/<slug>/` (gitignored) dengan `curl … drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`.
2. **Inventaris otomatis:** `python3 scripts/inventaris.py aset-drive/<slug>` → `inventaris/inventaris.md` (jam rekam, durasi, orientasi, kelas terang, ucapan lolos saringan) + `lembar-NN.jpg` (10 klip/lembar, 6 frame/klip). ±1 mnt per menit footage (Whisper medium, CPU).
3. **Lihat semua lembar** (Read gambar). Beri tiap klip **jenis gambar**: close-up tindakan · dokter lebar/dekat · asisten bersiap · alat/nampan · obrolan/penjelasan · suasana/ruangan · wajah pasien jelas.
4. **Saring aturan (Hard Gate):**
   - Alat rontgen / layar foto rontgen terlihat → buang/potong (keputusan Dir UPG). Laptop di latar yang isinya tak pasti → hindari.
   - UPG: hanya frame dengan **1 asisten**; jangan narasikan "2 orang/2 asisten".
   - Wajah pasien: tetap disamarkan (UPG mosaik, Ruma blur), data pasien diblur. Klip yang wajahnya tak bisa disamarkan tanpa merusak gambar → tandai.
   - SANGAT_GELAP → hanya sisipan pendek (koreksi warna `produksi-video-klinik` 12f).
5. **Verifikasi ucapan** sebelum dijadikan bahan cerita: Whisper sering salah tangkap ucapan pendek. Ucapan bertanda ⚠ atau ≤2 kata: transkrip ulang potongannya (medium, `word_timestamps`) dan cocokkan dengan konteks gambar. **Jangan pernah** mengisi kata yang tidak terdengar (mis. menambah "sakit"), dan jangan mengarang ucapan dokter/pasien.
6. **Hitung kapasitas (jujur):** video 45–60 dtk butuh ±15–18 gambar (ganti tiap 2–4 dtk). Hitung klip layak per jenis gambar; kalau >40% gambar akan terulang antar-video → kurangi jumlah video atau jadikan sebagian konten pendek (15–20 dtk)/carousel. Satu sesi, satu pasien, satu ruangan biasanya = **2 video panjang + 1 pendek**.
   - **Realistis, jangan dipaksa (keputusan Dir, 24 Nov 2026):** jumlah video mengikuti bahan. Bahannya cukup untuk 2 → 2, cukup untuk 3 → 3. Satu video layak hanya kalau pesannya utuh dari bahan yang ada: masalah, penjelasan, dan jalan keluar/ajakan terdengar atau terlihat jelas. Ide yang bahannya setengah (penjelasan terpotong, ucapan kurang dari ±15 dtk yang jelas, atau klip intinya sudah dipakai video lain) **dicoret**, bukan ditambal teks layar. Laporkan ke Dir: "bahan cukup untuk N video", lalu sebutkan ide yang dicoret dan alasannya.
7. **Cek waktu dari jam rekam** sebelum menulis klaim urutan ("sebelum kamu duduk", "lalu", "selesai dalam…"). Jam rekam **bukan** bahan ide konten: format montase jam ("Berapa lama sih…?", "1 jam dipadatkan") **dihapus untuk UPG dan Ruma** (keputusan Dir 25 Nov 2026: tidak cocok jadi pilar).
8. **Usulkan 3–5 ide**, diperingkat dalam tabel:

| Ide | Pilar / funnel | Hook 3 dtk | Kenapa orang berhenti scroll | Bahan suara | Perlu data dokter? | Bisa jalan hari ini? |

   **Ide WAJIB dipilih dari katalog pilar brand masing-masing, jangan mengarang format baru** (keputusan Dir 25 Nov 2026: pilar UPG dan Ruma dibedakan):
   - UPG → `upg-video/references/edukasi-dokter.md` §0 (A dokter ke kamera · C tindakan + teks · D testimoni · E interaksi duduk sampai pulang).
   - Ruma → skill `ruma-dental-video` §10e (Ruma Menjelaskan · Kalau Ditunda · Disiapkan untukmu/Tur Klinik · Cerita Pasien/Before-After).
   Pilar resmi per funnel: `panduan-visual-terpadu` §7. Bila ada obrolan dokter-pasien yang jelas, utamakan format interaksi/cerita (rasa dekat dengan pasien).
   - **Prioritas format (keputusan Dir, 24 Nov 2026, UPG + Ruma):** kalau footage berisi obrolan dokter-pasien yang jelas, utamakan **video interaksi dari awal sampai akhir** (duduk/konsultasi → periksa → tindakan dengan obrolan asli → hasil/pesan sesudahnya → pulang), seperti Izza-A (UPG) dan Konsultasi Tambal drg. Ainun (Ruma). Video interaksi ini diusulkan sebagai video **#1**; ide lain (edukasi satu topik, montase) dihitung dari sisa bahan dan tetap harus berupa interaksi utuh untuk topiknya, tanpa mengulang ucapan/gambar video #1.
9. **Rekomendasikan 1** yang bisa jalan sekarang + catat yang butuh validasi dokter. Lalu masuk ke alur rancangan → papan → ACC skill brand.

## Struktur video pendek (dipakai saat menilai ide)
0–3 dtk hook (pola pemutus scroll, frame paling kuat di awal) · 3–15 dtk janji/masalah · 15–50 dtk isi, satu ide per video, pertanyaan kedua di tengah untuk menahan · 50–60 dtk penutup standar brand + 1 ajakan sesuai funnel. Teks layar selalu ada (mayoritas menonton tanpa suara).

## Pemicu proaktif (sebutkan tanpa diminta)
- Ide yang bergantung pada ucapan yang tidak jelas/terverifikasi.
- Gambar akan terulang >40% antar-video.
- Klaim waktu/urutan yang tidak sesuai jam rekam.
- Konten klinis yang belum dicek dokter.
- Footage yang gelap/goyang dipakai sebagai hook.
- Saran syuting berikutnya bila bahan kurang (mic klip di dokter, lampu ruangan menyala, tap wajah dokter untuk terang).

## Hasil
`inventaris/inventaris.md` + lembar cuplikan, lalu laporan singkat ke Dir: total klip & menit, yang dibuang dan alasannya, kapasitas jujur, tabel ide berperingkat, rekomendasi.
