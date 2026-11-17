#!/usr/bin/env python3
"""V4: 28 baris (file per baris, tag emosi) -> audio/narasi.wav + src3d/timing.js (baris, kata perkiraan, batas shot)."""
import json, subprocess, pathlib, re
P=pathlib.Path(__file__).resolve().parents[1]; V=P/'audio/v1'
L=[('N1','N','Hari keempat misi Ijal. Gusinya mulai membaik… dan dia mulai bosan di rumah.',0.6,['membaik…']),
('I1','I','Om… Ijal udah empat hari di Makassar, belum pernah jalan-jalan.',0.4,[]),
('P1','P','Iye, betul juga. Sore ini Om ajak kamu cicip makanan Makassar.',0.4,['makanan','Makassar.']),
('P2','P','Ini pisang epe. Pisangnya dibakar, dipenyet, terus disiram gula merah. Coba mi.',2.4,['pisang','epe.']),
('I2','I','Hmm… enak banget, Om!',0.4,[]),
('I3','I','Eh, tapi Ijal kan lagi jaga gigi, Om. Manis begini aman nggak?',0.6,['aman']),
('P3','P','Ah, tidak apa-apa ji. Gula merah itu alami, tidak bikin rusak gigi.',0.3,['alami,']),
('I4','I','Oh, alami… ya udah, satu lagi deh!',0.4,[]),
('D1','D','Ijal, itu sudah kue keberapa? Jangan terlalu banyak. Nanti gigimu rusak, gusimu tambah berdarah.',2.2,['terlalu','banyak.']),
('I5','I','Santai, Kak… nanti malam juga Ijal sikat gigi.',0.3,[]),
('I6','I','Kakak juga… dari tadi cokelatnya dimakan terus.',0.6,['terus.']),
('D2','D','Beda, Ijal. Kakak makannya sedikit-sedikit. Kakak baca di sini, katanya makan manis sedikit-sedikit itu tidak merusak gigi.',0.3,['sedikit-sedikit']),
('I7','I','Masa sih, Kak…?',0.3,[]),
('N2','N','Tunggu dulu. Ada tiga hal yang perlu diluruskan.',1.0,['tiga']),
('N3','N','Hati-hati dengan info yang beredar. Setiap kali makan atau minum manis, kuman di gigi membuat asam selama kira-kira 20 sampai 30 menit. Kalau dimakan sedikit-sedikit dari sore sampai malam, gigi justru diserang terus-menerus.',0.4,['info','asam','diserang','terus-menerus.']),
('D3','D','…Jadi artikel ini salah?',0.4,[]),
('N4','N','Gula merah, gula aren, madu, semuanya tetap gula. Kuman tidak peduli asalnya.',0.6,['tetap','gula.']),
('N5','N','Sikat gigi malam itu penting. Tapi kalau ngemil manis terus dari sore, gigi sudah diserang berkali-kali sebelum disikat.',0.6,['berkali-kali']),
('I8','I','Yah… barongko-ku…',0.3,[]),
('N6','N','Yang benar: makan manis sekalian, jangan dicicil seharian. Setelahnya, kumur air putih. Perbanyak minum air putih, dan tetap sikat gigi dua kali sehari.',0.6,['sekalian,','kumur','air','putih.']),
('I9','I','Masih ada sedikit merahnya, Kak… tapi udah mendingan.',1.7,['mendingan.']),
('D4','D','Iye. Kakak catat, hari keempat membaik.',0.3,['membaik.']),
('D5','D','…Hambar.',1.3,['…Hambar.']),
('I10','I','Hahaha, sabar, Kak!',0.3,[]),
('N7','N','Gusi Ijal mulai membaik… tapi misinya belum selesai. Ikuti terus… Misi Anak Rantau.',1.2,['membaik…'])]
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
def span(f):
    o=subprocess.run(['ffmpeg','-i',str(f),'-af','silencedetect=n=-38dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
    ss=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',o)]; se=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
    d=dur(f); a=se[0] if se and ss and ss[0]<0.05 else 0.0
    b=ss[-1] if ss and (len(ss)>len(se) or (se and se[-1]>=d-0.05)) else d
    return a,max(b,a+0.3),d
t=0; lines={}; order=[]
for k,sp,txt,gap,hl in L:
    t+=gap; f=V/f'{k}.mp3'; a,b,d=span(f); ws=txt.split(); tot=sum(len(w)+1 for w in ws); cur=t+a; W=[]
    for w in ws:
        dd=(b-a)*(len(w)+1)/tot; W.append([w,round(cur,3),round(cur+dd*0.92,3)]); cur+=dd
    lines[k]={'id':k,'sp':sp,'at':round(t,3),'s':round(t+a,3),'e':round(t+b,3),'hl':hl,'w':W}; order.append(k); t+=b+0.18
S=lambda k:lines[k]['s']; E=lambda k:lines[k]['e']; A=lambda k:lines[k]['at']
wt=lambda k,w:[x[1] for x in lines[k]['w'] if x[0]==w][0]
total=round(E('N7')+3.6,2)
setiap=wt('N3','Setiap')
SH=[('living',0),('sore',E('P1')+0.4),('malam',E('I4')+0.5),('freeze',A('N2')-0.3),('mouthAcid',setiap-0.2),('dindaReact',A('D3')-0.2),
    ('flashback',A('N4')-0.2),('ijalMitos',A('N5')-0.2),('mouthTips',A('N6')-0.2),('bathNight',E('N6')+0.6),('exterior',A('N7')-0.4)]
shots=[{'n':n,'t0':round(a,3),'t1':round(SH[i+1][1] if i+1<len(SH) else total,3)} for i,(n,a) in enumerate(SH)]
cue={'cart':E('P1')+0.6,'i3':S('I3'),'p3':S('P3'),'i4':S('I4'),'d2':S('D2'),'phone':wt('D2','Kakak')+0.0,'tags':[A('N2')+0.3],'hoax':S('N3'),
     'sekalian':wt('N6','sekalian,'),'kumur':wt('N6','kumur'),'perbanyak':wt('N6','Perbanyak'),'dua':wt('N6','dua'),'d5':A('D5')-0.9,'i8':S('I8')}
# audio
args=['ffmpeg','-v','error','-y']; fl=[]; n=0
for k in order:
    args+=['-i',str(V/f'{k}.mp3')]; d=int(lines[k]['at']*1000)
    fl.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,aecho=0.8:0.4:18:0.1,adelay={d}|{d}[a{n}]"); n+=1
def amb(f,a,b,vol):
    global n
    args.extend(['-stream_loop','-1','-i',str(V/f'{f}.mp3')]); d=int(a*1000); du=b-a
    fl.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{du:.2f},afade=t=in:d=0.6,afade=t=out:st={max(0,du-0.6):.2f}:d=0.6,volume={vol},adelay={d}|{d}[a{n}]"); n+=1
amb('sfx-sore',shots[1]['t0'],shots[2]['t0'],0.16); amb('sfx-malam',shots[2]['t0'],shots[3]['t0'],0.14); amb('sfx-malam',shots[9]['t0'],shots[10]['t0']+3,0.14)
args+=['-i',str(V/'sfx-gerobak.mp3')]; d=int(cue['cart']*1000); fl.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,volume=0.5,adelay={d}|{d}[a{n}]"); n+=1
fl.append(''.join(f'[a{i}]' for i in range(n))+f'amix=inputs={n}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,apad=whole_dur={total},atrim=0:{total}[out]')
args+=['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2',str(P/'audio/narasi.wav')]
subprocess.run(args,check=True)
(P/'src3d/timing.js').write_text('window.TIMING='+json.dumps({'lines':[lines[k] for k in order],'shots':shots,'cue':cue,'total':total},ensure_ascii=False)+';\n')
print('total',total); [print(s['n'],s['t0'],s['t1']) for s in shots]
