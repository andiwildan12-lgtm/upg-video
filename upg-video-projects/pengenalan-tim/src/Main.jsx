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

const Label = ({s, t, f, fps}) => {
	if (!s.name || t < s.start || t >= s.start + s.dur) return null;
	const a = pop(f, fps, s.start + 0.05), b = pop(f, fps, s.start + 0.2);
	return (
		<div style={{position: 'absolute', left: 0, right: 0, top: 270, textAlign: 'center'}}>
			<div style={{transform: `scale(${0.5 + 0.5 * a})`, opacity: a}}>
				<span style={{display: 'inline-block', background: G.gr, color: G.ink, fontFamily: 'M', fontWeight: 900, fontSize: 84, padding: '6px 30px 12px', borderRadius: 22, boxShadow: SH, whiteSpace: 'nowrap'}}>{s.name}</span>
			</div>
			<div style={{marginTop: 16, transform: `translateY(${(1 - b) * 30}px)`, opacity: b}}>
				<span style={{display: 'inline-block', background: '#fff', color: G.ink, fontFamily: 'M', fontWeight: 800, fontSize: 44, padding: '8px 26px 12px', borderRadius: 999, boxShadow: SH, whiteSpace: 'nowrap'}}>{s.role}</span>
			</div>
		</div>
	);
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
			<OffthreadVideo src={staticFile('footage.mp4')} />
			<Hook t={t} f={f} fps={fps} />
			{SEG.map((s, i) => <Label key={i} s={s} t={t} f={f} fps={fps} />)}
			<End t={t} f={f} fps={fps} />
		</AbsoluteFill>
	);
};
export const _T = TOTAL;
