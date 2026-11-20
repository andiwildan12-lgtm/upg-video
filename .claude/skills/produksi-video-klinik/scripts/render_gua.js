const {chromium}=require('playwright');const fs=require('fs');
const cfg=JSON.parse(fs.readFileSync('cfg.json'));const mode=process.argv[2];
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 p.on('pageerror',e=>console.log('E:',e.message));p.on('console',m=>{if(m.type()==='error')console.log('C:',m.text())});
 await p.goto('http://localhost:8765/gua.html');await p.waitForFunction('window.ready===true',null,{timeout:90000});
 await p.evaluate(c=>window.setup(c),cfg);
 if(mode==='range'){const [a,b2]=process.argv.slice(3).map(Number);fs.mkdirSync('frames',{recursive:true});for(let i=a;i<=b2;i++){await p.evaluate(t=>window.render(t),i/30);await p.screenshot({path:`frames/${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}console.log('range done');await b.close();return;}
 const out=mode==='all'?'frames':'probe';fs.mkdirSync(out,{recursive:true});
 const N=Math.round(cfg.K.total*30);
 const times=mode==='all'?[...Array(N).keys()].map(i=>i/30):process.argv.slice(3).map(Number);
 const t0=Date.now();
 for(const [i,t] of times.entries()){await p.evaluate(t=>window.render(t),t);await p.screenshot({path:mode==='all'?`${out}/${String(i).padStart(4,'0')}.jpg`:`${out}/t${t}.jpg`,type:'jpeg',quality:92});
  if(mode==='all'&&i%300===0)console.log(i,(Date.now()-t0)/1000);}
 console.log('done',(Date.now()-t0)/1000);await b.close();})();
