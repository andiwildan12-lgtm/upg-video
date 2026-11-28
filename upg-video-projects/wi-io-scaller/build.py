import sys, html; sys.path.insert(0, '.')
from data import IO, SC

PER = 6  # 3 kolom x 2 baris per halaman
TIPS = {"WI-IO": ("Gambar tidak muncul di monitor?", ["Cek lagi: laptop & monitor satu WiFi.", "Monitor sudah di SOURCE → HDMI.", "Stop casting, lalu ulangi Cast dari Chrome."])}

def card(n, d, sec, t, j, isi):
    return f'''<div class="card"><div class="ph"><img src="foto/{d['kode']}_{t.replace(':','-')}.jpg"><span class="no">{n}</span></div>
<div class="tx"><span class="chip">{html.escape(sec.split(" (")[0])}</span><b>{html.escape(j)}</b><p>{html.escape(isi)}</p></div></div>'''

def box(cls, title, items):
    li = "".join(f"<li>{html.escape(x)}</li>" for x in items)
    return f'<div class="box {cls}"><h4>{title}</h4><ul>{li}</ul></div>'

def build(d):
    steps = [(sec, *s) for hal in d["halaman"] for sec, ss in hal for s in ss]
    chunks = [steps[i:i + PER] for i in range(0, len(steps), PER)]
    boxes = []
    if d["kode"] in TIPS:
        boxes.append(box("tip", *TIPS[d["kode"]]))
    boxes.append(box("warn", "⚠ Jangan", d["jangan"]))
    pages = []; n = 1
    for pi, ch in enumerate(chunks):
        cells = []
        for s in ch:
            cells.append(card(n, d, *s)); n += 1
        last = pi == len(chunks) - 1
        strip = ""
        if last:
            if len(ch) <= 3:  # baris ke-2 kosong: kotak mengisi baris itu
                cells.append(f'<div class="boxrow">{"".join(boxes)}</div>')
            else:
                strip = f'<div class="strip">{"".join(boxes)}</div>'
        pages.append((cells, strip))
    tot = len(pages); out = []
    for pi, (cells, strip) in enumerate(pages):
        out.append(f'''<section class="page">
<header><img class="logo" src="logo-upg-mendatar.png"><div class="ht"><span class="kode">WORK INSTRUCTION · {d['kode']}</span><h1>{d['judul']}</h1></div><span class="hal">Hal. {pi+1}/{tot}</span></header>
<main><div class="grid">{"".join(cells)}</div>{strip}</main>
<footer><span>Sumber: video serah terima alat, 26 Nov 2026 · Versi 2 · 28 Nov 2026</span><span>UPG Dental Care · Dokumen internal</span></footer></section>''')
    return "".join(out)

CSS = '''@font-face{font-family:N;src:url(nunito-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:N;src:url(nunito-latin-800-normal.woff2);font-weight:800}
@font-face{font-family:N;src:url(nunito-latin-900-normal.woff2);font-weight:900}
@page{size:A4;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:N,sans-serif;font-weight:600;color:#2A2A2A;background:#ddd}
.page{width:794px;height:1123px;background:#FFF7EF;display:flex;flex-direction:column;page-break-after:always;overflow:hidden;margin:0 auto}
header{display:flex;align-items:center;gap:14px;padding:12px 20px 10px;border-bottom:4px solid #FA7209;background:#fff}
.logo{height:40px}.ht{flex:1}.kode{font-size:11px;letter-spacing:.08em;color:#CF6515;font-weight:800}
h1{font-size:23px;font-weight:900;line-height:1.15}.hal{font-size:13px;font-weight:800;color:#CF6515}
main{flex:1;min-height:0;padding:12px 16px 4px;display:flex;flex-direction:column;gap:10px}
.grid{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,minmax(0,1fr));gap:10px}
.card{background:#fff;border-radius:10px;overflow:hidden;border:1px solid #f0dcc8;display:flex;flex-direction:column;min-height:0}
.ph{position:relative;flex:1;min-height:0}.ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.no{position:absolute;left:8px;top:8px;background:#FA7209;color:#2A2A2A;font-weight:900;font-size:24px;width:46px;height:46px;border-radius:50%;display:grid;place-items:center;border:3px solid #fff}
.tx{padding:8px 10px 10px;flex:none;height:132px;overflow:hidden}
.chip{display:inline-block;font-size:10.5px;font-weight:800;color:#CF6515;margin-bottom:2px}
.tx b{display:block;font-weight:900;font-size:17px;line-height:1.2;margin-bottom:4px}
.tx p{font-size:14px;line-height:1.35}
.boxrow{grid-column:1/-1;display:flex;gap:10px;align-items:stretch}
.strip{display:flex;gap:10px;flex:none}
.box{flex:1;border-radius:10px;padding:12px 16px}.box h4{font-weight:900;font-size:17px;margin-bottom:6px}
.box ul{padding-left:18px}.box li{font-size:14px;line-height:1.4;margin-bottom:3px}
.boxrow .box{display:flex;flex-direction:column;justify-content:center;padding:28px 36px}.boxrow .box h4{font-size:34px;margin-bottom:18px}.boxrow .box ul{padding-left:30px}.boxrow .box li{font-size:27px;line-height:1.35;margin-bottom:22px}
.warn{background:#FFE9D6;border:2px solid #CF6515}.warn h4{color:#CF6515}
.tip{background:#fff;border:2px dashed #FA7209}
footer{display:flex;justify-content:space-between;font-size:9.5px;color:#7a6a5c;padding:6px 20px 10px}
@media print{body{background:none}}'''

for d, fn in ((IO, "WI-IO"), (SC, "WI-Scaler")):
    open(fn + ".html", "w").write(f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>{fn}</title><style>{CSS}</style></head><body>{build(d)}</body></html>')
print("ok")
