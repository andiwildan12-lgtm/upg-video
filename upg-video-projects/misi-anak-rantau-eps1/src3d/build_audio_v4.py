#!/usr/bin/env python3
"""V4: 28 baris (file per baris, tag emosi) -> audio/narasi.wav + src3d/timing.js (baris, kata perkiraan, batas shot)."""
import json, subprocess, pathlib, re
P=pathlib.Path(__file__).resolve().parents[1]; V=P/'audio/v4'
L=[('N1','N','Ini Ijal. Tiga hari di Makassar… dan semalam, dia baru janji ke ibunya, bisa urus diri sendiri.',0.6,['janji']),
('I1','I','Tenang, Bu… Ijal sikat yang bersih banget…',0.3,[]),
('I2','I','Lho… lho… kok merah?! Kak… Kak Dinda!!',1.0,['merah?!']),
('D1','D','Kenapa, Ijal? Pagi-pagi sudah teriak.',0.5,[]),
('I3','I','Ini, Kak… normal, kan?',0.15,['normal,']),
('D2','D','Ijal… itu darah. Pernah begini sebelumnya?',0.6,['darah.']),
('I4','I','Kadang sih… sedikit. Kirain biasa.',0.35,['biasa.']),
('P1','P','Ah, gusi berdarah itu biasa ji. Om dulu juga begitu.',0.6,['biasa']),
('I5','I','Tuh kan, Kak! Kata Om biasa.',0.2,[]),
('D3','D','Tunggu… Kakak cek dulu. Nah, di sini katanya… karena kurang vitamin C.',0.4,['vitamin','C.']),
('I6','I','Oke! Kalau gitu, aku tahu harus ngapain!',0.3,[]),
('I7','I','Sikat gigi dengan bulu paling keras di toko! Biar kotorannya kagak berani balik.',2.0,['paling','keras']),
('D4','D','Jeruk tiga kilo. Vitamin C-nya cukup buat kita berdua.',0.3,['tiga','kilo.']),
('I8','I','Kak… itu buat sebulan?',0.7,['sebulan?']),
('D5','D','Buat seminggu.',0.35,['seminggu.']),
('P2','P','Ramai mi solusinya…',0.5,[]),
('N2','N','Tunggu dulu. Ada tiga hal yang perlu diluruskan.',1.0,['tiga']),
('N3','N','Gusi berdarah bukan hal biasa. Paling sering, itu tanda gusi meradang karena plak: lapisan kuman yang menumpuk di batas gigi dan gusi.',0.4,['bukan','plak:']),
('P3','P','…Om kira biasa ji.',0.5,[]),
('N4','N','Sikat lebih keras bukan solusi. Bulu sikat yang keras malah bisa melukai gusi.',0.5,['bukan','solusi.','melukai']),
('I9','I','Yah… sikat baruku…',0.3,[]),
('N5','N','Kurang vitamin C berat memang bisa bikin gusi berdarah, tapi itu jarang. Jeruknya tetap enak, kok.',0.5,['jarang.']),
('D6','D','Ya sudah… tetap Kakak makan.',0.3,[]),
('N6','N','Yang benar: pakai sikat bulu lembut, sikat dua kali sehari dengan gerakan pelan di batas gusi, dan bersihkan sela gigi. Kalau lebih dari dua minggu masih berdarah, periksa ke dokter gigi. Bisa jadi ada karang gigi, yang tidak hilang hanya dengan sikat gigi.',0.6,['lembut,','dua','kali','periksa']),
('I10','I','Oke, Kak. Dua minggu. Ijal buktiin… Ijal bisa urus sendiri.',1.8,['Dua','minggu.']),
('D7','D','Iye. Kakak catat, nah.',0.3,[]),
('I11','I','…Belum.',2.4,['…Belum.']),
('N7','N','Bisakah Ijal bertahan empat belas hari? Ikuti terus… Misi Anak Rantau.',1.2,['empat','belas','hari?'])]
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
i2k=lines['I2']['w'][3][1]   # kata "Kak…"
kalau=wt('N6','Kalau')
SH=[('bathBrush',0),('sink',A('I2')-0.6),('mirror',i2k-0.1),('bathWide',A('D1')-0.4),('bathPaman',A('P1')-0.7),
    ('living',E('I6')+0.5),('freeze',A('N2')-0.3),('mouthPlak',A('N3')-0.2),('pamanClose',A('P3')-0.2),('mouthHard',A('N4')-0.2),
    ('ijalSad',A('I9')-0.2),('dindaOrange',A('N5')-0.2),('mouthSoft',A('N6')-0.2),('mouth2w',kalau-0.15),('bathNight',E('N6')+0.6),('exterior',A('N7')-0.4)]
shots=[{'n':n,'t0':round(a,3),'t1':round(SH[i+1][1] if i+1<len(SH) else total,3)} for i,(n,a) in enumerate(SH)]
cue={'dEnter':A('D1')-0.4,'pEnter':A('P1')-0.7,'d3':S('D3'),'i6':S('I6'),'i3':S('I3'),'ting':A('I11')-1.7,'tags':[A('N2')+0.2,A('N2')+0.9,A('N2')+1.6],
     'k2':wt('N6','dua'),'i7':S('I7'),'d4':S('D4'),'lembut':wt('N6','lembut,'),'pelan':wt('N6','pelan'),'sela':wt('N6','sela')}
# audio
args=['ffmpeg','-v','error','-y']; fl=[]; n=0
for k in order:
    args+=['-i',str(V/f'{k}.mp3')]; d=int(lines[k]['at']*1000)
    fl.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,aecho=0.8:0.4:18:0.1,adelay={d}|{d}[a{n}]"); n+=1
def amb(f,a,b,vol):
    global n
    args.extend(['-stream_loop','-1','-i',str(V/f'{f}.mp3')]); d=int(a*1000); du=b-a
    fl.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{du:.2f},afade=t=in:d=0.6,afade=t=out:st={max(0,du-0.6):.2f}:d=0.6,volume={vol},adelay={d}|{d}[a{n}]"); n+=1
amb('sfx-mandi',0,shots[5]['t0'],0.18); amb('sfx-malam',shots[14]['t0'],shots[15]['t0']+3,0.15)
args+=['-i',str(V/'sfx-notif.mp3')]; d=int(cue['ting']*1000); fl.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,volume=0.5,adelay={d}|{d}[a{n}]"); n+=1
fl.append(''.join(f'[a{i}]' for i in range(n))+f'amix=inputs={n}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,apad=whole_dur={total},atrim=0:{total}[out]')
args+=['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2',str(P/'audio/narasi.wav')]
subprocess.run(args,check=True)
(P/'src3d/timing.js').write_text('window.TIMING='+json.dumps({'lines':[lines[k] for k in order],'shots':shots,'cue':cue,'total':total},ensure_ascii=False)+';\n')
print('total',total); [print(s['n'],s['t0'],s['t1']) for s in shots]
