const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/gw-on.html');await p.waitForTimeout(400);await p.screenshot({path:'../cover-onboarding-gaya-canva.jpg',type:'jpeg',quality:92});await b.close();})();
