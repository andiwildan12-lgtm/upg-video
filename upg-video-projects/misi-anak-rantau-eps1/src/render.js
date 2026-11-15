// Motion murni. node src/render.js stills "t1,t2" | node src/render.js video (butuh ACC)
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const path = require('path'), fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const GATE = path.resolve(ROOT, '../../.claude/skills/upg-video/scripts/acc_gate.py');
const FPS = 30, W = 1080, H = 1920, mode = process.argv[2] || 'stills';
if (mode === 'video') execFileSync('python3', [GATE, 'check', ROOT], { stdio: 'inherit' });
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  const dur = await page.evaluate(() => window.DURATION);
  fs.mkdirSync(path.join(ROOT, 'out/preview'), { recursive: true });
  if (mode === 'stills') {
    for (const t of process.argv[3].split(',').map(Number)) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: path.join(ROOT, `out/preview/papan-t${t.toFixed(1).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 88 });
    }
    console.log('stills ok');
  } else if (mode === 'sample') {
    // UJI GAYA (bukan video final): tidak lewat gerbang ACC, disimpan di out/preview/
    const out = path.join(ROOT, 'out/preview/uji-v2-sampel.mp4'), audio = path.join(ROOT, 'audio/narasi.wav');
    const ff = spawn('ffmpeg', ['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-i',audio,'-c:a','aac','-b:a','192k','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium','-r',String(FPS),'-movflags','+faststart','-shortest',out], { stdio: ['pipe','ignore','inherit'] });
    for (let i = 0, n = Math.ceil(dur * FPS); i < n; i++) { await page.evaluate(t => window.render(t), i / FPS); const buf = await page.screenshot({ type: 'jpeg', quality: 90 }); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
    ff.stdin.end(); await new Promise(r => ff.on('close', r)); console.log('sampel:', out);
  } else {
    const audio = path.join(ROOT, 'audio/narasi.wav'), has = fs.existsSync(audio);
    const out = path.join(ROOT, `out/upg-misi-anak-rantau-eps1-${require(path.join(ROOT, 'acc.json')).version}.mp4`);
    const args = ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-'];
    if (has) args.push('-i', audio, '-c:a', 'aac', '-b:a', '192k');
    args.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-r', String(FPS), '-movflags', '+faststart', '-shortest', out);
    const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'ignore', 'inherit'] });
    for (let i = 0, n = Math.ceil(dur * FPS); i < n; i++) {
      await page.evaluate(t => window.render(t), i / FPS);
      const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r)); console.log('video:', out);
  }
  await browser.close();
})();
