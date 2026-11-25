const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const logo of ['atas','bawah']){
 const u='file://'+path.resolve(__dirname,'thumb2.html')+`?bg=bg2_bleaching.jpg&l1=${encodeURIComponent('Mau bleaching,')}&l2=${encodeURIComponent('ada gigi berlubang?')}&logo=${logo}`;
 await p.goto(u);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:path.resolve(__dirname,'..','out',`contoh-thumbnail-logo-${logo}.jpg`),type:'jpeg',quality:92});}
await b.close();})();
