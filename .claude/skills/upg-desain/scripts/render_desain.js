// Render desain HTML -> gambar.
// Pakai: node render_desain.js <file.html> <out.jpg|out.png> [lebar=1080] [tinggi=1920]
//  - .jpg = draf (kualitas 95) + <out>-zona.jpg (overlay zona aman, bila halaman mendukung #guide)
//  - .png = FINAL (tanpa file zona)
const {chromium}=require('playwright');const path=require('path');
(async()=>{
  const [,,inp,out,w='1080',h='1920']=process.argv;
  if(!inp||!out){console.error('Pakai: node render_desain.js <file.html> <out.jpg|out.png> [lebar] [tinggi]');process.exit(1)}
  const png=/\.png$/i.test(out);
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+h}});
  const url='file://'+path.resolve(inp);
  const shot=async(u,o)=>{await p.goto('about:blank');await p.goto(u);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
    await p.screenshot(png?{path:o,type:'png'}:{path:o,type:'jpeg',quality:o.includes('-zona')?80:95})};
  await shot(url,out);
  if(!png) await shot(url+'#guide',out.replace(/\.jpe?g$/i,'')+'-zona.jpg');
  await b.close();console.log('OK',out);
})();
