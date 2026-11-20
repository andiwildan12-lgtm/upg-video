// Render frame deterministik + motion blur opsional.
// node render_frames.js <page.html> <cfg.json> all | range A B | p t1 t2 ...    (server lokal: PORT env, default 8765)
// cfg.blur = [[detikMulai,detikSelesai],...] -> frame di rentang itu dirata-rata dari 3 sub-frame (shutter 180°)
const {chromium}=require('playwright');const fs=require('fs');const {execFileSync}=require('child_process');
const [page,cfgPath,mode,...rest]=process.argv.slice(2);const cfg=JSON.parse(fs.readFileSync(cfgPath));const PORT=process.env.PORT||8765;
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 p.on('pageerror',e=>console.log('E:',e.message));
 await p.goto(`http://localhost:${PORT}/${page}`);await p.waitForFunction('window.ready===true',null,{timeout:90000});await p.evaluate(c=>window.setup(c),cfg);
 const N=Math.round(cfg.K.total*30);const blur=cfg.blur||[];const inBlur=t=>blur.some(([a,c])=>t>=a&&t<c);
 let list;if(mode==='all')list=[...Array(N).keys()];else if(mode==='range')list=[...Array(+rest[1]-+rest[0]+1).keys()].map(i=>i+ +rest[0]);else list=null;
 const out=list?'frames':'probe';fs.mkdirSync(out,{recursive:true});fs.mkdirSync('_sub',{recursive:true});
 const shot=async(t,path)=>{await p.evaluate(t=>window.render(t),t);await p.screenshot({path,type:'jpeg',quality:92});};
 const t0=Date.now();let nb=0;
 if(list){for(const i of list){const t=i/30,f=`${out}/${String(i).padStart(4,'0')}.jpg`;
   if(inBlur(t)){const subs=[-1/120,0,1/120].map((d,j)=>`_sub/${i}_${j}.jpg`);for(const [j,d] of [-1/120,0,1/120].entries())await shot(Math.max(0,t+d),subs[j]);
     execFileSync('python3',['-I',__dirname+'/blend_blur.py',f,...subs]);nb++;}
   else await shot(t,f);
   if(i%300===0)console.log(i,(Date.now()-t0)/1000);}}
 else for(const t of rest.map(Number))await shot(t,`${out}/t${t}.jpg`);
 console.log('done',(Date.now()-t0)/1000,'blur frames:',nb);await b.close();})();
