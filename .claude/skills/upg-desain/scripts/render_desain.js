// Render desain HTML -> JPG. Pakai: node render_desain.js <file.html> <out.jpg> [lebar=1080] [tinggi=1920]
// Juga membuat <out>-zona.jpg bila halaman mendukung #guide (overlay zona aman).
const {chromium}=require('playwright');const path=require('path');
(async()=>{
  const [,,inp,out,w='1080',h='1920']=process.argv;
  if(!inp||!out){console.error('Pakai: node render_desain.js <file.html> <out.jpg> [lebar] [tinggi]');process.exit(1)}
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+h}});
  const url='file://'+path.resolve(inp);
  const shot=async(u,o,q)=>{await p.goto(u);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:o,type:'jpeg',quality:q})};
  await shot(url,out,95);
  await shot(url+'#guide',out.replace(/\.jpe?g$/i,'')+'-zona.jpg',80);
  await b.close();console.log('OK',out);
})();
