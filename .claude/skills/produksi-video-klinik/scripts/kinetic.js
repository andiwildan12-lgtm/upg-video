// Subtitle kinetik: kata muncul tepat saat diucapkan (timestamp Scribe), kata kunci <b> pop dengan overshoot.
// Pakai: import {kineticSub} from './kinetic.js'; ... kineticSub(subEl, T, SUBS, WORDS)
// SUBS = [[t0,t1,"teks dengan <b>kunci</b>"],...]  WORDS = [[start,end,"kata"],...] (detik video, sudah + offset narasi)
const P=(T,a,d)=>Math.min(1,Math.max(0,(T-a)/d));
const easeOut=t=>1-Math.pow(1-t,3);
const back=t=>{if(t<=0)return 0;if(t>=1)return 1;const c1=1.9,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2)};
const norm=s=>s.toLowerCase().replace(/<[^>]+>/g,'').replace(/[^a-z0-9×%]/g,'');
let cacheKey=null,cacheSpans=[];
function tokens(html){const out=[];const re=/<b>(.*?)<\/b>|(\S+)/g;let m;while((m=re.exec(html))){if(m[1]!==undefined)out.push({html:m[1],key:true,first:m[1].split(/\s+/)[0]});else out.push({html:m[2],key:false,first:m[2]});}return out;}
function timeTokens(toks,t0,t1,WORDS){
  const ws=WORDS.filter(w=>w[0]>=t0-0.3&&w[0]<=t1+0.1);let cur=0;
  toks.forEach(tk=>{tk.t=null;const n=norm(tk.first);if(!n)return;for(let j=cur;j<Math.min(ws.length,cur+5);j++){const wn=norm(ws[j][2]);if(wn===n||(n.length>2&&wn.startsWith(n))||(wn.length>2&&n.startsWith(wn))){tk.t=ws[j][0];cur=j+1;break;}}});
  // isi yang tidak cocok (angka "2×", singkatan) dengan interpolasi
  const idx=toks.map((tk,i)=>tk.t!=null?i:-1).filter(i=>i>=0);
  toks.forEach((tk,i)=>{if(tk.t!=null)return;const prev=idx.filter(j=>j<i).pop(),next=idx.find(j=>j>i);
    const a=prev!=null?toks[prev].t:t0,b=next!=null?toks[next].t:Math.max(a+0.1,t1-0.4);const ia=prev!=null?prev:-1,ib=next!=null?next:toks.length;tk.t=a+(b-a)*(i-ia)/(ib-ia);});
  toks.forEach(tk=>tk.t=Math.max(t0,tk.t-0.03));return toks;}
export function kineticSub(el,T,SUBS,WORDS,opt={}){
  const s=SUBS.find(x=>T>=x[0]&&T<x[1]);
  if(!s){el.style.opacity=0;return;}
  const key=s[0]+'|'+s[2];
  if(key!==cacheKey){cacheKey=key;el.innerHTML='';
    const toks=timeTokens(tokens(s[2]),s[0],s[1],WORDS||[]);
    cacheSpans=toks.map((tk,i)=>{const sp=document.createElement(tk.key?'b':'span');sp.innerHTML=tk.html;sp.style.display='inline-block';sp.style.willChange='transform';el.appendChild(sp);if(i<toks.length-1)el.appendChild(document.createTextNode(' '));return {sp,tk};});}
  el.style.opacity=1-P(T,s[1]-0.12,0.12);
  cacheSpans.forEach(({sp,tk})=>{const k=P(T,tk.t,0.18);sp.style.opacity=k;
    if(tk.key){const sc=0.7+0.3*back(P(T,tk.t,0.32));sp.style.transform=`translateY(${(1-easeOut(k))*16}px) scale(${sc})`;}
    else sp.style.transform=`translateY(${(1-easeOut(k))*18}px)`;});
}
