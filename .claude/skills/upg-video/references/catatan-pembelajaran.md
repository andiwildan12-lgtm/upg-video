# Catatan Pembelajaran UPG Video

**Versi skill: 2.2 (15 Nov 2026)**. Naikkan nomor versi ini setiap kali skill diperbarui. Isi tabel riwayat versi di bagian paling bawah.

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
| Desain karakter | Mulut berupa garis senyum sederhana, hidung berupa garis kecil, **tanpa mata**. Gaya flat. Ilustrasi gigi tanpa wajah | Rancangan V2 (ACC) |
| Pelafalan "UPG" | **Ditulis dan dibaca "UPG"** apa adanya, bukan "U-Pe-Ge". (V2 awalnya memakai "U-Pe-Ge", lalu dikoreksi Dir.) | Dir, 15 Nov 2026 |
| Palet & font | `#FA7209`, `#F8C000`, `#CF6515`, teks `#2A2A2A`, latar `#FFF7EF` + Nunito. Disetujui untuk proyek 1. **Belum dikonfirmasi sebagai identitas brand resmi** | Rancangan V2 (ACC) |
| Tempat kerja | Chat biasa: diskusi, rancangan, ACC, narasi. **Render video selalu di Claude Code** | Dir, 15 Nov 2026 |
| Satu skill dua jalur | Skill digabung jadi **UPG Video**: jalur MOTION dan EDIT REKAMAN | Dir, 15 Nov 2026 |
| Musik di video rekaman | **Boleh**, hanya file dari Dir dengan lisensi jelas | Dir, 15 Nov 2026 |
| Aturan "tanpa mata" | Hanya untuk animasi atau ilustrasi. Orang asli di rekaman tampil apa adanya | Dir, 15 Nov 2026 |
| Tempat kerja video | Rekomendasi: semua di Claude Code. Repo khusus video menunggu dibuat Dir | 15 Nov 2026 |
| Cara kerja diskusi | **Diskusi dan draf langsung di chat**, tanpa file dokumen per revisi. Kata kunci produksi: **"gas render"** setelah draf lengkap ditampilkan | Dir, 15 Nov 2026 |
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

## Risiko dan catatan bisnis

- **Lisensi ElevenLabs:** akun Dir masih paket gratis (per 15 Nov 2026). Paket gratis setahu Claude tidak memberi lisensi komersial. Ingatkan Dir untuk upgrade minimal ke paket Starter sebelum video promo tayang, dan cek ketentuan resminya.
- Cek aturan iklan potongan harga untuk fasilitas kesehatan (Kemenkes/PDGI) sebelum tayang.

## Riwayat proyek

| Proyek | Versi ACC | Hasil | Catatan |
|---|---|---|---|
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
