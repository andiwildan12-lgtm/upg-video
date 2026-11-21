# Model "konsultasi dokter" (referensi drg. Firdha) — dipakai Ruma: Konsultasi Tambal drg. Ainun v1 (21 Nov 2026, 56,4 dtk)
Pola: hook = potongan ucapan paling jujur/menarik di atas close-up → konsultasi asli dokter-pasien (rontgen, pilihan) → tindakan dengan obrolan asli → pesan sesudahnya → penutup. Label langkah kecil di kiri atas (blok Turquoise).
1. Cari obrolan di SEMUA klip: ekstrak audio tiap klip (unduh satu-satu, simpan wav 16 kHz), transkrip dengan `vad_filter=True` + `initial_prompt` gigi, buang segmen `no_speech_prob>0.6`. Lalu cap waktu kata per kalimat terpilih (potong audio sumber + highpass/afftdn/loudnorm sebelum Whisper).
2. `build_k1.py`: SEG (klip, in, dur, zoom, proses, pusat zoom) → crossfade 8 frame, punch-in 1,08 di batas kalimat, blur wajah pasien titik kunci (FACE644 dll.), blur kotak nama pasien di monitor rontgen.
3. `ovk1.html` + `shotk1.js`: subtitle 2–4 kata dari cap waktu kata (global = posisi audio + (kata − awal potongan)), hook judul, label langkah, nama, penutup bertahap.
4. `mix_k1.py`: suara dokter dibersihkan (rantai VOICE), suara B-roll 0,18, suara ruangan terus, whoosh tiap batas (−13 dB), whoosh pelan di punch-in (−20), pop saat label (−15), shimmer penutup.
5. Cek akhir: STT file final; "kata asing" di jeda antarkalimat sering halusinasi Whisper → uji lapisan suara sendiri-sendiri sebelum memotong.
Suara dokter dipasang di atas gambar lain (dokter bermasker) boleh bila kamera tertutup.
