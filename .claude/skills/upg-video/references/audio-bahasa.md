# Audio dan Bahasa

## Narasi
- Narator AI **laki-laki** dengan artikulasi bahasa Indonesia yang jelas. Nada ramah dan profesional, kecepatan nyaman (±2,2–2,5 kata/detik), dengan jeda yang cukup untuk membaca teks layar.
- Suara yang dipilih Dir: **ElevenLabs "Denas"** (`arwfiAiEfIHHZCwcYYx2`). Detail ada di `catatan-pembelajaran.md`. Ganti suara hanya jika Dir meminta.
- Jangan meniru suara orang tertentu. Jangan mengklaim suara itu adalah dokter UPG.

## Tanpa musik
- Default audio **hanya narasi**.
- Tidak ada musik latar, intro, jingle, atau SFX bernada.
- SFX nonmusikal (klik/whoosh halus) hanya boleh jika sudah dibahas **dan** tercantum di rancangan yang di-ACC.

## Pelafalan
- Periksa pelafalan "UPG", istilah layanan (scaling, karang gigi, ortodonti, dll.), angka, dan nama brand.
- **"UPG" ditulis "UPG" apa adanya** di naskah TTS (keputusan Dir, 15 Nov 2026). Jangan diubah jadi "U-Pe-Ge". Kalau hasil suara terdengar salah, laporkan ke Dir dan tunggu arahan, jangan mengganti ejaan sendiri.
- Istilah Inggris ("scaling", "Happy Hour") ditulis biasa untuk suara Denas/eleven_v4. Ejaan fonetis seperti "skeling" hanya dipakai kalau Dir melaporkan pelafalannya salah. Teks layar tetap ejaan resmi.

## Naskah voiceover bertanda jeda
Di rancangan, selain naskah narasi biasa, tulis **versi voiceover** untuk dibaca Dir dan dijadikan dasar TTS:
- Satu baris = satu tarikan napas. Kalimat 5–12 kata.
- `/` = jeda pendek (±0,3 dtk), `//` = jeda panjang (±0,6 dtk).
- **KAPITAL** = kata yang ditekan, maksimal 1 per kalimat.
- Angka dan singkatan ditulis seperti diucapkan ("dua ratus ribu"). Pengecualian: nama brand **"UPG" tetap ditulis UPG**.
- Penanda bagian: `[HOOK]`, `[PENJELASAN]`, `[SOLUSI]`, `[PROMO]`, `[CTA]`.
- Di akhir: `Jumlah kata: N · Perkiraan durasi: ~X dtk (2,6 kata/dtk, suara Denas)`.

**Saat mengirim ke TTS (ElevenLabs), tanda-tanda ini harus dibersihkan:**
- `/` diganti koma.
- `//` diganti baris kosong (paragraf baru). Di proyek 1, paragraf baru menghasilkan jeda ±0,3–0,5 dtk.
- KAPITAL dikembalikan ke huruf biasa, karena huruf kapital bisa dieja per huruf.
- Penanda `[…]` dihapus.

Simpan hasil bersihnya sebagai `naskah-tts.txt`. Isi kalimatnya harus tetap persis sama dengan naskah yang di-ACC.

## Bahasa naskah
- Kalimat pendek, satu gagasan per kalimat, bahasa sehari-hari yang sopan.
- Nomor WA panjang **tidak dibacakan**. Cukup "hubungi WhatsApp UPG di layar", lalu nomornya tampil di end card.

## Dialog multi-suara (serial 3D)
- **1 kalimat = 1 generasi** (`generations_count:1`) dengan tag emosi v4 di depan kalimat: `[panicked]`, `[worried]`, `[sighs]`, `[chuckles]`, `[laughs]`, `[whispers]`, `[deadpan]`, `[teasing]`, `[proudly]`, `[hesitant]`, `[playfully]`, `[warmly]`. Tag tidak ikut dibaca.
- Jangan membuat satu take per tokoh lalu memotongnya: hasilnya datar dan "terpotong-potong" (ditolak Dir di Eps 1 V1).
- Sahutan kecil manusiawi (eh, lho, hmm, tawa, helaan napas) membuat dialog hidup.
- Angka di naskah v4 tulis apa adanya ("20 sampai 30 menit").
- Panggilan & partikel daerah: lihat `serial-3d.md` (Paman maks. 1 partikel Makassar per kalimat).
