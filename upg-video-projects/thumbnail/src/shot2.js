const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/cover-rapat.html');await p.waitForTimeout(400);await p.screenshot({path:'../cover-rapat-dokter.jpg',type:'jpeg',quality:92});await b.close();})();
