// render lapisan per frame (PNG transparan), frame identik -> symlink
const {chromium}=require('playwright');const fs=require('fs');
const OUT=process.argv[2],TL=JSON.parse(fs.readFileSync(process.argv[3])),N=Math.round(TL.T*30);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.addInitScript(tl=>{window.TL=tl},TL.frz);
await p.goto('http://localhost:8784/ov.html');await p.evaluate(()=>document.fonts.ready);
let prev=null,prevf=null,shots=0;
for(let i=0;i<N;i++){const t=i/30;const key=await p.evaluate(t=>{window.go(t);return document.getElementById('r').innerHTML},t);
 const f=`${OUT}/${String(i).padStart(4,'0')}.png`;
 if(key===prev){fs.symlinkSync(prevf,f);continue;}
 await p.screenshot({path:f,omitBackground:true});prev=key;prevf=f;shots++;}
console.log('shots',shots,N);await b.close();})();
