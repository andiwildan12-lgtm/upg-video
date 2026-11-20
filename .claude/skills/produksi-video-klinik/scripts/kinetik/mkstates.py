import json
P=json.load(open('plan.json'));F=30;N=round(P['end']*F)
POPS=[0.55,0.85,1.1,1.04,1.0];POPC=[0.86,0.96,1.05,1.0]
def pop(e,arr): return arr[min(e,len(arr)-1)]
frames=[]
for f in range(N):
  t=(f+0.5)/F;d={}
  if t>=P['card']:
    d['card']=True;d['cardA']=round(min(1,(t-P['card']+0.05)/0.3),2)
  else:
    c=[x for x in P['caps'] if x['t0']<=t<x['t1']]
    if c:
      c=c[0];d['cap']=c['txt'];d['capS']=pop(int((t-c['t0'])*F),POPC)
      if t>=32.9: d['capTop']=760
    st=[]
    for (t0,i,x,y,r,u) in P['ev']:
      if t0<=t<u: st.append(dict(i=i,x=x,y=y,r=r,s=pop(int((t-t0)*F),POPS)))
    if st: d['st']=st
    for (a,b,n,ti,su) in P['ch']:
      if a<=t<b: d['chip']=[n,ti,su];d['chipS']=pop(int((t-a)*F),POPS)
    if P['btn'][0]<=t<P['btn'][1]: d['btn']='Chat admin';d['btnS']=pop(int((t-P['btn'][0])*F),POPS)
  frames.append(json.dumps(d,sort_keys=True))
uniq=sorted(set(frames));idx={u:i for i,u in enumerate(uniq)}
json.dump([json.loads(u) for u in uniq],open('uniq.json','w'),ensure_ascii=False)
json.dump([idx[x] for x in frames],open('fmap.json','w'))
print(N,len(uniq))
