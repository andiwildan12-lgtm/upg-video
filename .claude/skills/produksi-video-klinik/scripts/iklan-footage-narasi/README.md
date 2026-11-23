# Iklan full footage + narasi Ricky (Ruma: Iklan Scaling v1, 21 Nov 2026, 51,6 dtk)
1. Narasi: ElevenLabs eleven_v4, Ricky, SATU generasi mengalir, 2 versi (±873 kredit/versi untuk ±48 dtk). Pilih versi dengan pelafalan paling tepat (cek STT: kata kunci seperti "garis", "kuotanya").
2. Cap waktu kata: faster-whisper `word_timestamps` pada mp3 → kunci adegan = kata pertama tiap kalimat (+0,3 dtk offset narasi).
3. `build_base.py`: SEG per adegan (crossfade 8 frame, zoom pelan). Klip iPhone HLG 4K60 → **konversi biasa (scale) sudah natural**; tonemap hable terlalu hangat, zscale langsung membakar highlight.
4. `overlay.html` (+ `shot_overlay.js`): hook, caption kinetik 2–4 kata (kata kunci Turquoise), kartu centang muncul per kata, judul, kartu harga (harga normal dicoret, di area meja agar wajah utuh), logo pojok standar, penutup standar inline.
5. Mix: narasi + suara ruangan klinik 0,09 + whoosh tiap batas + pop tiap elemen + shimmer penutup → loudnorm −16.
