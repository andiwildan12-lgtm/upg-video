
// ===== MOLAR CROSS-SECTION (buku pelajaran) =====
const V=(x,y)=>new THREE.Vector2(x,y);
function smoothShape(pts){const sh=new THREE.Shape();sh.moveTo(pts[0].x,pts[0].y);sh.splineThru(pts.slice(1).concat([pts[0]]));return sh;}
const OUT=[V(-0.66,0),V(-0.84,0.45),V(-0.86,0.9),V(-0.62,1.18),V(-0.36,1.14),V(0,0.98),V(0.36,1.14),V(0.62,1.18),V(0.86,0.9),V(0.84,0.45),V(0.66,0),V(0.6,-0.45),V(0.5,-1.15),V(0.36,-1.6),V(0.22,-1.5),V(0.15,-0.75),V(0,-0.5),V(-0.15,-0.75),V(-0.22,-1.5),V(-0.36,-1.6),V(-0.5,-1.15),V(-0.6,-0.45)];
const DEN=[V(-0.56,0.02),V(-0.72,0.45),V(-0.72,0.84),V(-0.55,1.02),V(-0.34,0.99),V(0,0.86),V(0.34,0.99),V(0.55,1.02),V(0.72,0.84),V(0.72,0.45),V(0.56,0.02),V(0.52,-0.45),V(0.43,-1.13),V(0.33,-1.5),V(0.25,-1.44),V(0.2,-0.78),V(0,-0.58),V(-0.2,-0.78),V(-0.25,-1.44),V(-0.33,-1.5),V(-0.43,-1.13),V(-0.52,-0.45)];
const PULP=[V(-0.36,0.38),V(-0.36,0.6),V(-0.22,0.72),V(0,0.64),V(0.22,0.72),V(0.36,0.6),V(0.36,0.38),V(0.4,-0.2),V(0.36,-1.3),V(0.31,-1.36),V(0.26,-0.25),V(0.1,0.18),V(-0.1,0.18),V(-0.26,-0.25),V(-0.31,-1.36),V(-0.36,-1.3),V(-0.4,-0.2)];
const DEPTH=0.9;
function mExt(pts,depth,bevel){return new THREE.ExtrudeGeometry(smoothShape(pts),{depth,bevelEnabled:bevel,bevelThickness:0.06,bevelSize:0.05,bevelSegments:6,curveSegments:24});}
const enamelMat=new THREE.MeshPhysicalMaterial({color:'#FBF8F3',roughness:0.3,clearcoat:0.6});
const dentMat2=new THREE.MeshStandardMaterial({color:'#EBD39B',roughness:0.7});
const pulpMat2=new THREE.MeshStandardMaterial({color:'#E27A7E',roughness:0.6});
const cavMat2=new THREE.MeshStandardMaterial({color:'#3B2A22',roughness:0.9});
const fillMat2=new THREE.MeshPhysicalMaterial({color:'#F6F0E2',roughness:0.35,clearcoat:0.4});
const outlineMat=new THREE.MeshBasicMaterial({color:'#2CCDBD',transparent:true,opacity:0,depthWrite:false});
function cavPts(g){const w=cl(0.1,0.3,g),d=cl(0.12,0.4,g),top=0.99;return [V(-w*0.55,top+0.06),V(-w,top-d*0.35),V(-w*0.8,top-d*0.8),V(0,top-d),V(w*0.8,top-d*0.8),V(w,top-d*0.35),V(w*0.55,top+0.06)];}
function makeMolar(){const G=new THREE.Group();
  const body=new THREE.Mesh(mExt(OUT,DEPTH,true),enamelMat);body.position.z=-DEPTH;body.castShadow=true;G.add(body);
  const den=new THREE.Mesh(new THREE.ShapeGeometry(smoothShape(DEN),24),dentMat2);den.position.z=0.065;G.add(den);
  const pulp=new THREE.Mesh(new THREE.ShapeGeometry(smoothShape(PULP),24),pulpMat2.clone());pulp.position.z=0.07;G.add(pulp);
  const cover=new THREE.Mesh(new THREE.ShapeGeometry(smoothShape(OUT),24),enamelMat);cover.position.z=0.075;G.add(cover);
  const spot=new THREE.Mesh(new THREE.CircleGeometry(0.07,24),cavMat2);spot.rotation.x=-Math.PI/2;spot.position.set(0,1.0,-DEPTH*0.45);G.add(spot);
  const cav=new THREE.Mesh(new THREE.BufferGeometry(),cavMat2);cav.position.z=0.08;G.add(cav);
  const fil=new THREE.Mesh(new THREE.BufferGeometry(),fillMat2);fil.position.z=0.085;G.add(fil);
  const out=new THREE.Mesh(new THREE.BufferGeometry(),outlineMat.clone());out.position.z=0.083;G.add(out);
  G.userData={body,den,pulp,cover,spot,cav,fil,out};scene.add(G);G.visible=false;return G;}
const molA=makeMolar(),molB=makeMolar();
function molState(M,o){const u=M.userData;u.cover.position.x=cl(0,2.6,o.open||0);u.cover.visible=(o.open||0)<0.999;
  u.spot.scale.setScalar(Math.max(0.0001,o.spot||0));
  const g=o.grow||0;u.cav.geometry.dispose();u.cav.geometry=new THREE.ShapeGeometry(smoothShape(cavPts(g)),16);u.cav.visible=(o.open||0)>0.3&&(o.fill||0)<0.999;
  u.cav.material=cavMat2;if(o.clean)u.cav.material=new THREE.MeshStandardMaterial({color:new THREE.Color('#3B2A22').lerp(new THREE.Color('#D9C9AE'),o.clean)});
  const f=o.fill||0;u.fil.geometry.dispose();const pts=cavPts(g).map(p=>V(p.x*f,0.99+(p.y-0.99)*f));u.fil.geometry=new THREE.ShapeGeometry(smoothShape(pts),16);u.fil.visible=f>0.01&&(o.open||0)>0.3;
  u.out.geometry.dispose();u.out.geometry=new THREE.ShapeGeometry(smoothShape(cavPts(g).map(p=>V(p.x*1.15,0.99+(p.y-0.99)*1.12))),16);u.out.material.opacity=o.glow||0;u.out.visible=(o.glow||0)>0.01;
  u.pulp.material.color.set('#E27A7E').lerp(new THREE.Color('#C02A31'),o.pain||0);}
// layer labels
const mLab=['email','dentin','saraf'].map(t=>{const d=document.createElement('div');d.textContent=t;d.style.cssText='position:absolute;font:600 44px Outfit;color:#0F4F4B;background:rgba(251,248,243,.92);padding:4px 14px 6px;border-radius:10px;display:none;white-space:nowrap';ov.appendChild(d);return d;});
const mLabP=[new THREE.Vector3(-0.86,0.62,0.1),new THREE.Vector3(-0.5,-0.2,0.1),new THREE.Vector3(0,-0.9,0.1)];
function showLabels(M,op){const pos=[[50,980],[250,1200],[470,1330]];mLab.forEach((d,i)=>{d.style.display=op>0.01?'block':'none';d.style.opacity=op;d.style.left=pos[i][0]+'px';d.style.top=pos[i][1]+'px';});}
const mSplitL=document.createElement('div'),mSplitR=document.createElement('div');
[mSplitL,mSplitR].forEach((d,i)=>{d.style.cssText=`position:absolute;top:1430px;${i?'right':'left'}:0;width:540px;text-align:center;font:700 50px/1.2 Outfit;color:${i?'#8A3B3E':'#0F4F4B'};display:none`;ov.appendChild(d);});
mSplitL.innerHTML='Sekarang:<br>ditambal';mSplitR.innerHTML='Nanti:<br>saluran akar';
// garansi text on card
const _tbCard=tbCard;tbCard=function(){_tbCard();const c5=document.getElementById('c5');if(c5)c5.textContent='garansi setelah perawatan · dokter gigi';};
const _rs3=window.renderScene;
window.renderScene=function(name,t,D){
  const ph=D?t/D:0;mLab.forEach(d=>d.style.display='none');mSplitL.style.display=mSplitR.style.display='none';
  if(!name.startsWith('m_')){molA.visible=molB.visible=false;return _rs3(name,t,D);}
  setVis({ground:true});smile.visible=false;scene.background=BG;ground.position.y=-2.4;sun.intensity=2.2;
  molA.visible=true;molB.visible=false;molA.position.set(0,0,0);molA.scale.setScalar(1);molA.rotation.set(0,0,0);
  if(name==='m_hook'){molA.rotation.set(0.35,-0.5+0.25*ease(ph),0);molState(molA,{spot:back((t-0.5)/0.4)*1.3});camera.position.set(0,2.4,8.6);camera.lookAt(0,0.95,0);
    fade.style.background='#F4EFE6';fade.style.opacity=1-ease(t/0.25);pills2('Lubang gigi','nggak bisa nutup sendiri',t,0.3);}
  if(name==='m_slice'){const op=ease(ph/0.45);molA.rotation.set(0.1*(1-op),-0.35*(1-op),0);molState(molA,{open:op,spot:1,grow:0.15+0.75*ease((ph-0.45)/0.5),pain:ph>0.9?0.5+0.5*Math.sin(t*9):0});
    camera.position.set(0,0.3,8.2);camera.lookAt(0,0.36,0);molA.updateMatrixWorld();showLabels(molA,ease((ph-0.35)/0.15)*(1-ease((ph-0.8)/0.15)));
    pills2('Di dalam,','makin dekat ke saraf',t,0.3);}
  if(name==='m_paths'){molB.visible=true;[molA,molB].forEach((M,i)=>{M.position.set(i?0.66:-0.66,0.1,0);M.scale.setScalar(0.52);});
    molState(molA,{open:1,grow:0.35,clean:ease(ph/0.25),fill:ease((ph-0.25)/0.35)});const pain=ease((ph-0.35)/0.2)*(0.5+0.5*Math.sin(t*9));molState(molB,{open:1,grow:cl(0.6,1,ease(ph/0.5)),pain});
    camera.position.set(0,0.3,8.2);camera.lookAt(0,0.3,0);mSplitL.style.display=mSplitR.style.display='block';
    pills2('Kalau masih kecil,','cukup ditambal',t,0.2);if(ph>0.33){x1.textContent='Sampai saraf,';x2.textContent='bisa sakit berdenyut';}}
  if(name==='m_fill'){molState(molA,{open:1,grow:0.4,clean:ease(ph/0.18),fill:ease((ph-0.18)/0.35),glow:0.8*ease((ph-0.5)/0.1)*(1-ease((ph-0.68)/0.15))});
    camera.position.set(0,0.3,cl(8.2,7.2,ease(ph)));camera.lookAt(0,0.36,0);
    pills2('Solusinya:','tambal gigi',t,0.2);if(ph>0.38){x1.textContent='Ruma Dental';x2.textContent='mulai Rp250.000';}}
  renderer.render(scene,camera);
};
