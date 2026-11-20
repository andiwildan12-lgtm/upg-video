// Sampul seragam dari scene 1-halaman.  node cover_make.js <page.html> <cfg.json> <detik> "<baris1>" "<BARIS2>" <out.png>   (PORT env, default 8765)
// Butuh cover.html, sym.png, font2.woff2 di folder kerja.
const {chromium}=require('playwright');const fs=require('fs');
const [page,cfgPath,t,l1,l2,out]=process.argv.slice(2);const cfg=JSON.parse(fs.readFileSync(cfgPath));const PORT=process.env.PORT||8765;
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto(`http://localhost:${PORT}/${page}`);await p.waitForFunction('window.ready===true',null,{timeout:90000});await p.evaluate(c=>window.setup(c),cfg);
await p.evaluate(t=>{window.render(t);document.getElementById('ov').style.display='none'},+t);await p.screenshot({path:'cover_bg.jpg',type:'jpeg',quality:94});
await p.goto(`http://localhost:${PORT}/cover.html?`+Date.now());await p.evaluate(([l1,l2])=>{document.querySelector('.bg').src='cover_bg.jpg?'+Date.now();document.querySelector('.l1').textContent=l1;document.querySelector('.l2').textContent=l2;},[l1,l2]);
await p.waitForTimeout(600);await p.screenshot({path:out});await b.close();console.log('cover',out);})();
