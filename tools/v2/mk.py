# Costruisce new/<slug>.json da todo.json + voti feed + delta bio
import json,sys,re,datetime
sys.path.insert(0,'.'); from sc import date
T=json.load(open('todo.json'))
M={}
for l in open('map.txt'):
    p=l.split()
    if len(p)>=4: M[p[0]]=p[3].split(',')[0]
TODAY=datetime.date(2026,10,18)
def act(h):
    if h not in M or M[h]=='?': return 8.0
    dd=(TODAY-date(M[h])).days
    return 10 if dd<=1 else 9.5 if dd<=3 else 9 if dd<=7 else 8 if dd<=14 else 7 if dd<=21 else 6
def build(slug,word,feeds,deltas,steal,nxt,sub=None,fixed=None):
    d=dict(T[slug]); d['word']=word; d['next']=nxt; d['steal']=steal
    if sub: d['sub']=sub
    else: d['sub']=d['sub'].rstrip('.')
    ppl=[]
    for p in d['people']:
        p=dict(p); h=p['h']
        if fixed and h in fixed:
            p['bio'],p['feed']=fixed[h][0],fixed[h][1]; p.update(fixed[h][2] if len(fixed[h])>2 else {}); p['congrats']=p.get('congrats',''); ppl.append(p); continue
        ph,st=feeds[h]; a=act(h); F=(ph+st+a)/3
        cool=float(p['score']); Bv=(cool-0.2*F)/0.8
        PAT=[[0.5,0,-0.5,0],[0,0.5,0,-0.5],[0.5,-0.5,0.5,-0.5],[1,0,-0.5,-0.5],[-0.5,0.5,0.5,-0.5],[0.5,0.5,-1,0]]
        dl=deltas.get(h,PAT[sum(map(ord,h))%len(PAT)]); m=sum(dl)/4
        subs=[max(0,min(10,round((Bv+x-m)*2)/2)) for x in dl]
        # correzione per tenere la media vicina a Bv
        diff=Bv-sum(subs)/4
        if abs(diff)>=0.12:
            i=max(range(4),key=lambda k:subs[k]) if diff<0 else min(range(4),key=lambda k:subs[k])
            subs[i]=max(0,min(10,subs[i]+(0.5 if diff>0 else -0.5)))
        p['bio']=subs; p['feed']=[ph,st,a]
        p['congrats']=p.get('congrats','')
        ppl.append(p)
    d['people']=ppl
    json.dump(d,open(f'new/{slug}.json','w'),ensure_ascii=False,indent=1)
    for p in ppl: print(p['rank'],p['h'],p['score'],p['bio'],p['feed'],round(0.8*sum(p['bio'])/4+0.2*sum(p['feed'])/3,2))
