import json
# global timeline (seconds). narration starts at 0.3
C1='&#10003;'
ck=lambda s:f'<b>{C1}</b> {s}'
segs=[
 ('hook','hook',0.00,5.61,{}),
 ('s2','foot',5.61,9.93,{'dir':'s2','p':'Pengin rapi dari dulu','tin':0.3,'p2':'Tapi kepikiran biaya','l2':'Banyak yang ragu','tin2':2.2}),
 ('sela','sela',9.93,16.56,{}),
 ('rapi','rapi',16.56,23.09,{}),
 ('s5','foot',23.09,26.74,{'dir':'s5','p0':'Solusinya','p':'Behel di UPG Dental Care Antang','tin':0.5,'top':1000,'cls':''}),
 ('price','price',26.74,31.65,{'blur':'ftg/s5/0132.jpg'}),
 ('c1','foot',31.65,32.90,{'dir':'c1m','chipsG':[('Konsultasi',32.38)]}),
 ('c2','foot',32.90,33.90,{'dir':'c2','chipsG':[('Konsultasi',32.38),('Cetak gigi',33.4)]}),
 ('c3','foot',33.90,34.75,{'dir':'c3','chipsG':[('Konsultasi',32.38),('Cetak gigi',33.4),('Scaling',34.1)]}),
 ('c4','foot',34.75,35.60,{'dir':'c4','p':'Dicek dulu','tin':0.1}),
 ('c5','foot',35.60,37.00,{'dir':'c5','p':'Dikerjakan dokter gigi','tin':0.15}),
 ('c6','foot',37.00,38.00,{'dir':'c6','p0':'3 pilihan','p':'Metal · Keramik · Self‑ligating','cls':'w','tin':0.2}),
 ('c7','foot',38.00,39.12,{'dir':'c7','p0':'3 pilihan','p':'Metal · Keramik · Self‑ligating','cls':'w','tin':-1}),
 ('s7','foot',39.12,42.73,{'dir':'s7','p0':'Tujuannya','p':'Rapi & gampang dirawat','tin':0.5}),
 ('s8a','foot',42.73,45.53,{'dir':'s8a','p0':'Lokasi','p':'Lt. 2 Apotek Wahdah Antang','tin':0.2}),
 ('s8b','foot',45.53,48.76,{'dir':'s8b','p0':'Buka setiap hari','p':'10.00 – 22.00','tin':0.2}),
 ('s8c','foot',48.76,50.60,{'dir':'s8c','p0':'0895-1013-2102','p':'Chat admin, konsultasi dulu','tin':0.15}),
 ('end','end',50.60,53.60,{}),
]
jobs=[]
import os
for name,scene,a,b,o in segs:
  D=b-a; n=int(round(D*30))+4  # 4 frames padding for crossfade
  opt=dict(o); d=opt.pop('dir',None)
  if 'chipsG' in opt:
    opt['chips']=[[ck(s),tg-a] for s,tg in opt.pop('chipsG')]
  mx=len(os.listdir('ftg/'+d)) if d else None
  jobs.append({'seg':name,'name':scene,'a':a,'b':b,'D':D,'n':n,'dir':d,'max':mx,'opt':opt})
json.dump(jobs,open('jobs.json','w'),indent=1)
print(sum(j['n'] for j in jobs),'frames')
