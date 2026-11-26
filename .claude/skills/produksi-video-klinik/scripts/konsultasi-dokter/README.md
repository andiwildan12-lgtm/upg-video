# Model "konsultasi dokter" (referensi drg. Firdha) — dipakai Ruma: Konsultasi Tambal drg. Ainun v1 (21 Nov 2026, 56,4 dtk)
Pola: hook = potongan ucapan paling jujur/menarik di atas close-up → konsultasi asli dokter-pasien (rontgen, pilihan) → tindakan dengan obrolan asli → pesan sesudahnya → penutup. Label langkah kecil di kiri atas (blok Turquoise).
1. Cari obrolan di SEMUA klip: ekstrak audio tiap klip (unduh satu-satu, simpan wav 16 kHz), transkrip dengan `vad_filter=True` + `initial_prompt` gigi, buang segmen `no_speech_prob>0.6`. Lalu cap waktu kata per kalimat terpilih (potong audio sumber + highpass/afftdn/loudnorm sebelum Whisper).
2. `build_k1.py`: SEG (klip, in, dur, zoom, proses, pusat zoom) → crossfade 8 frame, punch-in 1,08 di batas kalimat, blur wajah pasien titik kunci (FACE644 dll.), blur kotak nama pasien di monitor rontgen.
3. `ovk1.html` + `shotk1.js`: subtitle 2–4 kata dari cap waktu kata (global = posisi audio + (kata − awal potongan)), hook judul, label langkah, nama, penutup bertahap.
4. `mix_k1.py`: suara dokter dibersihkan (rantai VOICE), suara B-roll 0,18, suara ruangan terus, whoosh tiap batas (−13 dB), whoosh pelan di punch-in (−20), pop saat label (−15), shimmer penutup.
5. Cek akhir: STT file final; "kata asing" di jeda antarkalimat sering halusinasi Whisper → uji lapisan suara sendiri-sendiri sebelum memotong.
Suara dokter dipasang di atas gambar lain (dokter bermasker) boleh bila kamera tertutup.

## Varian montase visual "Di Balik ..." (Ruma: Di Balik Loupe drg. Ainun v1, 21 Nov 2026, 30,2 dtk)
`build_k2.py` + `ovk2.html` + `mix_k2.py`: 5 langkah × 4 dtk (penanda n/5 + nama alat, kalimat fungsi muncul 0,5 dtk kemudian dengan click), hook pertanyaan, foto dokter (Ken Burns, jenis klip `foto`), penutup logo. Audio = suara asli alat 0,30–0,35 (klip yang berisi ucapan tanpa subtitle → volume 0) + suara ruangan + whoosh/pop/click/shimmer. Cek akhir: STT dengan VAD harus kosong (tidak ada ucapan tak bersubtitle).

## Varian "kartu daftar bertambah" (Ruma: Pantangan setelah cabut gigi, drg. Akbar v1, 26 Nov 2026, 54,4 dtk)
Permintaan Pak Dir: kalau dokter menyebut beberapa poin berurutan, tampilkan **kartu daftar yang bertambah** supaya poin sebelumnya tetap bisa dibaca ulang. `build_k10.py` + `ovk10.html` + `mix_k10.py`: kartu putih di area dinding kosong (top 372, tidak menutup wajah), poin baru masuk dengan pop tepat saat diucapkan, poin aktif blok Turquoise, poin lama redup (opacity .6); bagian "Kenapa?" memakai kartu yang sama dengan sorotan pindah; kartu kedua bertanda ✓ untuk "yang dilakukan". Pergantian state memakai `data-nf` (tanpa fade ulang, hanya baris baru yang pop). Suara transisi uji coba "kertas dibalik" (`sfx_book`, −12 dB batas adegan, −19 dB punch-in).
Pelajaran: kata yang diucapkan pelan setelah jeda ("boleh kita … ganti") bisa terpotong; cek energi RMS per 0,1 dtk di ujung potongan, jangan hanya cap waktu kata.
