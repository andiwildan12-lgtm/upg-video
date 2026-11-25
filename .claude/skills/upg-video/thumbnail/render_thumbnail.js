// Render thumbnail UPG dari daftar JSON (aturan: references/thumbnail.md)
// Pakai: node render_thumbnail.js <folder-kerja> <daftar.json>
// daftar.json: [{"nama":"bleaching","bg":"bg_bleaching.jpg","l1":"Mau bleaching,","l2":"ada gigi berlubang?","top":1010}]
// folder-kerja berisi gambar latar (1080x1920); keluaran: <folder-kerja>/thumbnail-<nama>.jpg
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const [dir,list]=process.argv.slice(2);const K=__dirname;
for(const f of ['thumbnail.html','logo-upg-mendatar-putih.png','nunito-latin-800-normal.woff2','nunito-latin-900-normal.woff2'])
  fs.copyFileSync(path.join(f.endsWith('.html')?K:path.join(K,'..','assets'),f),path.join(dir,f));
const items=JSON.parse(fs.readFileSync(list));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const it of items){const u='file://'+path.resolve(dir,'thumbnail.html')+`?bg=${encodeURIComponent(it.bg)}&l1=${encodeURIComponent(it.l1)}&l2=${encodeURIComponent(it.l2)}&logo=atas${it.top?'&top='+it.top:''}`;
 await p.goto(u);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:path.resolve(dir,`thumbnail-${it.nama}.jpg`),type:'jpeg',quality:92});console.log('thumbnail ->',it.nama);}
await b.close();})();
