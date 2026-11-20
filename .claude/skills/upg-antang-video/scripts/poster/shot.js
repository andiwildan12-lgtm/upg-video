const {chromium}=require('playwright');const fs=require('fs');
const V={story:{H:1920,hh:'1000px',bt:'230px',lw:'150px',tt:'600px',h1:'128px',h2:'64px',h3:'44px',pm:'60px',bdt:'340px',cm:'34px',ctm:'40px',lm:'30px',cf:'30px',lf:'32px',pz:'1',cz:'1',bz:'1'},
 feed:{H:1350,hh:'640px',bt:'40px',lw:'100px',tt:'250px',h1:'100px',h2:'46px',h3:'34px',pm:'34px',bdt:'40px',cm:'20px',ctm:'24px',lm:'16px',cf:'26px',lf:'28px',pz:'0.78',cz:'0.82',bz:'0.75'}};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
for(const [k,v] of Object.entries(V)){await p.setViewportSize({width:1080,height:v.H});
 await p.goto('file://'+process.cwd()+'/poster.html');
 await p.evaluate(v=>{for(const [a,x] of Object.entries(v))document.documentElement.style.setProperty('--'+a,a==='H'?x+'px':x)},v);
 await p.waitForTimeout(300);await p.screenshot({path:`Behel_Antang_${k==='story'?'Story_1080x1920':'Feed_1080x1350'}.png`});}
await b.close();})();
