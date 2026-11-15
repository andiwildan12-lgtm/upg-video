// Renderer UPG Motion: render(t) per frame via Playwright -> ffmpeg (H.264).
// Pakai:  node src/render.js stills            -> out/preview/*.jpg (frame kunci + contact sheet)
//         node src/render.js video             -> out/<nama>.mp4 (pakai audio/narasi.wav bila ada)
// Selalu cek gerbang ACC lebih dulu.
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const path = require('path'), fs = require('fs');

const ROOT = path.resolve(__dirname, '..');
const GATE = path.resolve(ROOT, '../../.claude/skills/upg-video/scripts/acc_gate.py');
const FPS = 30, W = 1080, H = 1920;
const mode = process.argv[2] || 'stills';

execFileSync('python3', [GATE, 'check', ROOT], { stdio: 'inherit' }); // throws bila ditolak

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  const dur = await page.evaluate(() => window.DURATION);
  fs.mkdirSync(path.join(ROOT, 'out/preview'), { recursive: true });

  if (mode === 'stills') {
    const times = (process.argv[3] || '1.0,3.2,5.2,8,13.5,17.5,21,24.5,28,33.5,37,41,45.5').split(',').map(Number);
    for (const t of times) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: path.join(ROOT, `out/preview/v5-t${String(t).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 85 });
    }
    console.log('stills:', times.join(', '));
  } else {
    const audio = path.join(ROOT, 'audio/narasi-V5.wav');
    const hasAudio = fs.existsSync(audio);
    const out = path.join(ROOT, `out/upg-happy-hour-scaling-V5${hasAudio ? '-TES' : '-TES-tanpa-suara'}.mp4`);
    const args = ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-'];
    if (hasAudio) args.push('-i', audio, '-c:a', 'aac', '-b:a', '192k');
    args.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-r', String(FPS), '-movflags', '+faststart', '-shortest', out);
    const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'ignore', 'inherit'] });
    const n = Math.ceil(dur * FPS);
    for (let i = 0; i < n; i++) {
      await page.evaluate(t => window.render(t), i / FPS);
      const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (i % 150 === 0) process.stdout.write(`frame ${i}/${n}\n`);
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
    console.log('video:', out);
  }
  await browser.close();
})();
