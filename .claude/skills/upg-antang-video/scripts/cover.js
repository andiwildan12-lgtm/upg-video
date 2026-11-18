const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8766/upg.html');await p.waitForFunction('window.ready===true');
await p.evaluate(()=>{window.renderScene('rapi',6.2,6.53);document.getElementById('G').style.opacity=0;});
await p.screenshot({path:'clean_rapi.jpg',type:'jpeg',quality:95});
const h=fs.readFileSync('cover.html','utf8');
for(const [k,src] of [['a','clean_rapi.jpg'],['b','ftg/s7/0060.jpg']]){fs.writeFileSync(`cover_${k}.html`,h.replace('SRC',src));
 await p.goto(`http://localhost:8766/cover_${k}.html`);await p.waitForTimeout(300);await p.screenshot({path:`cover-behel-antang-${k}.png`});}
await b.close();})();
