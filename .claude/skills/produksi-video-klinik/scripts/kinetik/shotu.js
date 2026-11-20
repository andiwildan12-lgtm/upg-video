const {chromium}=require('playwright');const fs=require('fs');const U=JSON.parse(fs.readFileSync('uniq.json'));fs.mkdirSync('ust',{recursive:true});
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8766/bh/k/kin.html');await p.evaluate(()=>document.fonts.ready);
for(let i=0;i<U.length;i++){await p.evaluate(o=>window.setS(o),U[i]);await p.waitForTimeout(40);await p.screenshot({path:`ust/${String(i).padStart(4,'0')}.png`,omitBackground:true});}
await b.close();})();
