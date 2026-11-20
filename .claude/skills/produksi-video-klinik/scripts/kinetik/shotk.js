const {chromium}=require('playwright');const fs=require('fs');const P=JSON.parse(fs.readFileSync('P.json'));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8766/bh/k/kin.html');await p.evaluate(()=>document.fonts.ready);
for(let i=0;i<P.length;i++){await p.evaluate(o=>window.setS(o),P[i]);await p.waitForTimeout(300);await p.screenshot({path:`kp${i}.jpg`,type:'jpeg',quality:85});}
await b.close();})();
