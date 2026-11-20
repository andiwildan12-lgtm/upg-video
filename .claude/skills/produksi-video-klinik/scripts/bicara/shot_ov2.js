const {chromium}=require('playwright');const fs=require('fs');
const rows=JSON.parse(fs.readFileSync('edl2.json'));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8766/bh/ov.html');await p.waitForTimeout(500);
for(const r of rows){const n=String(r.no).padStart(2,'0');const card=r.v==='kartu';
 await p.evaluate(o=>window.setSeg(o),{bg:r.img,sub:r.sub,ov:r.ov,cm:r.cm,fb:r.fb,card});await p.waitForTimeout(200);
 await p.screenshot({path:`c${n}.jpg`,type:'jpeg',quality:85});
 await p.evaluate(o=>window.setSeg(o),{bg:null,sub:r.sub,ov:r.ov,cm:r.cm,fb:r.fb,card});await p.waitForTimeout(100);
 await p.screenshot({path:`ov${n}.png`,omitBackground:true});}
await b.close();})();
