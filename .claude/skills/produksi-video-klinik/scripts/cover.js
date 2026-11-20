const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const [bg,l1,l2,out] of [['cover_bg1.jpg','40% gigimu','NGGAK KESIKAT?','cover-160-a.png'],['cover_bg2.jpg','Gigimu punya','160 PERMUKAAN?','cover-160-b.png'],['cover_bg3.jpg','Kenapa karang gigi','NGGAK HILANG DISIKAT?','cover-160-c.png']]){
 await p.goto('http://localhost:8765/cover.html?'+Date.now());await p.evaluate(([bg,l1,l2])=>{document.querySelector('.bg').src=bg+'?'+Date.now();document.querySelector('.l1').textContent=l1;document.querySelector('.l2').textContent=l2;},[bg,l1,l2]);
 await p.waitForTimeout(500);await p.screenshot({path:'/home/user/ruma-dental-video/'+out});}
await b.close();})();
