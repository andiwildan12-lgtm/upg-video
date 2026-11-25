---
name: produksi-video-klinik
description: Teknik produksi video iklan dan konten klinik gigi (UPG Dental Care, Ruma Dental, atau brand klinik lain) dari naskah sampai file MP4 jadi. Gunakan saat diminta membuat, merender, mengedit, atau merevisi video: menyusun alur naskah, papan gambar, narasi AI ElevenLabs, animasi 3D explainer, menggabungkan footage klinik, transisi, teks layar, audio, dan ekspor untuk Meta/Instagram/TikTok. Selalu pakai bersama skill brand-nya (misalnya ruma-dental-video) untuk gaya, warna, suara, dan data resmi.
---

# Produksi Video Klinik

Skill ini berisi **cara kerja dan teknik** yang sudah terbukti: iklan bleaching Ruma Dental v2 (di-ACC 16 Nov 2026) dan konten TOFU @dalamgigi #01–#03 (16–17 Nov 2026). Versi skill: **1.3 (17 Nov 2026)**.
**Identitas brand** (warna, logo, suara narator, data harga, aturan khusus) **tidak ada di sini**; ambil dari skill brand:
- Ruma Dental → skill `ruma-dental-video`
- UPG Dental Care → skill di **repo `upg-video`** (bukan di repo ini): `upg-video` (umum), `upg-antang-video` (cabang Antang), `upg-hertasning-video` (cabang Hertasning).

Satu video = satu klinik/cabang; data, WA, logo, dan footage tidak boleh tertukar. Materi UPG tidak disimpan di repo `ruma-video`.

Kalau brand belum jelas, tanyakan dulu konten ini untuk klinik yang mana.

---

## 1. Cara Bekerja dengan Pak Dir

- Panggil **"Pak Dir"**. Bahasa Indonesia yang tegas dan praktis. Jadilah teman diskusi yang **kritis**; audit hasil sendiri sebelum dikirim.
- Data kurang → buat asumsi kerja yang masuk akal, tandai bagian yang perlu divalidasi, jangan banyak bertanya.
- Pak Dir suka hasil cepat ("gas render"). Setelah naskah dan papan gambar di-OK, langsung produksi.
- Kredit ElevenLabs sudah diizinkan untuk produksi. Sebutkan perkiraan kredit yang terpakai di laporan.
- Naskah disimpan di folder skill brand (`references/`), menimpa file yang sama setiap revisi. **Jangan disimpan ke Google Drive.**
- Fokus ke video. Jangan menawarkan hal di luar video (template admin dan sejenisnya) kecuali diminta.

## 2. Gerbang Audit 4 Lapis (3 sebelum render + 1 setelah encode) [WAJIB]

Tujuan: **tidak ada render dua kali dan tidak ada video cacat terkirim.** Render penuh hanya boleh dimulai setelah Pak Dir bilang OK **dan** Audit 1–3 lulus; video hanya boleh dikirim setelah Audit 4 lulus.

Aturan:
- **URUTAN WAJIB, TIDAK BOLEH DILOMPATI:**
  1. Naskah → **OK Pak Dir**
  2. **Papan gambar** (gambar 9:16 per adegan dari frame probe, teks layar, narasi, footage yang dipakai) → kirim → **ACC Pak Dir**
  3. Baru buat suara ElevenLabs + efek suara
  4. Gerbang Audit 3 Lapis
  5. Render penuh
  (Pelajaran iklan tambal v1: papan gambar terlewat dan suara dibuat sebelum naskah OK.)
- **Suara ElevenLabs, efek suara, dan render baru boleh dibuat SETELAH naskah DAN papan gambar di-ACC Pak Dir** (pelajaran iklan tambal: suara terlanjur dibuat lalu naskah berubah).
- Setelah Pak Dir OK, **audit sendiri tanpa memberi saran atau ide baru**. Yang dicari hanya **kesalahan**, lalu langsung diperbaiki. Jangan membuka diskusi ulang.
- Kalau ada temuan yang mengubah isi (fakta medis, data harga, naskah), **tanya Pak Dir dulu**. Selain itu, perbaiki sendiri.
- Kalau naskah diubah saat audit (termasuk menambah CTA, memangkas, atau menjanjikan topik berikutnya), tampilkan tabel **"Sebelum → Sesudah → Alasan"** + narasi final, lalu **tunggu OK Pak Dir sebelum membuat narasi ElevenLabs dan render**. Persetujuan ide/cerita bukan persetujuan naskah final.
- Lapor ringkas: "Audit 1–4: lulus, X hal diperbaiki".
- **Papan gambar wajib dikirim ke Pak Dir sebelum render penuh, termasuk setiap kali visual diubah** (arahan Pak Dir 18 Nov): lembar 20–24 frame probe berlabel waktu + narasi (`output/papan-NN-topik.jpg`). Render penuh hanya setelah Pak Dir OK papan.

**Audit 1: Naskah dan fakta**
- [ ] Fakta medis dan angka benar, atau sudah divalidasi Pak Dir.
- [ ] Data resmi (nama klinik, alamat, WA, harga) persis sama dengan skill brand.
- [ ] Funnel tepat: TOFU tanpa ajakan dan harga; MOFU/BOFU sesuai pola.
- [ ] Aturan iklan kesehatan: tanpa menyiratkan kondisi penonton, tanpa menakut-nakuti, tanpa janji hasil, tanpa kata "gratis".
- [ ] Narasi enak diucapkan, angka ditulis dengan kata, satu generasi mengalir.

**Audit 2: Visual dan papan gambar (pakai frame probe)**
- [ ] Render 6–12 frame probe dari seluruh durasi, lalu lihat lembar kontaknya.
- [ ] Tidak ada objek terpotong, teks menutupi objek penting, atau teks keluar dari area aman.
- [ ] Anti-monoton: kamera berganti tiap 2–4 detik, bentuk objek dikenali, suasana berubah per babak.
- [ ] Logo dan identitas brand benar; tidak ada atribut brand lain.
- [ ] Footage: casting benar (pasien ≠ admin), tanpa data sensitif (password, wajah tanpa izin).
- [ ] **Video orang bicara harus terasa natural (koreksi Pak Dir, behel Spil Harga v1 → v2):**
  - Transisi: crossfade 0,24 dtk di semua potongan (xfade, handle 0,12 dtk per sisi), zoom bergantian 1,00/1,08 antar-kalimat admin + dorong pelan 2%, footage bukti dengan zoom pelan 4%.
  - Bunyi transisi: whoosh pelan di setiap perpindahan ke/dari footage dan kartu; pop saat kartu harga/baris baru/kartu penutup; ting notifikasi saat kotak komentar muncul.
  - Pengganti musik: suara asli ruangan klinik (klip footage tanpa bicara, volume ±0,09, lowpass) sebagai latar terus-menerus + suara asli footage bukti ±0,18. Jangan hening mati.
  - Subtitle **pendek 2–4 kata per potongan**, mengikuti waktu kata (transkripsi), satu kata kunci berlatar Turquoise.
  - Font & warna video Ruma **ikut panduan resmi Canva**: Montserrat (Neue Montreal belum ada filenya), teks Deep Teal #354B49, blok Turquoise #28CDBD, latar putih/Mint White #E8F8F6. Bukan Outfit/krem.
  - **Panduan Canva versi 20 Nov 2026 (`DAHbTZUHi_Q`) untuk video Ruma:** subtitle maks. 2 baris × 5–7 kata; hook di sepertiga atas (0–3 dtk); 5 dtk terakhir logo + 1 ajakan sesuai funnel; cover maks. 6 kata. Gaya teks A (hook tanpa blok + subtitle pill putih) atau B (blok di kata kunci + subtitle putih di atas Deep Teal 30%). Editing: fade halus, slow zoom, **cut bersih**, **SFX/ambience sangat minim**, overlay clean, teks tipis tanpa stroke.
  - **KEPUTUSAN PAK DIR (21 Nov 2026): standar natural di atas (crossfade, zoom bergantian/punch-in, whoosh tiap perpindahan, pop saat teks/stiker muncul, suara ruangan terus-menerus, subtitle 2–4 kata) WAJIB untuk semua video Ruma dari rekaman/footage**, menang atas tulisan Canva "cut bersih, SFX sangat minim". Pelajaran: Tambal Ulang v1 dibuat cut bersih tanpa bunyi → dinilai "kaku, tidak natural, tidak ada suara perpindahan". Jangan pernah menurunkan standar ini tanpa perintah Pak Dir untuk video tertentu.
  - Lapisan teks dirender per frame (`ovseq/%04d.png`), bukan concat gambar diam (pernah terpotong di detik 32). Kartu penutup masuk dengan pudar ±0,3 dtk.
- [ ] **Data pasien di footage** (label film rontgen: nama, tgl lahir; layar monitor; rekam medis) → wajib di-blur per frame. Film rontgen: `scripts/kinetik/filmdet.py` (deteksi lembar film per frame lewat warna hitam-netral HSV, blur 42%×30% pojok kiri atas; pelacakan pola tulisan TIDAK andal karena film berputar/tertutup tangan). Cek ≥6 titik per klip. Pelajaran behel MOFU: film rontgen 4389–4393 memuat nama pasien.
- [ ] **Caption kinetik di atas footage**: pakai gaya label (kotak putih 96%, teks Deep Teal, kata kunci Turquoise), BUKAN teks putih + bayangan (tak terbaca di dinding klinik putih). Potongan 2–4 kata mengikuti waktu kata, masuk dengan pop skala; stiker ikon pop + bunyi pop (`scripts/kinetik/`).
- [ ] **Zona aman iklan Meta 9:16 (Reels/Story)**: semua teks, logo, harga, kotak komentar, kartu penutup, DAN wajah/mulut pembicara di area y 270–1250, x 65–1015 (atas 14% & bawah 35% tertutup UI Meta). Cek dengan frame + kotak merah zona sebelum kirim. Kartu penutup disusun mulai y≈310, selesai ≤1250.
- [ ] **Video orang bicara: subtitle di atas kepala, jangan menutupi wajah** (arahan Pak Dir, behel Spil Harga). Hook "spil/tanya" → kotak "Balas komentar" diam di dekat gestur tunjuk.
- [ ] **Cek seragam/atribut brand lain di footage** (pelajaran behel: seragam bertuliskan UPG di konten Ruma). Solusi yang disetujui Pak Dir: **blur hanya area logo**, dilacak per frame (`scripts/bicara/blurlogo.py`: lacak mikrofon klip hitam → blur elips lembut di kiri-bawahnya). **Jangan pakai pita/gradasi yang menutup bagian bawah video** (dikira video blur). Klip lain yang memperlihatkan logo jelas (mis. resepsionis 4429) tidak dipakai.
- [ ] **Setiap kata kerja di narasi terlihat di gambar pada detik yang sama** (pelajaran Kunjungan Pertama v1: "dokter gigi memeriksa" tanpa adegan pemeriksaan).
- [ ] Tidak ada benda yang Pak Dir minta tidak ditampilkan (contoh: rak sepatu).

**Audit 3: Teknis dan sinkron (terakhir sebelum render penuh)**
- [ ] Kunci waktu adegan dari **timestamp per kata (Scribe)**; subtitle cocok dengan kata yang diucapkan; `words` sudah di cfg.
- [ ] Jumlah frame footage cukup (`max` = jumlah file); server lokal hidup.
- [ ] Durasi total sesuai target (TOFU 50–70 detik, iklan ±50–60); kartu penutup benar.
- [ ] Setiap shot punya gerak pelan (tidak diam ≥1,5 dtk); rentang `blur` untuk gerakan cepat sudah diisi.
- [ ] Cover/thumbnail sudah disiapkan (bagian 9).

**Audit 4: Cek kualitas file jadi (setelah encode, sebelum kirim) [WAJIB SEMUA BRAND]**
- [ ] `scripts/qc.sh video.mp4 <durasi> <detik_kartu>` → hasil **LULUS** (detail bagian 11A). Kalau ada [CEK], perbaiki dulu; jangan kirim video yang belum lulus.
- [ ] Lembar kontak dari **render penuh** (bukan probe) sudah dilihat.

## 2b. Alur Satu Konten

1. **Ide dan funnel.** Pak Dir suka iklan **MOFU/BOFU**: edukasi yang menyatu dengan jualan.
2. **Naskah** dengan rumus 8 ketukan (bagian 3). Jalankan checklist 3a sendiri; kirim ke Pak Dir naskah + hasil audit + maks 4 hal yang perlu divalidasi.
3. **Papan gambar** (HTML artifact): panel 9:16 per adegan, narasi, teks layar, bunyi, transisi, alur produksi.
4. **Tes gaya** 5–9 detik untuk adegan baru.
5. **Narasi ElevenLabs** (bagian 4) → **transkripsi Scribe** (bagian 5).
6. **Gerbang Audit 1–3** (bagian 2), lalu **render penuh di latar** (bagian 6), lembar kontak render penuh, mix, encode, **Audit 4 (`qc.sh`)**, buat cover.
7. **Review Pak Dir → revisi.** Setelah di-ACC, perbarui skill brand: naskah final dan pelajaran baru.

## 3. Rumus Naskah Iklan MOFU/BOFU (8 Ketukan) [WAJIB]

Disusun dari iklan bleaching v2 dan tambal v2 serta koreksi Pak Dir. Tujuan: penonton **berhenti menggulir → paham masalahnya → percaya → chat admin.**
Orang tidak membeli perawatan, mereka membeli **lega**. Skrip menjawab berurutan: *Ini soal saya? → Kalau dibiarkan kenapa? → Ada jalan keluar? → Kenapa di sini, dan langkah pertamanya apa?*

| # | Ketukan | Isi | Contoh (tambal) |
|---|---|---|---|
| 1 | Hook fakta (0–4 dtk) | Fakta mengejutkan / menggugurkan anggapan | "Lubang gigi itu nggak pernah nutup sendiri." |
| 2 | "Itu saya" | Gejala/kebiasaan ringan yang umum | "Awalnya cuma ngilu sedikit… jadi dicuekin." |
| 3 | Yang terjadi di dalam | Edukasi visual 1–2 kalimat | "Di dalam, lubangnya melebar, makin dekat ke saraf." |
| 4 | Dua jalan | Taruhan jelas, nada tenang | "Kalau masih kecil, cukup ditambal. Sampai saraf, bisa sakit berdenyut." |
| 5 | Solusi + brand (+ harga bila ada) | Nama perawatan tegas + nama lengkap klinik **di tengah video** | "Solusinya, perawatan tambal gigi. Di Klinik Gigi Ruma Dental, mulai…" |
| 6 | Alasan percaya | Bukti nyata, bukan pujian | Footage dokter, "dicek dulu", "dikerjakan dokter gigi" |
| 7 | Hasil yang diinginkan | Gambaran hidup sesudahnya, positif | "Es teh pun aman lagi." |
| 8 | Ajakan ringan + pengaman | Langkah terkecil + penurun risiko | "Ada garansi setelah perawatan. Chat admin, cek dulu, ya." |

**6 aturan:**
1. Hook selalu **fakta**, bukan pertanyaan pribadi ("Gigimu berlubang?" ✗).
2. Taruhan nyata, **nada tenang**: tanpa darah, bengkak, nanah, kata "parah".
3. Brand disebut **di tengah**, menyatu dengan solusi.
4. Hilangkan **hambatan terbesar** per layanan:
   - Tambal: "nanti saja" → dua jalan sekarang vs nanti.
   - PSA: takut dicabut/sakit → "nggak selalu harus dicabut", "bius lokal" (bila valid).
   - Crown/veneer: mahal, ragu → "dicek dulu, dijelaskan pilihan dan biayanya".
   - Bungsu/cabut: takut → "dicek dulu", "dikerjakan dokter gigi".
   - Anak: takut trauma → "pengalaman pertama yang menyenangkan".
5. Ajakan = **langkah terkecil** ("cek dulu", "konsultasi dulu").
6. Klaim **hanya yang bisa dibuktikan**. Dilarang: "nyaris nggak kelihatan", "tanpa sakit", "pasti selamat", "permanen", "steril", "terbaik", "dikeraskan dengan sinar", foto sebelum-sesudah. Aman: "sewarna gigi", "dicek dulu", "dikerjakan dokter gigi", "garansi setelah perawatan", "tujuannya…".

**Bahasa:** santai dan dekat ("dicuekin", "cek dulu", "ya"); satu ide per kalimat (±12 kata); angka konkret; benda sehari-hari jadi benang cerita (es teh, kopi). Solusi disebut dengan pola Pak Dir: **"Solusinya, perawatan …"**.

Durasi ±50 detik (±105–115 kata narasi + kartu 3 dtk). Turunan: 15 detik (retarget) dan 4:5 bila diminta.

### 3a. Checklist Naskah — DIJALANKAN SENDIRI, BUKAN DIKIRIM KE PAK DIR [WAJIB]
Pak Dir: *"Itu checklist kau yang checklist sendiri."* Sebelum naskah dikirim, centang sendiri lalu laporkan **hasilnya** (tabel "draf awal → masalah → diganti jadi") dan **hanya hal yang butuh validasi Pak Dir** (maks 4).
- [ ] Hook fakta, terbaca ≤3 detik
- [ ] Ada momen "itu saya"
- [ ] Ada dua jalan / taruhan, nada tenang
- [ ] Solusi tegas + "Klinik Gigi Ruma Dental" (nama lengkap) di tengah
- [ ] Bukti nyata (footage/fakta), bukan pujian
- [ ] Gambaran hasil positif, tanpa janji
- [ ] Ajakan ringan + pengaman yang benar-benar berlaku
- [ ] Tidak ada klaim terlarang; fakta medis yang belum pasti ditandai ⚠️, bukan dicentang
- [ ] Jumlah kata cocok dengan durasi; data resmi (alamat, WA, harga) sesuai skill brand

**Batasan iklan kesehatan (Meta):** jangan menyiratkan tahu kondisi penonton, tanpa foto sebelum-sesudah, tanpa janji hasil tertentu, tanpa close-up klinis mulut asli, hindari kata "gratis" untuk layanan medis. Fakta medis harus benar; Pak Dir (dokter gigi) memvalidasi bila ragu.

## 4. Narasi AI (ElevenLabs)

- Model **eleven_v4**, suara sesuai skill brand.
- **Seluruh narasi dibuat dalam SATU generasi yang mengalir.** Jangan pakai `[long pause]` dan jangan memotong per kalimat lalu menempelkan per adegan. Cara itu terbukti membuat narasi kaku, terlalu banyak jeda, dan perpindahan adegan tidak nyambung (pelajaran iklan v1).
- Tag nada di awal kalimat: `[conversational] [warmly]`, `[cheerfully]` untuk "kabar baiknya", `[warmly]` untuk gambaran hasil.
- Bahasa santai dan sopan ("kamu", "nempel", "pas lihat foto", "ya"). Angka dan harga ditulis dengan kata.
- Default 2 versi (±950 kredit per versi untuk ±50 detik; ±1.250–1.350 untuk ±65 detik). Unduh keduanya, pilih yang jedanya paling rapi.
- Target naskah TOFU ±150–170 kata ≈ 62–68 detik suara (Ricky ±2,5 kata/detik).
- Panggil `creative_get_flow_run_status` sampai selesai, lalu unduh `content_url` dengan curl.

## 5. Gambar Mengikuti Suara

**Cara utama (sejak #03): transkripsi Scribe, timestamp per kata.**
1. `creative_add_flow_asset_node` (modality audio, `generation_id` take terpilih, flow yang sama) → `creative_transcribe_audio` (`eleven_scribe_v1`, gratis) → `creative_get_flow_run_status` → ambil `words` (atau unduh `words_download_url`; tautan kedaluwarsa, panggil status lagi untuk tautan baru).
2. Buang token tag (`[conversational]` dll.), tambahkan offset mulai narasi (0,3) → simpan ke cfg `"words":[[mulai,selesai,"kata"],...]`.
3. Kunci waktu adegan (`K`) = waktu kata pertama tiap kalimat/frasa. Subtitle per frasa ditulis di `subs`; `kinetic.js` mengatur kemunculan per kata.
4. Akhiri dengan kartu penutup yang tampil ±0,8 detik setelah kata terakhir, durasi kartu ±3 detik.

**Cadangan (tanpa Scribe):** RMS per 20 ms, jeda ≥0,18 dtk (±28 dB di bawah persentil 95) = batas kalimat; kata di tengah kalimat diperkirakan proporsional. Skrip: `gaps.py`.

## 6. Render dan Komposisi

Skrip di `scripts/` (template; aset brand diambil dari folder `assets/` skill brand).

**Persiapan folder kerja**
```bash
npm i three@0.160.0
cp <skill-brand>/assets/* .          # logo mug, logo kartu, font
python3 -m http.server 8765 &        # three.js butuh server lokal
```
Gabungkan halaman: sisipkan isi `extra.js` + `smile.js` ke `scene.html` tepat sebelum `window.ready=true;` → simpan sebagai `full.html`.

**3D (three.js + Playwright)**
- 1080×1920, 30 fps, Chromium headless dengan `--use-angle=swiftshader --enable-unsafe-swiftshader`.
- Satu fungsi `renderScene(nama, t, durasi)` per adegan. Teks layar, wipe, kartu, dan footage adalah lapisan HTML di atas kanvas, ditangkap bersama lewat `page.screenshot`.
- Adegan siap pakai: `hook` (lautan cangkir dan meja kerja), `sm_in` / `sm_out` / `sm_good` / `sm_steps` (senyum 3D, zoom gigi, scaling/bleaching), `p5` (ponsel), `c8` (kalender), `w12` (air putih), `foot` (frame footage + teks), `card` (kartu harga). Teks kartu dan logo berasal dari brand; ubah di `extra.js` untuk brand lain.
- **Selalu render 3–6 frame probe dulu** dan lihat hasilnya sebelum render penuh (komposisi, teks menutupi objek, objek terpotong).

**Footage iPhone (HEVC)**
```bash
ffmpeg -ss <mulai> -t <durasi> -i klip.mov -vf "crop=...,scale=1080:1920,colorbalance=rs=.03:bs=-.04:rm=.02:bm=-.02,eq=saturation=1.04:contrast=1.02,fps=30" -q:v 3 ftg/f1/%04d.jpg
```
Zoom pelan: `scale=w='trunc(1080*(1+0.03*t)/2)*2':h=-2:eval=frame,crop=1080:1920`.
Pastikan `max` di job sama dengan jumlah frame yang ada, karena gambar yang tidak ada membuat render macet.

**Scene satu halaman (TOFU @dalamgigi, sejak #02)**
- Satu HTML berisi beberapa "set" (mis. lengkung gigi, penampang, rak buku) yang ditampilkan bergantian; transisi antar-set dengan kilau krem/gelap 0,3 dtk.
- Kamera = array `shots` `[waktuMulai, fungsi(t) → [posisi, target]]`, blend 0,75 dtk; label (tag) diproyeksikan dari titik 3D.
- Template: `gua.html`, `domino.html` (+ `*_cfg.json`), `arch3.html`. Render: `node render_frames.js <page> <cfg> all|range A B|p t...` (PORT env, motion blur dari `cfg.blur`). Probe dulu, lalu render penuh di latar (±0,4 dtk/frame; 70 dtk ≈ 15 menit).
- Material yang diubah transparan di tengah video: set `needsUpdate=true` (atau transparan sejak awal).

**Job dan komposisi (iklan dengan footage)**
- `jobs.json`: per adegan `name`, `n` (frame + 8 cadangan), `D` (durasi detik), `out`, opsi `dir` / `max` / `opt` (teks `p`, `p0`, `wipe`, `s1`, `s2`).
- `node render2.js jobs.json` (±0,15–0,5 detik per frame). Untuk proses panjang, jalankan di latar dan tunggu notifikasi.
- `python3 compose.py`: segmen digabung dengan **crossfade 8 frame**. Perpindahan 3D → footage memakai **wipe** (misalnya wipe atap Ruma), tanpa crossfade.

**Audio dan encode**
```bash
# narasi mulai 0,3 dtk, -16 LUFS, suara latar ruangan sangat pelan, efek kecil opsional
ffmpeg -i narasi.mp3 -f lavfi -i "anoisesrc=color=brown:amplitude=0.6:d=<dur>,lowpass=f=420,highpass=f=60,volume=0.035" \
 -filter_complex "[0:a]adelay=300|300,loudnorm=I=-16:TP=-1.5:LRA=7,apad=whole_dur=<dur>[v];[1:a]afade=t=in:d=0.6[amb];[v][amb]amix=inputs=2:normalize=0[out]" \
 -map "[out]" -ar 48000 -ac 2 track.wav
# encode PERSIS: jangan pakai -shortest (membuang frame)
ffmpeg -framerate 30 -i frames/%04d.jpg -i track.wav -map 0:v -map 1:a -frames:v <dur×30> -t <dur> -r 30 \
 -c:v libx264 -pix_fmt yuv420p -crf 19 -c:a aac -b:a 160k -movflags +faststart out.mp4
bash scripts/qc.sh out.mp4 <dur> <detik_kartu>     # wajib LULUS
```
Suara latar fade-in 0,6 dtk dan fade-out hanya **0,5 dtk terakhir**. Mix SFX: `mix_gua.py` / `mix_domino.py` (daftar event `e(file, detik, dB, durasi)`). Musik mengikuti skill brand (Ruma: tanpa musik). Suara latar ruangan mencegah hening mati.

## 7. Prinsip Visual Umum

- Satu fokus per layar. Teks dua tingkat (label kecil + poin utama), singkat, di area aman (hindari ±15% atas dan ±35% bawah).
- Gerakan kamera pelan dan berlanjut antar-adegan. Angka berjalan untuk hook.
- Ilustrasi gigi: **senyum** (bibir + deretan gigi, tanpa wajah/mata), lalu zoom ke satu gigi untuk proses.
- **Potongan gigi wajib bergaya buku pelajaran** (`scripts/molar.js`): geraham dengan mahkota bertonjol + dua akar, dipotong tegak dari depan, lapisan email putih / dentin krem / saraf merah muda, boleh berlabel. Jangan bentuk kapsul atau balok (v1 iklan tambal ditolak Pak Dir karena tidak dikenali).
- Logo tampil alami di dalam adegan, dari file resmi; tidak dibuat AI.
- Casting footage: orang yang tampil sebagai pasien tidak boleh muncul juga sebagai admin dalam video yang sama.
- Lihat hasil sendiri sebelum mengirim: buat lembar kontak 12–16 frame dan periksa.

## 7a. Efek Suara (SFX) [DISEPAKATI]

Pak Dir minta setiap gerakan punya suara. Pustaka SFX (ElevenLabs `eleven_text_to_sound_v2`, 1 variasi per efek, ±19 kredit) ada di `scripts/sfx/`: `brush` (sikat), `whoosh` (perpindahan kamera), `pop` (objek muncul/angka berganti), `floss`, `scaler` (alat scaling, pelan dan tidak menakutkan), `crack` (karang rontok), `click` (angka/label muncul), `fizz` (asam), `dive` (kamera menyelam/masuk), `pulse` (denyut saraf, lembut), `shimmer` (momen positif, kartu penutup), `book` (buku ditarik/miring), `snap` (benda pas masuk, mis. gigi pengganti). Pakai ulang; buat baru hanya bila gerakannya baru.
- Penempatan: tepat di detik gerakan (bukan per kalimat). Whoosh di setiap perpindahan sudut kamera besar.
- Level: narasi -16 LUFS; SFX -14 s/d -24 dB di bawahnya; suara latar ruangan tetap ada; `alimiter` di akhir. Tanpa musik.
- Skrip mixing: `mix_gua.py` / `mix_domino.py` (daftar event `e(file, detik, dB, durasi)` → `adelay` + `amix normalize=0` + `alimiter`). Setiap angka/label muncul = `click`; setiap ganti set adegan = `shimmer` + `whoosh`.

## 7b. Anti-Monoton (pelajaran 160 Permukaan v1)

Video v1 dinilai Pak Dir "monoton, cuma kotak-kotak". Wajib untuk setiap video 3D:
1. **Ganti sudut kamera tiap 2–4 detik**, sambung dengan blend 0,75 detik: atas (peta) → menyusur rendah → mengitari objek → **masuk ke "lorong"** (misalnya sela gigi) → close-up detail → naik lagi.
2. **Bentuk objek harus dikenali**: gigi seri pipih, taring runcing, premolar 2 tonjol, geraham 4 tonjol. Jangan kotak polos.
3. **Suasana berubah per babak**: bagian masalah sedikit lebih redup/dingin, "kabar baiknya" lebih terang dan hangat.
4. Close-up untuk momen penting (plak mengeras, karang terangkat), supaya ada perubahan skala.
5. Pakai sistem *shot list* di `arch.html` (array `[waktu mulai, fungsi kamera]`) sebagai pola.

## 9. Cover / Thumbnail Seragam

Prinsip (contoh acuan: akun howcomeid): **semua cover satu rumus**, sehingga grid profil terlihat rapi dan senada.
- Latar: **frame 3D bersih** dari video (tanpa angka/subtitle). Render ulang dengan overlay disembunyikan (`scripts/clean.js`).
- Gradasi gelap di 60% bawah, warna dari skill brand.
- Judul **2 baris, rata tengah**: baris 1 putih (konteks), baris 2 **warna aksen, HURUF BESAR** (kata kunci, sering berbentuk pertanyaan).
- Logo/simbol brand kecil di pojok kiri atas.
- Teks berada di zona **crop grid 3:4** (y 240–1680 dari 1920) supaya tetap terbaca di grid profil.
- Template: `scripts/cover.html` + `scripts/cover.js`.

### 9a. Thumbnail wajib dikirim sebelum lanjut ke konten berikutnya [KEPUTUSAN DIR 25 Nov 2026, berlaku UPG · Ruma · GrowWith]
Alur per konten: rancangan → ACC → render → audit 2× → kirim video → revisi (versi baru) sampai Dir oke/tidak ada revisi. **Begitu video dinyatakan final (Dir oke, tidak ada revisi, atau Dir pindah ke footage/konten berikutnya), Claude LANGSUNG membuat dan mengirim thumbnail video itu, sebelum mulai analisis/rancangan konten berikutnya.** Dir tidak perlu meminta.
- Satu thumbnail per video final (bukan per versi revisi). Untuk video yang tidak diunggah, tanya singkat dulu atau lewati.
- Aturan visual per brand: **UPG** → `upg-video/references/thumbnail.md` + template `upg-video/thumbnail/` (foto pengerjaan tanpa mosaik, wajah pasien tidak terlihat kecuali testimoni, judul putih + oranye, logo putih atas). **Ruma** → palet & font Ruma (`ruma-dental-video`, `desain-grafis-ruma`), cover seragam bagian 9 di atas; **GrowWith** → palet GrowWith (`panduan-visual-terpadu` §2, §11). Untuk brand yang belum punya template thumbnail ter-ACC: buat **1 contoh dulu**, minta ACC Dir, lalu simpan aturannya di skill brand itu sebelum dipakai massal.
- Thumbnail ikut aturan privasi brand; thumbnail berisi wajah/nama pasien tidak disimpan di Git.
- Laporan kirim video final selalu ditutup: "Thumbnail menyusul di pesan berikut" atau langsung disertakan.

## 9b. Aturan Isi (pelajaran video #01, v1→v3)

1. **Hook = fakta paling mengejutkan di detik 0–3**, dengan visual yang sudah bergerak. Jangan dibuka dengan layar kosong atau kalimat pengantar.
2. **Setiap anjuran wajib disertai cara singkat.** Contoh: "benang gigi" harus diikuti 40 cm → lilit → selipkan → huruf C → naik turun.
3. **Setiap istilah klinis dijelaskan dalam satu kalimat** (contoh: scaling = pembersihan karang oleh dokter gigi pakai alat bergetar).
4. **Jangan memakai angka yang bisa membingungkan** atau butuh penjelasan tambahan (contoh: "1 jam setahun" dihapus).
5. Durasi 50–70 detik. Kalau naskah lebih panjang, potong bagian yang paling tidak penting, jangan percepat suara.

## 9c. Paket Kirim ke Pak Dir (setiap konten)

Setiap konten selesai dikirim sebagai satu paket:
1. **Video** `<akun>-<NN>-<topik>-v<versi>.mp4` (contoh: `dalamgigi-01-160-permukaan-v3.mp4`).
2. **Sampul** `cover-<topik>-<a/b/c>.png` (pilih satu, kirim sebagai lampiran).
3. **Caption Instagram** siap salin: kalimat hook → isi singkat → poin cara/solusi bernomor → ajakan simpan/kirim (bukan ajakan ke klinik) → hashtag (5–7).
4. **Caption TikTok**: sama + `#edukasigigi #faktaunik`.
5. **Komentar pertama**: satu pertanyaan ringan untuk memancing diskusi.
6. **Langkah unggah**: sampul dari rol kamera, atur crop grid 3:4, tanpa musik, lokasi Makassar, jam 19.00–21.00 WITA.
7. Kalau mengganti video yang sudah terbit: **arsipkan** (jangan hapus) versi lama, dan **perbarui caption** bila isinya berubah.
8. Hasil `qc.sh` (harus LULUS) disebut singkat di laporan. Caption disimpan di `output/<akun>-<NN>-caption.md`; video tidak masuk Git, ingatkan Pak Dir mengunduh.

## 10. Laporan ke Pak Dir

Kirim video dengan `SendUserFile` (display render), lalu jelaskan singkat:
- Apa yang berubah dibanding versi sebelumnya.
- Tabel alur per detik.
- Hal yang perlu Pak Dir cek, terutama **pelafalan**, karena Claude tidak bisa mendengar audio.
- Kredit yang terpakai.

Ingatkan bahwa file di sesi cloud bersifat sementara dan perlu diunduh.

## 11. Standar Kualitas Semua Brand dan Format [DISEPAKATI 17 Nov 2026]

Berlaku untuk **semua video**: konten TOFU (@dalamgigi), **iklan Ruma Dental (MOFU/BOFU)**, dan **video UPG Dental Care**. Asal: bagian terbaik skill "motion-graphics-by-nalarka" yang sudah diuji di #02/#03 dan di-ACC Pak Dir. Aturan identitas tiap brand (musik, durasi, rasio, gaya) tetap mengikuti skill brand masing-masing.

| Fitur | TOFU @dalamgigi | Iklan Ruma (MOFU/BOFU) | Video UPG |
|---|---|---|---|
| A. QC otomatis | Wajib | Wajib | Wajib |
| B. Teks mengikuti kata | Subtitle kinetik per kata | Teks dua tingkat muncul tepat di kata kuncinya; harga/nama klinik pop | Subtitle dialog per kata (warna per karakter bila ada) |
| C. Motion blur | Dive, whoosh, pindah kamera cepat | Wipe atap 3D → footage, zoom cepat | Transisi cepat / whip |

**Penyesuaian per format**
- **Footage asli** (iklan Ruma, UPG): footage diam yang disengaja (mis. papan logo) bisa terdeteksi "frame beku". Bila ≥1,5 dtk, beri zoom pelan (`scale ... 1+0.03*t`) supaya tidak beku; kalau memang disengaja, catat di laporan.
- **Brand yang memakai musik** (bila skill brand mengizinkan, mis. UPG): QC loudness tetap -18…-13 LUFS; narasi/dialog harus dominan; hening mati tetap dilarang.
- **Rasio lain** (4:5 Feed, 1:1): jalankan `qc.sh` lalu abaikan baris resolusi bila memang sengaja; jumlah frame dan durasi tetap harus persis.
- Word timestamp: selalu transkripsi narasi/dialog final dengan **Scribe** (`creative_transcribe_audio`, gratis) lalu simpan ke cfg `"words"` (+ offset mulai narasi).

### Rincian Teknis

**11A. Cek kualitas otomatis (wajib sebelum kirim)**
`scripts/qc.sh video.mp4 <durasi> <detik_kartu>` → codec H.264+AAC, 1080×1920, 30 fps CFR, durasi persis, jumlah frame = durasi×30, tanpa frame hitam, tanpa frame beku tak disengaja (kartu penutup diabaikan), tanpa hening mati, puncak < -0,5 dB, loudness -18…-13 LUFS. Harus "LULUS" sebelum dikirim.
- Encode **tanpa `-shortest`**: pakai `-map 0:v -map 1:a -frames:v <durasi×30> -t <durasi>` (pelajaran: `-shortest` membuang 1–3 frame).
- Suara latar fade-out hanya 0,5 dtk terakhir (pelajaran: fade 1,2 dtk membuat hening mati di kartu penutup).
- Temuan pertama QC (#03): kamera langkah 3 diam 1,7 dtk → setiap shot wajib punya gerak pelan (drift), walau singkat.

**11B. Subtitle/teks kinetik per kata**
`scripts/kinetic.js` → `kineticSub(subEl, T, SUBS, WORDS)`. Kata muncul tepat saat diucapkan (naik halus 0,18 dtk), kata kunci `<b>` pop dengan overshoot; posisi kalimat tidak bergeser. `WORDS` = timestamp Scribe + offset narasi (0,3), disimpan di cfg sebagai `"words":[[mulai,selesai,"kata"],...]`. Kata layar yang beda dari ucapan (mis. "2×") otomatis diinterpolasi.

**11C. Motion blur di gerakan cepat**
`scripts/render_frames.js <page> <cfg> all|range A B|p t...` (+ `blend_blur.py`). Rentang di `cfg.blur=[[a,b],...]` dirender 3 sub-frame (shutter 180°) lalu dirata-rata. Pakai hanya di dive, whoosh, dan perpindahan kamera cepat (render 3× lebih lama di rentang itu).

## 12. Jalur Produksi Tambahan [TERBUKTI 18 Nov 2026]

Urutan wajib tetap sama: naskah OK → papan gambar ACC → (suara) → audit → render → QA frame + zona aman → kirim.

### 12a. Transkripsi lokal (gratis)
`python3 -I .claude/skills/produksi-video-klinik/scripts/stt.py medium <audio1.wav> [...]` → `stt.json` (waktu per kata) di folder audio pertama. Izin sudah ada di `.claude/settings.json`; jaringan huggingface sudah dibuka di lingkungan "Video Editing". Dipakai untuk rekaman asli (ucapan staf) dan narasi ElevenLabs (kunci waktu adegan + caption). ElevenLabs tidak bisa mengambil file langsung dari Drive (tipe file octet-stream).

### 12b. Video orang bicara (admin/staf, suara asli) — `scripts/bicara/`
1. Unduh klip dari Drive (`drive.usercontent.google.com/download?id=…&confirm=t`), transkripsi (12a), susun EDL dari waktu kata (buang salah ucap & ucapan berulang).
2. Atribut brand lain di seragam → `blurlogo.py` (lacak mikrofon klip hitam → blur elips di kiri-bawahnya), sumber diproses ke 30 fps.
3. Overlay per kondisi (`ov2.html` + `shot_states.js`/`shot_states_var.js`) → urutan per frame (`mkseq.py`, termasuk pudar kartu penutup) → `build2.py`/`build_var.py` (crossfade 0,24 dtk, zoom bergantian 1,00/1,08 + dorong 2%, whoosh/pop/ting, suara ruangan klinik asli, loudnorm -16).
4. Hook "spil/tanya" → kotak "Balas komentar" di atas gestur tunjuk (tanpa nama akun). Subtitle 2–4 kata di atas kepala.
5. Varian A/B dari satu rekaman: B (bicara + bukti klinik), C (dibuka cuplikan klinik 2,6 dtk).

### 12c. Iklan footage + narasi + caption kinetik + stiker — `scripts/kinetik/`
1. Narasi Ricky (2 versi) → pilih jeda terapi → transkripsi lokal → `plan.json` (EDL per kata, potongan caption, waktu stiker/kartu langkah/tombol).
2. Data pasien di film rontgen → `filmdet.py` (deteksi lembar film per frame, blur label). Cek ≥6 titik per klip.
3. `mkstates.py` (kondisi per frame + animasi pop) → `shotu.js` (render unik) → `build_k.py` (crossfade, zoom bergantian, whoosh tiap potongan, pop tiap stiker, suara ruangan, mix).
4. Caption gaya label (kotak putih, teks Deep Teal, kata kunci Turquoise), stiker ikon (bukan emoji wajah).

### 12f. Koreksi warna otomatis footage — `scripts/warna/koreksi_warna.py` [TERBUKTI 23 Nov 2026]
Wajib untuk semua footage asli (UPG & Ruma) sebelum dipakai: tiap klip **diukur** (signalstats, 10 frame) lalu diberi resep sesuai kelasnya.
- **NORMAL** (luma rata-rata ≥ 70): regang kontras dari persentil 10/90, terang dijaga natural, buang 40% warna cast (dinding kuning), `vibrance` (bukan saturasi rata, supaya baju hijau tidak makin norak), tajam ringan. Brand `upg` = hangat-dekat, kontras maks 1,30; `ruma` = clean-lembut, kontras maks 1,15 (sesuai skill `panduan-visual-terpadu`).
- **GELAP** (25–70): kurangi bintik (`hqdn3d`) lalu angkat bayangan dengan gamma ke target terang (mis. 30 → ±65).
- **SANGAT_GELAP** (< 25): resep gelap dengan batas angkat; tandai **cek dulu**, pakai hanya sebagai sisipan pendek.
- Perintah: `ukur <klip…>` (tabel + `warna.json`), `banding <klip…> --out x.jpg` (sebelum|sesudah, kirim ke Pak Dir/Dir untuk dicek), `terapkan <in> <out> --brand upg|ruma`, `filter <klip>` (string -vf untuk skrip lain). Jalur EDUKASI UPG: `prep_klip.py … --warna upg`.
- Penyebab gelap ada di syuting, bukan editing: lampu ruangan mati + kamera mengunci terang ke mulut pasien. Arahan syuting: lampu ruangan tetap menyala, tap wajah dokter untuk kunci terang, jangan arahkan kamera ke lampu unit.
- Skill GitHub yang dicek (kajisho5/color-grading-skill, josiahsiegel ffmpeg-color-grading, browser-use/video-use) tidak dipasang: manual/tanpa pengukuran otomatis atau tidak terbaca; resep di sini dibuat sendiri.

### 12g. Samarkan wajah/data pasien per frame: `scripts/privasi/samarkan.py` [TERBUKTI 23 Nov 2026]
`samarkan.py <masuk> <keluar> <kotak.json> --gaya mosaik|blur`. kotak.json = daftar area `{"kf": [[t, x, y, w, h], ...]}` (detik & piksel klip), posisi diinterpolasi di antara keyframe sehingga kotak mengikuti wajah yang bergerak. **UPG = `mosaik`** (kotak-kotak bersudut bulat, keputusan Dir 23 Nov 2026), **Ruma = `blur`** (kabur halus). Cara cepat menentukan kotak: ambil 3 frame per potongan (awal/tengah/akhir) dengan grid, catat posisi wajah, jadikan keyframe. Jangan menutup mulut/area tindakan yang sedang diperlihatkan; mosaik hanya mata–hidung. Simpan klip asli di `work/clips-tanpa-mosaik/`.

### 12h. Mosaik MATA saja (gigi terlihat): `scripts/privasi/samarkan_mata.py` [TERBUKTI 24 Nov 2026]
Permintaan Dir: samarkan hanya mata pasien supaya penonton bisa melihat gigi. MediaPipe FaceLandmarker (`face_landmarker.task` di folder ini; `pip install mediapipe` + `apt-get install -y libegl1 libgles2`), dicari di area pasien (`cari.json` = format samarkan.py) yang diperbesar dengan rotasi 0/90/180/270 (pasien rebahan). Pita mata berputar menutup mata + alis; celah deteksi diinterpolasi ≤1 dtk, selebihnya kotak area penuh (aman). Terbukti 18–50 deteksi per klip scaling. **Wajib cek visual tiap 0,5 dtk**: wajah menyamping (bercermin) bisa meleset → tambah kotak manual berjendela waktu (`samarkan.py`, kunci `dari`/`sampai`). Wajah tertutup dokter / di tepi gambar → tetap kotak.

### 12d. Poster/desain statis
Pakai skill `desain-grafis-ruma`. Font resmi Ruma sejak 20 Nov 2026 untuk grafis **dan** video: Neue Montreal + Montserrat (render lokal: Montserrat sampai file Neue Montreal berlisensi tersedia).

### 12e. Konektor
Nama konektor ElevenLabs bisa berubah setelah masuk ulang (mis. `ElevenLabs-56894adb`). Bila konektor ditolak/kedaluwarsa: minta Pak Dir masuk ulang di claude.ai/customize/connectors; jangan memakai suara pengganti.

## 13. Pelajaran Gaya 3 versi Ruma [TERBUKTI 21 Nov 2026, Tambal Ulang drg. Ainun]
- **Mencerahkan klip gelap bisa memunculkan wajah pasien** (mata pasien terlihat setelah gamma 1,35 di klip sinar biru). Cek ulang blur wajah **setelah** koreksi cahaya, bukan sebelum.
- Klip gimbal bergerak: tandai posisi wajah tiap 0,5 dtk dari frame bergrid lalu interpolasi (lebih andal daripada deteksi wajah untuk pasien berbaring).
- Kertas di meja dokter = kemungkinan dokumen pasien → blur kotak.
- Whisper perlu `initial_prompt` konteks gigi + `word_timestamps` untuk subtitle presisi; kata yang tetap tidak jelas ditulis "…" (jangan ditebak).
- Ucapan berulang di dua klip → pakai sekali saja (potong di cap waktu kata).
- Garis penunjuk harus berakhir tepat di benda yang dimaksud; cek di 3 titik waktu karena orang bergerak.
- **Suara bergema "seperti di dalam ruangan"** (koreksi Pak Dir v1): rekaman DJI Mimo di meja memakai **mic kamera** (stereo, fase ±0,6, RMS −38 dB) padahal dokter memakai mic kerah. Cek dulu: `aphasemeter` ≈1,0 = mic kerah/mono, ≈0,6 = mic kamera. Kalau mic kamera: minta file rekaman internal mic kerah (DJI Mic) ke Pak Dir; sementara bersihkan dengan rantai `VOICE` di `mix_v2.py` (mono, highpass 100, afftdn, potong 250 Hz −5 dB, angkat 3,2 kHz +4 dB, agate, kompresor) → noise floor turun ±9 dB.
- Script: `scripts/gaya3-ruma/` (v2 = `build_v2.py` crossfade + punch-in, `ov2.html` subtitle 2–4 kata + pop, `mix_v2.py` suara bersih + SFX).

- Model konsultasi dokter (hook ucapan → konsultasi → tindakan → pesan sesudahnya): `scripts/konsultasi-dokter/` (Ruma: Konsultasi Tambal drg. Ainun v1, 21 Nov 2026).

- **Footage iPhone (HLG HDR 4K60)**: cukup `scale` biasa (hasil natural, sesuai grading Ruma clean-soft); jangan tonemap hable (terlalu hangat) atau zscale langsung (highlight terbakar). Pola iklan full footage + narasi Ricky: `scripts/iklan-footage-narasi/` (Iklan Scaling Ruma v1, 21 Nov 2026).

- **Bug mix audio (konten 3 drg. Ainun, 23 Nov 2026):** bila tidak ada lapisan yang mulai tepat di detik 0, keluaran `amix` mulai dari pts lapisan pertama → file audio lebih pendek (24,5 vs 27,8 dtk) dan semua suara maju 3,3 dtk. Wajib `amix=...,aresample=48000:async=1:first_pts=0,apad=whole_dur=T` (sudah dipasang di `mix_k1/k2/k3.py`). Selalu cek durasi WAV = durasi video sebelum digabung.
