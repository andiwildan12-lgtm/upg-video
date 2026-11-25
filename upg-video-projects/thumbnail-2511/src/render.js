const {chromium}=require('playwright');const path=require('path');
const items=[
 ['izza-scaling-A','Scaling bareng','drg. Izza',''],
 ['izza-tambalan-B','Tambalan lama kamu','masih aman?',''],
 ['adhila-scaling-A','Pertama scaling,','gusi berdarah?',''],
 ['adhila-bleaching-tambal','Mau bleaching,','ada gigi berlubang?',''],
 ['adhila-lubang-dalam','Lubangnya dalam,','harus rawat saraf?',''],
 ['testimoni-kurnia','Awalnya cuma','antar anak','Cerita Ibu Kurnia'],
];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const [n,l1,l2,tag] of items){
 const u='file://'+path.resolve(__dirname,'thumb.html')+`?bg=bg_${n}.jpg&l1=${encodeURIComponent(l1)}&l2=${encodeURIComponent(l2)}&tag=${encodeURIComponent(tag)}`;
 await p.goto(u);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:path.resolve(__dirname,'..','out',`thumbnail-${n}.jpg`),type:'jpeg',quality:92});}
await b.close();})();
