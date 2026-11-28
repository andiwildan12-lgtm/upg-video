import sys, html; sys.path.insert(0,'.')
from data import IO, SC
COLS=5
TIPS = {"WI-IO": ("Gambar tidak muncul di monitor?", ["Cek lagi: laptop & monitor satu WiFi.", "Monitor sudah di SOURCE → HDMI.", "Stop casting, lalu ulangi Cast dari Chrome."])}
def card(n,d,t,j,isi):
    return f'''<div class="card"><div class="ph"><img src="foto/{d['kode']}_{t.replace(':','-')}.jpg"><span class="no">{n}</span></div>
<div class="tx"><b>{html.escape(j)}</b><p>{html.escape(isi)}</p></div></div>'''
def box(cls,title,items,span):
    li="".join(f"<li>{html.escape(x)}</li>" for x in items)
    return f'<div class="box {cls}" style="grid-column:span {span}"><h4>{title}</h4><ul>{li}</ul></div>'
def page(d,hal,pi,last,start):
    out=[]; col=0; row=[]; rows=[]; n=start
    # build bands: list of (headers, cells)
    bands=[]; cur_h=[]; cur_c=[]
    for sec,steps in hal:
        if 0<col and len(steps)<=COLS and col+len(steps)>COLS:
            bands.append((cur_h,cur_c)); cur_h=[]; cur_c=[]; col=0
        for k,s in enumerate(steps):
            if col==COLS:
                bands.append((cur_h,cur_c)); cur_h=[]; cur_c=[]; col=0
            if k==0 or col==0:
                # header for remaining cards of this section in this row
                rem=len(steps)-k; span=min(rem,COLS-col)
                cur_h.append((col,span,sec if k==0 else sec.split(" ")[0]+" lanjutan"))
            cur_c.append(card(n,d,*s)); n+=1; col+=1
    extra=COLS-col
    if last:
        if extra>=2: cur_c.append(box("warn","⚠ Jangan",d["jangan"],extra)); cur_h.append((col,extra,"")); extra=0
    elif d["kode"] in TIPS and extra>=2:
        tt,it=TIPS[d["kode"]]; cur_c.append(box("tip",tt,it,extra)); cur_h.append((col,extra,"")); extra=0
    bands.append((cur_h,cur_c))
    body=""
    for hs,cs in bands:
        hh="".join(f'<div class="sec" style="grid-column:{c+1}/span {s}">{html.escape(t)}</div>' for c,s,t in hs if t)
        body+=f'<div class="band"><div class="hrow">{hh}</div><div class="crow">{"".join(cs)}</div></div>'
    if last and extra:  # jangan box below
        body+=f'<div class="band"><div class="crow">{box("warn","⚠ Jangan",d["jangan"],COLS)}</div></div>'
    tot=len(d["halaman"])
    return f'''<section class="page">
<header><img class="logo" src="logo-upg-mendatar.png"><div class="ht"><span class="kode">WORK INSTRUCTION · {d['kode']}</span><h1>{d['judul']}</h1></div><span class="hal">Hal. {pi+1}/{tot}</span></header>
<main>{body}</main>
<footer><span>Sumber: video serah terima alat, 26 Nov 2026 · Versi 1 · 28 Nov 2026</span><span>UPG Dental Care · Dokumen internal</span></footer></section>''', n
CSS='''@font-face{font-family:N;src:url(nunito-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:N;src:url(nunito-latin-800-normal.woff2);font-weight:800}
@font-face{font-family:N;src:url(nunito-latin-900-normal.woff2);font-weight:900}
@page{size:A4;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:N,sans-serif;font-weight:600;color:#2A2A2A;background:#ddd}
.page{width:794px;height:1123px;background:#FFF7EF;display:flex;flex-direction:column;page-break-after:always;overflow:hidden;margin:0 auto}
header{display:flex;align-items:center;gap:16px;padding:18px 24px 14px;border-bottom:4px solid #FA7209;background:#fff}
.logo{height:44px}.ht{flex:1}.kode{font-size:11px;letter-spacing:.08em;color:#CF6515;font-weight:800}
h1{font-size:23px;font-weight:900;line-height:1.15}.hal{font-size:12px;font-weight:800;color:#CF6515}
main{flex:1;padding:12px 24px 6px;display:flex;flex-direction:column;justify-content:space-evenly}
.band{display:flex;flex-direction:column;gap:5px}
.hrow,.crow{display:grid;grid-template-columns:repeat(5,1fr);column-gap:10px}
.sec{font-weight:900;font-size:12.5px;color:#fff;background:#2A2A2A;border-radius:4px;padding:3px 8px}
.card{background:#fff;border-radius:8px;overflow:hidden;border:1px solid #f0dcc8;display:flex;flex-direction:column}
.ph{position:relative;aspect-ratio:540/670}.ph img{width:100%;height:100%;object-fit:cover;display:block}
.no{position:absolute;left:6px;top:6px;background:#FA7209;color:#2A2A2A;font-weight:900;font-size:17px;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;border:2px solid #fff}
.tx{padding:6px 7px 8px}.tx b{display:block;font-weight:900;font-size:11.5px;line-height:1.2;margin-bottom:3px}
.tx p{font-size:10px;line-height:1.3}
.box{border-radius:8px;padding:12px 14px;align-self:start}.box h4{font-weight:900;font-size:14px;margin-bottom:6px}
.box ul{padding-left:16px}.box li{font-size:11.5px;line-height:1.4;margin-bottom:3px}
.warn{background:#FFE9D6;border:2px solid #CF6515}.warn h4{color:#CF6515}
.tip{background:#fff;border:2px dashed #FA7209}
footer{display:flex;justify-content:space-between;font-size:9.5px;color:#7a6a5c;padding:8px 24px 12px}
@media print{body{background:none}}'''
for d,fn in ((IO,"WI-IO"),(SC,"WI-Scaler")):
    pages=[]; n=1
    for i,hal in enumerate(d["halaman"]):
        p,n=page(d,hal,i,i==len(d["halaman"])-1,n); pages.append(p)
    open(fn+".html","w").write(f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>{fn}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
print("ok")
