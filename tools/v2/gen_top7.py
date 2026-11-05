# Classifiche Top 5, direzione "Wrapped": colori pieni saturi per slide, forme a tinta unita che attraversano le slide,
# cornice blu attorno, card con bordo e ombra piena, Anton per numeri e titoli, grafico a ragnatela + barre.
# Uso: python3 gen_top7.py new/<slug>.json [all]   output in out7/
import json,sys,os,asyncio,math,random
B=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,B+'/../packs')
import gen_top6 as T
from gen6_base import E,LOGO
OUT=B+'/out7/'; W,H=1080,1350; F=24; M=74
NAVY='#0B1631'; CREAM='#F6F1E6'
PAL={'orange':'#FF5A1F','pink':'#FF3D9A','violet':'#6A2CFF','lime':'#C8FF3D','sky':'#38B6FF','navy':NAVY,'cream':CREAM}
DARK={'violet','navy'}
FONTS='<link href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Inter:wght@400;500;600;700;800&amp;family=Hanken+Grotesk:ital,wght@1,500&amp;display=swap" rel="stylesheet">'
LAB=['Personality','Clarity','Call to action','Details','Photos','Style','Activity']
CTX={}
def fgc(name): return CREAM if name in DARK else NAVY
def A(t,size,col,extra=''): return f'<span style="font-family:Anton;font-size:{size}px;line-height:.88;color:{col};{extra}">{t}</span>'
def shapes():
    seq,i,n=CTX['seq'],CTX['i'],CTX['n']; rnd=random.Random(CTX['slug']); out=''
    for k in range(1,n):                                   # forme sui confini tra slide k e k+1
        x=k*W; y=rnd.choice([rnd.randint(120,380),rnd.randint(980,1260)]); r=rnd.randint(170,260)
        c=PAL[[s for s in ('lime','pink','orange','sky','violet','cream') if s not in (seq[k-1],seq[k])][k%3]]
        kind=k%3
        if kind==0: out+=f'<div style="position:absolute;left:{x-r}px;top:{y-r}px;width:{2*r}px;height:{2*r}px;border-radius:50%;background:{c}"></div>'
        elif kind==1: out+=f'<div style="position:absolute;left:{x-r}px;top:{y-r}px;width:{2*r}px;height:{2*r}px;border-radius:50%;border:34px solid {c}"></div>'
        else: out+=f'<div style="position:absolute;left:{x-340}px;top:{y-60}px;width:680px;height:120px;border-radius:60px;background:{c};transform:rotate(-12deg)"></div>'
    base=''.join(f'<div style="position:absolute;left:{k*W}px;top:0;width:{W}px;height:{H}px;background:{PAL[s]}"></div>' for k,s in enumerate(seq))
    return f'<div style="position:absolute;top:0;left:{-(i-1)*W}px;width:{n*W}px;height:{H}px;z-index:0">{base}{out}</div>'
GR='<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:1;mix-blend-mode:multiply;opacity:.16;pointer-events:none"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>'
def page(body):
    return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>body{{margin:0}}*{{box-sizing:border-box}}.z{{position:absolute;z-index:2}}.sub{{font-family:'Hanken Grotesk';font-style:italic}}</style></head><body>
<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Inter,'Noto Color Emoji',sans-serif">{shapes()}{GR}{body}
<div style="position:absolute;inset:0;border:{F}px solid {NAVY};z-index:5;pointer-events:none"></div></div></body></html>'''
def hdr(fg,right):
    return f'''<div class="z" style="left:{M}px;right:{M}px;top:56px;display:flex;justify-content:space-between;align-items:center;color:{fg}">
<div style="display:flex;align-items:center;gap:12px"><img src="{LOGO}" style="width:44px;height:44px;border-radius:50%;background:{NAVY}"><span style="font-weight:800;font-size:26px;letter-spacing:-1px">coolbio·360</span></div>
<span style="font-family:Anton;font-size:30px">{right}</span></div>'''
BR=lambda c=NAVY,o=10: f'border:4px solid {NAVY};box-shadow:{o}px {o}px 0 {c}'
def radar(vals,col,ink,size):
    cx,cy,R=200,175,128
    def pt(i,s): a=-math.pi/2+i*2*math.pi/7; return f"{cx+R*s/10*math.cos(a):.1f},{cy+R*s/10*math.sin(a):.1f}"
    rings=''.join(f'<polygon points="{" ".join(pt(i,s) for i in range(7))}" fill="none" stroke="{ink}" stroke-opacity=".25" stroke-width="1.5"/>' for s in (10,7.5,5,2.5))
    poly=f'<polygon points="{" ".join(pt(i,v) for i,v in enumerate(vals))}" fill="{col}" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>'
    labs=''
    for i,l in enumerate(LAB):
        a=-math.pi/2+i*2*math.pi/7; x=cx+(R+20)*math.cos(a); y=cy+(R+20)*math.sin(a)+6
        an='middle' if abs(math.cos(a))<.3 else ('start' if math.cos(a)>0 else 'end')
        labs+=f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{an}" font-size="17" font-family="Inter" font-weight="700" fill="{ink}">{l}</text>'
    return f'<svg viewBox="-70 0 540 350" style="width:{size}px;height:{size*350/540:.0f}px;flex:none">{rings}{poly}{labs}</svg>'
def bars(vals,col,ink):
    out=''
    for name,vs,ls in (('The bio',vals[:4],LAB[:4]),('The feed',vals[4:],LAB[4:])):
        out+=f'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin:{0 if name=="The bio" else 14}px 0 6px;color:{ink}"><span style="font-size:19px;font-weight:800">{name}</span>{A(f"{sum(vs)/len(vs):.1f}",40,col)}</div>'
        out+=''.join(f'<div style="display:grid;grid-template-columns:140px 1fr 40px;gap:12px;align-items:center;margin:6px 0;font-size:18px;font-weight:600;color:{ink}"><span>{l}</span><div style="height:12px;border-radius:6px;background:{ink}22"><div style="width:{x*10}%;height:12px;border-radius:6px;background:{col}"></div></div><span style="font-weight:800;text-align:right">{x:g}</span></div>' for l,x in zip(ls,vs))
    return f'<div style="flex:1">{out}</div>'
def cover(d):
    s=CTX['seq'][0]; fg=fgc(s); P={p['rank']:p for p in d['people']}
    def pod(r,x,y,sz,rot):
        return f'''<div class="z" style="left:{x}px;top:{y}px;width:{sz}px;transform:rotate({rot}deg)">
<div style="width:{sz}px;height:{sz}px;border-radius:50%;background:url({T.avatar(P[r]['h'])}) center/cover;{BR()}"></div>
<div style="position:absolute;left:-14px;top:-18px;background:{PAL['lime'] if r==1 else CREAM};{BR(o=6)};border-radius:16px;padding:6px 18px 2px">{A(r,int(sz*.3),NAVY)}</div>
<div style="margin:22px auto 0;width:max-content;background:{NAVY};border-radius:14px;padding:8px 18px">{A(P[r]['score'],int(sz*.2),PAL['lime'] if r==1 else CREAM)}</div></div>'''
    b=f'''{hdr(fg,'VOL. '+d['vol'])}
<div class="z" style="left:{M}px;right:{M}px;top:150px;color:{fg}">{A('THE 5 BEST',168,fg)}<br>{A(E(d['word']).upper()+' BIOS',168,NAVY if fg==NAVY else PAL['lime'],f'-webkit-text-stroke:0;')}
<div class="sub" style="font-size:34px;margin-top:22px">{E(d['sub'])}</div></div>
{pod(2,M+6,800,290,-6)}{pod(3,W-M-296,840,290,6)}{pod(1,(W-360)//2,730,360,0)}'''
    return page(b)
def profile(d,p,i,n):
    s=CTX['seq'][i-1]; fg=fgc(s); win=p['rank']==1; vals=p['bio']+p['feed']
    hi=PAL['lime'] if s!='lime' else NAVY
    sc_bg=NAVY; sc_fg=PAL['lime'] if s!='lime' else CREAM
    phs=''.join(f'<div style="flex:1;height:170px;border-radius:18px;background:url({T.b64(T.CAP+p["h"]+f"_{k}.jpg")}) center/cover;{BR(o=7)}"></div>' for k in (1,2,3))
    panel_bg=CREAM if s in DARK else '#FFFFFF'
    b=f'''{hdr(fg,f'{i}/{n}')}
<div class="z" style="left:{M-4}px;top:118px">{A(p['rank'],270,NAVY if fg==NAVY else hi)}</div>
<div class="z" style="left:300px;right:{M}px;top:150px;color:{fg}">
<div class="sub" style="font-size:30px">{'The winner 🏆' if win else 'No.'+str(p['rank'])+' of 5'}</div>
<div style="font-family:Anton;font-size:64px;line-height:1.02;margin-top:6px;word-break:break-all">@{E(p['h'])}</div>
<div style="font-size:24px;font-weight:600;margin-top:8px">{E(p['cat'])}</div></div>
<div class="z" style="left:{M}px;right:{M}px;top:410px;background:#fff;border-radius:26px;padding:14px;{BR()}">
<img src="{T.b64(T.CAP+p['h']+'_head.png')}" style="width:100%;max-height:240px;object-fit:cover;object-position:top;display:block;border-radius:12px">
<div style="position:absolute;right:-10px;top:-58px;background:{sc_bg};border-radius:20px;padding:10px 24px 6px;transform:rotate(4deg);{BR(hi,6)}"><div style="font-size:16px;font-weight:800;color:{CREAM}">Cool Score</div>{A(p['score'],86,sc_fg)}</div></div>
<div class="z" style="left:{M}px;right:{M}px;top:700px;display:flex;gap:18px">{phs}</div>
<div class="z" style="left:{M}px;right:{M}px;top:905px;background:{panel_bg};border-radius:26px;padding:14px 24px 14px 0;display:flex;align-items:center;gap:10px;{BR()}">{radar(vals,PAL['violet'] if s!='violet' else PAL['pink'],NAVY,370)}{bars(vals,PAL['violet'] if s!='violet' else PAL['pink'],NAVY)}</div>
<div class="z sub" style="left:{M}px;right:{M}px;bottom:44px;font-size:26px;line-height:1.25;color:{fg}">{E(p['v'])}</div>'''
    return page(b)
SEQ=['orange','violet','lime','pink','sky','navy','cream']
async def main(path,mode):
    d=json.load(open(path)); os.makedirs(OUT,exist_ok=True); P={p['rank']:p for p in d['people']}
    want=range(1,7) if mode=='all' else (1,2,6)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':W,'height':H})
        for i in want:
            CTX.update(seq=SEQ,i=i,n=7,slug=d['slug'])
            h=cover(d) if i==1 else profile(d,P[7-i],i,7)
            f=OUT+f"{d['slug']}_{i:02d}.html"; open(f,'w').write(h)
            await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(700)
            await pg.screenshot(path=OUT+f"coolbio360_{d['slug']}_{i:02d}.jpg",type='jpeg',quality=92)
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1],(sys.argv[2:] or [''])[0]))
