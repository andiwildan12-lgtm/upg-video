const {chromium}=require('playwright');
const V={feed:{H:1350,vars:'--H:1350px;--top:48px;--hd:160px;--fs:100px;--fs2:62px;--op:50%;--sbt:0;--sbw:0;--st:0;--cols:1;--gap:20px;--fb:44px',cls:'feed'},
story:{H:1920,vars:'--H:1920px;--top:150px;--hd:270px;--fs:132px;--fs2:90px;--ph:560px;--phh:760px;--op:50%;--sbt:380px;--sbw:270px;--st:1250px;--cols:2;--gap:24px 26px;--fb:330px'}};
(async()=>{const b=await chromium.launch();
for(const [k,v] of Object.entries(V)){const p=await b.newPage({viewport:{width:1080,height:v.H},deviceScaleFactor:1});
await p.goto('http://localhost:8765/poster/p.html');await p.evaluate(([s,c])=>{document.body.setAttribute('style',s);if(c)document.body.className=c;},[v.vars,v.cls||'']);await p.waitForTimeout(700);
await p.screenshot({path:`poster/poster-${k}.png`});await p.close();}
await b.close();})();
