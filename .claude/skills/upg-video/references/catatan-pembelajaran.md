# Catatan Pembelajaran UPG Video

**Versi skill: 2.8 (15 Nov 2026)**. Naikkan nomor versi ini setiap kali skill diperbarui. Isi tabel riwayat versi di bagian paling bawah.

Baca file ini di awal setiap proyek. Isinya keputusan yang sudah disetujui Dir dan fakta teknis yang sudah terbukti, supaya tidak ditanyakan ulang.

**Aturan mengisi file ini:**
- Hanya catat keputusan yang **disetujui Dir** atau fakta teknis yang **terbukti** di proyek nyata.
- Tulis sumbernya (nama proyek dan tanggal).
- Perubahan pada aturan inti (gaya visual, alur ACC, brand) harus ditanyakan ke Dir dulu sebelum ditulis di sini atau di `SKILL.md`.

---

## Keputusan Dir (berlaku untuk proyek berikutnya)

| Topik | Keputusan | Sumber |
|---|---|---|
| Suara narasi | **ElevenLabs "Denas – High class catchy storyteller"**, voice_id `arwfiAiEfIHHZCwcYYx2` (pria, bahasa Indonesia). Dipilih Dir lewat link | Happy Hour Scaling, 15 Nov 2026 |
| Model TTS | `eleven_v4` | idem |
| Serial TOFU (format acuan) | **Misi Anak Rantau, 3D penuh layar**, suara per kalimat beremosi, aturan cerita di `serial-3d.md` | Dir, Eps 1 V4 "sudah ok sihh mantab mi" (15 Nov 2026) |
| Bahasa serial | Ijal sopan ke Dinda ("Kak", bukan "gue"); Dinda "Ijal"; **Paman maks. 1 partikel Makassar per kalimat**; tokoh hadir hanya bila logis; dialog harus sebab-akibat | Koreksi Dir, Eps 1–2 (15 Nov 2026) |
| Versi iklan Eps 1 | Tidak dibuat dulu ("gak usah versi iklannya, mending lanjut produksi eps 2") | Dir, 15 Nov 2026 |
| Suara serial TOFU "Misi Anak Rantau" (draf) | **Dinda = Zulsyifah** `QuLloIKxiP3i9uFXzfgD` (dipilih Dir). Bahasa **Indonesia baku/santai**, logat Makassar tidak perlu kental; warna lokal cukup lewat sedikit kata (iye, ji, mi). Ijal = Satria `SCDJ1Fy4al0KS1awS6H9` (usulan), Paman = Macazzart Makassar Natural `hGKBtk3J6UEQtxLtsVRC` (usulan), narator = Denas. Konsep musim belum ACC | Dir, 15 Nov 2026 |
| Desain karakter | Mulut berupa garis senyum sederhana, hidung berupa garis kecil, **tanpa mata**. Gaya flat. Ilustrasi gigi tanpa wajah | Rancangan V2 (ACC) |
| Pelafalan "UPG" | **Ditulis dan dibaca "UPG"** apa adanya, bukan "U-Pe-Ge". (V2 awalnya memakai "U-Pe-Ge", lalu dikoreksi Dir.) | Dir, 15 Nov 2026 |
| Palet & font | `#FA7209`, `#F8C000`, `#CF6515`, teks `#2A2A2A`, latar `#FFF7EF` + Nunito. Disetujui untuk proyek 1. **Belum dikonfirmasi sebagai identitas brand resmi** | Rancangan V2 (ACC) |
| Tempat kerja | Chat biasa: diskusi, rancangan, ACC, narasi. **Render video selalu di Claude Code** | Dir, 15 Nov 2026 |
| Satu skill dua jalur | Skill digabung jadi **UPG Video**: jalur MOTION dan EDIT REKAMAN | Dir, 15 Nov 2026 |
| Musik di video rekaman | **Boleh**, hanya file dari Dir dengan lisensi jelas | Dir, 15 Nov 2026 |
| Aturan "tanpa mata" | Hanya untuk animasi atau ilustrasi. Orang asli di rekaman tampil apa adanya | Dir, 15 Nov 2026 |
| Tempat kerja video | Rekomendasi: semua di Claude Code. Repo khusus video menunggu dibuat Dir | 15 Nov 2026 |
| Cara kerja diskusi | **Diskusi dan draf langsung di chat**, tanpa file dokumen per revisi. Kata kunci produksi: **"gas render"** setelah draf lengkap ditampilkan | Dir, 15 Nov 2026 |
| Tampilan logo | **Tanpa kotak putih, menyatu dengan latar.** Logo transparan untuk latar krem, logo putih untuk latar oranye (`brand.md`) | Dir, 15 Nov 2026 |
| Alur papan gambar | Naskah oke → papan gambar 6–8 frame → revisi → **"gas render"** → narasi + video final (usulan Dir) | Dir, 15 Nov 2026 |
| Footage asli | Drive = perpustakaan footage (`pustaka-footage.md`). Cek dulu setiap proyek, unduh hanya yang dipilih. Video gabungan motion + footage disetujui | Dir, 15 Nov 2026 |
| Nilai jual klinik | Snack, minuman, dan es krim gratis; area bermain anak; pojok baca. Masih berlaku dan boleh disebut | Dir, 15 Nov 2026 |
| Konten keluarga tanpa footage anak | Pakai **karakter animasi ibu + anak (tanpa mata)** + footage fasilitas kosong. UPG melayani tambal gigi **dewasa dan anak** | Dir, 15 Nov 2026 |
| Harga berupa kisaran | Tampilkan hanya **harga mulai** dengan bahasa iklan ("mulai Rp250 rb-an") + teks kecil "Harga tergantung kondisi gigi". **Batas atas tidak ditampilkan**, dijelaskan admin | Dir, 15 Nov 2026 |
| Komposisi konten promo | ±60% edukasi di depan, ±40% promo. Harga muncul setelah penjelasan | Happy Hour Scaling |
| Promo dengan syarat | Tulis "S&K berlaku" kecil di kartu promo. Admin harus punya jawaban baku untuk S&K | Happy Hour Scaling |

## Data promo terkonfirmasi (cek ulang sebelum dipakai lagi)

- Happy Hour scaling **Rp200.000**, Senin–Jumat **10.00–14.00**, **wajib booking**, ada S&K, periode tidak ditampilkan (Dir, 15 Nov 2026).
- Jangan anggap promo ini masih berlaku di proyek berikutnya. Konfirmasi dulu ke Dir.

## Fakta teknis yang terbukti

- **Tempo Denas: ±2,6 kata/detik** (111 kata = 42,8 detik). Pakai angka ini untuk estimasi durasi, bukan 2,3.
- **Jalur produksi yang berhasil:**
  1. Naskah → `creative_generate_speech` (konektor ElevenLabs) → unduh MP3 dari `elevenlabsusercontent.com`. Host ini wajib ada di allowlist environment.
  2. Normalisasi audio: `loudnorm=I=-14:TP=-1.5:LRA=11`, lalu `apad` hingga durasi video.
  3. Sinkronisasi: `silencedetect` (noise −35 dB, d 0,12) → cocokkan jeda dengan kalimat → isi `TL.cue` di `src/index.html`.
  4. Render: `node src/render.js stills` (cek frame), lalu `node src/render.js video`. ±1 menit untuk 46 detik.
- **Antrean akun gratis ElevenLabs sering penuh** ("Free generations are busy"). Generasi atau transkripsi bisa gagal tanpa memotong kredit. Jangan langsung mengulang; tunggu sebentar.
- **Transkripsi per kata** (`creative_transcribe_audio`) lebih presisi untuk sinkronisasi daripada deteksi jeda. Coba itu dulu kalau antreannya kosong.
- **Hasil QA layout proyek 1:**
  - Harga 9 karakter muat di kotak 760 px dengan font 128 px.
  - Judul 2 kata besar perlu `white-space:nowrap` dan font ≤112 px.
  - Teks pendamping panjang sebaiknya ≤44 px.
- Claude **tidak bisa mendengar audio**. Pelafalan dan rasa tempo selalu minta dicek Dir.
- **Dari skill `shortform-edit` (pelajaran teknis, diadopsi):**
  - Teks oranye yang tipis sulit dibaca. Teks oranye `#FA7209` harus tebal (≥800) dan besar. Teks kecil pakai `#2A2A2A`.
  - Kata atau angka yang ditekankan harus tampil minimal ±0,4 dtk sebelum berganti.
  - True peak audio maksimal −1 dBTP, dan proyek 1 lolos di −4,3. Cek dengan `scripts/verify_video.py`.
  - Jangan menghapus atau memproses ulang file render final. Simpan setiap versi.
  - **Alternatif transkripsi lokal** (whisper.cpp) bisa dipakai kalau transkripsi ElevenLabs penuh. Syaratnya environment mengizinkan unduhan model dari GitHub/HuggingFace, dan ini **belum diizinkan**. Usulkan ke Dir hanya kalau benar-benar dibutuhkan.

- **Jalur gabungan motion + footage sudah terbukti (V6):**
  - `build_base.py` menyusun jalur footage, dengan bagian hitam saat adegan motion.
  - Overlay HTML dirender sebagai PNG transparan (`omitBackground`), lalu ditumpuk dengan ffmpeg `overlay`.
  - Contoh: `upg-video-projects/happy-hour-scaling/src-v6/`. Render 45 dtk butuh ±3 menit.
- **Sinkronisasi terbaik:** pakai ElevenLabs Scribe (`creative_transcribe_audio`) untuk waktu per kata. Dengan akun berbayar, transkripsi langsung jalan, gratis kredit, dan akurat. "UPG" ditranskrip sebagai "UPG".
- **Tempo Denas di V6:** 109 kata = 42,4 dtk (±2,6 kata/dtk). **Proyek behel:** 125 kata = 50,8 dtk (±2,5 kata/dtk). Untuk estimasi aman, pakai ±2,45 kata/dtk.

- **Koreksi Dir (V6):** logo kecil di pojok kiri atas (x80, y250, lebar 120) **menimpa kartu nomor 1** di adegan 3 kartu. Untuk video berikutnya:
  - Konten dimulai **di bawah y 420**, atau
  - logo kecil disembunyikan di adegan yang memakai area pojok atas.
  - **Selalu cek tabrakan logo dengan konten di papan gambar/stills.**

- **Loudness dengan ekor sunyi panjang (Cerita Rina):** `loudnorm` lalu `apad` sampai durasi video (end card 3,5 dtk sunyi) menurunkan loudness terintegrasi jadi −15,6 LUFS (gagal). Solusi: ukur ulang hasil akhir, lalu tambah `volume=+X dB` dan remux audio saja (`-c:v copy`), tanpa render ulang. Untuk naskah ±53 dtk + end card, tambahan ±1,6 dB sudah cukup.
- **Format cerita/MOFU:** tokoh ilustrasi (tanpa mata) + label kecil "Ilustrasi" di kanan atas, footage asli untuk suasana dan dokter. Tempo Denas: 128 kata = 53,4 dtk (±2,4 kata/dtk).
- **Alur cerita serial (koreksi Dir, Eps 1):** jangan potong adegan di kalimat yang belum dijawab; beri reaksi 0,8–1,5 dtk; setiap pindah adegan harus beralasan (kartu waktu, tokoh berjalan, narator masuk karena ada pertanyaan); alur maju; logika waktu harus konsisten (mis. jangan "janji semalam" lalu "sudah 3 hari berdarah"); tiap adegan punya fungsi (pola "3 tokoh, 3 mitos").
- **Suara natural (koreksi Dir):** buat **per baris** dengan tag emosi v4 ([sighs], [chuckles], [whispers], [panicked]…), bukan satu take per tokoh. Jeda bervariasi. Durasi hasil akting ±20–25% lebih panjang dari perkiraan kata/detik.
- **Gaya visual serial = 3D penuh layar (pilihan Dir):** three.js r149 di Chromium headless (`--use-gl=swiftshader`), `src3d/dunia.js` (tokoh tanpa mata, mulut & pose bisa di-toggle, ruangan, dunia mulut) + `src3d/film.html` (shot list dari `timing.js`). Render ±0,4 dtk/frame → video 150 dtk ±30 menit (latar belakang). Aset tokoh/ruangan dipakai ulang untuk episode berikutnya.
- **Warna three.js:** wajib `THREE.ColorManagement.legacyMode=false` + `outputEncoding=sRGBEncoding`, kalau tidak warna pudar (oranye jadi kuning).
- **Dialog banyak suara (Misi Anak Rantau Eps 1):** 1 take per tokoh (semua baris tokoh itu dipisah baris kosong) → Scribe per take → dipotong per baris dengan batas waktu kata → disusun ulang dengan jeda (`src/build_audio.py`, tulis `work/timing.json`). Hemat: 4 generasi, bukan 22. Hati-hati: jeda antarparagraf narator kadang hanya ±0,05 dtk, jadi potong di tengah celah kata.
- **Gaya 2.5D isometrik (HTML/SVG):** fungsi `iso(x,y,z)`, `room()`, `box()`, `wallL/wallR()`; tokoh flat diletakkan di titik lantai. Cukup untuk serial; 3D sungguhan belum diuji.
- **Bentrok kelas CSS:** `_style.css` sudah punya `.card` (tinggi 270, flex). Pakai nama lain (mis. `.kcard`) untuk kartu baru.
- **Subtitle dari waktu kata Scribe langsung** (bukan dibagi rata per kalimat): maksimal 4 kata per grup, dipotong di akhir kalimat. Hasilnya lebih pas dengan suara.

## Risiko dan catatan bisnis

- **Lisensi ElevenLabs:** sejak 15 Nov 2026 akun Dir **paket Creator (berbayar)**, 131.000 karakter/bulan, lisensi komersial. Narasi yang dibuat sejak itu aman untuk iklan. (Sebelumnya: paket gratis.) Paket gratis setahu Claude tidak memberi lisensi komersial. Ingatkan Dir untuk upgrade minimal ke paket Starter sebelum video promo tayang, dan cek ketentuan resminya.
- Cek aturan iklan potongan harga untuk fasilitas kesehatan (Kemenkes/PDGI) sebelum tayang.

## Riwayat proyek

| Proyek | Versi ACC | Hasil | Catatan |
|---|---|---|---|
| `pov-nur-fo-hertasning` | **V2 ("ok", 20 Nov 2026)** — MP4 56,8 dtk, LULUS. V1→V2: potongan Nur menoleh ke kamera lalu tertawa (0319) dinilai Dir "kurang natural" → diganti 0343. Pelajaran: pilih take yang tidak sadar kamera untuk POV. V3: audit antislop 001 (10 temuan), Dir "Gas" untuk 1–5 dan 8: judul montase tanpa klaim angka, coretan sesuai ucapan & kontras, label jendela digelapkan, emoji hiasan dibuang, stiker montase dibuang | POV Front Office Nur, Gaya 3, ±57 dtk dari 15 potongan (40 klip Drive) | Keputusan Dir: cabang **Hertasning**, nama "Nur · Front Office" OK, "highlight terus ucapan terima kasihnya" → kata terima kasih disorot + penghitung 7× + montase |
| `edukasi-cabut-firdha` | **V4 ("gas render versi utama aja", 20 Nov 2026)** — MP4 73,6 dtk, LULUS verifikasi | Reels edukasi ±83 dtk dari 10 take drg. Firdha (54 klip di Drive) | Proyek pertama jalur EDUKASI DOKTER. Keputusan Dir: lokasi bebas "asal orang singgah nonton", organik, "drg. Firdha aja", backsound "gas buatin" (ElevenLabs). Papan V1→V2: name tag cukup "drg. Firdha" (tanpa UPG Dental Care); stiker 😰 di samping dokter tersenyum diganti 💡 "tips" (emoji harus cocok ekspresi). V3 audit: burst di wajah, emoji 🗣️, label ilustrasi, nocap, zoom 1,3. V4: dipadatkan 83→73,5 dtk atas saran (bagian berulang dibuang), caption gelap di kartu. True peak −0,89 → loudnorm TP −2 (render_edukasi.py diperbaiki) |
| `misi-anak-rantau-eps2` | V1 ("gas rendern", 15 Nov 2026) | MP4 156 dtk, 3D, 25 baris suara + SFX (gerobak, sore, jangkrik) | Topik frekuensi gula; mitos: sedikit-sedikit (hoaks HP), gula alami, asal sikat malam. Kalender 4/14 |
| `misi-anak-rantau-eps1` | **V4 ("Gas render.", 15 Nov 2026) — disetujui Dir: "sudah ok sihh mantab mi"** | MP4 150 dtk, **3D three.js**, 28 baris suara beremosi, naskah "3 tokoh, 3 mitos" | V1 (2.5D, 107 dtk) ditolak: kaku & lompat-lompat. **V4 = format acuan untuk Eps 2–6** |
| `cerita-rina` | V3 ("Gas render", 15 Nov 2026) | MP4 57,1 dtk, MOFU cerita, gabungan animasi Rina + footage suasana/dokter | Fakta: edukasi dulu, biaya dijelaskan sebelum tindakan, boleh menolak, admin menemani |
| `tambal-keluarga` | V3 ("Gas render", 15 Nov 2026) | MP4 43,8 dtk, gabungan, karakter keluarga animasi (tanpa footage anak) | Harga "mulai Rp250 rb-an" (kisaran sampai 700 rb dijelaskan admin, tidak ditampilkan — keputusan Dir) |
| `behel-cicilan` | V3 ("Gas render", 15 Nov 2026) | MP4 53,9 dtk, gabungan motion + footage, narasi Creator | Data harga & cicilan di `rancangan-V3.md` |
| `happy-hour-scaling` | V2 ("Acc", 15 Nov 2026) | MP4 46 detik + narasi Denas | Revisi Dir: "UPG" harus dibaca UPG. `naskah-tts.txt` sudah diperbarui, narasi dan render ulang tertunda (antrean ElevenLabs penuh). Untuk iklan Meta: audio wajib dibuat ulang dengan paket ElevenLabs berbayar sebelum tayang |

## Riwayat versi skill

| Versi | Tanggal | Perubahan |
|---|---|---|
| 1.0 | 15 Nov 2026 | Skill awal dari brief |
| 1.1 | 15 Nov 2026 | Catatan pembelajaran proyek 1 (suara Denas, tempo, karakter, jalur produksi). Mode kerja untuk chat biasa dan Claude Code. Template render ikut dalam skill |
| 1.2 | 15 Nov 2026 | Keputusan Dir: render video **selalu di Claude Code**. Chat biasa untuk diskusi, rancangan, ACC, dan narasi |
| 1.3 | 15 Nov 2026 | Diadopsi dari skill `reels-cepat` (disetujui Dir): 3 sudut + skor di tahap A, naskah voiceover bertanda jeda, caption per platform + teks iklan Meta yang aman. Gaya "lu/gua" dan CTA opsional **tidak** diambil |
| 1.4 | 15 Nov 2026 | Dari skill `shortform-edit`: skrip `verify_video.py` (cek akhir video), pelajaran keterbacaan teks oranye, durasi tampil penekanan, true peak, dan larangan menimpa versi render |
| 2.0 | 15 Nov 2026 | Ganti nama jadi **upg-video**. Tambah jalur EDIT REKAMAN (Remotion, diadaptasi dari `shortform-edit`): setup, prep footage, template caption/promo/logo/end card/musik, render dengan gerbang ACC. Sudah diuji dengan rekaman uji buatan |
| 2.1 | 15 Nov 2026 | Keputusan Dir: "UPG" ditulis dan dibaca **UPG**, bukan "U-Pe-Ge". Narasi Happy Hour perlu dibuat ulang (tertunda: antrean ElevenLabs gratis penuh) |
| 2.2 | 15 Nov 2026 | Keputusan Dir: draf di chat (tanpa kirim dokumen). "Gas render" setelah draf lengkap = ACC produksi |
| 2.3 | 15 Nov 2026 | Logo transparan + logo putih, aturan logo tanpa kotak putih |
| 2.4 | 15 Nov 2026 | Alur papan gambar, pustaka footage Drive, jalur gabungan motion + footage, nilai jual fasilitas, logo resmi PNG |
| 2.5 | 15 Nov 2026 | ElevenLabs Creator aktif, alur sinkronisasi pakai Scribe, jalur gabungan terbukti (V6 dengan suara) |
| 2.6 | 15 Nov 2026 | Aturan: logo kecil tidak boleh menimpa konten (koreksi Dir di V6) |
| 2.7 | 15 Nov 2026 | Proyek behel selesai. Estimasi tempo diperbarui. Renderer: gerbang ACC hanya untuk video final, stills papan gambar boleh |
| 2.8 | 15 Nov 2026 | Proyek tambal-keluarga. Aturan harga kisaran dan konten keluarga tanpa footage anak |
| 2.9 | 15 Nov 2026 | Proyek cerita-rina (MOFU). Format cerita + label Ilustrasi, subtitle dari waktu kata Scribe, perbaikan loudness ekor sunyi |
| 3.0 | 15 Nov 2026 | Serial TOFU Misi Anak Rantau Eps 1: dialog multi-suara, gaya 2.5D isometrik |
| 3.1 | 15 Nov 2026 | Serial: aturan alur cerita, suara per baris + emosi, pipeline 3D three.js |
| 3.2 | 15 Nov 2026 | Eps 1 V4 disetujui Dir; format serial 3D + suara per baris jadi acuan |
| 3.3 | 17 Nov 2026 | Jalur SERIAL CERITA 3D masuk SKILL.md; `references/serial-3d.md` (bible + pipeline); `templates/serial-3d/`; produksi.md diperbarui (Creator, 3D, logo); Eps 2 selesai |
| 3.4 | 20 Nov 2026 | Jalur ke-4 **EDUKASI DOKTER (Gaya 1)** atas permintaan Dir ("jadikan skill untuk konten khusus edukasi UPG"): template Remotion (caption per kata, stiker, pill coret, zoom wajah, kartu chat/checklist dengan polaroid, SFX otomatis), `edit.json` berjangkar kata, transkrip Whisper lokal, deteksi wajah. Keputusan Dir: backsound boleh dibuat dengan ElevenLabs Music |
| 3.5 | 20 Nov 2026 | Gaya 3 (retro) + jalur POV staf (proyek POV Nur FO Hertasning V3): caption `say` manual, `blur` privasi, coretan, penghitung, kartu berlabel. Filter **antislop** dipakai (mode during; audit = after); hasil audit 001 jadi bawaan template: tanpa pola titik, tanpa lampu jendela, bayangan minim, aksen #7A3608 turunan UPG, cek kontras/klaim/emoji di daftar cek |
| 3.6 | 20 Nov 2026 | Canva "Panduan Visual Terpadu" diaudit (antislop after, 13 temuan) dan diperbaiki atas perintah Dir ("perbaiki semua"), lalu **dikunci** ke `references/panduan-visual-terpadu.md` untuk UPG, Ruma, GrowWith. Area aman bawah jadi **400 px** (y 250–1520). Keputusan Dir: Canva ikut skill; POV staf UPG tayang di akun UPG (Gaya 3). Asumsi yang perlu validasi: font Ruma Neue Montreal + Montserrat |
| 3.7 | 20 Nov 2026 | Keputusan Dir: repo dipisah. `upg-video` = UPG + GrowWith, `ruma-video` = Ruma + Dalam Gigi. Skill bersama (`produksi-video-klinik`, `motion-klinik-gigi`, `panduan-visual-terpadu`, `antislop` x3) disimpan utuh di kedua repo dan dijaga identik oleh `.claude/scripts/skill-bersama.sh` (cek/kirim/tarik/zip); hook SessionStart hanya mengecek. Panduan Visual Terpadu jadi skill bersama |
| 3.8 | 23 Nov 2026 | Koreksi warna otomatis (permintaan Dir: footage drg. Naya terlihat gelap): `produksi-video-klinik/scripts/warna/koreksi_warna.py` (skill bersama) + `prep_klip.py --warna upg`. Terbukti di footage organik 23 Nov: klip gelap 30 → 65, klip normal 101 → 120, kulit tetap natural. Skill GitHub pihak ketiga dicek, tidak dipasang |
| 3.9 | 23 Nov 2026 | Keputusan Dir: (1) alat rontgen dan layar foto rontgen **tidak boleh tampil** sampai izin jelas; (2) wajah pasien yang terlihat jelas tetap disamarkan walau sudah izin, dengan gaya UPG yang beda dari Ruma (usulan: mosaik kotak, menunggu lihat papan); (3) footage drg. Naya 23 Nov = PSA, jadi 3 konten organik pertama: Di Balik Layar "2 orang di samping kamu", edukasi PSA, kenapa PSA bolak-balik |
| 3.10 | 23 Nov 2026 | Fakta dari Dir: **UPG memakai 1 asisten per tindakan**; footage dengan 2 asisten hanya kebetulan. Jangan pernah membuat konten/klaim "2 asisten" atau "2 orang di samping kamu". Konten organik drg. Naya: Hertasning, durasi 45–60 dtk; Video A (edukasi PSA, gabungan R1+R3) di-OK Dir; R2 "2 orang" dibatalkan |
| 3.11 | 23 Nov 2026 | Penutup standar organik UPG di template edukasi (`EndCard`): oranye menyapu, logo putih, "Klinik Gigi UPG Dental", `end.line1` + `end.cta`; tanpa wajah dokter (banyak dokter) dan tanpa nama cabang di penutup (keputusan Dir). `setup_edukasi.py` menyalin `logo-upg-putih.png`. Pelajaran teknis: file di `public/` Remotion **tidak boleh symlink** (Audio gagal dimuat); salin filenya |
| 3.12 | 23 Nov 2026 | Keputusan Dir: **logo UPG versi mendatar** (ikon kiri, tulisan kanan) jadi aset resmi kedua untuk video (logo pojok + penutup); tulisan "Klinik Gigi UPG Dental" di penutup **dihapus** (logo sudah cukup). Template edukasi diperbarui, `setup_edukasi.py` menyalin `logo-upg-mendatar*.png`. Video yang sudah jadi (Firdha V4, POV Nur V3, dll.) **tidak** di-render ulang (keputusan Dir); berlaku mulai Video A drg. Naya |
| 3.13 | 23 Nov 2026 | Koreksi klinis drg. Naya (Video A): sinar biru = tambal setelah PSA; PSA **tidak selalu** bolak-balik (ada kasus satu kunjungan), jangan ditulis seolah selalu; tambal permanen setelah saluran akar **bersih dan kering**, bukan "setelah tidak ada keluhan". Pelajaran: kalimat edukasi klinis selalu dicek dokter sebelum papan final |
| 3.14 | 23 Nov 2026 | Keputusan Dir: kalimat penutup **tetap** untuk semua konten organik UPG: "Jangan tunggu sakit untuk ke dokter gigi." (bawaan `build_timeline.py`). Template: volume suara per potongan (`cuts[].vol`) untuk memelankan suara alat |
| 3.15 | 23 Nov 2026 | Produksi Video A drg. Naya: mosaik per frame (`produksi-video-klinik/scripts/privasi/samarkan.py`, gaya UPG), ucapan asli dipasang sebagai SFX di atas gambar pengganti (klip asal ada laptop rontgen), suara alat vol 0,25, backsound ElevenLabs Music baru. Whisper small berhalusinasi "terima kasih kerana menonton" pada klip tanpa ucapan: pakai medium + VAD untuk mencari ucapan, transkrip proyek dikosongkan  Hasil: `naya-psa-videoA/out/naya-psa-videoA-V2.mp4` 59 dtk LULUS (−14,3 LUFS, TP −1,2); `render_edukasi.py final` kini loudnorm dua tahap (satu tahap meleset ke −16,7) |
| 3.16 | 23 Nov 2026 | Keputusan Dir: **konten organik UPG tanpa backsound musik**; ganti bunyi perpindahan ("kling", whoosh). Audit 2x setelah render jadi standar. Video A V4 (59 dtk, LULUS, −14,5 LUFS): tanpa kilatan putih, teks penjelasan utuh (`kind: teks`), suara ruangan diratakan. Template: `kind: teks`, `sfx_potongan`, `flash` bawaan false |
| 3.17 | 23 Nov 2026 | Skill bersama baru **`analisis-footage-konten`** (permintaan Dir: skill yang melihat footage lalu cepat menyimpulkan jadi konten apa). Skill GitHub dicek (video-content-strategist, ECC video-editing, highlight-reel-scripter): tidak ada yang menganalisis footage; bagian struktur pendek diadaptasi (MIT). `inventaris.py`: jam rekam (WITA), terang, ucapan tersaring halusinasi + tanda ragu, lembar cuplikan. Koreksi: "Oke, manis"/"Bagus" ternyata salah tangkap Whisper (tidak terpakai di Video A) |
| 3.18 | 23 Nov 2026 | Fakta klinis dari Dir/drg. Naya (PSA): **sinar biru dipakai beberapa kali** untuk mengeraskan tambalan komposit **berlapis**; alat putih mirip scaler = **endo activator** (bagian bilas saluran); alat seperti jarum suntik = **bilas saluran akar**. Pelajaran: label tahapan dicocokkan dengan jam rekam + konfirmasi dokter, jangan dari tebakan bentuk alat. Video A diperbaiki (V5): tahap 1 pakai klip 16.42–16.43, endo activator pindah ke tahap 2 |
| 3.19 | 23 Nov 2026 | Video B drg. Naya "Berapa lama sih perawatan saraf?" V1 (49,6 dtk, LULUS, −14,3 LUFS): montase urut jam rekam asli, badge jam (`kind: jam`, kanan atas, "tik" click), tanpa musik, mosaik per klip, logo pojok dimatikan (bertabrakan dengan wajah dokter di close-up; badge jam sudah di atas). Template: logo pojok tidak lagi disembunyikan oleh `teks`/`jam` (pakai `"logo": false` bila menimpa wajah). Video A V5: tahap 1 klip 16.42–16.43, endo activator di tahap 2 |
| 3.20 | 23 Nov 2026 | Permintaan Dir: tidak boleh ada kotak tulisan bertumpuk → skrip `cek_tumpang.py` (wajib sebelum render). Video A: name tag menimpa kutipan → kutipan ke y 1210; teks "Alat ini namanya endo activator" dihapus atas permintaan Dir, diganti "Saluran akar dibersihkan dulu, sebelum ditambal" (V6). Video B: AMAN |
| 3.21 | 23 Nov 2026 | Testimoni pasien PSA "Kak Nabil" (izin tertulis ada, konfirmasi Dir; nama tampil "Kak Nabil"). Model Video C: wawancara + pertanyaan pewawancara diganti pill, selingan footage perawatan dengan ucapan pasien lewat SFX, MOFU "Tanya lewat DM". Pasien di testimoni = pasien di footage perawatan (dicocokkan kemeja + jam rekam). Benda oranye di tepi lokasi wawancara → perbesar 8% |
| 3.22 | 23 Nov 2026 | Koreksi Dir: suara Video C terputus. Penyebab: (1) template memotong SFX di 3 dtk → ucapan pasien 5,7 dtk terpotong; kini `build_timeline.py` mengisi `len` = durasi file; (2) titik potong di tengah kata → pilih titik potong dari profil energi 20 ms (jeda <55 dB), bukan cap waktu Whisper; (3) fade audio 3 frame di setiap sambungan (template). Audit audio wajib: bandingkan suara render vs sumber per potongan |
| 3.23 | 23 Nov 2026 | Koreksi Dir: bunyi perpindahan/ding menutup suara pasien. `build_timeline.py`: SFX otomatis tidak boleh menimpa ucapan (`sfx_hindari_ucapan`, bawaan aktif): dipindah ke jeda ≤0,6 dtk sebelumnya + vol ≤0,3, atau dibuang. Untuk video orang bicara, efek suara harus jauh lebih sedikit daripada video b-roll |
| 3.24 | 24 Nov 2026 | Video scaling drg. Izza (Hertasning): nama pasien di suara dipotong, kertas di meja dimosaik. Pelajaran: keyframe mosaik 3 titik per potongan tidak cukup bila pasien bergerak → cek klip pasien tiap 0,5 dtk dan tambah keyframe sebelum render final |
| 3.25 | 24 Nov 2026 | Keputusan Dir: **mosaik pasien hanya di mata, gigi/mulut terlihat** (edukatif). Alat `samarkan_mata.py` (skill bersama 12h, deteksi otomatis). Berlaku untuk konten organik berikutnya |
| 3.26 | 24 Nov 2026 | `cek_tumpang.py` kini juga memeriksa teks ucapan (caption): caption terakhir bisa tertinggal ±0,4 dtk di potongan berikutnya → kotak `teks` di potongan baru mulai `@0.6`. Video Izza-B (tambalan) V2 |
| 3.27 | 24 Nov 2026 | Dir: jumlah video realistis sesuai bahan (2 ya 2, 3 ya 3). Jangan dipaksa sampai informasinya tidak sampai/setengah jadi. Contoh: ide "Habis scaling kok ngilu?" (drg. Izza) dicoret; bahannya hanya ±10 dtk di d145526 yang sudah dipakai Izza-A, tanpa penjelasan sebab dan saran. Aturan masuk skill bersama `analisis-footage-konten` langkah 6. |
| 3.28 | 24 Nov 2026 | Dir: utamakan konten interaksi dokter-pasien dari awal sampai akhir (model Izza-A UPG & Konsultasi Tambal drg. Ainun Ruma) bila ada obrolan yang jelas. Masuk skill bersama `analisis-footage-konten` langkah 8. |
| 3.29 | 25 Nov 2026 | Audit Adhila-A V1: potongan bunyi alat (vol rendah, tanpa `say`) tetap memunculkan caption dari Whisper ("anggap-anggap"). `build_timeline.py` kini menerima `"caption": false` per potongan; pakai untuk semua potongan montase/bunyi alat. Teks `say` dicocokkan ulang ke STT file final (kata yang terpotong di awal klip, mis. "untuk", tidak ditulis). |
