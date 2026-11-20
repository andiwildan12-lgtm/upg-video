const {chromium}=require('playwright');const fs=require('fs');
const rows=JSON.parse(fs.readFileSync('edl.json'));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8766/bh/ov.html');await p.waitForTimeout(500);
for(const r of rows){const n=String(r.no).padStart(2,'0');
 // board frame
 await p.evaluate(o=>window.setSeg(o),{bg:r.v==='kartu'?null:`f${n}.jpg`,sub:r.sub,ov:r.ov,cm:r.cm,card:r.v==='kartu'});await p.waitForTimeout(250);
 await p.screenshot({path:`b${n}.jpg`,type:'jpeg',quality:85});
 // transparent overlay for final compositing
 await p.evaluate(o=>window.setSeg(o),{bg:null,sub:r.sub,ov:r.ov,cm:r.cm,card:r.v==='kartu'});await p.waitForTimeout(100);
 await p.screenshot({path:`o${n}.png`,omitBackground:true});}
await b.close();})();
