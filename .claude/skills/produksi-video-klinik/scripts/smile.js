
// ===== SMILE =====
const smile=new THREE.Group();scene.add(smile);smile.visible=false;
const TINT0=new THREE.Color('#F7F1E4'),TINTY=new THREE.Color('#E8D29C'),BRIGHT=new THREE.Color('#FFFFFF');
const teethMat=new THREE.MeshPhysicalMaterial({color:'#F7F1E4',roughness:0.3,clearcoat:0.5,clearcoatRoughness:0.3});
const planeF=new THREE.Plane(new THREE.Vector3(0,0,-1),5);
const incMat=new THREE.MeshPhysicalMaterial({color:'#F7F1E4',roughness:0.3,clearcoat:0.5,side:THREE.DoubleSide});incMat.clippingPlanes=[planeF];
const incDent=new THREE.MeshStandardMaterial({color:'#E3BC66',roughness:0.6,side:THREE.DoubleSide});incDent.clippingPlanes=[planeF];
const upper=[];const R=3.1;
const spec=[[0.46,0.66],[0.48,0.74],[0.5,0.86],[0.6,0.96],[0.6,0.96],[0.5,0.86],[0.48,0.74],[0.46,0.66]];
let total=spec.reduce((a,s)=>a+s[0],0),acc=-total/2;
spec.forEach(([w,h],i)=>{const mid=acc+w/2;acc+=w;const a=mid/R;
  const g=new THREE.Group();g.position.set(R*Math.sin(a),0,R*Math.cos(a)-R);g.rotation.y=a;smile.add(g);
  const mat=i===3?incMat:teethMat;
  const m=new THREE.Mesh(new RoundedBoxGeometry(w*0.93,h,0.42,5,0.13),mat);m.position.y=-h/2;m.castShadow=true;g.add(m);
  if(i===3){const d=new THREE.Mesh(new RoundedBoxGeometry(w*0.6,h*0.72,0.22,4,0.08),incDent);d.position.set(0,-h/2+0.06,-0.03);g.add(d);}
  // stain dots on front face
  const ds=[];let s=i*97+13;const rnd=()=>{s=(s*16807)%2147483647;return s/2147483647};
  for(let k=0;k<(i===3?16:7);k++){const dm=new THREE.Mesh(new THREE.SphereGeometry(0.028+rnd()*0.022,10,8),new THREE.MeshStandardMaterial({color:'#6B4630',transparent:true}));
    const p=new THREE.Vector3((rnd()-0.5)*w*0.72,-h*(0.15+rnd()*0.7),0.215);dm.position.copy(p);dm.scale.set(1,1,0.4);dm.userData={p:p.clone(),r:rnd()};g.add(dm);ds.push(dm);}
  const gel=new THREE.Mesh(new RoundedBoxGeometry(w*0.98,h*1.04,0.48,5,0.15),new THREE.MeshStandardMaterial({color:'#2CCDBD',transparent:true,opacity:0,depthWrite:false,roughness:0.2}));gel.position.y=-h/2;g.add(gel);
  upper.push({g,m,ds,gel,x:g.position.x,inc:i===3});});
// lower teeth
for(let i=0;i<8;i++){const w=0.4,a=(i-3.5)*w/2.75;const g=new THREE.Group();g.position.set(2.75*Math.sin(a),-1.0,2.75*Math.cos(a)-2.75-0.12);g.rotation.y=a;smile.add(g);
  const m=new THREE.Mesh(new RoundedBoxGeometry(w*0.92,0.62,0.36,4,0.11),teethMat);m.position.y=-0.31;g.add(m);}
// gums
const gumM=new THREE.MeshStandardMaterial({color:'#E3A49B',roughness:0.7});
upper.forEach(u=>{const gm=new THREE.Mesh(new RoundedBoxGeometry(0.66,0.42,0.5,3,0.15),gumM);gm.position.set(u.g.position.x,0.16,u.g.position.z-0.04);gm.rotation.y=u.g.rotation.y;smile.add(gm);});
// mouth interior
const inside=new THREE.Mesh(new THREE.ShapeGeometry((()=>{const sh=new THREE.Shape();sh.moveTo(-3.3,-0.42);sh.bezierCurveTo(-2.4,-1.05,-1.3,-1.3,0,-1.3);sh.bezierCurveTo(1.3,-1.3,2.4,-1.05,3.3,-0.42);sh.bezierCurveTo(2.4,0.0,1.4,0.35,0,0.35);sh.bezierCurveTo(-1.4,0.35,-2.4,0.0,-3.3,-0.42);return sh})()),new THREE.MeshStandardMaterial({color:'#5A2C2C',roughness:1}));inside.position.set(0,0,-1.2);smile.add(inside);
// lips
const lipM=new THREE.MeshStandardMaterial({color:'#CF8D84',roughness:0.62});
function lipShape(outer,inner){const sh=new THREE.Shape();sh.moveTo(...outer[0]);for(let i=1;i<outer.length;i+=3)sh.bezierCurveTo(...outer[i],...outer[i+1],...outer[i+2]);for(let i=1;i<inner.length;i+=3)sh.bezierCurveTo(...inner[i],...inner[i+1],...inner[i+2]);return sh;}
const ulO=[[-3.45,-0.42],[-2.6,0.25],[-1.4,0.66],[-0.45,0.62],[-0.2,0.6],[-0.08,0.5],[0,0.47],[0.08,0.5],[0.2,0.6],[0.45,0.62],[1.4,0.66],[2.6,0.25],[3.45,-0.42]];
const ulI=[[3.45,-0.42],[2.4,-0.05],[1.4,0.22],[0,0.24],[-1.4,0.22],[-2.4,-0.05],[-3.45,-0.42]];
const llI=[[-3.45,-0.42],[-2.4,-0.95],[-1.3,-1.17],[0,-1.17],[1.3,-1.17],[2.4,-0.95],[3.45,-0.42]];
const llO=[[3.45,-0.42],[2.7,-1.45],[1.4,-1.7],[0,-1.7],[-1.4,-1.7],[-2.7,-1.45],[-3.45,-0.42]];
const ext={depth:0.35,bevelEnabled:true,bevelThickness:0.28,bevelSize:0.16,bevelSegments:8,curveSegments:40};
const lipU=new THREE.Mesh(new THREE.ExtrudeGeometry(lipShape(ulO,ulI),ext),lipM);lipU.position.z=0.28;lipU.castShadow=true;smile.add(lipU);
const lipL=new THREE.Mesh(new THREE.ExtrudeGeometry(lipShape(llI,llO),ext),lipM);lipL.position.z=0.28;lipL.castShadow=true;smile.add(lipL);
// skin backdrop (soft, no face)
smile.position.y=0;

function smileState(o){ // o:{tint,dots,dotSink,cut,steps:{scal,gel,white},wide}
  teethMat.color.copy(TINT0).lerp(TINTY,o.tint||0);
  incMat.color.copy(teethMat.color);
  upper.forEach(u=>{const ux=(u.x+2.6)/5.2;
    const scalK=o.scal!==undefined?Math.min(1,Math.max(0,(o.scal*1.4-ux*0.4))):0;
    u.ds.forEach(d=>{const app=o.dots===undefined?1:Math.min(1,Math.max(0,(o.dots*1.6-d.userData.r*0.6)));
      const sink=o.dotSink||0;d.position.copy(d.userData.p);d.position.z-=0.07*sink;d.position.y+=1.2*scalK;
      const sc=app*(1-0.45*sink);d.scale.set(sc,sc,sc*0.4);d.material.opacity=(1-0.55*sink)*(1-scalK);d.visible=sc>0.001&&scalK<0.999;});
    const gk=o.gel!==undefined?Math.min(1,Math.max(0,(o.gel*1.4-ux*0.4))):0;const go=o.gelOut||0;u.gel.material.opacity=0.3*gk*(1-go);
  });
  if(o.white!==undefined){teethMat.color.lerp(BRIGHT,o.white);incMat.color.copy(teethMat.color);}
  planeF.constant=o.cut!==undefined?cl(5,-0.06,o.cut):5;
  const w=1+(o.wide||0)*0.05;smile.scale.set(w,1+(o.wide||0)*0.015,1);lipU.position.y=(o.wide||0)*0.06;lipL.position.y=-(o.wide||0)*0.08;
}
function smileCam(k){ // k=0 full, 1 incisor close
  const inc=upper[3].g.position;const A=new THREE.Vector3(0,0.4,24),LA=new THREE.Vector3(0,0.2,0);
  const B=new THREE.Vector3(inc.x+0.55,-0.35,2.5),LB=new THREE.Vector3(inc.x,-0.45,0);
  camera.position.copy(A).lerp(B,k);camera.lookAt(LA.clone().lerp(LB,k));}

const _rs=window.renderScene;
window.renderScene=function(name,t,D){
  if(!name.startsWith('sm_')){smile.visible=false;return _rs(name,t);}
  setVis({});smile.visible=true;scene.background=BG;sun.intensity=2.1;
  const ph=D?t/D:0;
  if(name==='sm_in'){ // nempel -> meresap + cut
    const z=ease(ph/0.45);smileCam(z);
    const dk=Math.min(1,Math.max(0,(ph-0.15)/0.35));const sink=ease((ph-0.55)/0.25);
    smileState({tint:0.15+0.5*sink,dots:dk,dotSink:sink,cut:ease((ph-0.72)/0.22)});
    fade.style.background='#3A2418';fade.style.opacity=1-ease(t/0.5);
    if(ph<0.55)pills2('Warna kopi & teh','nempel di permukaan',ph*D,0.4,0.52*D);else pills2('Lama-lama','meresap ke dalam',t,0.57*D);}
  if(name==='sm_out'){smileCam(1-ease(ph/0.7));smileState({tint:0.75,dots:1,dotSink:1,cut:1-ease(ph/0.4)});
    pills2('Makanya','gigi makin kuning',t,0.2);}
  if(name==='sm_good'){smileCam(0);smileState({tint:0.75,dots:1,dotSink:1});sun.intensity=2.1+0.6*ease(ph/0.6);
    pills2('Kabar baiknya,','bisa dicerahkan lagi',t,0.2);}
  if(name==='sm_steps'){ // o.s1,o.s2 split points (fractions), wipe at end
    const o=window._fo||{};const s1=o.s1||0.3,s2=o.s2||0.62;smileCam(0);
    const scal=ease((ph-s1)/(s2-s1-0.04));const gel=ease((ph-s2)/0.18);const white=ease((ph-s2-0.04)/0.14);const gout=ease((ph-s2-0.13)/0.06);
    smileState({tint:0.75*(1-0.35*scal),dots:1,dotSink:1,scal,gel,white,gelOut:gout,wide:ease((ph-0.82)/0.08)});
    if(ph<s1)pills2('Klinik Gigi Ruma Dental','2 langkah',t,0.2,s1*D-0.15);else if(ph<s2)pills2('Langkah 1','scaling: noda permukaan',t,s1*D);else pills2('Langkah 2','bleaching: warna dalam',t,s2*D);
    const wk=ease((ph-0.9)/0.1);if(wk>0){wipe.style.display='block';wipe.style.opacity=1;wipe.style.transform=`scale(${cl(0.15,1.25,wk)})`;roof.style.opacity=wk;}}
  renderer.render(scene,camera);
};
