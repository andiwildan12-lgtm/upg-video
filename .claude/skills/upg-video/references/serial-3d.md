# Jalur SERIAL CERITA 3D (TOFU) — "Misi Anak Rantau"

Format acuan: **Eps 1 V4** (disetujui Dir: "sudah ok sihh mantab mi", 15 Nov 2026) dan **Eps 2 V1**. Pakai jalur ini saat Dir minta konten TOFU berbentuk cerita/serial animasi.

## 1. Bible serial
| Unsur | Ketentuan |
|---|---|
| Judul | **Misi Anak Rantau** (serial TOFU UPG, tanpa harga/promo, tanpa CTA booking) |
| Premis | Ijal, mahasiswa Betawi, tinggal di rumah Om-nya di Makassar. Belajar bahwa mandiri juga berarti berani bertanya. Satu topik gigi per episode |
| Gaya | **3D penuh layar** (three.js), tokoh **tanpa mata**, tanpa musik, suasana (SFX) ringan boleh |
| Durasi nyata | ±150–156 dtk per episode (dialog berakting ±20–25% lebih panjang dari perkiraan kata/detik). Kalau Dir ingin ±2 menit, padatkan naskah sejak awal |
| Penutup | Logo UPG putih + judul serial + 1 pertanyaan komentar |

### Tokoh dan suara (ElevenLabs, model `eleven_v4`)
| Tokoh | Suara (voice_id) | Watak | Bahasa |
|---|---|---|---|
| **Ijal** (22, kaos oranye, rambut jabrik) | Satria `SCDJ1Fy4al0KS1awS6H9` | Santai, sok bisa, banyak "solusi" ngawur | Indonesia santai, rasa Betawi tipis (kagak, aje). **Ke Dinda: "Kak/Kak Dinda", "aku/Ijal" (bukan "gue")**. Ke Paman: "Om" |
| **Dinda** (24, hijab biru, baju kuning) | Zulsyifah `QuLloIKxiP3i9uFXzfgD` (pilihan Dir) | Teliti, humor datar, **gampang percaya bacaan internet** | Hampir baku; panggil "Ijal" (bukan "Jal"), sebut diri "Kakak"; ke ayahnya "Bapak" |
| **Paman/Om** (songkok recca, kemeja hijau, sarung) | Macazzart Makassar Natural `hGKBtk3J6UEQtxLtsVRC` | Hangat, sumber mitos generasi lama | **Maks. 1 partikel Makassar per kalimat** (ji, mi, di') — Dir menilai partikel berlebihan "kaku dan kacau" |
| Narator | Denas `arwfiAiEfIHHZCwcYYx2` | Hangat, sedikit jahil, meluruskan fakta | Baku santai |
| Ibu Ijal | **Tanpa suara**, hanya chat di HP | Penyayang, pengingat | — |

### Rencana musim 1
| Eps | Judul | Topik | Status |
|---|---|---|---|
| 1 | Gue Bisa Sendiri! | Gusi berdarah: bukan biasa, bukan sikat lebih keras, vit C jarang, >2 minggu periksa | ✅ V4 selesai |
| 2 | Manis-Manis Makassar | Frekuensi gula (serangan asam 20–30 mnt), gula alami tetap gula, kumur air putih | ✅ V1 selesai |
| 3 | Begadang Tugas | Sikat gigi malam sebelum tidur paling penting. **Akhir = titik pilihan penonton** (Eps 5 ikut Ijal "satu ronde lagi" atau Dinda "pulang lembur") | Berikutnya |
| 4 | Ternyata Bukan Cuma Ijal | Satu-satunya episode di klinik: periksa dulu, karang gigi → pembersihan sesuai pemeriksaan | |
| 5 | (hasil pilihan) | Rutin 2×/hari + saling mengingatkan | |
| 6 | Laporan Anak Mandiri | Rekap 5 pelajaran + mitos Paman (arang/garam) + punchline piring | |
Benang merah: kalender **HARI x/14** (Eps 1 = 1/14, Eps 2 = 4/14), gusi membaik tapi masih sedikit berdarah → Eps 4.

## 2. Aturan cerita (koreksi Dir — wajib)
1. **Alur maju & logika waktu konsisten.** Jangan kilas balik tanpa tanda; jangan kontradiksi ("janji semalam" lalu "sudah 3 hari berdarah").
2. **Jangan potong adegan di kalimat yang belum dijawab.** Setiap momen penting punya reaksi (jeda 0,8–1,5 dtk di wajah tokoh).
3. **Setiap pindah adegan punya alasan:** kartu waktu ("Sore harinya…", "Malamnya…"), tokoh berjalan, narator masuk karena ada pertanyaan/kekeliruan.
4. **Dialog saling menyahut (sebab-akibat).** Contoh koreksi Dir: Paman baru bilang "gula merah alami" setelah **Ijal bertanya** "aman nggak?"; Dinda menegur dengan **alasan** ("nanti gusimu tambah berdarah"), Ijal menjawab sesuai teguran.
5. **Tokoh tidak wajib hadir di setiap adegan** — hanya bila logis (Dinda kerja siang, Paman tidur malam). Kehadiran yang dipaksa terasa sandiwara.
6. **Pola episode: "3 tokoh, 3 mitos"** → gambar membeku abu-abu + label MITOS di atas tiap tokoh → narator meluruskan (dunia di dalam mulut) → kartu YANG BENAR. Mitos Dinda boleh dari **info hoaks di HP** (cap HOAKS, judul artikel fiktif — jangan meniru media nyata).
7. **Edukasi tetap 1 topik**, fakta medis dicek Dir sebelum ACC. Dir sudah menilai porsi edukasi Eps 1 "oke".
8. TOFU: UPG hanya hadir lewat logo & narator; klinik baru tampil di Eps 4.

## 3. Alur kerja (sama dengan SKILL.md, plus detail serial)
1. Naskah di chat (per adegan: tokoh, arahan emosi *[…]*, ⏸ jeda reaksi, 🎬 visual) → revisi sampai Dir oke.
2. **Papan gambar 3D** 12 frame bernomor (`papan.html` + `papan.js`, tile 6×2) → Dir cek.
3. "**gas render**" → `acc_gate.py record` → produksi.

## 4. Pipeline produksi (terbukti Eps 1–2)
Salin `templates/serial-3d/` ke `upg-video-projects/<slug>/src3d/` (beserta `vendor/`), salin `assets/` dan `src/_style.css` dari proyek sebelumnya.

| Langkah | Alat | Catatan |
|---|---|---|
| Suara | `creative_generate_speech`, **1 kalimat = 1 generasi**, `generations_count:1`, tag emosi v4 (`[panicked]`, `[sighs]`, `[chuckles]`, `[whispers]`, `[deadpan]`, `[teasing]`…) | Satu take per tokoh lalu dipotong = **kaku** (ditolak Dir). Biaya ±2.500 kredit/episode |
| SFX suasana | `creative_generate_in_flow` node `sfx` (hasil 1–3 dtk, di-loop pelan) | Air menetes, jangkrik, gerobak, notifikasi HP. **Bukan musik** |
| Unduh | `curl` dari `elevenlabsusercontent.com` (izin host di environment Video Editing) | Simpan `audio/v{n}/<ID>.mp3` |
| Timing | `build_audio.py` (contoh: `build_audio_contoh.py`): daftar baris (ID, penutur, teks, jeda, kata sorot) → `silencedetect` → kata diperkirakan proporsional panjang huruf → `audio/narasi.wav` (loudnorm −14) + `src3d/timing.js` (baris, shot, cue) | Jeda bervariasi: sahutan cepat 0,15–0,4; reaksi 0,6–1,0; ganti waktu 1,7–2,4 |
| Animasi | `film.html` (contoh: `film-contoh.html`): objek `SHOT{}` per adegan → bangun set sekali, `upd(t)` atur pose/mulut/kamera, kembalikan overlay HTML | Mulut bergerak saat kata aktif (`talking`), `setPose`, `lerpPos` (tokoh masuk), `camKeys` (kamera), `FADES` (transisi gelap) |
| Cek | `node src3d/film.js stills "t1,t2,…"` → contact sheet | Cek tabrakan teks/tokoh, tokoh terpotong, framing |
| Render | `node src3d/film.js video` (latar belakang, **±0,4 dtk/frame → ±30–35 mnt**) | Gerbang ACC otomatis; audio di-mux di akhir |
| Verifikasi | `scripts/verify_video.py` | Loudness boleh −15,3 s/d −12,5 LUFS |

### `dunia.js` (aset 3D dipakai ulang)
- Tokoh: `W3.ijal/dinda/paman({pos,ry,L,R,mood})` → `userData.setPose(L,R)`, `userData.setMouth(m)`; pose: down, head, up, brush, point, phone, hip, hold, raise, cup, cross, note; mulut: smile, o, talk, flat, worry, grin.
- Set: `bathroom(night)`, `livingroom()`, `terrace('sore'|'malam')`, `mouth()` (+`plaque/swell/drops`, `acid()`), `exterior()`.
- Properti: `toothbrush`, `phone`, `mug`, `orangeBag`, `notebook`, `plateEpe`, `barongkoPlate`, `icedTea`, `choco`, `newspaper`, `calendarOn(pos,'x/14')`, `cart`.
- Penting: `THREE.ColorManagement.legacyMode=false` + `sRGBEncoding` (kalau tidak, warna pudar); Chromium `--use-gl=swiftshader`.

### Kesalahan yang pernah terjadi (jangan ulangi)
- Tokoh/teks terpotong saat kamera terlalu dekat → cek stills sebelum render.
- Kelas CSS `.card` bentrok dengan `_style.css` lama → di 2.5D pakai `.kcard`; di film 3D `.card` sudah didefinisikan ulang.
- Durasi naskah diremehkan → hitung ulang dari audio nyata, laporkan jujur ke Dir.
