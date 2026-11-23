// GrowWith "UPG Dental Care belum lengkap tanpa…": footage + label nama/peran + hook + kartu penutup.
import {AbsoluteFill, OffthreadVideo, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {SEG, TOTAL} from './timeline.js';
const G = {gr: '#01AB7A', or: '#F28621', ink: '#020202', soft: '#F3F4F7'};
const SH = '0 10px 28px rgba(0,0,0,.28)';
const fontFace = [600, 700, 800, 900].map((w) => `@font-face{font-family:M;font-weight:${w};src:url(${staticFile(`fonts/montserrat-latin-${w}-normal.woff2`)}) format("woff2")}`).join('\n');
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const pop = (f, fps, at) => spring({frame: f - at * fps, fps, config: {damping: 12, stiffness: 190, mass: 0.6}});

const Hook = ({t, f, fps}) => {
	const s = SEG[0]; if (t >= s.start + s.dur) return null;
	const a = pop(f, fps, 0.15), b = pop(f, fps, 0.75);
	const box = (bg) => ({display: 'inline-block', background: bg, color: G.ink, fontFamily: 'M', fontWeight: 900, padding: '8px 28px 14px', borderRadius: 22, boxShadow: SH, whiteSpace: 'nowrap'});
	return (
		<div style={{position: 'absolute', left: 0, right: 0, top: 290, textAlign: 'center'}}>
			<div style={{transform: `scale(${a})`}}><span style={{...box(G.gr), fontSize: 92}}>UPG Dental Care</span></div>
			<div style={{marginTop: 22, transform: `scale(${b})`}}><span style={{...box(G.or), fontSize: 76}}>belum lengkap tanpa…</span></div>
		</div>
	);
};

// Kalimat tetap di atas + nama/peran berganti tanpa hilang (menyambung "belum lengkap tanpa…")
const ORANG = SEG.filter((s) => s.name);
const Label = ({t, f, fps}) => {
	const s = ORANG.find((x) => t >= x.start && t < x.start + x.dur); if (!s) return null;
	const first = s === ORANG[0];
	const k = first ? pop(f, fps, s.start) : 1;
	const lt = t - s.start, up = interpolate(lt, [0, 0.14], [46, 0], clamp), op = interpolate(lt, [0, 0.08], [0.2, 1], clamp);
	const rb = interpolate(lt, [0.06, 0.22], [0, 1], clamp);
	return (
		<div style={{position: 'absolute', left: 0, right: 0, top: 250, textAlign: 'center'}}>
			<div style={{transform: `scale(${k})`}}><span style={{display: 'inline-block', background: '#fff', color: G.ink, fontFamily: 'M', fontWeight: 800, fontSize: 40, padding: '8px 26px 11px', borderRadius: 999, boxShadow: SH, whiteSpace: 'nowrap'}}>UPG Dental Care belum lengkap tanpa…</span></div>
			<div style={{marginTop: 14, height: 112, overflow: 'hidden'}}>
				<span style={{display: 'inline-block', transform: `translateY(${up}px) scale(${k})`, opacity: op, background: G.gr, color: G.ink, fontFamily: 'M', fontWeight: 900, fontSize: 84, padding: '4px 30px 10px', borderRadius: 22, whiteSpace: 'nowrap'}}>{s.name}</span>
			</div>
			<div style={{marginTop: 6, opacity: rb, transform: `translateY(${(1 - rb) * 16}px)`}}>
				<span style={{display: 'inline-block', background: G.or, color: G.ink, fontFamily: 'M', fontWeight: 800, fontSize: 42, padding: '6px 24px 10px', borderRadius: 999, boxShadow: SH, whiteSpace: 'nowrap'}}>{s.role}</span>
			</div>
		</div>
	);
};

// Efek pergantian: kilat putih singkat + zoom-punch, sinkron dengan whoosh
const cutAt = (t) => SEG.slice(1).map((s) => s.start).filter((c) => t >= c && t < c + 0.25)[0];
const Flash = ({t}) => {
	const c = cutAt(t); if (c === undefined) return null;
	return <AbsoluteFill style={{background: '#fff', opacity: interpolate(t - c, [0, 0.12], [0.55, 0], clamp)}} />;
};

const End = ({t, f, fps}) => {
	const s = SEG[SEG.length - 1]; if (t < s.start) return null;
	const k = interpolate(t, [s.start, s.start + 0.3], [0, 1], clamp);
	const a = pop(f, fps, s.start + 0.2), b = pop(f, fps, s.start + 0.9), c = interpolate(t, [s.start + 1.4, s.start + 1.7], [0, 1], clamp);
	return (
		<AbsoluteFill style={{background: `rgba(243,244,247,${0.93 * k})`, alignItems: 'center', justifyContent: 'center', textAlign: 'center'}}>
			<div style={{transform: `scale(${a})`, fontFamily: 'M', fontWeight: 900, fontSize: 92, lineHeight: 1.12, color: G.gr, letterSpacing: -2}}>UPG Dental Care<br />belum lengkap<br />tanpa…</div>
			<div style={{marginTop: 30, transform: `scale(${b})`}}><span style={{display: 'inline-block', background: G.or, color: G.ink, fontFamily: 'M', fontWeight: 900, fontSize: 130, padding: '4px 40px 16px', borderRadius: 28, boxShadow: SH}}>kamu 🫶</span></div>
			<div style={{marginTop: 50, opacity: c}}><span style={{display: 'inline-block', background: G.ink, color: '#fff', fontFamily: 'M', fontWeight: 800, fontSize: 44, padding: '14px 38px', borderRadius: 999}}>Follow @growwithupgruma</span></div>
		</AbsoluteFill>
	);
};

export const Main = () => {
	const f = useCurrentFrame(); const {fps} = useVideoConfig(); const t = f / fps;
	return (
		<AbsoluteFill style={{background: '#000'}}>
			<style>{fontFace}</style>
			<AbsoluteFill style={{transform: `scale(${(() => { const c = cutAt(t); return c === undefined ? 1 : interpolate(t - c, [0, 0.22], [1.07, 1], clamp); })()})`}}><OffthreadVideo src={staticFile('footage.mp4')} /></AbsoluteFill>
			<Hook t={t} f={f} fps={fps} />
			<Label t={t} f={f} fps={fps} />
			<Flash t={t} />
			<End t={t} f={f} fps={fps} />
		</AbsoluteFill>
	);
};
export const _T = TOTAL;
