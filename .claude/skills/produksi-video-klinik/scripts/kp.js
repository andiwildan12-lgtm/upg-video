
// ===== KUNJUNGAN PERTAMA =====
function drawNotif(n,pressed){phX.fillStyle='#DDE7E1';phX.fillRect(0,0,360,720);
  phX.fillStyle='#1F2A28';phX.textAlign='center';phX.font='300 84px Outfit';phX.fillText('07.30',180,150);phX.font='500 22px Outfit';phX.fillText('Jumat, 20 November',180,186);
  for(let i=0;i<n;i++){const y=230+i*118;phX.fillStyle='rgba(255,255,255,.93)';phX.beginPath();phX.roundRect(16,y,328,104,18);phX.fill();
    phX.textAlign='left';phX.fillStyle='#5E6B67';phX.font='500 18px Outfit';phX.fillText('PENGINGAT',34,y+30);
    phX.fillStyle='#1F2A28';phX.font='700 28px Outfit';phX.fillText('Cek gigi',34,y+66);
    const last=i===n-1;phX.fillStyle=(last&&pressed)?'#0F4F4B':'#2CCDBD';phX.beginPath();phX.roundRect(232,y+40,96,44,22);phX.fill();
    phX.fillStyle=(last&&pressed)?'#fff':'#06332F';phX.textAlign='center';phX.font='700 22px Outfit';phX.fillText('Nanti',280,y+69);}
  phTex.needsUpdate=true;}
mSplitL.innerHTML='Dicek lebih awal:<br>lebih ringan';mSplitR.innerHTML='Ditunda:<br>lebih panjang';
function kpCard(){card.innerHTML=`<img src="card_logo.png" style="width:440px" id="c0"><div id="c1" style="font:700 132px/1 Outfit;color:#0F4F4B;margin-top:80px;letter-spacing:-2px">Cek dulu,</div>
<div id="c2" style="font:600 64px Outfit;color:#0F4F4B;margin-top:14px">baru putuskan</div>
<div id="c3" style="font:600 44px/1.3 Outfit;background:#2CCDBD;color:#06332F;padding:12px 30px 16px;border-radius:12px;margin-top:50px">kondisi · pilihan · biaya<br>dijelaskan sebelum tindakan</div>
<div id="c4" style="font:600 46px Outfit;color:#0F4F4B;margin-top:40px">dikerjakan dokter gigi</div>
<div id="c5" style="font:500 40px Outfit;color:#5E6B67;margin-top:60px">Tempat Nyaman untuk Kembali Tersenyum</div>
<div id="c6" style="font:500 44px/1.45 Inter,Outfit;color:#1F2A28;margin-top:24px">Jl. Rusa No. 65, Maricaya, Makassar</div>
<div id="c7" style="font:700 44px Inter,Outfit;color:#1F2A28">WA 0898-7735-463</div>`;}
tbCard=kpCard;
const _rs4=window.renderScene;
window.renderScene=function(name,t,D){const ph=D?t/D:0;phone.rotation.y=name.startsWith('kp_')?0:-0.35;
  if(name==='kp_hook'||name==='kp_snooze'){mLab.forEach(d=>d.style.display='none');mSplitL.style.display=mSplitR.style.display='none';molA.visible=molB.visible=false;
    setVis({hero:true,desk:true,steam:true,ground:true,phone:true});deskBase();sun.intensity=2.1;scene.background=BG;
    if(name==='kp_hook'){drawCal('JUMAT',20);const pr=(t%1.6)>1.1;const key='h'+pr;if(window._ph!==key){drawNotif(1,pr);window._ph=key;}
      const k=ease(t/D);camera.position.set(1.05,cl(4.4,3.6,k),cl(2.6,2.2,k));camera.lookAt(1.05,0,0.25);
      fade.style.background='#F4EFE6';fade.style.opacity=1-ease(t/0.25);pills2('Bukan sakitnya,','tapi nggak tahu bakal diapain',t,0.3);}
    else{const n=1+Math.min(3,Math.floor(ph*4));const day=['JUMAT','SABTU','SENIN','RABU'][n-1];drawCal(day,[20,21,23,25][n-1]);const key='s'+n;if(window._ph!==key){drawNotif(n,true);window._ph=key;}
      const k=ease(ph);camera.position.set(cl(1.3,0.9,k),cl(3.9,4.3,k),cl(2.6,2.9,k));camera.lookAt(1.0,0,0.3);
      pills2('Takut dicabut,','takut biaya',t,0.2);if(ph>0.6){x1.textContent='Jadi…';x2.textContent='ditunda, ditunda lagi';}}
    renderer.render(scene,camera);return;}
  if(name==='kp_early'){mLab.forEach(d=>d.style.display='none');setVis({ground:true});smile.visible=false;scene.background=BG;ground.position.y=-2.4;sun.intensity=2.2;
    molA.visible=molB.visible=true;[molA,molB].forEach((M,i)=>{M.position.set(i?0.66:-0.66,0.1,0);M.scale.setScalar(0.52);M.rotation.set(0,0,0);});
    molState(molA,{open:1,grow:0.12});molState(molB,{open:1,grow:cl(0.3,1,ease(ph/0.7)),pain:ph>0.6?0.5+0.5*Math.sin(t*9):0});
    camera.position.set(0,0.3,8.2);camera.lookAt(0,0.3,0);mSplitL.style.display=mSplitR.style.display='block';
    pills2('Padahal, kalau dicek lebih awal,','pilihannya lebih ringan',t,0.2);renderer.render(scene,camera);return;}
  if(name==='kp_sched'){molA.visible=molB.visible=false;mSplitL.style.display=mSplitR.style.display='none';return _rs4('c8',t*1.5,D);}
  return _rs4(name,t,D);};
