// Render V6: lapisan overlay (Playwright, PNG transparan) ditumpuk di atas work/base.mp4 (footage) via ffmpeg.
// node src-v6/render.js stills "1,13,18,23,27,33,40,45"   |   node src-v6/render.js video
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const path = require('path'), fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const GATE = path.resolve(ROOT, '../../.claude/skills/upg-video/scripts/acc_gate.py');
const FPS = 30, W = 1080, H = 1920, BASE = path.join(ROOT, 'work/base.mp4');
const mode = process.argv[2] || 'stills';
// Gerbang ACC hanya untuk video final. Papan gambar (stills) boleh setelah naskah oke (aturan skill C0).
if (mode === 'video') execFileSync('python3', [GATE, 'check', ROOT], { stdio: 'inherit' });
if (!fs.existsSync(BASE)) execFileSync('python3', [path.join(__dirname, 'build_base.py')], { stdio: 'inherit' });
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  const dur = await page.evaluate(() => window.DURATION);
  fs.mkdirSync(path.join(ROOT, 'out/preview'), { recursive: true });
  if (mode === 'stills') {
    for (const t of (process.argv[3] || '1,8,14,18,23,28,33,41,45').split(',').map(Number)) {
      await page.evaluate(t => window.render(t), t);
      const ov = path.join(ROOT, 'work/_ov.png');
      await page.screenshot({ path: ov, omitBackground: true });
      execFileSync('ffmpeg', ['-v', 'error', '-y', '-ss', String(t), '-i', BASE, '-i', ov, '-filter_complex', '[0:v][1:v]overlay=0:0', '-frames:v', '1',
        path.join(ROOT, `out/preview/papan-t${t.toFixed(1).padStart(4, '0')}.jpg`)]);
    }
    console.log('stills ok');
  } else {
    const audio = path.join(ROOT, 'audio/narasi.wav'), has = fs.existsSync(audio);
    const out = path.join(ROOT, `out/upg-tambal-keluarga-${require(path.join(ROOT,'acc.json')).version}${has ? '' : '-tanpa-suara'}.mp4`);
    const args = ['-v', 'error', '-y', '-i', BASE, '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-'];
    if (has) args.push('-i', audio);
    args.push('-filter_complex', '[0:v][1:v]overlay=0:0:shortest=1,format=yuv420p[v]', '-map', '[v]');
    if (has) args.push('-map', '2:a', '-c:a', 'aac', '-b:a', '192k');
    args.push('-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-r', String(FPS), '-movflags', '+faststart', out);
    const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'ignore', 'inherit'] });
    const n = Math.round(dur * FPS);
    for (let i = 0; i < n; i++) {
      await page.evaluate(t => window.render(t), i / FPS);
      const buf = await page.screenshot({ omitBackground: true, type: 'png' });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
    console.log('video:', out);
  }
  await browser.close();
})();
