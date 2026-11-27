# GrowWith: Kenalan sama tim Ruma Dental (27 Nov 2026)

- Akun: **GrowWith** (keputusan Pak Dir 27 Nov: "ini masuk di GrowWith"), TOFU, tanpa promo/harga/WA/lowongan; ajakan hanya follow.
- Footage: Drive `16qpWR1bImVmouqXEbNxnvRntaJayX7W7` ("Pengenalan Tim RUMA", induk GrowWith): 11 klip 3–5 dtk (tanpa ucapan, hanya suara lokasi) + 11 foto; referensi TikTok di subfolder Referensi (kartu nama miring + foto potong berbingkai putih).
- Format: satu staf pemandu menghampiri tiap anggota tim, pose bersama → foto beku miring berbingkai putih di atas latar blur + kartu hijau miring (nama, peran, julukan). Pemotong latar (rembg) tidak dipasang (izin ditolak), diganti foto beku berbingkai.
- Urutan klip (alur masuk klinik): e101547 parkir → v102119 pintu depan → m0010 resepsionis → v102351 resepsionis (logo Ruma) → v102204 lobi → e101715 area APAR → e101614 pintu ruang tindakan → m0024 (baju awan) → e101647 (baju biru) → m0027 (gaun teal) → m0019.
- Keputusan Pak Dir 27 Nov: tanpa logo GrowWith; julukan dibuat Claude; "gass render" (izin tampil dianggap sudah ada).

## Daftar tim (dari Pak Dir 27 Nov; julukan dibuat Claude atas permintaan Pak Dir)
1 Hardi, Helper (Penjaga helm paling ramah) · 2 Dian, Admin Rekam Medis (Si paling rapi berkas) · 3 Nurul, Admin Online (Balas chat secepat kilat) · 4 Jibri, Front Office (Senyum pertama di Ruma) · 5 Alya, Admin Rekam Medis (Teliti sampai titik koma) · 6 Uswah, Admin Rekam Medis (Si paling cek ulang) · 7 Lisa, Perawat (Cekatan tapi tetap kalem) · 8 drg. Ainun, Dokter Gigi (Jelasin dulu, baru kerja) · 9 drg. Akbar, Dokter Gigi (Tenang walau gigi bungsu) · 10 Saldi, Perawat (Sigap tanpa disuruh) · 11 Baptu, Helper (Ruangan selalu siap).
Staf pemandu (ada di semua klip) belum bernama.

## Render v1 (27 Nov 2026), 39,6 dtk
`scripts/build_gw.py` (klip hidup 1,5 dtk + foto beku 1,6 dtk per orang, hook 2,5 dtk, penutup 3 dtk) → `scripts/shot.js` + `scripts/ov.html` (latar blur, foto miring berbingkai putih "jepret", kartu hijau meluncur, julukan orange pop, nomor n/11) → `scripts/mix_gw.py` (suara lokasi + suara ruangan Ruma m0700 + klik kamera + pop; tanpa musik karena belum ada musik berlisensi). Loudness −17,2 LUFS, puncak −2,3 dB.
Pelajaran teknis: video yang banyak heningnya tidak naik dengan loudnorm satu lintasan (berhenti di −21/−25 LUFS); pakai ukur → `volume` + `alimiter` dengan **`level=0`** (bawaan alimiter menaikkan keluaran ke 0 dBFS dan membuat puncak lewat 0).

## Cover (27 Nov 2026)
`scripts/cover.html`: kolase 5 polaroid miring (Jibri, drg. Ainun, drg. Akbar, Hardi, Saldi) + judul blok hijau/orange + label "11 orang di balik Ruma"; tanpa logo. Hanya staf, tanpa pasien.

## Revisi v2 (27 Nov 2026): suara bocor
Pak Dir: "ada suara yang bocor di awal dan akhir video". Penyebab: suara asli klip (klip parkir e101547 di awal −11 dB, klip m0019 di akhir −16 dB) ikut terangkat penguatan +13 dB. Perbaikan: suara asli semua klip **dimatikan** (`mix_gw.py` `[0:a]volume=0`), hanya suara ruangan + klik kamera + pop. Gambar/teks tidak diubah. Hasil −23,3 LUFS, rata (tanpa lonjakan), VAD tanpa ucapan. Musik ditambahkan Pak Dir saat unggah.
Pelajaran: sebelum menaikkan volume keseluruhan, ukur RMS per detik dan cari lonjakan; suara lokasi klip HP/DJI tanpa ucapan yang dipakai = matikan atau ratakan, jangan dinaikkan.

## Revisi v3 (27 Nov 2026)
Pak Dir: "mute semua dulu suaranya" (masih terdengar suara sumbang) + "tambah Kak di depan nama kecuali Baptu; drg tetap drg". v3: audio **hening total** (anullsrc, tanpa suara ruangan/SFX), nama staf jadi "Kak …" (Hardi, Dian, Nurul, Jibri, Alya, Uswah, Lisa, Saldi), Baptu tanpa "Kak", drg. Ainun/drg. Akbar tetap. Suara latar ditambahkan Pak Dir saat unggah (pustaka musik komersial TikTok/Meta).

## Contoh musik latar (27 Nov 2026)
Pak Dir minta dengar contoh suara latar. Dibuat 3 musik orisinal instrumental di ElevenLabs Music (eleven_music_v2, 40 dtk, ±1.007 kredit/musik, flow `Ryw0ZxUpSJxKXqEnCvZL`): 1 ukulele ceria 110 BPM · 2 siulan + tepuk tangan 115 BPM · 3 lo-fi pop ringan 100 BPM. Semua dicek tanpa vokal (VAD kosong). Dipasang ke v3 dengan `scripts/pasang_musik.py` (fade-in 0,3, fade-out 1,5, −16 LUFS). Menunggu pilihan Pak Dir.
