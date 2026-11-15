/* ===== helpers ===== */
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const seg=(t,a,b)=>clamp((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3);
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const back=x=>{const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const $=id=>document.getElementById(id);
function show(el,t,a,dur=.45,dy=40){const p=eo(seg(t,a,a+dur));el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px)`;}
function pop(el,t,a,dur=.45){const p=seg(t,a,a+dur);el.style.opacity=clamp(p*2);el.style.transform=`scale(${p<=0?0.4:back(p)})`;}
function slideX(el,t,a,dur=.5,dx=160){const p=eo(seg(t,a,a+dur));el.style.opacity=p;el.style.transform=`translateX(${(1-p)*dx}px)`;}

/* ===== ilustrasi — karakter TANPA MATA ===== */
const CROWN="M80,120 C78,58 140,38 200,70 C260,38 322,58 320,120 C328,200 312,262 302,304 L98,304 C88,262 72,200 80,120 Z";
function toothSVG(id,{tartar=1,gum='#F4A9A0',clipTartar=false,tool=false}={}){
  return `<svg viewBox="0 0 400 420" width="100%" height="100%" style="overflow:visible">
   <defs>
    <linearGradient id="${id}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EFE6DC"/></linearGradient>
    <clipPath id="${id}c"><path d="${CROWN}"/></clipPath>
    ${clipTartar?`<clipPath id="${id}r"><rect id="${id}rr" x="80" y="0" width="400" height="420"/></clipPath>`:''}
   </defs>
   <ellipse cx="200" cy="415" rx="190" ry="14" fill="rgba(207,101,21,.10)"/>
   <path id="${id}gum" d="M20,300 Q110,258 200,294 Q290,258 380,300 Q392,360 360,404 Q200,430 40,404 Q8,360 20,300 Z" fill="${gum}"/>
   <path d="${CROWN}" fill="url(#${id}g)" stroke="#E6D6C5" stroke-width="6"/>
   <path d="M116,112 C118,84 140,72 164,76" stroke="#FFFFFF" stroke-width="16" fill="none" stroke-linecap="round"/>
   <path d="M290,150 C296,200 290,240 280,272" stroke="#E9DCCD" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/>
   <g clip-path="url(#${id}c)"><g ${clipTartar?`clip-path="url(#${id}r)"`:''}><g id="${id}tar" opacity="${tartar}">
     <path d="M80,304 C96,272 128,258 160,268 C182,252 214,262 236,252 C262,262 292,258 320,304 Z" fill="#D9A43A"/>
     <path d="M104,292 C126,280 148,286 166,280 M206,274 C230,266 252,274 276,268" stroke="#B9821F" stroke-width="8" fill="none" stroke-linecap="round" opacity=".7"/>
     <circle cx="132" cy="284" r="5" fill="#C48E2B"/><circle cx="248" cy="278" r="6" fill="#C48E2B"/><circle cx="196" cy="290" r="4" fill="#C48E2B"/>
   </g></g></g>
   <path id="${id}glow" d="M80,304 C96,272 128,258 160,268 C182,252 214,262 236,252 C262,262 292,258 320,304" fill="none" stroke="#FA7209" stroke-width="10" stroke-linecap="round" opacity="0"/>
   <path d="M20,300 Q110,258 200,294 Q290,258 380,300" fill="none" stroke="#EE8E84" stroke-width="8"/>
   ${tool?`<g id="${id}tool"><path d="M0,0 L70,-120" stroke="#8A97A3" stroke-width="12" stroke-linecap="round"/><path d="M70,-120 L120,-210" stroke="#5A6B78" stroke-width="20" stroke-linecap="round"/><circle cx="0" cy="0" r="7" fill="#5A6B78"/></g>`:''}
  </svg>`;
}
function brushSVG(){
  return `<svg viewBox="0 0 640 130" width="640" height="130" style="overflow:visible">
   <rect x="0" y="40" width="430" height="44" rx="22" fill="#FA7209"/>
   <rect x="400" y="30" width="230" height="64" rx="20" fill="#FFFFFF" stroke="#E9D9C9" stroke-width="4"/>
   ${Array.from({length:9},(_,i)=>`<rect x="${414+i*23}" y="94" width="14" height="34" rx="5" fill="#8FD3E8"/>`).join('')}
  </svg>`;
}
function face(cx,cy){ /* tanpa mata: hidung garis kecil + mulut senyum */
  return `<circle cx="${cx}" cy="${cy}" r="72" fill="#F2C29B"/>
   <path d="M${cx},${cy+2} q7,16 -3,20" stroke="#C98E66" stroke-width="5" fill="none" stroke-linecap="round"/>
   <path d="M${cx-24},${cy+38} Q${cx},${cy+56} ${cx+24},${cy+38}" stroke="#7A3F2A" stroke-width="6" fill="none" stroke-linecap="round"/>`;
}
function doctorSVG(){
  return `<svg viewBox="0 0 380 660" width="100%" height="100%" style="overflow:visible">
   <rect x="165" y="190" width="50" height="50" fill="#E6B48C"/>
   <path d="M60,660 L76,300 Q190,228 304,300 L320,660 Z" fill="#FFFFFF" stroke="#E5DCD2" stroke-width="5"/>
   <path d="M150,248 L190,330 L230,248" fill="#8FD3E8"/>
   <path d="M150,248 L190,360 L176,660 M230,248 L190,360" stroke="#E5DCD2" stroke-width="5" fill="none"/>
   <path d="M150,300 C130,380 160,420 190,420 C220,420 250,380 230,300" stroke="#5A6B78" stroke-width="7" fill="none"/>
   <circle cx="190" cy="424" r="14" fill="#5A6B78"/>
   <g id="docArm"><path d="M296,310 Q352,250 360,180" stroke="#E5DCD2" stroke-width="62" stroke-linecap="round" fill="none"/>
   <path d="M296,310 Q352,250 360,180" stroke="#FFFFFF" stroke-width="52" stroke-linecap="round" fill="none"/>
   <circle cx="362" cy="150" r="26" fill="#F2C29B"/></g>
   <rect x="250" y="470" width="44" height="10" rx="5" fill="#FA7209"/>
   ${face(190,140)}
   <path d="M118,128 C112,54 268,54 262,128 C246,92 136,92 118,128 Z" fill="#3B2A20"/>
  </svg>`;
}
function calWhite(){return `<svg viewBox="0 0 100 100" width="100%" height="100%"><rect x="8" y="16" width="84" height="78" rx="14" fill="none" stroke="#fff" stroke-width="8"/><path d="M8,40 L92,40" stroke="#fff" stroke-width="8"/><rect x="26" y="4" width="10" height="22" rx="5" fill="#fff"/><rect x="64" y="4" width="10" height="22" rx="5" fill="#fff"/></svg>`;}
function clkWhite(){return `<svg viewBox="0 0 100 100" width="100%" height="100%"><circle cx="50" cy="50" r="42" fill="none" stroke="#fff" stroke-width="8"/><path d="M50,24 L50,52 L68,62" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round"/></svg>`;}
function waSVG(){return `<svg viewBox="0 0 200 200" width="100%" height="100%"><path d="M100,14 C52,14 14,50 14,96 C14,114 20,130 30,144 L20,186 L64,174 C76,180 88,182 100,182 C148,182 186,144 186,96 C186,50 148,14 100,14 Z" fill="#1FAF55"/><path d="M72,62 C66,62 60,70 62,82 C66,108 92,134 118,140 C130,142 138,136 138,130 L138,118 C138,114 134,112 130,110 L116,104 C112,102 108,104 106,108 L102,114 C90,108 84,102 78,90 L84,86 C88,84 90,80 88,76 L82,64 C80,62 76,62 72,62 Z" fill="#fff"/></svg>`;}
function mini(stage){
  const dots = Array.from({length:7},(_,i)=>`<circle cx="${70+i*10}" cy="${120+(i%2)*6}" r="5" fill="#E8C66A"/>`).join('');
  const layer = stage===1? dots : `<path d="M30,152 C46,120 80,112 100,122 C122,110 152,118 170,152 Z" fill="#C9902B"/>`;
  return `<svg viewBox="0 0 200 200" width="100%" height="100%" style="overflow:visible"><defs><clipPath id="mc${stage}"><path d="M40,60 C40,30 70,20 100,36 C130,20 160,30 160,60 C164,100 156,130 151,152 L49,152 C44,130 36,100 40,60 Z"/></clipPath></defs>
   <path id="mg${stage}" d="M15,150 Q57,132 100,148 Q143,132 185,150 L185,200 L15,200 Z" fill="#F4A9A0"/>
   <path d="M40,60 C40,30 70,20 100,36 C130,20 160,30 160,60 C164,100 156,130 151,152 L49,152 C44,130 36,100 40,60 Z" fill="#fff" stroke="#E9D9C9" stroke-width="4"/>
   <g clip-path="url(#mc${stage})">${layer}</g>
   ${stage===3?`<g id="warn" transform="translate(150,10)"><path d="M30,0 L60,52 L0,52 Z" fill="#E0533D"/><rect x="27" y="16" width="6" height="20" rx="3" fill="#fff"/><circle cx="30" cy="43" r="4" fill="#fff"/></g>`:''}</svg>`;
}

