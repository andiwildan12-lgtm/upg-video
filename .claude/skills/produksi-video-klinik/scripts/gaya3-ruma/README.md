# Gaya 3 versi Ruma (cerita kasus dokter dari rekaman asli)
Proyek pertama: organik Tambal Ulang drg. Ainun (21 Nov 2026), 40,4 dtk.
1. `build_base.py <folder-klip> base.mp4`: potong klip (daftar SEG), slow zoom 1,00-1,04, blur wajah pasien (elips; klip gimbal pakai titik kunci per 0,5 dtk KF671), blur kertas meja, cerahkan close-up gelap (gamma 1,35), kartu putih + video dokter kecil, latar penutup Mint White.
2. `ov.html` (+ font Montserrat, logo.png di folder yang sama, disajikan lewat http.server): daftar E = [mulai, selesai, html]; fade 0,25 dtk.
3. `node shotov.js <folder-keluaran>`: PNG transparan per frame (frame yang sama dibuat symlink; 1212 frame = 183 tangkapan).
4. Audio: potong ucapan per kata (faster-whisper word_timestamps), suara B-roll 0,22-0,30, suara ruangan penutup fade 2,5 dtk, loudnorm -16 LUFS, TP <= -1 dBFS.
5. Gabung: overlay PNG di atas base + audio; cek ulang STT di file final untuk sinkron subtitle.
