const {chromium}=require('playwright');const fs=require('fs');
const jobs=JSON.parse(fs.readFileSync('jobs.json'));
const only=process.argv[2]?process.argv[2].split(','):null; // seg names
const probe=process.argv[3]==='probe';
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 p.on('pageerror',e=>console.log('E:',e.message));p.on('console',m=>{if(m.type()==='error')console.log('C:',m.text())});
 await p.goto('http://localhost:8766/upg.html');await p.waitForFunction('window.ready===true',null,{timeout:60000});
 const t0=Date.now();
 for(const j of jobs){ if(only&&!only.includes(j.seg))continue;
   const dir=probe?'probe':'seg/'+j.seg;fs.mkdirSync(dir,{recursive:true});
   await p.evaluate(o=>{window._fo=o;},j.opt||{});
   if(j.opt&&j.opt.blur)await p.evaluate(s=>window.setImg('ftgB',s),j.opt.blur);
   const frames=probe?[0,Math.floor(j.n*0.5),j.n-5]:[...Array(j.n).keys()];
   for(const i of frames){const t=i/30;
     if(j.dir){await p.evaluate(s=>window.setImg('ftg',s),`ftg/${j.dir}/${String(Math.min(i+1,j.max)).padStart(4,'0')}.jpg`);}
     await p.evaluate(([n,t,D])=>window.renderScene(n,t,D),[j.name,t,j.D]);
     const out=probe?`${dir}/${j.seg}_${String(i).padStart(4,'0')}.jpg`:`${dir}/${String(i).padStart(4,'0')}.jpg`;
     await p.screenshot({path:out,type:'jpeg',quality:92});}
   console.log(j.seg,'done',((Date.now()-t0)/1000).toFixed(1));}
 await b.close();})();
