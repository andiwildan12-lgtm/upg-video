// Komposisi Edit Rekaman UPG Video (Remotion). Diadaptasi dari template skill `shortform-edit`.
// Overlay didesain di kanvas 1080x1920 lalu di-scale ke resolusi footage (S = lebar / 1080).
// Isi proyek cukup lewat src/timeline.js — file ini jarang perlu diubah.
import {AbsoluteFill, Audio, Easing, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {CAPTIONS, CUTS, END_CARD_SEC, END_TITLE, LABELS, LOGO_BUG, LOGO_HIDE, MUSIC, NOTE, PROMO, WA, totalSec} from './timeline.js';

const W = 1080, H = 1920;
const C = {or: '#FA7209', yl: '#F8C000', or2: '#CF6515', ink: '#2A2A2A', bg: '#FFF7EF', wa: '#1FAF55'};
const FONT = 'Nunito, sans-serif';
const ease = Easing.bezier(0.22, 1, 0.36, 1);
const prog = (t, a, b) => interpolate(t, [a, b], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease});
const fade = (t, from, to, d = 0.25) => Math.min(prog(t, from, from + d), 1 - prog(t, to - d, to));

const fontFace = `
@font-face{font-family:Nunito;font-weight:600;src:url(${staticFile('fonts/nunito-latin-600-normal.woff2')}) format("woff2")}
@font-face{font-family:Nunito;font-weight:800;src:url(${staticFile('fonts/nunito-latin-800-normal.woff2')}) format("woff2")}
@font-face{font-family:Nunito;font-weight:900;src:url(${staticFile('fonts/nunito-latin-900-normal.woff2')}) format("woff2")}`;

// Caption: kata muncul dari blur. Kata hl = kotak oranye + teks putih (teks oranye tipis sulit dibaca).
const Word = ({w, t}) => {
	const p = prog(t, w.at, w.at + 0.16);
	const base = {display: 'inline-block', margin: '0 8px', fontSize: 80, fontWeight: 900, lineHeight: 1.15, opacity: p,
		filter: `blur(${(1 - p) * 10}px)`, transform: `translateY(${(1 - p) * 16}px)`};
	return w.hl
		? <span style={{...base, color: '#fff', background: C.or, borderRadius: 18, padding: '2px 18px'}}>{w.text}</span>
		: <span style={{...base, color: '#fff', textShadow: '0 3px 10px rgba(0,0,0,.75), 0 0 2px rgba(0,0,0,.9)'}}>{w.text}</span>;
};
const Captions = ({t}) => {
	const g = CAPTIONS.find((c) => t >= c.from && t < c.to);
	if (!g) return null;
	return <div style={{position: 'absolute', left: 90, right: 150, top: 1260, textAlign: 'center'}}>{g.words.map((w, i) => <Word key={i} w={w} t={t} />)}</div>;
};

const Label = ({l, t}) => {
	const a = fade(t, l.from, l.to);
	if (a <= 0) return null;
	const top = l.pos === 'center' ? 820 : 300;
	return (
		<div style={{position: 'absolute', left: 90, right: 150, top, textAlign: 'center', opacity: a, transform: `translateY(${(1 - a) * 30}px)`}}>
			<span style={{display: 'inline-block', background: 'rgba(255,255,255,.94)', color: C.ink, fontWeight: 900, fontSize: 64, lineHeight: 1.15,
				padding: '18px 34px', borderRadius: 28, boxShadow: '0 12px 30px rgba(0,0,0,.25)'}}>{l.text}</span>
		</div>
	);
};

const Note = ({t}) => {
	if (!NOTE) return null;
	const a = fade(t, NOTE.from, NOTE.to, 0.3);
	if (a <= 0) return null;
	return <div style={{position: 'absolute', left: 0, right: 0, top: 1560, textAlign: 'center', opacity: a * 0.95, fontWeight: 800, fontSize: 38, color: '#fff',
		textShadow: '0 2px 6px rgba(0,0,0,.8)'}}>{NOTE.text}</div>;
};

const Promo = ({t}) => {
	if (!PROMO) return null;
	const a = fade(t, PROMO.from, PROMO.to, 0.35);
	if (a <= 0) return null;
	const top = PROMO.pos === 'center' ? 560 : 280;
	const pp = prog(t, PROMO.from + 0.35, PROMO.from + 0.8);
	return (
		<div style={{position: 'absolute', left: 110, width: 820, top, opacity: a, transform: `translateY(${(1 - a) * 80}px)`,
			borderRadius: 48, background: `linear-gradient(160deg, ${C.or} 0%, #F8A100 60%, ${C.yl} 100%)`,
			boxShadow: '0 24px 60px rgba(0,0,0,.35)', color: '#fff', textAlign: 'center', padding: '44px 30px 34px'}}>
			<div style={{fontWeight: 900, fontSize: 66, letterSpacing: 3, lineHeight: 1.05}}>{PROMO.title}</div>
			<div style={{margin: '26px auto 0', width: 660, borderRadius: 34, background: '#fff', color: C.or, fontWeight: 900, fontSize: 112,
				lineHeight: 1.3, transform: `scale(${0.6 + 0.4 * pp})`, opacity: pp}}>{PROMO.price}</div>
			{(PROMO.lines || []).map((s, i) => <div key={i} style={{marginTop: 18, fontWeight: 900, fontSize: 56}}>{s}</div>)}
			{PROMO.note && <div style={{marginTop: 18, fontWeight: 600, fontSize: 32}}>{PROMO.note}</div>}
		</div>
	);
};

// Logo kecil memudar saat kartu promo tampil (agar tidak bertabrakan).
const LogoBug = ({t}) => (
	<div style={{position: 'absolute', right: 130, top: 240, width: 170,
		opacity: (LOGO_HIDE || []).reduce((a, [x, y]) => Math.min(a, 1 - fade(t, x, y, 0.25)), 1),
		filter: 'drop-shadow(0 2px 6px rgba(255,255,255,.9)) drop-shadow(0 2px 10px rgba(0,0,0,.25))'}}>
		<Img src={staticFile('logo-upg-transparan.png')} style={{width: '100%'}} />
	</div>
);

const EndCard = ({t0, t}) => {
	const a = prog(t, t0, t0 + 0.5);
	return (
		<AbsoluteFill style={{background: C.bg, opacity: a, alignItems: 'center'}}>
			<div style={{marginTop: 420, width: 640}}>
				<Img src={staticFile('logo-upg-transparan.png')} style={{width: '100%'}} />
			</div>
			<div style={{marginTop: 110, fontWeight: 900, fontSize: 60, color: C.ink}}>{END_TITLE}</div>
			<div style={{marginTop: 14, fontWeight: 700, fontSize: 40, color: C.or2}}>Chat admin via WhatsApp</div>
			<div style={{marginTop: 16, background: C.wa, color: '#fff', fontWeight: 900, fontSize: 80, borderRadius: 999, padding: '10px 40px'}}>{WA}</div>
		</AbsoluteFill>
	);
};

export const Main = () => {
	const frame = useCurrentFrame();
	const {fps, width, durationInFrames} = useVideoConfig();
	const t = frame / fps;
	const S = width / W;
	const cutsEnd = CUTS.reduce((a, c) => a + c.dur, 0);
	let acc = 0;
	return (
		<AbsoluteFill style={{backgroundColor: '#000', fontFamily: FONT}}>
			<style>{fontFace}</style>
			{CUTS.map((c, i) => {
				const from = Math.round(acc * fps);
				acc += c.dur;
				return (
					<Sequence key={i} from={from} durationInFrames={Math.round(c.dur * fps)}>
						<OffthreadVideo src={staticFile('footage.mp4')} startFrom={Math.round(c.src * fps)} />
					</Sequence>
				);
			})}
			<AbsoluteFill>
				<div style={{position: 'absolute', left: 0, top: 0, width: W, height: H, transform: `scale(${S})`, transformOrigin: '0 0'}}>
					{t < cutsEnd && LABELS.map((l, i) => <Label key={i} l={l} t={t} />)}
					{t < cutsEnd && <Promo t={t} />}
					{t < cutsEnd && <Captions t={t} />}
					{t < cutsEnd && <Note t={t} />}
					{t < cutsEnd && LOGO_BUG && <LogoBug t={t} />}
					{END_CARD_SEC > 0 && t >= cutsEnd && <EndCard t0={cutsEnd} t={t} />}
				</div>
			</AbsoluteFill>
			{MUSIC && (
				<Audio src={staticFile(MUSIC.file)} loop
					volume={(f) => MUSIC.volume * interpolate(f, [0, 15, durationInFrames - 45, durationInFrames - 1], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})} />
			)}
		</AbsoluteFill>
	);
};

export const _totalSec = totalSec;
