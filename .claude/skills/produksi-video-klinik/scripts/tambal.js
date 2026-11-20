
// ===== TAMBAL v2 =====
wt.material.color.set('#C98A3C');wt.material.opacity=0.62;
const tbIce=[];for(let i=0;i<3;i++){const c=new THREE.Mesh(new RoundedBoxGeometry(0.2,0.18,0.2,2,0.04),new THREE.MeshStandardMaterial({color:'#F2FAFC',transparent:true,opacity:0.7,roughness:0.05}));c.position.set(Math.sin(i*2.1)*0.12,0.62+i*0.04,Math.cos(i*2.1)*0.12);c.rotation.set(i,i*1.3,0.3*i);glass.add(c);tbIce.push(c);}
for(let i=0;i<26;i++){const a=i*2.4,y=0.12+((i*37)%70)/100;const d=new THREE.Mesh(new THREE.SphereGeometry(0.018+((i*7)%4)*0.005,8,6),new THREE.MeshStandardMaterial({color:'#FFFFFF',transparent:true,opacity:0.55,roughness:0.05}));d.position.set(Math.sin(a)*0.355,y,Math.cos(a)*0.355);glass.add(d);}
const tbInc=upper[3];const _h=0.96;
const tbPlane=new THREE.Plane(new THREE.Vector3(-1,0,0),5);
const tbSpot=new THREE.Mesh(new THREE.CircleGeometry(0.05,24),new THREE.MeshStandardMaterial({color:'#3A2A22',roughness:0.8}));tbSpot.position.set(0.03,-_h*0.55,0.214);tbInc.g.add(tbSpot);
const mkM=(c,ph)=>{const m=ph?new THREE.MeshPhysicalMaterial({color:c,roughness:0.3,clearcoat:0.5,side:THREE.DoubleSide}):new THREE.MeshStandardMaterial({color:c,roughness:0.85,side:THREE.DoubleSide});m.clippingPlanes=[tbPlane];return m;};
const tbPulpM=mkM('#D96A6E');const tbPulp=new THREE.Mesh(new THREE.SphereGeometry(1,32,24),tbPulpM);tbPulp.scale.set(0.07,0.3,0.06);tbPulp.position.set(0,-0.36,-0.04);tbInc.g.add(tbPulp);
const tbCavM=mkM('#4A3226');const tbCav=new THREE.Mesh(new THREE.SphereGeometry(1,32,24),tbCavM);tbInc.g.add(tbCav);
const tbFillM=mkM('#F5EEDF',true);const tbFill=new THREE.Mesh(new THREE.SphereGeometry(1,32,24),tbFillM);tbInc.g.add(tbFill);
// grow: 0 small near surface -> 1 reaches pulp
function tbCavity(grow,fill,cleaned){const z=cl(0.17,0.06,grow),s=cl(0.05,0.13,grow);tbCav.position.set(0.0,-_h*0.55+0.04*grow,z);tbCav.scale.set(s*0.9,s*1.2,s);
  tbCav.visible=fill<0.99;tbCavM.color.set('#4A3226').lerp(new THREE.Color('#E9DCC8'),cleaned);
  tbFill.position.copy(tbCav.position);const f=Math.max(0.0001,fill);tbFill.scale.set(s*0.92*f,s*1.22*f,s*1.02*f);tbFill.visible=fill>0.01;
  tbSpot.visible=fill<0.5;tbSpot.scale.setScalar(0.8+0.6*grow);}
function tbIsolate(on){smile.children.forEach(c=>{if(c!==tbInc.g)c.visible=!on;});tbInc.g.visible=true;
  [incMat,incDent].forEach(m=>{m.clippingPlanes=on?[tbPlane]:[planeF];});}
function tbSideCam(k){const p=new THREE.Vector3();tbInc.g.getWorldPosition(p);camera.position.set(p.x+cl(3.2,2.2,k),-0.35,p.z+0.25);camera.lookAt(p.x,-0.42,p.z+0.05);tbPlane.constant=p.x;}
// split labels
const tbL=document.createElement('div'),tbR=document.createElement('div');
[tbL,tbR].forEach((d,i)=>{d.style.cssText=`position:absolute;top:1400px;${i?'right':'left'}:0;width:540px;text-align:center;font:700 48px/1.2 Outfit;color:${i?'#8A3B3E':'#0F4F4B'};display:none`;ov.appendChild(d);});
const tbDiv=document.createElement('div');tbDiv.style.cssText='position:absolute;left:538px;top:330px;width:4px;height:1300px;background:#E2D9CA;display:none';ov.appendChild(tbDiv);
function tbCard(){card.innerHTML=`<img src="card_logo.png" style="width:440px" id="c0"><div id="c1" style="font:700 124px/1 Outfit;color:#0F4F4B;margin-top:80px;letter-spacing:-2px">Tambal Gigi</div>
<div id="c2" style="font:600 50px Outfit;background:#2CCDBD;color:#06332F;padding:10px 30px 14px;border-radius:12px;margin-top:26px">sewarna gigi</div>
<div id="c3" style="font:500 56px Outfit;color:#5E6B67;margin-top:70px">mulai</div>
<div id="c4" style="font:700 132px/1.05 Outfit;color:#0F4F4B;letter-spacing:-2px">Rp250.000</div>
<div id="c5" style="font:600 46px Outfit;color:#0F4F4B;margin-top:14px">bergaransi · dikerjakan dokter gigi</div>
<div id="c6" style="font:500 40px Outfit;color:#5E6B67;margin-top:70px">Tempat Nyaman untuk Kembali Tersenyum</div>
<div id="c7" style="font:500 44px/1.45 Inter,Outfit;color:#1F2A28;margin-top:24px">Jl. Rusa No. 65, Maricaya, Makassar<br><b style="font-weight:700">WA 0898-7735-463</b></div>`;}
tbCard();
const _rs2=window.renderScene;
window.renderScene=function(name,t,D){
  const ph=D?t/D:0;tbL.style.display=tbR.style.display=tbDiv.style.display='none';renderer.setScissorTest(false);renderer.setViewport(0,0,1080,1920);
  if(name==='tb_desk'||name==='tb_desk2'){
    setVis({hero:true,desk:true,ground:true,glass:true});smile.visible=false;deskBase();sun.intensity=2.1;
    hero.position.set(1.15,0,-0.5);glass.position.set(0,0,0);glass.scale.setScalar(1);tbIce.forEach((c,i)=>{c.position.y=0.62+i*0.04+0.02*Math.sin(t*3+i);});
    const k=ease(ph);
    if(name==='tb_desk'){camera.position.set(cl(1.9,1.3,k),cl(2.4,1.75,k),cl(3.4,2.4,k));camera.lookAt(0,0.45,0);pills2('Awalnya cuma','ngilu sedikit',t,0.2);if(ph>0.62){x1.textContent='Jadi…';x2.textContent='dicuekin';}}
    else{camera.position.set(cl(-1.4,-1.0,k),cl(2.2,2.0,k),cl(3.0,2.6,k));camera.lookAt(0.2,0.45,0);pills2('Es teh pun','aman lagi',t,0.15);}
    renderer.render(scene,camera);return;}
  if(name.startsWith('tb_')){setVis({});smile.visible=true;scene.background=BG;sun.intensity=2.1;
    if(name==='tb_hook'){tbIsolate(false);smileState({tint:0.08,dots:0});const z=ease(ph/0.8);smileCam(0.35+0.65*z);tbCavity(0,0,0);tbSpot.scale.setScalar(Math.max(0.0001,back((t-0.4)/0.4))*1.2);
      fade.style.background='#F4EFE6';fade.style.opacity=1-ease(t/0.25);pills2('Lubang gigi','nggak bisa nutup sendiri',t,0.3);}
    if(name==='tb_cave'){smileState({tint:0.08,dots:0});tbIsolate(true);tbSideCam(ease(ph));const g=ease((ph-0.15)/0.75);tbCavity(g,0,0);const pulse=g>0.9?0.5+0.5*Math.sin(t*9):0;tbPulpM.color.set('#D96A6E').lerp(new THREE.Color('#B8282E'),pulse);
      pills2('Di dalam,','makin dekat ke saraf',t,0.3);}
    if(name==='tb_paths'){smileState({tint:0.08,dots:0});tbIsolate(true);tbL.style.display=tbR.style.display=tbDiv.style.display='block';tbL.innerHTML='Sekarang:<br>ditambal';tbR.innerHTML='Nanti:<br>saluran akar';
      renderer.setScissorTest(true);const asp=camera.aspect;camera.aspect=540/1920;camera.updateProjectionMatrix();
      // left: fill
      tbSideCam(0.45);const fl=ease((ph-0.25)/0.4);tbCavity(0.3,fl,ease(ph/0.25));tbPulpM.color.set('#D96A6E');renderer.setViewport(0,0,540,1920);renderer.setScissor(0,0,540,1920);renderer.render(scene,camera);
      // right: reaches pulp
      tbSideCam(0.45);tbCavity(cl(0.5,1,ease(ph/0.5)),0,0);const pulse=0.5+0.5*Math.sin(t*9);tbPulpM.color.set('#D96A6E').lerp(new THREE.Color('#B8282E'),pulse*ease((ph-0.4)/0.2));renderer.setViewport(540,0,540,1920);renderer.setScissor(540,0,540,1920);renderer.render(scene,camera);
      camera.aspect=asp;camera.updateProjectionMatrix();renderer.setScissorTest(false);renderer.setViewport(0,0,1080,1920);
      pills2('Kalau masih kecil,','cukup ditambal',t,0.2);if(ph>0.33){x1.textContent='Sampai saraf,';x2.textContent='bisa sakit berdenyut';}
      return;}
    if(name==='tb_fill'){smileState({tint:0.05,dots:0});tbIsolate(true);tbSideCam(1-0.3*ease(ph));const fl=ease((ph-0.15)/0.4);tbCavity(0.35,fl,ease(ph/0.15));tbPulpM.color.set('#D96A6E');
      if(ph>0.72){tbIsolate(false);smileState({tint:0.05,dots:0});smileCam(0.75-0.25*ease((ph-0.72)/0.28));tbCavity(0.35,1,1);tbSpot.visible=false;}
      pills2('Solusinya:','tambal gigi',t,0.2);if(ph>0.38){x1.textContent='Ruma Dental';x2.textContent='mulai Rp250.000';}}
    renderer.render(scene,camera);return;}
  tbIsolate(false);
  if(name==='card'){tbCard();}
  return _rs2(name,t,D);
};
