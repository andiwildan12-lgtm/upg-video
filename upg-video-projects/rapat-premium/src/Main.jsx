// Rapat Dokter — Premium Cut (GrowWith). Footage + kata kunci kinetik + ikon SVG + kartu.
import {AbsoluteFill, Easing, OffthreadVideo, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {CAPTIONS, CARDS, ICONS, KEYS, TOTAL} from './timeline.js';

const G = {gr: '#00691d', yl: '#fbb03b', g2: '#009b5f', ink: '#000', cream: '#f5eee2'};
const fontFace = [600, 700, 800, 900].map((w) => `@font-face{font-family:M;font-weight:${w};src:url(${staticFile(`fonts/montserrat-latin-${w}-normal.woff2`)}) format("woff2")}`).join('\n');
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const ease = Easing.bezier(0.22, 1, 0.36, 1);
const out = (t, to, d = 0.18) => interpolate(t, [to - d, to], [1, 0], clamp);
const pop = (frame, fps, at) => spring({frame: frame - at * fps, fps, config: {damping: 11, stiffness: 170, mass: 0.7}});

// ---------- kata kunci kinetik ----------
const Key = ({k, t, frame, fps}) => {
	if (t < k.from || t > k.to) return null;
	const s = pop(frame, fps, k.from), o = out(t, k.to);
	const yl = k.style !== 'wh';
	return (
		<div style={{position: 'absolute', left: 60, right: 60, top: k.y ?? 1060, textAlign: 'center', opacity: o,
			transform: `scale(${0.4 + 0.6 * s}) rotate(${(1 - s) * (k.rot ?? -6)}deg)`}}>
			<span style={{display: 'inline-block', fontFamily: 'M', fontWeight: 900, fontSize: k.size ?? 104, lineHeight: 1.05, letterSpacing: -2, whiteSpace: 'nowrap',
				padding: yl ? '6px 30px 14px' : 0, borderRadius: 26, border: yl ? '7px solid #000' : 'none',
				background: yl ? (k.bg ?? G.yl) : 'transparent', color: yl ? (k.fg ?? G.ink) : '#fff',
				WebkitTextStroke: yl ? 0 : '4px #000', paintOrder: 'stroke fill', boxShadow: yl ? '10px 10px 0 #000' : 'none',
				textShadow: yl ? 'none' : '0 8px 30px rgba(0,0,0,.6)'}}>{k.text}</span>
		</div>
	);
};

// ---------- ikon SVG (garis hitam tebal, warna GrowWith) ----------
const S = {stroke: '#000', strokeWidth: 10, strokeLinejoin: 'round', strokeLinecap: 'round'};
const Tooth = ({x, y, s = 1, fill = '#fff'}) => (
	<path transform={`translate(${x},${y}) scale(${s})`} {...S} fill={fill}
		d="M-40,-45 C-60,-45 -62,-10 -50,15 C-42,32 -40,55 -30,60 C-20,64 -15,30 0,30 C15,30 20,64 30,60 C40,55 42,32 50,15 C62,-10 60,-45 40,-45 C25,-45 15,-35 0,-35 C-15,-35 -25,-45 -40,-45 Z" />
);
const icons = {
	rapor: (p) => (
		<g>
			<rect x="40" y="20" width="220" height="280" rx="22" fill="#fff" {...S} />
			<rect x="40" y="20" width="220" height="64" rx="22" fill={G.gr} {...S} />
			<text x="150" y="64" textAnchor="middle" fontFamily="M" fontWeight="900" fontSize="34" fill="#fff">RAPOR</text>
			{[120, 170, 220].map((y, i) => (
				<g key={y} opacity={interpolate(p, [0.3 + i * 0.15, 0.45 + i * 0.15], [0, 1], clamp)}>
					<rect x="70" y={y - 14} width="28" height="28" rx="6" fill={G.yl} {...S} strokeWidth="6" />
					<path d={`M75 ${y} l7 8 l14 -16`} {...S} strokeWidth="7" fill="none" stroke={G.gr} />
					<rect x="115" y={y - 8} width={110 - i * 20} height="16" rx="8" fill="#ddd" />
				</g>
			))}
		</g>
	),
	timeline: (p) => (
		<g>
			<line x1="40" y1="170" x2={40 + 330 * interpolate(p, [0, 0.6], [0, 1], clamp)} y2="170" {...S} strokeWidth="14" stroke={G.gr} />
			<Tooth x={70} y={110} s={0.9} fill="#e9e1cf" />
			<g opacity={interpolate(p, [0.55, 0.75], [0, 1], clamp)}><Tooth x={360} y={110} s={1.05} fill="#fff" />
				<path d="M410 40 l8 18 l20 2 l-15 13 l5 20 l-18 -11 l-18 11 l5 -20 l-15 -13 l20 -2 z" fill={G.yl} {...S} strokeWidth="6" /></g>
			<text x="80" y="240" textAnchor="middle" fontFamily="M" fontWeight="900" fontSize="27" fill="#000">BULAN 1</text>
			<text x="345" y="240" textAnchor="middle" fontFamily="M" fontWeight="900" fontSize="27" fill="#000" opacity={interpolate(p, [0.55, 0.75], [0, 1], clamp)}>AKHIR TAHUN</text>
		</g>
	),
	chart: (p) => (
		<g>
			{[0, 1, 2, 3].map((i) => {
				const h = (60 + i * 55) * interpolate(p, [i * 0.12, i * 0.12 + 0.3], [0, 1], clamp);
				return <rect key={i} x={50 + i * 80} y={290 - h} width="56" height={h} rx="8" fill={i === 3 ? G.yl : G.g2} {...S} strokeWidth="7" />;
			})}
			<path d="M50 230 L150 180 L230 190 L340 70" fill="none" {...S} strokeWidth="12" stroke="#000" strokeDasharray="500" strokeDashoffset={500 * (1 - interpolate(p, [0.3, 0.8], [0, 1], clamp))} />
			<path d="M300 60 L350 62 L345 110" fill="none" {...S} strokeWidth="12" opacity={interpolate(p, [0.75, 0.85], [0, 1], clamp)} />
		</g>
	),
	hierarki: (p) => (
		<g>
			<rect x="150" y="20" width="100" height="70" rx="14" fill={G.gr} {...S} />
			<path d="M200 90 V130 M100 130 H300 M100 130 V160 M300 130 V160" {...S} fill="none" />
			<rect x="50" y="160" width="100" height="70" rx="14" fill="#fff" {...S} />
			<rect x="250" y="160" width="100" height="70" rx="14" fill="#fff" {...S} />
			<g opacity={interpolate(p, [0.35, 0.5], [0, 1], clamp)} transform={`scale(${interpolate(p, [0.35, 0.55], [1.4, 1], clamp)})`} style={{transformOrigin: '200px 125px'}}>
				<path d="M60 20 L340 240 M340 20 L60 240" stroke="#e23b2e" strokeWidth="26" strokeLinecap="round" />
			</g>
		</g>
	),
	sejajar: (p) => (
		<g>
			{[90, 310].map((x, i) => (
				<g key={x} transform={`translate(0,${(1 - interpolate(p, [i * 0.15, i * 0.15 + 0.35], [0, 1], clamp)) * 60})`}>
					<circle cx={x} cy="80" r="45" fill={i ? G.yl : G.g2} {...S} />
					<path d={`M${x - 70} 240 C${x - 70} 150 ${x + 70} 150 ${x + 70} 240 Z`} fill={i ? G.yl : G.g2} {...S} />
				</g>
			))}
			<g opacity={interpolate(p, [0.5, 0.65], [0, 1], clamp)}>
				<rect x="170" y="110" width="60" height="16" rx="6" fill="#000" /><rect x="170" y="145" width="60" height="16" rx="6" fill="#000" />
			</g>
		</g>
	),
	tangga: (p) => (
		<g>
			{[0, 1, 2, 3].map((i) => <rect key={i} x={60 + i * 70} y={240 - i * 55} width="80" height={30 + i * 55} rx="8" fill={i === 1 ? G.yl : '#fff'} {...S} strokeWidth="7" />)}
			<circle cx="170" cy={150 - interpolate(p, [0.2, 0.6], [0, 0], clamp)} r="22" fill={G.gr} {...S} strokeWidth="6" />
			<path d="M375 210 V60 M350 85 L375 55 L400 85" {...S} strokeWidth="12" fill="none" opacity={interpolate(p, [0.4, 0.55], [0, 1], clamp)} />
			<path d="M25 60 V210 M0 185 L25 215 L50 185" {...S} strokeWidth="12" fill="none" opacity={interpolate(p, [0.25, 0.4], [0, 1], clamp)} />
		</g>
	),
	timbangan: (p, t) => {
		const a = Math.sin(t * 3.2) * 9 * interpolate(p, [0, 0.4], [0, 1], clamp);
		return (
			<g>
				<path d="M200 60 V260 M130 270 H270" {...S} strokeWidth="14" fill="none" />
				<g transform={`rotate(${a} 200 70)`}>
					<path d="M60 70 H340" {...S} strokeWidth="14" />
					<path d="M60 70 L20 170 H100 Z M340 70 L300 170 H380 Z" fill="none" {...S} strokeWidth="7" />
					<path d="M15 170 Q60 220 105 170 Z" fill={G.g2} {...S} strokeWidth="7" />
					<path d="M295 170 Q340 220 385 170 Z" fill={G.yl} {...S} strokeWidth="7" />
				</g>
				<circle cx="200" cy="60" r="18" fill="#000" />
			</g>
		);
	},
};
const Icon = ({ic, t, frame, fps}) => {
	if (t < ic.from || t > ic.to) return null;
	const s = pop(frame, fps, ic.from), o = out(t, ic.to, 0.2);
	const p = interpolate(t, [ic.from, ic.from + (ic.anim ?? 1.2)], [0, 1], clamp);
	const W = ic.w ?? 430;
	return (
		<div style={{position: 'absolute', left: ic.x ?? 600, top: ic.y ?? 300, width: W, opacity: o, transform: `scale(${s}) translateY(${Math.sin(t * 2) * 6}px)`, transformOrigin: 'center'}}>
			<div style={{background: G.cream, border: '7px solid #000', borderRadius: 34, boxShadow: '12px 12px 0 #000', padding: 18}}>
				<svg viewBox="0 0 440 310" width="100%">{icons[ic.name](p, t)}</svg>
			</div>
		</div>
	);
};

// ---------- kartu judul & penutup ----------
const Card = ({c, t, frame, fps}) => {
	if (t < c.from || t > c.to) return null;
	const s = pop(frame, fps, c.from), o = out(t, c.to, 0.15);
	return (
		<AbsoluteFill style={{background: c.full ? 'rgba(0,105,29,.92)' : 'transparent', opacity: o, alignItems: 'center', justifyContent: 'center'}}>
			<div style={{transform: `scale(${0.6 + 0.4 * s})`, textAlign: 'center', padding: '0 70px', marginTop: c.full ? 0 : 900}}>
				{c.kicker && <div style={{display: 'inline-block', background: G.yl, color: '#000', fontFamily: 'M', fontWeight: 900, fontSize: 40, padding: '10px 30px', borderRadius: 999, border: '6px solid #000', letterSpacing: 1}}>{c.kicker}</div>}
				<div style={{marginTop: 34, display: 'inline-block', background: c.full ? 'transparent' : G.yl, border: c.full ? 'none' : '7px solid #000', boxShadow: c.full ? 'none' : '12px 12px 0 #000',
					borderRadius: 34, padding: c.full ? 0 : '26px 40px', color: c.full ? '#fff' : '#000', fontFamily: 'M', fontWeight: 900, fontSize: c.size ?? 92, lineHeight: 1.08}}>
					{c.lines.map((l, i) => <div key={i} dangerouslySetInnerHTML={{__html: l}} />)}
				</div>
				{c.handle && <div style={{marginTop: 34}}><span style={{display: 'inline-block', background: G.gr, color: '#fff', fontFamily: 'M', fontWeight: 800, fontSize: 46, padding: '10px 34px', borderRadius: 999, border: '6px solid #000', opacity: interpolate(t, [c.from + 0.5, c.from + 0.9], [0, 1], clamp)}}>{c.handle}</span></div>}
			</div>
		</AbsoluteFill>
	);
};

// ---------- caption kecil (sound-off) ----------
const Captions = ({t}) => {
	const g = CAPTIONS.find((c) => t >= c.from && t < c.to);
	if (!g) return null;
	return (
		<div style={{position: 'absolute', left: 90, right: 150, top: 1440, textAlign: 'center'}}>
			{g.words.map((w, i) => <span key={i} style={{display: 'inline-block', margin: '0 7px', fontFamily: 'M', fontWeight: 800, fontSize: 50, color: t >= w.at ? '#fff' : 'rgba(255,255,255,.55)',
				WebkitTextStroke: '3px #000', paintOrder: 'stroke fill', textShadow: '0 3px 10px rgba(0,0,0,.6)'}}>{w.text}</span>)}
		</div>
	);
};

export const Main = () => {
	const frame = useCurrentFrame();
	const {fps, width} = useVideoConfig();
	const t = frame / fps, S2 = width / 1080;
	return (
		<AbsoluteFill style={{backgroundColor: '#000'}}>
			<style>{fontFace}</style>
			<OffthreadVideo src={staticFile('footage.mp4')} />
			<AbsoluteFill>
				<div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: 1920, transform: `scale(${S2})`, transformOrigin: '0 0'}}>
					{ICONS.map((ic, i) => <Icon key={i} ic={ic} t={t} frame={frame} fps={fps} />)}
					{KEYS.map((k, i) => <Key key={i} k={k} t={t} frame={frame} fps={fps} />)}
					<Captions t={t} />
					{CARDS.map((c, i) => <Card key={i} c={c} t={t} frame={frame} fps={fps} />)}
				</div>
			</AbsoluteFill>
		</AbsoluteFill>
	);
};
export const _TOTAL = TOTAL;
