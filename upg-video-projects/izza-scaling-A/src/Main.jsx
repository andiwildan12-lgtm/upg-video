// Komposisi EDUKASI DOKTER (Gaya 1) — UPG Video.
// Talking-head dokter + caption per kata + stiker pop + zoom punch-in + kartu ilustrasi (video jadi polaroid)
// + lapisan SFX + backsound. Kanvas 1080x1920 @30fps.
// Isi proyek TIDAK diketik di sini: src/timeline.js dibuat oleh scripts/build_timeline.py dari edit.json.
import {AbsoluteFill, Audio, Easing, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {CAPTIONS, CARDS, COUNTER, CUTS, DOTS, END, GAYA, LOGO, MUSIC, NAMETAG, NOTES, SFX, STICKERS, TITLES, ZOOMS, cutsEnd} from './timeline.js';
// GAYA 1 = default (caption putih + pill oranye). GAYA 3 = retro: judul slab diketik, caption kotak putih, pill cokelat, coretan tangan, penghitung.
const G3 = GAYA === 3;
// BR = cokelat-oranye tua turunan #CF6515 UPG (antislop audit 001 #10: identitas UPG, bukan cokelat template). Putih di atasnya ±7:1.
const BR = '#7A3608', CRM = '#FFF1D0';
const SLAB = '"Alfa Slab One", "Noto Color Emoji", serif', HAND = 'Caveat, "Noto Color Emoji", cursive', MONO = '"Courier Prime", monospace';

const W = 1080, H = 1920, FPS = 30;
const C = {or: '#FA7209', yl: '#F8C000', or2: '#CF6515', ink: '#2A2A2A', cream: '#FFF7EF', red: '#E5484D', mute: '#8A7F75'};
const FONT = 'Nunito, "Noto Color Emoji", sans-serif';
const EMO = '"Noto Color Emoji", sans-serif';
const out3 = Easing.bezier(0.22, 1, 0.36, 1);
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const prog = (t, a, b, e = out3) => interpolate(t, [a, b], [0, 1], {...clamp, easing: e});
const lerp = (a, b, p) => a + (b - a) * p;
// pegas sederhana: naik melewati 1 lalu kembali (efek "pop")
const pop = (t, a, d = 0.35) => {
	const x = Math.max(0, Math.min(1, (t - a) / d));
	return x <= 0 ? 0 : 1 + Math.sin(x * Math.PI) * 0.18 * (1 - x) - (1 - x) * (1 - x) * (1 - x);
};
const vis = (t, a, b, d = 0.2) => Math.min(prog(t, a, a + d), 1 - prog(t, b - d, b));

const fontFace = `
@font-face{font-family:Nunito;font-weight:600;src:url(${staticFile('fonts/nunito-latin-600-normal.woff2')}) format("woff2")}
@font-face{font-family:Nunito;font-weight:800;src:url(${staticFile('fonts/nunito-latin-800-normal.woff2')}) format("woff2")}
@font-face{font-family:Nunito;font-weight:900;src:url(${staticFile('fonts/nunito-latin-900-normal.woff2')}) format("woff2")}
@font-face{font-family:"Alfa Slab One";src:url(${staticFile('fonts/alfa-slab-one-latin-400-normal.woff2')}) format("woff2")}
@font-face{font-family:Caveat;font-weight:700;src:url(${staticFile('fonts/caveat-latin-700-normal.woff2')}) format("woff2")}
@font-face{font-family:"Courier Prime";font-weight:700;src:url(${staticFile('fonts/courier-prime-latin-700-normal.woff2')}) format("woff2")}`;

// ---------- status kartu (0 = video penuh, 1 = video jadi polaroid) ----------
const cardAt = (t) => CARDS.find((c) => t >= c.from - 0.4 && t < c.to + 0.4);
const cardState = (t) => {
	const c = cardAt(t);
	if (!c) return 0;
	return Math.min(prog(t, c.from - 0.05, c.from + 0.4), 1 - prog(t, c.to - 0.05, c.to + 0.35));
};
const PIP = {x: 70, y: 1050, w: 270}; // polaroid kiri bawah (di atas area UI platform)

// ---------- zoom ----------
const zoomAt = (t) => {
	let z = 1;
	for (const k of ZOOMS) {
		if (t < k.from || t > k.to + 0.3) continue;
		if (k.mode === 'slow') z *= lerp(1, k.scale, prog(t, k.from, k.to, Easing.inOut(Easing.quad)));
		else z *= lerp(1, k.scale, Math.min(prog(t, k.from, k.from + 0.14), 1 - prog(t, k.to, k.to + 0.25)));
	}
	return z;
};

const VideoLayer = ({t}) => {
	const p = cardState(t);
	const w = lerp(W, PIP.w, p), h = (w * 16) / 9;
	const x = lerp(0, PIP.x, p), y = lerp(0, PIP.y, p);
	let acc = 0;
	return (
		<div style={{position: 'absolute', left: x, top: y, width: w, height: h, overflow: 'hidden', borderRadius: 26 * p,
			border: `${12 * p}px solid #fff`, boxShadow: p > 0 ? `0 ${24 * p}px ${50 * p}px rgba(80,40,0,${0.28 * p})` : 'none',
			transform: `rotate(${-4 * p}deg)`, background: '#000'}}>
			<div style={{position: 'absolute', left: 0, top: 0, width: W, height: H, transform: `scale(${w / W})`, transformOrigin: '0 0'}}>
				{CUTS.map((c, i) => {
					const from = Math.round(acc * FPS);
					acc += c.dur;
					const local = t - c.start;
					if (local < -0.1 || local > c.dur + 0.1) return null;
					// tiap potongan masuk dengan "settle" kecil (1.06 -> 1) supaya pergantian take terasa hidup
					const settle = i === 0 ? 1 : lerp(1.06, 1, prog(local, 0, 0.3));
					const s = c.scale * zoomAt(t) * settle;
					// geser wajah (fx,fy) ke titik target (tx,ty), dibatasi agar tepi video tidak pernah terlihat
					const cl = (v, a, b) => Math.max(a, Math.min(b, v));
					const dx = cl((c.tx ?? 540) - c.fx, (W - c.fx) * (1 - s), c.fx * (s - 1));
					const dy = cl((c.ty ?? 780) - c.fy, (H - c.fy) * (1 - s), c.fy * (s - 1));
					return (
						<Sequence key={i} from={from} durationInFrames={Math.round(c.dur * FPS)}>
							<div style={{position: 'absolute', inset: 0, transform: `translate(${dx}px, ${dy}px) scale(${s})`, transformOrigin: `${c.fx}px ${c.fy}px`}}>
								<OffthreadVideo src={staticFile(`clips/${c.clip}.mp4`)} startFrom={Math.round(c.in * FPS)} volume={(f) => (c.vol ?? 1) * Math.min(1, (f + 1) / 3, (Math.round(c.dur * FPS) - f) / 3)} style={{width: W, height: H}} />
								{/* blur area privasi (formulir/layar/data pasien), koordinat rekaman 1080x1920, ikut zoom */}
								{(c.blur || []).map(([bx, by, bw, bh], j) => (
									<div key={j} style={{position: 'absolute', left: bx, top: by, width: bw, height: bh, borderRadius: 24,
										backdropFilter: 'blur(18px)', WebkitBackdropFilter: 'blur(18px)', background: 'rgba(240,240,240,.25)'}} />
								))}
							</div>
						</Sequence>
					);
				})}
			</div>
		</div>
	);
};

// ---------- latar kartu ----------
const CardBg = ({t}) => {
	const p = cardState(t);
	if (p <= 0) return null;
	return (
		<AbsoluteFill style={{opacity: p, background: `radial-gradient(circle at 85% 12%, rgba(248,192,0,.28), transparent 38%),
			radial-gradient(circle at 10% 80%, rgba(250,114,9,.16), transparent 40%), ${C.cream}`}}>
			{DOTS && <AbsoluteFill style={{backgroundImage: 'radial-gradient(rgba(207,101,21,.22) 2.2px, transparent 2.6px)', backgroundSize: '44px 44px'}} />}
		</AbsoluteFill>
	);
};

const CardTitle = ({text, t, at}) => (
	<div style={{position: 'absolute', left: 80, right: 80, top: 240, textAlign: 'center', fontWeight: 900, fontSize: 60, color: C.ink, lineHeight: 1.12,
		opacity: prog(t, at, at + 0.3), transform: `translateY(${(1 - prog(t, at, at + 0.4)) * 30}px)`}}>{text}</div>
);

const ChatCard = ({c, t}) => (
	<>
		<CardTitle text={c.title} t={t} at={c.from + 0.1} />
		{c.note && <div style={{position: 'absolute', right: 90, top: 1000, fontWeight: 800, fontSize: 28, color: C.mute, background: 'rgba(255,255,255,.8)',
			padding: '4px 16px', borderRadius: 999, opacity: prog(t, c.from + 0.2, c.from + 0.5)}}>{c.note}</div>}
		<div style={{position: 'absolute', left: 80, right: 80, top: 380, display: 'flex', flexDirection: 'column', gap: 20}}>
			{c.bubbles.map((b, i) => {
				const typing = t >= b.at - 0.5 && t < b.at;
				const a = prog(t, b.at, b.at + 0.25);
				if (t < b.at - 0.5) return null;
				const me = b.side === 'kanan';
				return (
					<div key={i} style={{display: 'flex', justifyContent: me ? 'flex-end' : 'flex-start', alignItems: 'flex-end', gap: 16}}>
						{!me && <div style={{fontFamily: EMO, fontSize: 64}}>{b.avatar || '😟'}</div>}
						<div style={{maxWidth: 660, background: me ? C.or : '#fff', color: me ? '#fff' : C.ink, fontWeight: 800, fontSize: 44, lineHeight: 1.2,
							padding: '20px 30px', borderRadius: 36, borderBottomLeftRadius: me ? 36 : 8, borderBottomRightRadius: me ? 8 : 36,
							boxShadow: '0 10px 28px rgba(80,40,0,.14)', transform: `scale(${typing ? 1 : 0.85 + 0.15 * a})`, transformOrigin: me ? '100% 100%' : '0 100%'}}>
							{typing ? <span style={{letterSpacing: 8, color: C.mute}}>{'•'.repeat(1 + (Math.floor(t * 6) % 3))}</span> : b.text}
						</div>
						{me && <div style={{fontFamily: EMO, fontSize: 64}}>{b.avatar || '👩‍⚕️'}</div>}
					</div>
				);
			})}
		</div>
	</>
);

const Check = ({p}) => (
	<svg width="64" height="64" viewBox="0 0 64 64">
		<circle cx="32" cy="32" r="28" fill={p > 0 ? C.or : '#fff'} stroke={C.or} strokeWidth="5" />
		<path d="M18 33 L28 43 L46 22" fill="none" stroke="#fff" strokeWidth="7" strokeLinecap="round" strokeLinejoin="round"
			strokeDasharray="44" strokeDashoffset={44 * (1 - p)} />
	</svg>
);

const ChecklistCard = ({c, t}) => (
	<>
		<CardTitle text={c.title} t={t} at={c.from + 0.1} />
		{G3 && <div style={{position: 'absolute', left: 70, right: 70, top: 370, height: 70, background: '#fff', borderRadius: '28px 28px 0 0', display: 'flex', alignItems: 'center', gap: 12, paddingLeft: 28,
			boxShadow: '0 -2px 0 rgba(0,0,0,.04)', fontFamily: MONO, fontWeight: 700, fontSize: 34, color: BR}}>
			<span>{c.window || 'hari ini'}</span></div>}
		<div style={{position: 'absolute', left: 90, right: 90, top: G3 ? 460 : 420, display: 'flex', flexDirection: 'column', gap: G3 ? 14 : 24}}>
			{c.items.map((it, i) => {
				const a = prog(t, it.at, it.at + 0.35);
				const ck = prog(t, it.at + 0.25, it.at + 0.55);
				return (
					<div key={i} style={{display: 'flex', alignItems: 'center', gap: 22, background: '#fff', borderRadius: 32, padding: G3 ? '12px 24px' : '20px 26px',
						boxShadow: G3 ? 'none' : '0 10px 28px rgba(80,40,0,.12)', border: G3 ? '2px solid rgba(122,54,8,.15)' : 'none', opacity: a, transform: `translateX(${(1 - a) * -80}px)`,
						outline: ck > 0 && ck < 1 ? `4px solid ${C.yl}` : 'none'}}>
						<div style={{fontFamily: EMO, fontSize: 60, width: 76, textAlign: 'center'}}>{it.emoji}</div>
						<div style={{flex: 1, fontWeight: 900, fontSize: 48, color: C.ink, lineHeight: 1.15}}>{it.text}</div>
						<Check p={ck} />
					</div>
				);
			})}
		</div>
	</>
);

const JudulCard = ({c, t}) => (
	<div style={{position: 'absolute', left: 70, right: 70, top: 330, textAlign: 'center'}}>
		{c.lines.map((l, i) => {
			const s = pop(t, l.at);
			return (
				<div key={i} style={{fontWeight: 900, fontSize: l.size || 92, lineHeight: 1.1, margin: '10px 0', color: l.hl ? '#fff' : C.ink,
					transform: `scale(${s})`, opacity: Math.min(1, s * 1.5)}}>
					<span style={l.hl ? {background: C.or, borderRadius: 28, padding: '4px 30px', boxShadow: '0 12px 30px rgba(250,114,9,.35)'} : {}}>{l.text}</span>
				</div>
			);
		})}
	</div>
);

const Cards = ({t}) => {
	const c = cardAt(t);
	if (!c) return null;
	const a = Math.min(prog(t, c.from, c.from + 0.3), 1 - prog(t, c.to - 0.1, c.to + 0.25));
	return (
		<AbsoluteFill style={{opacity: a}}>
			{c.type === 'chat' && <ChatCard c={c} t={t} />}
			{c.type === 'checklist' && <ChecklistCard c={c} t={t} />}
			{c.type === 'judul' && <JudulCard c={c} t={t} />}
		</AbsoluteFill>
	);
};

// ---------- teks di atas video ----------
const Titles = ({t}) => TITLES.map((k, i) => {
	const v = vis(t, k.from, k.to, 0.15);
	if (v <= 0) return null;
	const s = pop(t, k.from);
	const y = k.y ?? 330;
	if (k.kind === 'retro') {
		// judul slab krem bergaris cokelat, diketik huruf per huruf (Gaya 3)
		const n = Math.floor(Math.max(0, t - k.from) / (k.cps ?? 0.035));
		let left = n;
		const subA = prog(t, k.from + k.text.length * (k.cps ?? 0.035) + 0.1, k.from + k.text.length * (k.cps ?? 0.035) + 0.4);
		return (
			<div key={i} style={{position: 'absolute', left: 50, right: 50, top: y, textAlign: 'center', opacity: v}}>
				{k.text.split('\n').map((ln, j) => {
					const shown = [...ln].slice(0, Math.max(0, left)).join('');
					left -= [...ln].length;
					return <div key={j} style={{fontFamily: SLAB, fontSize: k.size || 84, lineHeight: 1.12, color: CRM, minHeight: (k.size || 84) * 1.12,
						WebkitTextStroke: `4px ${BR}`, paintOrder: 'stroke fill', textShadow: `0 7px 0 ${BR}, 0 10px 22px rgba(0,0,0,.35)`}}>{shown}</div>;
				})}
				{k.sub && <div style={{display: 'inline-block', marginTop: 18, background: BR, color: CRM, fontFamily: MONO, fontWeight: 700, fontSize: 40,
					padding: '8px 26px', borderRadius: 14, opacity: subA, transform: `translateY(${(1 - subA) * 16}px)`}}>{k.sub}</div>}
			</div>
		);
	}
	if (k.kind === 'jam') {
		// jam rekam asli (konten "1 jam dipadatkan"): badge gelap kecil kanan atas, di dalam area aman (atas 250, kanan 120)
		return (
			<div key={i} style={{position: 'absolute', right: 140, top: k.y ?? 270, display: 'flex', alignItems: 'center', gap: 14, background: 'rgba(42,42,42,.88)',
				color: '#fff', borderRadius: 999, padding: '12px 30px 12px 20px', fontWeight: 900, fontSize: 52, opacity: v, fontVariantNumeric: 'tabular-nums'}}>
				<svg width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="18" fill="none" stroke={C.or} strokeWidth="5" />
					<line x1="22" y1="22" x2="22" y2="11" stroke={C.or} strokeWidth="5" strokeLinecap="round" />
					<line x1="22" y1="22" x2="30" y2="22" stroke={C.or} strokeWidth="5" strokeLinecap="round" /></svg>
				{k.text}
			</div>
		);
	}
	if (k.kind === 'teks') {
		// teks penjelasan tanpa suara: kalimat UTUH sekaligus (bukan per kata), 1-2 baris kotak putih, *kata* = sorot oranye
		const r = prog(t, k.from, k.from + 0.3);
		return (
			<div key={i} style={{position: 'absolute', left: 70, right: 70, top: y, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10,
				opacity: v, transform: `translateY(${(1 - r) * 24}px)`}}>
				{k.text.split('\n').map((ln, j) => (
					<div key={j} style={{background: '#fff', borderRadius: 18, padding: '10px 26px', fontWeight: 900, fontSize: k.size || 54, lineHeight: 1.15,
						color: C.ink, textAlign: 'center'}}>
						{ln.split(/(\*[^*]+\*)/).map((w, q) => w.startsWith('*')
							? <span key={q} style={{background: C.or, borderRadius: 10, padding: '0 10px'}}>{w.slice(1, -1)}</span> : w)}
					</div>
				))}
			</div>
		);
	}
	if (k.kind === 'hook') {
		return (
			<div key={i} style={{position: 'absolute', left: 60, right: 60, top: y, textAlign: 'center', opacity: v, transform: `scale(${s})`}}>
				{k.text.split('\n').map((ln, j) => (
					<div key={j} style={{fontWeight: 900, fontSize: k.size || 96, lineHeight: 1.08, color: '#fff', letterSpacing: -1,
						textShadow: '0 6px 0 rgba(0,0,0,.18), 0 4px 18px rgba(0,0,0,.55), 0 0 3px rgba(0,0,0,.9)'}}>{ln}</div>
				))}
			</div>
		);
	}
	const strike = k.strikeAt != null ? prog(t, k.strikeAt, k.strikeAt + 0.25) : 0;
	return (
		<div key={i} style={{position: 'absolute', left: 0, right: 0, top: y, display: 'flex', justifyContent: 'center', opacity: v, transform: `scale(${s})`}}>
			<div style={{position: 'relative', background: '#fff', color: C.ink, fontWeight: 900, fontSize: k.size || 56, padding: '14px 34px', borderRadius: 999,
				boxShadow: '0 12px 30px rgba(0,0,0,.28)', display: 'flex', alignItems: 'center', gap: 14}}>
				{k.emoji && <span style={{fontFamily: EMO}}>{k.emoji}</span>}
				<span style={{opacity: 1 - 0.45 * strike}}>{k.text}</span>
				{strike > 0 && <div style={{position: 'absolute', left: 20, top: '50%', height: 10, width: `calc(${strike * 100}% - 40px)`, background: C.red,
					borderRadius: 6, transform: 'rotate(-6deg)'}} />}
			</div>
		</div>
	);
});

// ---------- stiker emoji pop ----------
const Stickers = ({t}) => STICKERS.map((k, i) => {
	const end = k.at + (k.dur ?? 1.6);
	if (t < k.at || t > end) return null;
	if (k.kind === 'burst') {
		const p = prog(t, k.at, end, Easing.out(Easing.cubic));
		return [...Array(8)].map((_, j) => {
			const ang = (j / 8) * Math.PI * 2 + 0.3;
			const r = 40 + 220 * p;
			return <div key={`${i}-${j}`} style={{position: 'absolute', left: k.x + Math.cos(ang) * r - 30, top: k.y + Math.sin(ang) * r - 30,
				fontFamily: EMO, fontSize: j % 2 ? 44 : 60, opacity: 1 - p, transform: `rotate(${p * 90}deg)`}}>{k.emoji || '✨'}</div>;
		});
	}
	const s = pop(t, k.at) * (1 - prog(t, end - 0.2, end));
	const fl = Math.sin((t - k.at) * 3.2 + i) * 8;
	const size = k.size || 130;
	return (
		<div key={i} style={{position: 'absolute', left: k.x - size / 2, top: k.y - size / 2 + fl, width: size, transform: `scale(${s}) rotate(${k.rot ?? (i % 2 ? 8 : -8)}deg)`,
			display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
			<div style={{width: size, height: size, borderRadius: size / 2, background: k.bare ? 'transparent' : '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center',
				boxShadow: k.bare ? 'none' : (G3 ? '0 3px 8px rgba(0,0,0,.18)' : '0 10px 26px rgba(0,0,0,.25)'), fontFamily: EMO, fontSize: size * 0.58}}>{k.emoji}</div>
			{k.label && <div style={{marginTop: 10, whiteSpace: 'nowrap', background: C.or, color: '#fff', fontWeight: 900, fontSize: 34, padding: '4px 18px', borderRadius: 999}}>{k.label}</div>}
		</div>
	);
});

// ---------- caption per kata ----------
const Word = ({w, t, dark}) => {
	const p = prog(t, w.at, w.at + 0.14);
	const base = {display: 'inline-block', margin: '0 7px', fontSize: 66, fontWeight: 900, lineHeight: 1.25, opacity: p,
		transform: `translateY(${(1 - p) * 14}px) scale(${w.hl ? pop(t, w.at, 0.3) : 1})`};
	if (G3) return w.hl
		? <span style={{...base, fontSize: 58, margin: '0 4px', color: '#fff', background: BR, borderRadius: 14, padding: '0 16px'}}>{w.text}</span>
		: <span style={{...base, fontSize: 58, margin: '0 4px', color: C.ink}}>{w.text}</span>;
	return w.hl
		? <span style={{...base, color: '#fff', background: C.or, borderRadius: 18, padding: '0 18px', boxShadow: '0 8px 20px rgba(0,0,0,.25)'}}>{w.text}</span>
		: dark
			? <span style={{...base, color: C.ink}}>{w.text}</span> // mode kartu: latar krem -> teks gelap (putih tidak terbaca)
			: <span style={{...base, color: '#fff', textShadow: '0 3px 10px rgba(0,0,0,.8), 0 0 3px rgba(0,0,0,.95)'}}>{w.text}</span>;
};
const Captions = ({t}) => {
	const g = CAPTIONS.find((c) => t >= c.from && t < c.to);
	if (!g) return null;
	if (TITLES.some((k) => k.nocap && t >= k.from && t < k.to)) return null; // judul sudah memuat kalimat yang sama
	const p = cardState(t);
	const st = p > 0.5 ? {left: PIP.x + PIP.w + 40, right: 120, top: 1250} : {left: 90, right: 150, top: 1240};
	if (G3) return (
		<div style={{position: 'absolute', ...st, display: 'flex', justifyContent: 'center'}}>
			<div style={{background: 'rgba(255,255,255,.96)', borderRadius: 22, padding: '8px 18px', boxShadow: '0 2px 6px rgba(0,0,0,.18)', textAlign: 'center'}}>
				{g.words.map((w, i) => <Word key={i} w={w} t={t} />)}</div></div>);
	return <div style={{position: 'absolute', ...st, textAlign: 'center'}}>{g.words.map((w, i) => <Word key={i} w={w} t={t} dark={p > 0.5} />)}</div>;
};

// ---------- coretan tangan + panah (Gaya 3) ----------
const Notes = ({t}) => NOTES.map((k, i) => {
	const v = vis(t, k.from, k.to, 0.2);
	if (v <= 0) return null;
	const d = prog(t, k.from + 0.15, k.from + 0.55);
	const [x1, y1, x2, y2] = k.arrow || [0, 0, 0, 0];
	const mx = (x1 + x2) / 2 + (k.bend ?? 80), my = (y1 + y2) / 2 - (k.bend ?? 80);
	const ang = Math.atan2(y2 - my, x2 - mx);
	const col = k.color || '#fff';
	return (
		<div key={i} style={{position: 'absolute', inset: 0, opacity: v}}>
			<div style={{position: 'absolute', left: k.x, top: k.y, fontFamily: HAND, fontWeight: 700, fontSize: k.size || 72, color: col, whiteSpace: 'pre', lineHeight: 0.95,
				transform: `rotate(${k.rot ?? -6}deg) scale(${pop(t, k.from, 0.3)})`, textShadow: col === '#fff' ? '0 3px 10px rgba(0,0,0,.6)' : 'none'}}>{k.text}</div>
			{k.arrow && <svg width={W} height={H} style={{position: 'absolute', left: 0, top: 0}}>
				<path d={`M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}`} fill="none" stroke={col} strokeWidth="9" strokeLinecap="round" pathLength="1"
					strokeDasharray="1" strokeDashoffset={1 - d} style={{filter: 'drop-shadow(0 2px 6px rgba(0,0,0,.45))'}} />
				{d > 0.95 && <path d={`M${x2 - 40 * Math.cos(ang - 0.5)} ${y2 - 40 * Math.sin(ang - 0.5)} L${x2} ${y2} L${x2 - 40 * Math.cos(ang + 0.5)} ${y2 - 40 * Math.sin(ang + 0.5)}`}
					fill="none" stroke={col} strokeWidth="9" strokeLinecap="round" strokeLinejoin="round" />}
			</svg>}
		</div>
	);
});

// ---------- penghitung (mis. "terima kasih ke-N") ----------
const Counter = ({t}) => {
	if (!COUNTER) return null;
	const n = COUNTER.hits.filter((h) => t >= h).length;
	if (n === 0 || t > (COUNTER.to ?? cutsEnd) || cardState(t) > 0.05) return null; // disembunyikan saat kartu (polaroid di kiri bawah)
	const last = COUNTER.hits[n - 1];
	const s = pop(t, last, 0.4);
	return (
		<div style={{position: 'absolute', left: 0, right: 0, top: COUNTER.y ?? 1420, display: 'flex', justifyContent: 'center'}}>
			<div style={{display: 'flex', alignItems: 'center', gap: 16, background: CRM, border: `5px solid ${BR}`, borderRadius: 24, padding: '10px 26px',
				boxShadow: `0 7px 0 ${BR}`, transform: `scale(${0.9 + 0.1 * s}) rotate(-2deg)`}}>
				<span style={{fontFamily: MONO, fontWeight: 700, fontSize: 38, color: BR}}>{COUNTER.label}</span>
				<span style={{fontFamily: SLAB, fontSize: 64, color: C.or, transform: `scale(${s})`, display: 'inline-block', minWidth: 60, textAlign: 'center'}}>{n}</span>
				<span style={{fontFamily: EMO, fontSize: 50, transform: `scale(${s})`, display: 'inline-block'}}>{COUNTER.emoji || '❤️'}</span>
			</div>
		</div>
	);
};

const NameTag = ({t}) => {
	if (!NAMETAG) return null;
	const v = vis(t, NAMETAG.from, NAMETAG.to, 0.3);
	if (v <= 0) return null;
	return (
		<div style={{position: 'absolute', left: 70, top: 1080, opacity: v, transform: `translateX(${(1 - v) * -60}px)`}}>
			<div style={{background: G3 ? CRM : '#fff', borderRadius: 26, padding: '12px 28px', boxShadow: G3 ? `0 6px 0 ${BR}` : '0 10px 26px rgba(0,0,0,.25)', borderLeft: `12px solid ${G3 ? BR : C.or}`}}>
				<div style={{fontWeight: 900, fontSize: 46, color: C.ink}}>{NAMETAG.name}</div>
				{NAMETAG.sub && <div style={{fontWeight: 700, fontSize: 30, color: C.or2}}>{NAMETAG.sub}</div>}
			</div>
		</div>
	);
};

// Logo kecil kiri atas; memudar saat judul/kartu tampil supaya tidak bertabrakan
const Logo = ({t}) => {
	if (!LOGO) return null;
	const busy = [...TITLES.filter((k) => k.kind !== 'teks' && k.kind !== 'jam'), ...NOTES].some((k) => t > k.from - 0.3 && t < k.to + 0.3) ? 1 : 0;
	const a = (1 - cardState(t)) * (busy ? 0 : 1);
	return <Img src={staticFile('logo-upg-mendatar.png')} style={{position: 'absolute', left: 60, top: 250, width: 270, opacity: a * 0.95,
		filter: 'drop-shadow(0 2px 6px rgba(255,255,255,.9))'}} />;
};

// Penutup standar konten organik UPG (keputusan Dir 23 Nov 2026): oranye penuh menyapu dari bawah, logo mendatar putih,
// 1 kalimat penutup per konten (END.line1), 1 tombol putih (END.cta). Tanpa wajah dokter,
// tanpa nama cabang. Beda dari Ruma (mint, diam). Teks di atas oranye selalu gelap #2A2A2A.
const EndCard = ({t}) => {
	const w = prog(t, cutsEnd - 0.4, cutsEnd); // menyapu di atas 0,4 dtk terakhir video
	const cta = END.komen ? 'Komen' : (END.cta || 'Simpan untuk nanti');
	return (
		<AbsoluteFill style={{alignItems: 'center'}}>
			<AbsoluteFill style={{background: C.or, transform: `translateY(${(1 - w) * 100}%)`}} />
			<Img src={staticFile('logo-upg-mendatar-putih.png')} style={{position: 'absolute', top: 560, width: 640, transform: `scale(${pop(t, cutsEnd + 0.3, 0.45)})`}} />
			{END.line1 && <div style={{position: 'absolute', top: 840, left: 90, right: 90, fontWeight: 900, fontSize: 60, lineHeight: 1.18, color: C.ink, textAlign: 'center', whiteSpace: 'pre-line',
				opacity: prog(t, cutsEnd + 0.7, cutsEnd + 1.0)}}>{END.line1}</div>}
			{END.line2 && <div style={{position: 'absolute', top: 1010, left: 90, right: 90, fontWeight: 800, fontSize: 42, color: C.ink, textAlign: 'center', opacity: prog(t, cutsEnd + 0.8, cutsEnd + 1.1)}}>{END.line2}</div>}
			<div style={{position: 'absolute', top: 1110, display: 'flex', alignItems: 'center', gap: 14, background: '#fff', borderRadius: 48, padding: '20px 56px',
				fontWeight: 900, fontSize: 50, color: C.ink, transform: `scale(${pop(t, cutsEnd + 1.0, 0.4)})`}}>
				{END.komen && <span style={{fontFamily: EMO}}>💬</span>}{cta}</div>
		</AbsoluteFill>
	);
};

// Kilatan putih tipis di pergantian take (bukan saat kartu) supaya potongan terasa disengaja
const CutFlash = ({t}) => {
	let a = 0;
	for (const c of CUTS) if (c.flash && t >= c.start && t < c.start + 0.18) a = 1 - (t - c.start) / 0.18;
	return a > 0 ? <AbsoluteFill style={{background: '#fff', opacity: a * 0.55}} /> : null;
};

export const Main = () => {
	const t = useCurrentFrame() / FPS;
	const main = t < cutsEnd;
	return (
		<AbsoluteFill style={{backgroundColor: '#000', fontFamily: FONT}}>
			<style>{fontFace}</style>
			{main && <CardBg t={t} />}
			{main && <Cards t={t} />}
			{main && <VideoLayer t={t} />}
			{main && <CutFlash t={t} />}
			{main && <Logo t={t} />}
			{main && <Titles t={t} />}
			{main && <NameTag t={t} />}
			{main && <Stickers t={t} />}
			{main && <Notes t={t} />}
			{main && <Counter t={t} />}
			{main && <Captions t={t} />}
			{t >= cutsEnd - 0.4 && <EndCard t={t} />}
			{SFX.map((s, i) => (
				<Sequence key={i} from={Math.max(0, Math.round(s.at * FPS))} durationInFrames={Math.round((s.len || 3) * FPS)}>
					<Audio src={staticFile(`sfx/${s.file}`)} volume={s.vol ?? 0.5} />
				</Sequence>
			))}
			{MUSIC && (
				<Audio src={staticFile(MUSIC.file)} loop
					volume={(f) => MUSIC.volume * interpolate(f / FPS, [0, 1, cutsEnd + END.sec - 1.5, cutsEnd + END.sec], [0, 1, 1, 0], clamp)} />
			)}
		</AbsoluteFill>
	);
};
