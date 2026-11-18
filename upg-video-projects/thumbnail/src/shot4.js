const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of ['A','B','C']){await p.goto('file://'+process.cwd()+'/fl-'+n+'.html');await p.waitForTimeout(400);await p.screenshot({path:'../cover-rapat-tanpa-wajah-'+n+'.jpg',type:'jpeg',quality:92});}
await b.close();})();
