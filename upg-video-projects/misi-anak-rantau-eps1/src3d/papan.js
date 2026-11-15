// node src3d/papan.js "1,2,3"  -> out/preview3d/f01.jpg ...
const { chromium } = require('playwright'); const path=require('path'), fs=require('fs');
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-unsafe-swiftshader']}); const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('err:',e.message));
await p.goto('file://'+path.join(__dirname,'papan.html')); await p.waitForFunction(()=>window.READY); await p.evaluate(()=>document.fonts.ready);
const out=path.join(__dirname,'../out/preview3d'); fs.mkdirSync(out,{recursive:true});
for(const n of (process.argv[2]||'1,2,3,4,5,6,7,8,9,10,11,12').split(',').map(Number)){await p.evaluate(n=>window.renderFrame(n),n); await p.waitForTimeout(150);
  await p.screenshot({path:path.join(out,`f${String(n).padStart(2,'0')}.jpg`),type:'jpeg',quality:88});}
await b.close(); console.log('ok');})();
