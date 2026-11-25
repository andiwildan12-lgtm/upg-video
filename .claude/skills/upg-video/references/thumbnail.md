# Aturan thumbnail (cover Reels) UPG — keputusan Dir 25 Nov 2026

Template: `thumbnail/thumbnail.html` + `thumbnail/render_thumbnail.js` (Playwright, 1080×1920). Contoh hasil yang di-ACC: `upg-video-projects/thumbnail-2511/out/`.

| Unsur | Aturan |
|---|---|
| Foto latar | Momen pengerjaan nyata (close-up gigi, tangan dokter + alat, dokter bekerja, dokter menjelaskan). Ambil dari **footage asli** (bukan video jadi yang ada teks), tanpa zoom berlebih. |
| Privasi | **Tanpa mosaik/blur.** Wajah pasien tidak terlihat: pilih frame yang wajah tertutup dokter/alat, membelakangi, atau di luar frame. **Kecuali testimoni** (wajah boleh, izin tertulis). Dokumen/kertas yang terbaca tetap disamarkan kecil. |
| Testimoni | Pilih frame terbaik: tersenyum, kedua mata terbuka, menghadap kamera (cari per 0,2 dtk). Judul diturunkan ke bawah dagu (`top` ±1190) agar wajah tidak tertutup. |
| Judul | Maks. 6 kata, 2 baris: baris 1 kotak putih, baris 2 (kata kunci) kotak oranye #FA7209; teks #2A2A2A (bukan putih di atas oranye); Nunito 900; ukuran mengecil otomatis agar 1 baris. Posisi tengah agak bawah (`top` 1010), masuk area grid profil 3:4. |
| Logo | Logo mendatar **putih tanpa latar**, tinggi 132 px, **atas tengah** (y ±290), bayangan tipis + gradasi gelap di atas. Bukan di bawah judul (tenggelam di foto). |
| Dokter | Wajah/kepala dokter jangan tertutup kotak judul; geser crop bila perlu. |
