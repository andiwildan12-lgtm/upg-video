const {chromium}=require('playwright');const fs=require('fs');const cfg=JSON.parse(fs.readFileSync('arch_cfg.json'));
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8765/arch.html');await p.waitForFunction('window.ready===true');await p.evaluate(c=>window.setup(c),cfg);
for(const [t,o] of [[17.4,'cover_bg1.jpg'],[7.6,'cover_bg2.jpg'],[27.8,'cover_bg3.jpg']]){await p.evaluate(t=>{window.render(t);document.getElementById('ov').style.display='none'},t);await p.screenshot({path:o,type:'jpeg',quality:94});}
await b.close();})();
