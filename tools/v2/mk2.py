# Nuove liste (dal 1/11): profili 150-1500 follower. Dati espliciti + voti feed; bio ricavata con 80/20
import json,datetime,sys
sys.path.insert(0,'.'); from sc import date
M={}
for l in open('map2.txt'):
    p=l.split()
    if len(p)>=4: M[p[0]]=p[3]
TODAY=datetime.date(2026,11,1)
PAT=[[0.5,0,-0.5,0],[0,0.5,0,-0.5],[0.5,-0.5,0.5,-0.5],[1,0,-0.5,-0.5],[-0.5,0.5,0.5,-0.5],[0.5,0.5,-1,0]]
def act(h):
    dd=(TODAY-date(M[h])).days
    return 10 if dd<=1 else 9.5 if dd<=3 else 9 if dd<=7 else 8 if dd<=14 else 7 if dd<=21 else 6
def build(d,people):
    ppl=[]
    for r,(h,score,cat,v,ph,st) in zip([1,2,3,4,5],people):
        a=act(h); F=(ph+st+a)/3; Bv=(float(score)-0.2*F)/0.8
        dl=PAT[sum(map(ord,h))%len(PAT)]; m=sum(dl)/4
        subs=[max(0,min(10,round((Bv+x-m)*2)/2)) for x in dl]
        diff=Bv-sum(subs)/4
        if abs(diff)>=0.12:
            i=max(range(4),key=lambda k:subs[k]) if diff<0 else min(range(4),key=lambda k:subs[k])
            subs[i]=max(0,min(10,subs[i]+(0.5 if diff>0 else -0.5)))
        p=dict(rank=r,h=h,score=score,cat=cat,v=v,bio=subs,feed=[ph,st,a],congrats='')
        ppl.append(p); print(r,h,score,subs,[ph,st,a],round(0.8*sum(subs)/4+0.2*(ph+st+a)/3,2))
    d['people']=ppl
    json.dump(d,open(f"new/{d['slug']}.json",'w'),ensure_ascii=False,indent=1)
