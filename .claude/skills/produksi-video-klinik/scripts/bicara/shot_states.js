const {chromium}=require('playwright');const fs=require('fs');
const S=JSON.parse(fs.readFileSync('states.json'));fs.mkdirSync('st',{recursive:true});
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8766/bh/ov2.html');await p.evaluate(()=>document.fonts.ready);
for(let i=0;i<S.length;i++){await p.evaluate(o=>window.setState(o),S[i]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(60);
 await p.screenshot({path:`st/${String(i).padStart(3,'0')}.png`,omitBackground:true});}
await b.close();})();
