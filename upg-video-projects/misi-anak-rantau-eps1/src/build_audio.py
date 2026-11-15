#!/usr/bin/env python3
"""Potong take per tokoh jadi baris, susun dialog, tulis audio/narasi.wav + work/timing.json"""
import json, subprocess, pathlib
P=pathlib.Path(__file__).resolve().parents[1]; A=P/'audio'
LINES=[('N','Hari ketiga Ijal di Makassar. Dia sudah kenal tiga hal: coto… macet… dan darah di sikat giginya.',['coto…','macet…','darah']),
('I','Din… ini normal, kan?',[]),('D','Itu darah, Jal.',['darah,']),
('N','Ijal, mahasiswa baru dari Jakarta. Semalam dia baru janji ke ibunya…',['Jakarta.']),
('I','Tenang, Bu. Gue bisa ngurus diri sendiri!',['sendiri!']),('I','Beres!',[]),
('I','Tenang. Gue udah beli yang bulunya paling keras. Biar kotorannya kagak berani balik.',['paling','keras.']),
('D','Gusimu berdarah… terus solusimu sikat lebih keras?',['lebih','keras?']),('I','Namanya juga usaha.',[]),
('P','Dulu Om sikat pakai sabut kelapa. Aman ji.',['sabut','kelapa.']),('D','Bapak…',[]),
('D','Tunggu. Di sini katanya gusi berdarah itu karena kurang vitamin C.',['vitamin','C.']),
('I','Din… ini buat sebulan?',['sebulan?']),('D','Buat seminggu.',['seminggu.']),
('N','Tunggu dulu. Gusi berdarah paling sering karena plak: lapisan kuman yang menumpuk di batas gigi dan gusi. Gusinya meradang, jadi gampang berdarah.',['plak:','meradang,']),
('N','Sikat lebih keras bukan solusi. Bulu sikat yang keras malah bisa melukai gusi.',['bukan','solusi.','melukai']),
('N','Jeruk? Kurang vitamin C berat memang bisa bikin gusi berdarah, tapi jarang. Jeruknya tetap enak, kok.',['jarang.']),
('N','Yang benar: pakai sikat bulu lembut, sikat dua kali sehari dengan gerakan pelan di batas gusi, dan bersihkan sela gigi.',['lembut,','pelan']),
('N','Kalau lebih dari dua minggu masih berdarah, periksa ke dokter gigi. Bisa jadi ada karang gigi, yang tidak hilang hanya dengan sikat gigi.',['dua','minggu','periksa']),
('I','Oke. Dua minggu. Gue buktiin gue bisa sendiri.',['Dua','minggu.']),('D','Iye. Saya catat.',[]),
('N','Bisakah Ijal bertahan empat belas hari? Ikuti terus Misi Anak Rantau.',['empat','belas','hari?'])]
GAP={0:0.3,3:0.3,4:1.5,5:2.0,9:0.3,10:0.5,11:1.0,13:0.7,18:0.8,20:2.8}
SRC={'N':'narator','I':'ijal','D':'dinda','P':'paman'}
W={k:[w for w in json.load(open(A/f'w-{v}.json'))['words'] if w.get('type','word')=='word'] for k,v in SRC.items()}
ptr={k:0 for k in SRC}; t=0.4; out=[]; parts=[]
for i,(sp,text,hl) in enumerate(LINES):
    n=len(text.split()); ws=W[sp][ptr[sp]:ptr[sp]+n]; ptr[sp]+=n
    assert [w['text'] for w in ws]==text.split(), (i,[w['text'] for w in ws])
    allw=W[sp]; j=ptr[sp]
    prev_end=allw[j-n-1]['end'] if j-n-1>=0 else 0
    nxt=allw[j]['start'] if j<len(allw) else ws[-1]['end']+0.3
    a=max(prev_end+0.02,ws[0]['start']-0.06); b=min(nxt-0.02,ws[-1]['end']+0.15) if j<len(allw) else ws[-1]['end']+0.25
    a=max(0,a); off=t-a
    out.append({'sp':sp,'s':round(ws[0]['start']+off,3),'e':round(ws[-1]['end']+off,3),'hl':hl,'w':[[w['text'],round(w['start']+off,3)] for w in ws]})
    parts.append((SRC[sp],a,b,t)); t+= (b-a)+GAP.get(i,0.35)
total=round(out[-1]['e']+3.2,2)
args=['ffmpeg','-v','error','-y']; fl=[]
for k,(src,a,b,st) in enumerate(parts):
    args+=['-i',str(A/f'{src}.mp3')]
    fl.append(f"[{k}:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={max(0,b-a-0.04):.3f}:d=0.04,adelay={int(st*1000)}|{int(st*1000)}[a{k}]")
fl.append(''.join(f'[a{k}]' for k in range(len(parts)))+f'amix=inputs={len(parts)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,apad=whole_dur={total}[out]')
args+=['-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2',str(A/'narasi.wav')]
subprocess.run(args,check=True)
(P/'work').mkdir(exist_ok=True); json.dump({'lines':out,'total':total},open(P/'work/timing.json','w'),ensure_ascii=False)
print('total',total)
