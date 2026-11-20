
// ===== EXTRA SCENES =====
renderer.localClippingEnabled=true;
const ov=document.getElementById('ov');
// generic pills
const gx=document.createElement('div');gx.className='lbl';gx.innerHTML='<div class="row"><span class="p1" id="x1"></span></div><div class="row"><span class="p2" id="x2"></span></div>';ov.appendChild(gx);
const x1=document.getElementById('x1'),x2=document.getElementById('x2');
function pills2(a,b,t,t0,tout){ if(!a){gx.style.display='none';return;} gx.style.display='block';x1.textContent=a;x2.textContent=b;x1.style.display=a?'inline-block':'none';pill(x1,t0,t,tout);pill(x2,t0+0.15,t,tout);}
// side tags
function mkTag(left){const d=document.createElement('div');d.style.cssText=`position:absolute;top:1560px;${left?'left:150px':'right:150px'};font:600 52px Outfit;padding:10px 26px 14px;border-radius:999px;background:${left?'#0F4F4B':'#2CCDBD'};color:${left?'#fff':'#06332F'};opacity:0`;d.textContent=left?'scaling':'bleaching';ov.appendChild(d);return d;}
const tagL=mkTag(true),tagR=mkTag(false);
const divider=document.createElement('div');divider.style.cssText='position:absolute;left:539px;top:720px;width:2px;height:960px;background:repeating-linear-gradient(#8C8577 0 14px,transparent 14px 26px);opacity:0';ov.appendChild(divider);
// fades / wipes
const fade=document.createElement('div');fade.style.cssText='position:absolute;inset:0;opacity:0';ov.appendChild(fade);
const wipe=document.createElement('div');wipe.style.cssText='position:absolute;left:0;top:0;width:1080px;height:1920px;background:#2CCDBD;clip-path:polygon(0 0,100% 0,100% 88%,50% 100%,0 88%);transform-origin:50% 45%;display:none';ov.appendChild(wipe);
const roof=document.createElement('div');roof.innerHTML='<svg width="1080" height="1920" viewBox="0 0 1080 1920"><path d="M140 980 L540 700 L940 980" fill="none" stroke="#0F4F4B" stroke-width="34" stroke-linejoin="round" stroke-linecap="round"/></svg>';roof.style.cssText='position:absolute;inset:0;opacity:0';ov.appendChild(roof);
// footage image
const ft=document.createElement('img');ft.style.cssText='position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;display:none';document.getElementById('wrap').insertBefore(ft,ov);
window.setFootage=src=>new Promise(r=>{ft.onload=()=>r();ft.src=src;});
// card
const card=document.createElement('div');card.style.cssText='position:absolute;inset:0;background:#FBF8F3;display:none;flex-direction:column;align-items:center;justify-content:center;font-family:Outfit;color:#1F2A28;text-align:center';
card.innerHTML=`<img src="card_logo.png" style="width:470px" id="c0"><div id="c1" style="font:700 132px/1 Outfit;color:#0F4F4B;margin-top:90px;letter-spacing:-2px">Bleaching</div>
<div id="c2" style="font:600 50px Outfit;background:#2CCDBD;color:#06332F;padding:10px 30px 14px;border-radius:12px;margin-top:26px">sudah termasuk scaling</div>
<div id="c3" style="font:500 58px Outfit;color:#8A8478;text-decoration:line-through;margin-top:80px">Rp1.700.000</div>
<div id="c4" style="font:700 128px/1.05 Outfit;color:#0F4F4B;letter-spacing:-2px">Rp1.530.000</div>
<div id="c5" style="font:600 54px Outfit;color:#0F4F4B;margin-top:8px">diskon 10%</div>
<div id="c6" style="font:500 40px Outfit;color:#5E6B67;margin-top:90px">Tempat Nyaman untuk Kembali Tersenyum</div>
<div id="c7" style="font:500 44px/1.45 Inter,Outfit;color:#1F2A28;margin-top:26px">Jl. Rusa No. 65, Maricaya, Makassar<br><b style="font-weight:700">WA 0898-7735-463</b></div>`;
document.getElementById('wrap').insertBefore(card,ov);
// ----- tooth -----
function toothGeo(){
  const parts=[];
  const crown=new THREE.SphereGeometry(1,64,48);crown.scale(1.12,0.78,0.98);crown.translate(0,0.75,0);parts.push(crown);
  [[-.48,.4],[.48,.4],[-.48,-.4],[.48,-.4]].forEach(([x,z])=>{const c=new THREE.SphereGeometry(0.52,32,24);c.scale(1,0.85,1);c.translate(x,1.18,z);parts.push(c)});
  const neck=new THREE.CylinderGeometry(1.06,0.78,0.85,48);neck.translate(0,0.18,0);parts.push(neck);
  [[-0.42,0.14],[0.42,-0.14]].forEach(([x,a])=>{const r=new THREE.CylinderGeometry(0.5,0.14,1.9,32);r.translate(0,-0.95,0);r.rotateZ(a);r.translate(x,-0.05,0);parts.push(r);const tip=new THREE.SphereGeometry(0.12,16,12);tip.translate(0,-1.9,0);tip.rotateZ(a);tip.translate(x,-0.05,0);parts.push(tip)});
  return mergeGeometries(parts.map(g=>g.toNonIndexed()));
}
const TG=toothGeo();
const tooth=new THREE.Group();scene.add(tooth);tooth.visible=false;
const enamelM=()=>new THREE.MeshPhysicalMaterial({color:'#FBF8F3',roughness:0.32,clearcoat:0.6,clearcoatRoughness:0.3,side:THREE.DoubleSide});
const planeL=new THREE.Plane(new THREE.Vector3(-1,0,0),0),planeR=new THREE.Plane(new THREE.Vector3(1,0,0),0),planeS=new THREE.Plane(new THREE.Vector3(-1,0,0),3);
const enA=enamelM();enA.clippingPlanes=[planeS];
const enL=enamelM();enL.clippingPlanes=[planeL];
const enR=enamelM();enR.clippingPlanes=[planeR];
const outer=new THREE.Mesh(TG,enA);outer.castShadow=true;tooth.add(outer);
const outerL=new THREE.Mesh(TG,enL),outerR=new THREE.Mesh(TG,enR);tooth.add(outerL,outerR);
const dentM=new THREE.MeshStandardMaterial({color:'#E7C477',roughness:0.6,side:THREE.DoubleSide});dentM.clippingPlanes=[planeS];
const dentin=new THREE.Mesh(TG,dentM);dentin.scale.setScalar(0.8);dentin.position.y=0.05;tooth.add(dentin);
const gelM=new THREE.MeshStandardMaterial({color:'#2CCDBD',transparent:true,opacity:0,roughness:0.2,depthWrite:false});gelM.clippingPlanes=[planeR];
const gel=new THREE.Mesh(TG,gelM);gel.scale.set(1.045,1.03,1.045);gel.position.y=-0.01;tooth.add(gel);
// stain dots on crown surface
const dots=[];const dotM=new THREE.MeshStandardMaterial({color:'#6B4630',roughness:0.5,transparent:true});
{let s=7;const rnd=()=>{s=(s*16807)%2147483647;return s/2147483647};
 for(let i=0;i<46;i++){const th=(rnd()-0.5)*2.6,ph=0.25+rnd()*1.0;const dir=new THREE.Vector3(Math.sin(th)*Math.sin(ph),Math.cos(ph),Math.cos(th)*Math.sin(ph));
  const p=new THREE.Vector3(dir.x*1.12,dir.y*0.78+0.75,dir.z*0.98);
  const m=new THREE.Mesh(new THREE.SphereGeometry(0.055+rnd()*0.035,12,10),dotM.clone());m.position.copy(p);m.userData={p:p.clone(),d:dir.clone(),t:rnd()};m.scale.set(1,0.55,1);m.lookAt(p.clone().add(dir));m.rotateX(Math.PI/2);tooth.add(m);dots.push(m);}}
const C_WHITE=new THREE.Color('#FBF8F3'),C_TINT=new THREE.Color('#EED9A6'),C_BRIGHT=new THREE.Color('#FFFFFF');
// phone
const phone=new THREE.Group();desk.add(phone);phone.visible=false;
const pb=new THREE.Mesh(new RoundedBoxGeometry(0.78,0.07,1.58,4,0.06),new THREE.MeshStandardMaterial({color:'#2F3432',roughness:0.4}));pb.position.y=0.035;pb.castShadow=true;phone.add(pb);
const phCv=document.createElement('canvas');phCv.width=360;phCv.height=720;const phX=phCv.getContext('2d');const phTex=new THREE.CanvasTexture(phCv);phTex.colorSpace=THREE.SRGBColorSpace;
function drawPhone(on){phX.fillStyle=on?'#F1F3EF':'#111514';phX.fillRect(0,0,360,720);if(!on){phTex.needsUpdate=true;return;}
  phX.fillStyle='#1F2A28';phX.font='600 30px Outfit';phX.fillText('Galeri',22,62);
  const cols=['#C9B8A6','#AFC3B0','#D8CBB8','#B7C6CC','#CDBBA9','#C4D0C2','#BFAE9C','#D4C7B5','#B1BFB9','#CBB59F','#C2CFC6','#D9CDBC','#B9A894','#C6D2CC','#D2C0AA'];
  phX.filter='blur(7px)';for(let i=0;i<15;i++){phX.fillStyle=cols[i];phX.fillRect(14+(i%3)*112,90+Math.floor(i/3)*120,104,112)}phX.filter='none';phTex.needsUpdate=true;}
const ps=new THREE.Mesh(new THREE.PlaneGeometry(0.7,1.46),new THREE.MeshStandardMaterial({map:phTex,emissive:'#ffffff',emissiveMap:phTex,emissiveIntensity:0.6,roughness:0.3}));ps.rotation.x=-Math.PI/2;ps.position.y=0.072;phone.add(ps);
phone.position.set(1.05,0,0.75);phone.rotation.y=-0.35;
// glass of water
const glass=new THREE.Group();desk.add(glass);glass.visible=false;
const gw=new THREE.Mesh(new THREE.CylinderGeometry(0.36,0.31,0.95,48,1,true).translate(0,0.475,0),new THREE.MeshStandardMaterial({color:'#E8F3F5',transparent:true,opacity:0.32,roughness:0.08,side:THREE.DoubleSide,depthWrite:false}));
const wt=new THREE.Mesh(new THREE.CylinderGeometry(0.33,0.30,0.7,48).translate(0,0.36,0),new THREE.MeshStandardMaterial({color:'#CFE8EE',transparent:true,opacity:0.42,roughness:0.1,depthWrite:false}));
const gb=new THREE.Mesh(new THREE.CylinderGeometry(0.31,0.31,0.05,48).translate(0,0.025,0),new THREE.MeshStandardMaterial({color:'#E3EFF1',transparent:true,opacity:0.6}));
glass.add(wt,gw,gb);
function drawCalText(lines,teal){calX.fillStyle='#FBF8F3';calX.fillRect(0,0,512,420);calX.fillStyle='#A9BFA6';calX.fillRect(0,0,512,96);
  calX.fillStyle='#fff';calX.font='600 52px Outfit';calX.textAlign='center';calX.fillText('NOVEMBER',256,66);
  if(teal){calX.fillStyle='#2CCDBD';calX.beginPath();calX.roundRect(40,130,432,250,22);calX.fill();}
  calX.fillStyle=teal?'#06332F':'#0F4F4B';calX.font='500 60px Outfit';calX.fillText(lines[0],256,225);calX.font='700 64px Outfit';calX.fillText(lines[1],256,315);calTex.needsUpdate=true;}

function setVis(o){cups.visible=coffee.visible=!!o.field;hero.visible=!!o.hero;desk.visible=!!o.desk;tooth.visible=!!o.tooth;steam.forEach(s=>s.visible=!!o.steam);ground.visible=!!o.ground;phone.visible=!!o.phone;glass.visible=!!o.glass;
  renderer.domElement.style.visibility=o.canvas===false?'hidden':'visible';ft.style.display=o.foot?'block':'none';card.style.display=o.card?'flex':'none';
  document.getElementById('g1').style.display='none';document.getElementById('g2').style.display='none';
  tagL.style.opacity=tagR.style.opacity=divider.style.opacity=0;fade.style.opacity=0;wipe.style.display='none';roof.style.opacity=0;gx.style.display='none';}
function deskBase(){desk.position.y=0;ground.position.y=-0.6;pile.forEach(g=>g.scale.setScalar(0.72));hero.scale.setScalar(1);hero.rotation.y=-0.25;hero.position.set(0,0,0);}
function toothCam(t,dur,spin){camera.position.set(Math.sin(spin)*13,2.4,Math.cos(spin)*13);camera.lookAt(0,0.75,0);}
function resetTooth(){planeS.constant=3;enA.color.copy(C_WHITE);enL.color.copy(C_WHITE);enR.color.copy(C_WHITE);outer.visible=true;outerL.visible=outerR.visible=false;gelM.opacity=0;outer.scale.setScalar(1);dentin.scale.setScalar(0.8);
  dots.forEach(d=>{d.visible=true;d.position.copy(d.userData.p);d.scale.set(1,0.55,1);d.material.opacity=1;});}

window.renderScene=function(name,t){
  if(name==='hook'){setVis({field:true,hero:true,desk:true,steam:true,ground:true});hero.position.set(0,0,0);window.renderAt(t);
    if(t>8.25){const k=ease((t-8.25)/0.75);const p0=camera.position.clone();camera.position.lerp(new THREE.Vector3(0.02,1.05,0.06),k);const l=new THREE.Vector3(0.3,-0.6,-0.9).lerp(new THREE.Vector3(0,0.7,0),k);camera.lookAt(l);
      document.getElementById('g2').style.opacity=1-k;renderer.render(scene,camera);fade.style.background='#3A2418';fade.style.opacity=Math.max(0,(k-0.75)/0.25);}
    else document.getElementById('g2').style.opacity=1;
    return;}
  if(['t3','t4','t6','t7'].includes(name)){setVis({tooth:true});resetTooth();scene.background=BG;sun.intensity=2.1;
    tooth.position.set(0,-0.15,0);
    if(name==='t3'){toothCam(t,5,-0.35+t*0.06);tooth.rotation.y=0;
      dots.forEach(d=>{const k=back((t-0.8-d.userData.t*3.0)/0.35);d.scale.set(k,0.55*k,k);d.visible=k>0.001});
      fade.style.background='#3A2418';fade.style.opacity=1-ease(t/0.7);
      pills2('Warna kopi & teh','menempel di permukaan',t,0.6);}
    if(name==='t4'){toothCam(t,7,-0.05+0.8*ease((t-2.4)/2.6));
      const k1=ease(t/3);dots.forEach(d=>{d.visible=d.position.x<planeS.constant-0.02;d.position.copy(d.userData.p).addScaledVector(d.userData.d,-0.12*k1);const s=1-0.6*k1;d.scale.set(s,0.55*s,s);d.material.opacity=1-0.8*k1;d.visible=d.userData.p.x<planeS.constant-0.02});
      enA.color.copy(C_WHITE).lerp(C_TINT,0.55*k1);
      const k2=ease((t-3)/1.6);planeS.constant=cl(3,0,k2);
      const k3=ease((t-4.6)/2);outer.scale.set(1-0.05*k3,1-0.03*k3,1-0.05*k3);dentin.scale.setScalar(0.8+0.07*k3);dentM.color.set('#E7C477').lerp(new THREE.Color('#E2B65C'),k3);
      if(t<3.4)pills2('Lama-lama','meresap ke dalam',t,0.3,3.0);else pills2('Seiring waktu','lapisan dalam makin terlihat',t,3.6);}
    if(name==='t6'){toothCam(t,5,0.25-t*0.05);enA.color.copy(C_TINT);dots.forEach(d=>{d.material.opacity=0.55;d.scale.set(0.8,0.44,0.8)});sun.intensity=2.1+0.5*ease(t/3);
      pills2('Tenang,','ada solusinya',t,0.5);}
    if(name==='t7'){toothCam(t,9,0);outer.visible=false;outerL.visible=outerR.visible=true;dentin.visible=false;
      const kL=ease((t-0.6)/2.6);dots.forEach(d=>{if(d.userData.p.x>=0){d.visible=false;return;}d.position.copy(d.userData.p).add(new THREE.Vector3(-0.6*kL,1.4*kL,0.5*kL));d.material.opacity=0.85*(1-kL);d.scale.set(0.8,0.44,0.8)});
      enL.color.copy(C_TINT).lerp(C_WHITE,0.35*kL);
      const kg=ease((t-3.4)/1.2),kw=ease((t-4.6)/2.4),kgo=ease((t-7.0)/0.8);gelM.opacity=0.42*kg*(1-kgo);enR.color.copy(C_TINT).lerp(C_BRIGHT,kw);
      const kf=ease((t-7.6)/1.2);enL.color.lerp(C_BRIGHT,kf);
      tagL.style.opacity=Math.min(1,Math.max(0,(t-0.5)/0.4));tagR.style.opacity=Math.min(1,Math.max(0,(t-3.3)/0.4));divider.style.opacity=0.6*Math.min(1,t/0.5)*(1-kf);
      if(t<4.6)pills2('Noda permukaan','dibersihkan: scaling',t,0.4,4.3);else pills2('Warna yang meresap','dicerahkan: bleaching',t,4.7);}
    dentin.visible=name!=='t7';
    renderer.render(scene,camera);return;}
  if(['p5','c8','w12'].includes(name)){setVis({hero:true,desk:true,steam:true,ground:true,phone:name==='p5',glass:name==='w12'});deskBase();sun.intensity=2.1;
    // steam
    steam.forEach((s,i)=>{const life=2.4,ph=((t*0.9+i*life/steam.length)%life)/life;s.position.set(Math.sin(i*2.1+t*1.3)*0.12*(1+ph),0.8+ph*1.5,Math.cos(i*1.3)*0.1);s.position.add(hero.position);const sc=0.35+ph*0.7;s.scale.set(sc,sc,sc);s.material.opacity=Math.sin(Math.PI*ph)*0.9;});
    if(name==='p5'){drawCal('JUMAT',20);const on=t>0.15;if(window._ph!==on){drawPhone(on);window._ph=on;}
      phone.position.x=1.05+(t>0.15&&t<0.8?Math.sin(t*90)*0.012:0);
      const k=ease(t/5);camera.position.set(cl(2.3,1.9,k),cl(4.3,3.6,k),cl(3.6,3.0,k));camera.lookAt(0.75,0,0.45);
      pills2('Apalagi','pas lihat foto',t,0.15);}
    if(name==='c8'){const teal=t>0.7;const key='c'+teal;if(window._cal!==key){drawCalText(['Jadwal:','ke dokter gigi'],teal);window._cal=key;}
      const k=ease(t/1.4);camera.position.set(cl(3.4,2.75,k),cl(2.2,1.45,k),cl(1.6,0.75,k));camera.lookAt(1.75,0.47,-1.2);
      fade.style.background='#F4EFE6';fade.style.opacity=1-ease(t/0.4);
      const kw=ease((t-1.3)/1.1);if(t>1.3){wipe.style.display='block';wipe.style.transform=`translateY(0) scale(${cl(0.18,1.25,kw)})`;wipe.style.opacity=Math.min(1,(t-1.3)/0.2);roof.style.opacity=Math.min(1,Math.max(0,(t-2.1)/0.3));}}
    if(name==='w12'){drawCal('SENIN',23);window._cal=null;const k=ease((t-0.3)/0.9);hero.position.set(cl(0,1.1,k),0,cl(0,-0.4,k));
      const kg=back((t-0.7)/0.5);glass.scale.setScalar(Math.max(0.0001,kg));glass.position.set(0,0,0);
      const off=new THREE.Vector3(1.4,6.4,8.4).sub(new THREE.Vector3(0.3,-0.6,-0.9));off.applyAxisAngle(UP,-0.2);camera.position.copy(new THREE.Vector3(0.3,-0.6,-0.9).add(off.multiplyScalar(0.92)));camera.lookAt(0.3,-0.6,-0.9);
      pills2('Setelahnya','air putih dulu',t,0.4);}
    renderer.render(scene,camera);return;}
  if(name==='foot'){setVis({canvas:false,foot:true});const o=window._fo||{};
    if(o.wipe){const k=ease(t/0.6);wipe.style.display='block';wipe.style.opacity=1;wipe.style.transform=`translateY(${-112*k}%) scale(1.25)`;roof.style.opacity=1-ease(t/0.35);}
    if(o.p)pills2(o.p[0],o.p[1],t,o.p0||0.3);
    return;}
  if(name==='card'){setVis({canvas:false,card:true});
    ['c0','c1','c2','c3','c4','c5','c6','c7'].forEach((id,i)=>{const e=document.getElementById(id);const k=ease((t-0.1-i*0.09)/0.45);e.style.opacity=k;e.style.transform=`translateY(${(1-k)*40}px)`});
    fade.style.background='#FBF8F3';fade.style.opacity=1-ease(t/0.3);return;}
};
