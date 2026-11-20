const {chromium}=require('playwright');const fs=require('fs');
const jobs=JSON.parse(fs.readFileSync(process.argv[2]));
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 p.on('pageerror',e=>console.log('E:',e.message));p.on('console',m=>{if(m.type()==='error')console.log('C:',m.text())});
 await p.goto('http://localhost:8765/full.html');await p.waitForFunction('window.ready===true',null,{timeout:60000});
 fs.mkdirSync('final',{recursive:true});const t0=Date.now();
 for(const j of jobs){
   await p.evaluate(o=>{window._fo=o;},j.opt||{});
   for(let i=0;i<j.n;i++){const t=(j.t0||0)+i/30;
     if(j.dir){await p.evaluate(s=>window.setFootage(s),`ftg/${j.dir}/${String(Math.min(i+1,j.max||9999)).padStart(4,'0')}.jpg`);}
     await p.evaluate(([n,t,D])=>window.renderScene(n,t,D),[j.name,t,j.D||j.n/30]);
     const out=j.out?`${j.out}/${String(i).padStart(4,'0')}.jpg`:`final/${String(j.start+i).padStart(4,'0')}.jpg`;
     await p.screenshot({path:out,type:'jpeg',quality:92});}
   console.log(j.name,'done',(Date.now()-t0)/1000);}
 await b.close();})();
