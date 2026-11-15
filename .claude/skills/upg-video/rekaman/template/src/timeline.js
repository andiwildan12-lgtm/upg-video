// =====================================================================
// TIMELINE EDIT REKAMAN — satu-satunya file yang diisi per proyek.
// Semua waktu dalam DETIK. Isi sesuai rancangan yang di-ACC.
// =====================================================================

// 1) POTONGAN dari footage asli, diputar berurutan.
//    src = detik mulai di footage asli, dur = lama potongan.
export const CUTS = [
	{src: 0.0, dur: 8.0},
];

// 2) CAPTION per kata (waktu = detik di VIDEO HASIL, bukan di footage asli).
//    Satu grup = 1–4 kata yang tampil bersamaan. hl:true = kata disorot (kotak oranye).
//    Ejaan nama/istilah dicek manual (transkrip otomatis sering salah).
export const CAPTIONS = [
	// {from: 0.2, to: 1.4, words: [{text: 'Sudah', at: 0.2}, {text: 'sikat', at: 0.5}, {text: 'gigi?', at: 0.8, hl: true}]},
];

// 3) KARTU PROMO (null bila tidak ada). pos: 'top' | 'center'. Cek wajah tidak tertutup lewat contact sheet.
export const PROMO = null;
// export const PROMO = {from: 4, to: 7.5, pos: 'top', title: 'HAPPY HOUR SCALING', price: 'Rp200.000',
//   lines: ['Senin–Jumat', '10.00–14.00 WITA'], note: 'S&K berlaku'};

// 4) TEKS JUDUL/POIN di atas video (opsional). pos: 'top' | 'center'.
export const LABELS = [
	// {from: 0.0, to: 2.5, text: 'Kerak kuning nggak hilang?', pos: 'top'},
];

// 5) LOGO kecil di pojok (true/false) dan END CARD (detik, 0 = tanpa end card).
export const LOGO_BUG = true;
export const END_CARD_SEC = 3.0;
export const WA = '0896-7341-5806';

// 6) MUSIK LATAR — hanya file dari Dir dengan lisensi jelas (catat di LISENSI-MUSIK.md proyek).
//    null = tanpa musik. volume 0.08–0.15 agar suara tetap jelas.
export const MUSIC = null;
// export const MUSIC = {file: 'music.mp3', volume: 0.1};

export const totalSec = () => CUTS.reduce((a, c) => a + c.dur, 0) + END_CARD_SEC;
