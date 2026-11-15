// node src3d/film.js stills "1,2,3"  |  node src3d/film.js video   (video butuh ACC)
const { chromium } = require('playwright'); const { spawn, execFileSync } = require('child_process'); const path=require('path'), fs=require('fs');
const ROOT=path.resolve(__dirname,'..'), mode=process.argv[2]||'stills', FPS=30;
if(mode==='video') execFileSync('python3',[path.resolve(ROOT,'../../.claude/skills/upg-video/scripts/acc_gate.py'),'check',ROOT],{stdio:'inherit'});
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-unsafe-swiftshader']}); const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('err:',e.message));
await p.goto('file://'+path.join(__dirname,'film.html')); await p.waitForFunction(()=>window.READY); await p.evaluate(()=>document.fonts.ready);
const dur=await p.evaluate(()=>window.DURATION); fs.mkdirSync(path.join(ROOT,'out/preview3d'),{recursive:true});
if(mode==='stills'){for(const t of process.argv[3].split(',').map(Number)){await p.evaluate(t=>window.render(t),t);await p.screenshot({path:path.join(ROOT,`out/preview3d/v-${t.toFixed(1).padStart(5,'0')}.jpg`),type:'jpeg',quality:85});}console.log('ok');}
else{const out=path.join(ROOT,`out/upg-misi-anak-rantau-eps1-${require(path.join(ROOT,'acc.json')).version}.mp4`);
  const from=Number(process.argv[3]||0), to=Number(process.argv[4]||dur), tmp=path.join(ROOT,'work/_v3d.mp4');
  const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium','-r',String(FPS),tmp],{stdio:['pipe','ignore','inherit']});
  const n0=Math.round(from*FPS), n1=Math.ceil(to*FPS); const t0=Date.now();
  for(let i=n0;i<n1;i++){await p.evaluate(t=>window.render(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:90});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));
    if(i%300===0)console.log('frame',i,'/',n1,((Date.now()-t0)/1000).toFixed(0)+'s');}
  ff.stdin.end();await new Promise(r=>ff.on('close',r));
  execFileSync('ffmpeg',['-v','error','-y','-i',tmp,'-i',path.join(ROOT,'audio/narasi.wav'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',out]);
  console.log('video:',out);}
await b.close();})();
