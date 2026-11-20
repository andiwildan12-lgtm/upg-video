const {chromium}=require('playwright');const fs=require('fs');
const cfg=JSON.parse(fs.readFileSync('arch3_cfg.json'));const mode=process.argv[2];
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 p.on('pageerror',e=>console.log('E:',e.message));
 await p.goto('http://localhost:8765/arch3.html');await p.waitForFunction('window.ready===true',null,{timeout:60000});
 await p.evaluate(c=>window.setup(c),cfg);
 const out=mode==='all'?'arch3f':'arch3p';fs.mkdirSync(out,{recursive:true});
 const times=mode==='all'?[...Array(Math.round(66*30)).keys()].map(i=>i/30):process.argv.slice(3).map(Number);
 const t0=Date.now();
 for(const [i,t] of times.entries()){await p.evaluate(t=>window.render(t),t);await p.screenshot({path:mode==='all'?`${out}/${String(i).padStart(4,'0')}.jpg`:`${out}/t${t}.jpg`,type:'jpeg',quality:92});}
 console.log('done',(Date.now()-t0)/1000);await b.close();})();
