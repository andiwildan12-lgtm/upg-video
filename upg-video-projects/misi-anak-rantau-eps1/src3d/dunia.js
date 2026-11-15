/* Dunia 3D Misi Anak Rantau — tokoh TANPA MATA, ruangan, properti. Three.js r149 (global THREE). */
THREE.ColorManagement.legacyMode = false;
const W3 = {};
W3.M = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: o.r ?? 0.7, metalness: o.m ?? 0, transparent: !!o.op, opacity: o.op ?? 1, ...(o.x || {}) });
W3.mesh = function (g, m, x, y, z, o = {}) {
  const k = new THREE.Mesh(g, m); k.position.set(x, y, z); k.castShadow = o.cs !== false; k.receiveShadow = true;
  if (o.rx) k.rotation.x = o.rx; if (o.ry) k.rotation.y = o.ry; if (o.rz) k.rotation.z = o.rz; if (o.s) k.scale.set(...o.s);
  (o.p || W3.S).add(k); return k;
};
W3.tex = function (draw, w = 512, h = 512, rep) {
  const cv = document.createElement('canvas'); cv.width = w; cv.height = h; draw(cv.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(cv); t.encoding = THREE.sRGBEncoding; if (rep) { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(...rep); } return t;
};
W3.tiles = (c1, c2, n, rep) => W3.tex((g, w) => { g.fillStyle = c1; g.fillRect(0, 0, w, w); g.strokeStyle = c2; g.lineWidth = 6; for (let i = 0; i <= n; i++) { g.beginPath(); g.moveTo(i * w / n, 0); g.lineTo(i * w / n, w); g.stroke(); g.beginPath(); g.moveTo(0, i * w / n); g.lineTo(w, i * w / n); g.stroke(); } }, 512, 512, rep);
W3.wood = (rep) => W3.tex((g, w) => { for (let i = 0; i < 8; i++) { g.fillStyle = i % 2 ? '#C9A27C' : '#D2AE88'; g.fillRect(0, i * w / 8, w, w / 8); g.fillStyle = 'rgba(120,80,50,.25)'; g.fillRect(((i * 137) % w), i * w / 8, 4, w / 8); } }, 512, 512, rep);

/* ---------- bagian tubuh ---------- */
const SK = '#E2A982', SKD = '#C98E66';
function limb(p, col, a, b, r) {
  a = new THREE.Vector3(...a); b = new THREE.Vector3(...b); const d = b.clone().sub(a), L = d.length();
  const k = W3.mesh(new THREE.CapsuleGeometry(r, L, 6, 14), W3.M(col), 0, 0, 0, { p }); k.position.copy(a.clone().add(b).multiplyScalar(0.5));
  k.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.normalize()); return k;
}
function arm(p, col, sh, el, ha, r = 0.065) { limb(p, col, sh, el, r); limb(p, col, el, ha, r * 0.92); W3.mesh(new THREE.SphereGeometry(r * 1.15, 18, 18), W3.M(SK), ...ha, { p }); }
function face(p, y, z, mood, w = 1) {      // hidung kecil + mulut, TANPA MATA
  W3.mesh(new THREE.SphereGeometry(0.028, 14, 14), W3.M(SKD), 0, y, z + 0.005, { p, s: [0.8, 1.2, 0.9] });
  const my = y - 0.1, mz = z - 0.02;
  if (mood === 'o') W3.mesh(new THREE.SphereGeometry(0.045, 18, 18), W3.M('#5E2A1E'), 0, my, mz, { p, s: [0.9, 1.25, 0.35] });
  else if (mood === 'flat') W3.mesh(new THREE.CapsuleGeometry(0.012, 0.06 * w, 4, 8), W3.M('#5E2A1E'), 0, my, mz, { p, rz: Math.PI / 2 });
  else if (mood === 'worry') { const t = W3.mesh(new THREE.TorusGeometry(0.04 * w, 0.011, 8, 20, Math.PI), W3.M('#5E2A1E'), 0, my - 0.03, mz, { p }); }
  else { const t = W3.mesh(new THREE.TorusGeometry(0.045 * w, 0.012, 8, 20, Math.PI), W3.M('#5E2A1E'), 0, my + 0.02, mz, { p, rz: Math.PI }); }
  // pipi merona
  W3.mesh(new THREE.SphereGeometry(0.035, 12, 12), W3.M('#EFA394', { op: 0.55 }), -0.13, y - 0.07, z - 0.05, { p, s: [1, 0.6, 0.3], cs: false });
  W3.mesh(new THREE.SphereGeometry(0.035, 12, 12), W3.M('#EFA394', { op: 0.55 }), 0.13, y - 0.07, z - 0.05, { p, s: [1, 0.6, 0.3], cs: false });
}
/* pose lengan: [bahu, siku, tangan] kiri & kanan, koordinat lokal tokoh (depan = +z) */
const POSE = {
  down: [[-0.27, 1.36, 0], [-0.33, 1.08, 0.02], [-0.34, 0.82, 0.05]],
  head: [[-0.27, 1.36, 0], [-0.42, 1.55, 0.12], [-0.27, 1.83, 0.12]],
  up: [[-0.27, 1.36, 0], [-0.42, 1.58, 0.06], [-0.4, 1.86, 0.1]],
  brush: [[-0.27, 1.36, 0], [-0.4, 1.38, 0.25], [-0.22, 1.68, 0.36]],
  point: [[-0.27, 1.36, 0], [-0.42, 1.3, 0.25], [-0.62, 1.2, 0.45]],
  phone: [[-0.27, 1.36, 0], [-0.22, 1.12, 0.25], [-0.06, 1.3, 0.36]],
  hip: [[-0.27, 1.36, 0], [-0.46, 1.14, -0.02], [-0.26, 1.0, 0.06]],
  hold: [[-0.27, 1.36, 0], [-0.3, 1.12, 0.2], [-0.26, 1.08, 0.38]],
  raise: [[-0.27, 1.36, 0], [-0.38, 1.6, 0.15], [-0.3, 1.92, 0.25]],
  cup: [[-0.27, 1.36, 0], [-0.3, 1.12, 0.18], [-0.2, 1.3, 0.3]],
  cross: [[-0.27, 1.36, 0], [-0.3, 1.12, 0.2], [0.1, 1.18, 0.24]],
  note: [[-0.27, 1.36, 0], [-0.28, 1.12, 0.2], [-0.1, 1.2, 0.3]],
};
const mir = a => a.map(([x, y, z]) => [-x, y, z]);
function arms(p, col, L, R, r) { const l = POSE[L], rr = mir(POSE[R]); arm(p, col, ...l, r); arm(p, col, ...rr, r); return { L: l[2], R: rr[2] }; }

W3.toothbrush = function (p, at, soft, rot = [0, 0, 0.3]) {
  const g = new THREE.Group(); g.position.set(...at); g.rotation.set(...rot); p.add(g);
  W3.mesh(new THREE.CapsuleGeometry(0.018, 0.26, 4, 10), W3.M(soft ? '#8FD3E8' : '#E0533D', { r: 0.4 }), 0, 0.13, 0, { p: g });
  W3.mesh(new THREE.BoxGeometry(0.045, 0.07, 0.03), W3.M('#ffffff'), 0, 0.3, 0.012, { p: g });
  W3.mesh(new THREE.BoxGeometry(0.04, 0.06, 0.035), W3.M(soft ? '#D9F3FA' : '#3A3A3A'), 0, 0.3, 0.04, { p: g });
  return g;
};
W3.phone = (p, at, rot = [0.4, 0, 0]) => { const g = new THREE.Group(); g.position.set(...at); g.rotation.set(...rot); p.add(g); W3.mesh(new THREE.BoxGeometry(0.1, 0.19, 0.015), W3.M('#1E1E28', { r: 0.3 }), 0, 0, 0, { p: g }); W3.mesh(new THREE.PlaneGeometry(0.088, 0.17), W3.M('#9FD8F0', { x: { emissive: '#7FC8E8', emissiveIntensity: 0.6 } }), 0, 0, 0.009, { p: g }); return g; };
W3.mug = (p, at) => { W3.mesh(new THREE.CylinderGeometry(0.055, 0.05, 0.11, 20), W3.M('#ffffff', { r: 0.3 }), ...at, { p }); W3.mesh(new THREE.TorusGeometry(0.03, 0.01, 8, 16), W3.M('#ffffff'), at[0] + 0.06, at[1], at[2], { p, ry: Math.PI / 2 }); W3.mesh(new THREE.CylinderGeometry(0.048, 0.048, 0.005, 20), W3.M('#5A3A28'), at[0], at[1] + 0.05, at[2], { p }); };
W3.orangeBag = (p, at) => { const g = new THREE.Group(); g.position.set(...at); p.add(g); W3.mesh(new THREE.CylinderGeometry(0.2, 0.16, 0.36, 20, 1, true), W3.M('#ffffff', { op: 0.35, x: { side: THREE.DoubleSide } }), 0, 0, 0, { p: g, cs: false });
  for (let i = 0; i < 14; i++) { const a = i * 2.39, r = 0.06 + (i % 3) * 0.04; W3.mesh(new THREE.SphereGeometry(0.06, 16, 16), W3.M('#F7931E', { r: 0.5 }), Math.cos(a) * r, -0.1 + (i / 14) * 0.3, Math.sin(a) * r, { p: g }); } return g; };
W3.notebook = (p, at) => W3.mesh(new THREE.BoxGeometry(0.16, 0.22, 0.02), W3.M('#ffffff'), ...at, { p, rx: -0.3 });

/* ---------- tokoh ---------- */
W3.ijal = function (o = {}) {   // o: {pos, ry, L, R, mood}
  const p = new THREE.Group(); p.position.set(...(o.pos || [0, 0, 0])); p.rotation.y = o.ry || 0; W3.S.add(p);
  W3.mesh(new THREE.CapsuleGeometry(0.095, 0.62, 6, 14), W3.M('#35507A'), -0.11, 0.42, 0, { p }); W3.mesh(new THREE.CapsuleGeometry(0.095, 0.62, 6, 14), W3.M('#3E5C8A'), 0.11, 0.42, 0, { p });
  W3.mesh(new THREE.CapsuleGeometry(0.08, 0.14, 6, 12), W3.M('#FFFFFF'), -0.11, 0.06, 0.06, { p, rx: Math.PI / 2 }); W3.mesh(new THREE.CapsuleGeometry(0.08, 0.14, 6, 12), W3.M('#F2F2F2'), 0.11, 0.06, 0.06, { p, rx: Math.PI / 2 });
  W3.mesh(new THREE.CapsuleGeometry(0.25, 0.42, 10, 20), W3.M('#FA7209'), 0, 1.13, 0, { p, s: [1.05, 1, 0.78] });
  W3.mesh(new THREE.TorusGeometry(0.1, 0.025, 8, 20), W3.M('#CF6515'), 0, 1.42, 0.02, { p, rx: Math.PI / 2 });
  W3.mesh(new THREE.CylinderGeometry(0.065, 0.07, 0.12, 16), W3.M(SKD), 0, 1.5, 0, { p });
  W3.mesh(new THREE.SphereGeometry(0.29, 40, 40), W3.M(SK), 0, 1.82, 0, { p, s: [1, 1.02, 0.95] });
  W3.mesh(new THREE.SphereGeometry(0.06, 16, 16), W3.M(SK), -0.29, 1.82, -0.01, { p }); W3.mesh(new THREE.SphereGeometry(0.06, 16, 16), W3.M(SK), 0.29, 1.82, -0.01, { p });
  W3.mesh(new THREE.SphereGeometry(0.305, 40, 40, 0, Math.PI * 2, 0, Math.PI * 0.45), W3.M('#1F1A17', { r: 0.85 }), 0, 1.86, -0.025, { p });
  for (let i = 0; i < 9; i++) { const a = -1.3 + i * 0.33; W3.mesh(new THREE.ConeGeometry(0.075, 0.2, 10), W3.M('#1F1A17', { r: 0.85 }), Math.sin(a) * 0.22, 2.08 + Math.cos(a) * 0.02, Math.cos(a) * 0.1 - 0.02, { p, rz: -Math.sin(a) * 0.7, rx: 0.35 }); }
  W3.mesh(new THREE.BoxGeometry(0.5, 0.07, 0.14), W3.M('#1F1A17', { r: 0.85 }), 0, 1.98, 0.2, { p, rx: -0.3 });   // poni
  face(p, 1.8, 0.285, o.mood || 'smile');
  const h = arms(p, '#FA7209', o.L || 'down', o.R || 'down');
  p.userData.hands = h; return p;
};
W3.dinda = function (o = {}) {
  const p = new THREE.Group(); p.position.set(...(o.pos || [0, 0, 0])); p.rotation.y = o.ry || 0; W3.S.add(p);
  W3.mesh(new THREE.CylinderGeometry(0.19, 0.3, 0.92, 28), W3.M('#3B4A5E'), 0, 0.46, 0, { p });
  W3.mesh(new THREE.CapsuleGeometry(0.11, 0.08, 6, 12), W3.M('#5A4A40'), -0.1, 0.04, 0.08, { p, rx: Math.PI / 2 }); W3.mesh(new THREE.CapsuleGeometry(0.11, 0.08, 6, 12), W3.M('#5A4A40'), 0.1, 0.04, 0.08, { p, rx: Math.PI / 2 });
  W3.mesh(new THREE.CapsuleGeometry(0.23, 0.36, 10, 20), W3.M('#F2C14E'), 0, 1.13, 0, { p, s: [1.05, 1, 0.8] });
  // hijab: kepala + kain jatuh ke bahu (lathe)
  const prof = [[0.0, 0.0], [0.42, 0.02], [0.4, 0.12], [0.3, 0.3], [0.24, 0.42]].map(([r, y]) => new THREE.Vector2(r, y));
  W3.mesh(new THREE.LatheGeometry(prof, 40), W3.M('#2F80C0', { x: { side: THREE.DoubleSide } }), 0, 1.32, 0, { p });
  W3.mesh(new THREE.SphereGeometry(0.31, 40, 40), W3.M('#2F80C0'), 0, 1.84, -0.02, { p, s: [1, 1.1, 1] });
  W3.mesh(new THREE.SphereGeometry(0.215, 40, 40), W3.M(SK), 0, 1.83, 0.12, { p, s: [0.92, 1.08, 0.85] });
  W3.mesh(new THREE.TorusGeometry(0.215, 0.03, 10, 40), W3.M('#24679C'), 0, 1.83, 0.14, { p, s: [0.92, 1.08, 1] });
  face(p, 1.84, 0.3, o.mood || 'flat', 0.9);
  const h = arms(p, '#F2C14E', o.L || 'down', o.R || 'down', 0.06);
  p.userData.hands = h; return p;
};
W3.paman = function (o = {}) {
  const p = new THREE.Group(); p.position.set(...(o.pos || [0, 0, 0])); p.rotation.y = o.ry || 0; W3.S.add(p);
  const sar = W3.tex((g, w, h) => { g.fillStyle = '#8B5A3C'; g.fillRect(0, 0, w, h); g.strokeStyle = '#5E3A26'; g.lineWidth = 14; for (let i = 0; i < 8; i++) { g.beginPath(); g.moveTo(i * w / 8, 0); g.lineTo(i * w / 8, h); g.stroke(); g.beginPath(); g.moveTo(0, i * h / 8); g.lineTo(w, i * h / 8); g.stroke(); } g.strokeStyle = '#C9A27C'; g.lineWidth = 4; for (let i = 0; i < 8; i++) { g.beginPath(); g.moveTo(i * w / 8 + 20, 0); g.lineTo(i * w / 8 + 20, h); g.stroke(); } });
  W3.mesh(new THREE.CylinderGeometry(0.27, 0.3, 0.9, 28), new THREE.MeshStandardMaterial({ map: sar, roughness: 0.8 }), 0, 0.46, 0, { p });
  W3.mesh(new THREE.CapsuleGeometry(0.11, 0.08, 6, 12), W3.M('#4A3A30'), -0.12, 0.04, 0.08, { p, rx: Math.PI / 2 }); W3.mesh(new THREE.CapsuleGeometry(0.11, 0.08, 6, 12), W3.M('#4A3A30'), 0.12, 0.04, 0.08, { p, rx: Math.PI / 2 });
  W3.mesh(new THREE.SphereGeometry(0.34, 32, 32), W3.M('#2E9E6B'), 0, 1.12, 0, { p, s: [1.0, 1.05, 0.9] });     // perut bulat
  W3.mesh(new THREE.CylinderGeometry(0.07, 0.075, 0.12, 16), W3.M(SKD), 0, 1.48, 0, { p });
  W3.mesh(new THREE.SphereGeometry(0.29, 40, 40), W3.M(SK), 0, 1.79, 0, { p });
  W3.mesh(new THREE.SphereGeometry(0.06, 16, 16), W3.M(SK), -0.29, 1.79, -0.01, { p }); W3.mesh(new THREE.SphereGeometry(0.06, 16, 16), W3.M(SK), 0.29, 1.79, -0.01, { p });
  W3.mesh(new THREE.CapsuleGeometry(0.05, 0.12, 6, 10), W3.M('#B9B2AA'), -0.26, 1.85, -0.05, { p }); W3.mesh(new THREE.CapsuleGeometry(0.05, 0.12, 6, 10), W3.M('#B9B2AA'), 0.26, 1.85, -0.05, { p });
  const sk = W3.tex((g, w, h) => { g.fillStyle = '#E8D9A8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#8C6A2E'; g.lineWidth = 10; for (let i = 0; i < 16; i++) { g.beginPath(); g.moveTo(i * w / 16, h * 0.15); g.lineTo(i * w / 16 + w / 32, h * 0.55); g.lineTo(i * w / 16 + w / 16, h * 0.15); g.stroke(); } g.fillStyle = '#8C6A2E'; g.fillRect(0, h * 0.8, w, h * 0.2); });
  W3.mesh(new THREE.CylinderGeometry(0.27, 0.3, 0.22, 36), new THREE.MeshStandardMaterial({ map: sk, roughness: 0.8 }), 0, 2.02, -0.02, { p });   // songkok recca
  W3.mesh(new THREE.CylinderGeometry(0.27, 0.27, 0.02, 36), W3.M('#D9C793'), 0, 2.13, -0.02, { p });
  W3.mesh(new THREE.SphereGeometry(0.028, 14, 14), W3.M(SKD), 0, 1.78, 0.29, { p, s: [0.9, 1.2, 0.9] });
  W3.mesh(new THREE.CapsuleGeometry(0.03, 0.14, 6, 10), W3.M('#8E8780'), 0, 1.71, 0.275, { p, rz: Math.PI / 2 });   // kumis
  const m = o.mood || 'smile';
  if (m === 'o') W3.mesh(new THREE.SphereGeometry(0.04, 16, 16), W3.M('#5E2A1E'), 0, 1.65, 0.27, { p, s: [0.9, 1.2, 0.35] });
  else W3.mesh(new THREE.TorusGeometry(0.045, 0.012, 8, 20, Math.PI), W3.M('#5E2A1E'), 0, 1.66, 0.27, { p, rz: Math.PI });
  const h = arms(p, '#2E9E6B', o.L || 'down', o.R || 'down', 0.07);
  p.userData.hands = h; return p;
};

/* ---------- ruangan ---------- */
W3.lights = function (mood) {
  const S = W3.S;
  if (mood === 'night') { S.add(new THREE.HemisphereLight('#8FA4D8', '#2A2F45', 0.55)); const l = new THREE.PointLight('#FFD9A0', 1.6, 9, 1.6); l.position.set(0.6, 3.0, 0.6); l.castShadow = true; l.shadow.mapSize.set(1024, 1024); S.add(l); return; }
  if (mood === 'mouth') { S.add(new THREE.HemisphereLight('#FFD8D2', '#5A1E22', 0.9)); const l = new THREE.DirectionalLight('#FFF4EC', 1.1); l.position.set(1, 3, 4); l.castShadow = true; S.add(l); return; }
  S.add(new THREE.HemisphereLight('#FFFFFF', mood === 'warm' ? '#B9967A' : '#9FB6C0', 0.75));
  const L = new THREE.DirectionalLight(mood === 'warm' ? '#FFE9CF' : '#FFF4E6', 1.05); L.position.set(3, 6, 4); L.castShadow = true; L.shadow.mapSize.set(2048, 2048);
  Object.assign(L.shadow.camera, { left: -6, right: 6, top: 6, bottom: -6 }); L.shadow.radius = 4; S.add(L);
};
W3.bathroom = function (night) {
  const S = W3.S, M = W3.M, mesh = W3.mesh; S.background = new THREE.Color(night ? '#2B3352' : '#cfe3ea');
  mesh(new THREE.PlaneGeometry(10, 10), new THREE.MeshStandardMaterial({ map: W3.tiles('#e9eef0', '#cfd9dd', 4, [4, 4]), roughness: 0.45 }), 0, 0, 1, { rx: -Math.PI / 2, cs: false });
  const wm = () => new THREE.MeshStandardMaterial({ map: W3.tiles('#cfe6ee', '#b7d3de', 6, [2.6, 2]), roughness: 0.55 });
  mesh(new THREE.PlaneGeometry(10, 6), wm(), 0, 3, -1.6, { cs: false });
  mesh(new THREE.PlaneGeometry(10, 6), wm(), -2.6, 3, 2, { ry: Math.PI / 2, cs: false });
  mesh(new THREE.BoxGeometry(0.08, 2.2, 1.0), M('#8a6a55'), -2.55, 1.1, 1.3); mesh(new THREE.SphereGeometry(0.04, 12, 12), M('#d9c39a', { m: 0.6, r: 0.3 }), -2.48, 1.05, 0.95);
  mesh(new THREE.BoxGeometry(1.5, 0.9, 0.7), M('#ffffff', { r: 0.4 }), 0.9, 0.45, -1.25); mesh(new THREE.BoxGeometry(1.6, 0.08, 0.78), M('#f4f7f8', { r: 0.25 }), 0.9, 0.94, -1.22);
  mesh(new THREE.CylinderGeometry(0.34, 0.26, 0.1, 32), M('#ffffff', { r: 0.2 }), 0.9, 0.99, -1.18);
  W3.foam = mesh(new THREE.CylinderGeometry(0.3, 0.24, 0.02, 32), M('#f3b1ad', { r: 0.3 }), 0.9, 1.03, -1.18);
  W3.blood = [[0.82, -1.15], [0.98, -1.22], [0.9, -1.08], [1.02, -1.12]].map(([x, z]) => mesh(new THREE.SphereGeometry(0.028, 12, 12), M('#C8102E'), x, 1.045, z, { s: [1, 0.5, 1] }));
  mesh(new THREE.CylinderGeometry(0.025, 0.025, 0.25, 12), M('#c9d2d6', { m: 0.8, r: 0.25 }), 0.9, 1.12, -1.45); mesh(new THREE.BoxGeometry(0.04, 0.04, 0.22), M('#c9d2d6', { m: 0.8, r: 0.25 }), 0.9, 1.24, -1.36);
  mesh(new THREE.BoxGeometry(1.3, 0.9, 0.03), new THREE.MeshStandardMaterial({ color: night ? '#9fb3c4' : '#e8f6fb', roughness: 0.05, metalness: 0.6 }), 0.9, 1.95, -1.58); mesh(new THREE.BoxGeometry(1.38, 0.98, 0.02), M('#9fc3d0'), 0.9, 1.95, -1.595);
  mesh(new THREE.BoxGeometry(0.9, 0.04, 0.04), M('#b9c7cc', { m: 0.6 }), -1.2, 1.65, -1.55);
  mesh(new THREE.BoxGeometry(0.28, 0.6, 0.03), M('#f4a9a0'), -1.42, 1.37, -1.53); mesh(new THREE.BoxGeometry(0.28, 0.6, 0.03), M('#8fd3e8'), -1.0, 1.37, -1.53);
  mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.16, 16), M('#8FD3E8', { r: 0.3 }), 0.35, 1.06, -1.35);   // gelas sikat
  if (night) { mesh(new THREE.SphereGeometry(0.12, 16, 16), M('#FFE9B0', { x: { emissive: '#FFD27A', emissiveIntensity: 1.2 } }), 0.6, 3.0, 0.6, { cs: false }); }
  W3.lights(night ? 'night' : 'day');
};
W3.livingroom = function () {
  const S = W3.S, M = W3.M, mesh = W3.mesh; S.background = new THREE.Color('#F3E3CF');
  mesh(new THREE.PlaneGeometry(12, 12), new THREE.MeshStandardMaterial({ map: W3.wood([3, 3]), roughness: 0.6 }), 0, 0, 1, { rx: -Math.PI / 2, cs: false });
  mesh(new THREE.PlaneGeometry(12, 6), M('#F3E3CF', { r: 0.9 }), 0, 3, -1.8, { cs: false }); mesh(new THREE.PlaneGeometry(12, 6), M('#F7EBDD', { r: 0.9 }), -3.2, 3, 2, { ry: Math.PI / 2, cs: false });
  mesh(new THREE.CylinderGeometry(1.5, 1.5, 0.02, 48), M('#E9776A'), 0, 0.01, 0.4, { cs: false, s: [1.3, 1, 0.8] });
  mesh(new THREE.BoxGeometry(2.4, 0.5, 0.9), M('#5B95C4'), -1.2, 0.35, -1.25); mesh(new THREE.BoxGeometry(2.4, 0.7, 0.25), M('#4E86B5'), -1.2, 0.85, -1.62);
  mesh(new THREE.BoxGeometry(0.25, 0.65, 0.9), M('#4E86B5'), -2.35, 0.55, -1.25); mesh(new THREE.BoxGeometry(0.25, 0.65, 0.9), M('#4E86B5'), -0.05, 0.55, -1.25);
  mesh(new THREE.BoxGeometry(0.5, 0.45, 0.12), M('#F2C14E'), -1.7, 0.75, -1.4, { rz: 0.15 });
  mesh(new THREE.BoxGeometry(1.0, 0.06, 0.6), M('#B07A52'), 0.2, 0.45, 0.3); for (const [x, z] of [[-0.25, 0.05], [0.65, 0.05], [-0.25, 0.55], [0.65, 0.55]]) mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.42, 10), M('#8A5A3A'), x, 0.21, z);
  mesh(new THREE.BoxGeometry(1.4, 1.1, 0.06), M('#BFE6F2', { x: { emissive: '#DFF4FA', emissiveIntensity: 0.5 } }), 1.6, 1.8, -1.77); mesh(new THREE.BoxGeometry(1.5, 1.2, 0.04), M('#ffffff'), 1.6, 1.8, -1.79);
  mesh(new THREE.BoxGeometry(0.04, 1.1, 0.07), M('#ffffff'), 1.6, 1.8, -1.74);
  mesh(new THREE.CylinderGeometry(0.2, 0.16, 0.4, 20), M('#C47A4A'), 2.6, 0.2, -1.3); mesh(new THREE.SphereGeometry(0.45, 20, 20), M('#3FA06A'), 2.6, 0.85, -1.3);
  mesh(new THREE.BoxGeometry(0.9, 0.6, 0.05), M('#E8C77A'), -3.17, 1.9, 0.3, { ry: Math.PI / 2 });
  W3.lights('warm');
};
W3.mouth = function () {
  const S = W3.S, M = W3.M, mesh = W3.mesh; S.background = new THREE.Color('#5A1E26'); S.fog = new THREE.Fog('#5A1E26', 5, 11);
  const gumMat = W3.gumMat = M('#E98A86', { r: 0.55 });
  mesh(new THREE.BoxGeometry(8, 1.2, 3), gumMat, 0, -0.6, -0.5);                         // gusi
  for (let i = -3; i <= 3; i++) mesh(new THREE.SphereGeometry(0.62, 32, 32), gumMat, i * 1.05, 0.02, 0.35, { s: [1, 0.55, 0.7] });
  W3.teeth = [];
  const prof = [[0, 0], [0.38, 0], [0.46, 0.25], [0.48, 0.7], [0.44, 1.05], [0.3, 1.2], [0.0, 1.22]].map(([r, y]) => new THREE.Vector2(r, y));
  for (let i = -3; i <= 3; i++) { const t = mesh(new THREE.LatheGeometry(prof, 40), M('#FBF8F2', { r: 0.25 }), i * 1.05, -0.05, 0.1, { s: [1, 1, 0.8] }); W3.teeth.push(t); }
  W3.plaque = []; for (let i = -3; i <= 3; i++) for (let k = 0; k < 6; k++) { const a = k / 6 * Math.PI - Math.PI / 2; W3.plaque.push(mesh(new THREE.SphereGeometry(0.09 + (k % 2) * 0.04, 14, 14), M('#E8C66A', { r: 0.8 }), i * 1.05 + Math.sin(a) * 0.4, 0.2 + (k % 3) * 0.05, 0.42 + Math.cos(a) * 0.02, {})); }
  W3.swell = []; for (let i = -3; i <= 3; i++) W3.swell.push(mesh(new THREE.SphereGeometry(0.3, 24, 24), M('#D9473F', { r: 0.5 }), i * 1.05 + 0.52, 0.08, 0.52, { s: [1, 0.55, 0.6] }));
  W3.drops = [-2, 0, 1].map(i => mesh(new THREE.SphereGeometry(0.07, 16, 16), M('#B0102A', { r: 0.2 }), i * 1.05 + 0.5, -0.05, 0.75, { s: [1, 1.4, 1] }));
  W3.lights('mouth');
};
W3.exterior = function () {
  const S = W3.S, M = W3.M, mesh = W3.mesh; S.background = new THREE.Color('#1E2A4A'); S.fog = new THREE.Fog('#1E2A4A', 10, 22);
  mesh(new THREE.PlaneGeometry(30, 30), M('#3E6B4A', { r: 0.95 }), 0, 0, 0, { rx: -Math.PI / 2, cs: false });
  mesh(new THREE.BoxGeometry(3.2, 0.12, 1.4), M('#C9B79F'), 0, 0.06, 1.3);
  mesh(new THREE.BoxGeometry(3.6, 2.2, 2.4), M('#F3E3CF', { r: 0.9 }), 0, 1.1, -0.6);
  const roof = new THREE.Shape(); roof.moveTo(-2.1, 0); roof.lineTo(0, 1.3); roof.lineTo(2.1, 0); roof.lineTo(-2.1, 0);
  mesh(new THREE.ExtrudeGeometry(roof, { depth: 2.9, bevelEnabled: false }), M('#C2552F', { r: 0.8 }), 0, 2.2, -2.05);
  mesh(new THREE.BoxGeometry(0.75, 1.5, 0.05), M('#8A6A55'), 0, 0.75, 0.62);
  for (const x of [-1.15, 1.15]) { mesh(new THREE.BoxGeometry(0.75, 0.65, 0.05), M('#FFD98A', { x: { emissive: '#FFC65A', emissiveIntensity: 1.1 } }), x, 1.3, 0.62); }
  for (const x of [-1.5, 1.5]) mesh(new THREE.CylinderGeometry(0.07, 0.07, 2.0, 12), M('#ffffff'), x, 1.0, 1.9);
  mesh(new THREE.BoxGeometry(3.4, 0.08, 1.5), M('#D2603A'), 0, 2.05, 1.25);
  for (const [x, z, r] of [[-3, 1.5, 0.8], [3.1, 0.6, 1.0], [-3.6, -1.2, 1.1]]) { mesh(new THREE.CylinderGeometry(0.1, 0.12, 0.9, 10), M('#6E4630'), x, 0.45, z); mesh(new THREE.SphereGeometry(r, 20, 20), M('#2E7D52'), x, 0.9 + r * 0.8, z); }
  const moon = mesh(new THREE.SphereGeometry(0.35, 24, 24), M('#FFF6D0', { x: { emissive: '#FFF0B0', emissiveIntensity: 1 } }), 3.2, 5.6, -5, { cs: false });
  S.add(new THREE.HemisphereLight('#7F93C8', '#1C2A1E', 0.6));
  const l = new THREE.PointLight('#FFC97A', 1.4, 7, 1.5); l.position.set(0, 1.8, 1.8); l.castShadow = true; S.add(l);
  const d = new THREE.DirectionalLight('#AFC2FF', 0.35); d.position.set(4, 8, 3); S.add(d);
};
