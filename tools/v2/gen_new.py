# Generatore liste coolbio360, nuova grafica (podio, profilo intero con 7 voti, Steal this bio)
import json,math,os,sys,asyncio,html
B=os.path.dirname(os.path.abspath(__file__))
CAP=B+'/cap/'; OUT=B+'/out/'; os.makedirs(OUT,exist_ok=True)
LOGO='/home/claude/coolbio360-media/tools/assets/logo-coolbio360-gradiente.svg'
FONTS='<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&amp;family=Hanken+Grotesk:ital,wght@0,400;0,500;0,700;1,400;1,500&amp;display=swap" rel="stylesheet">'
BG="width: 1080px; height: 1350px; box-sizing: border-box; border: 26px solid {A}; background: linear-gradient(160deg, #1B1C1F 0%, #111726 55%, #0B1631 100%); color: #F3EEE4; font-family: 'Hanken Grotesk', sans-serif;"
def page(body,title):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>{FONTS}<style>body{{margin:0}}</style></head><body>{body}</body></html>'
def fu(p): return 'file://'+p
def r1(x): return f'{x:.1f}' if x<10 else '10'
def under(word,A):
    return f'<span style="position: relative; display: inline-block">{word}<svg aria-hidden="true" viewBox="0 0 300 40" preserveAspectRatio="none" style="position: absolute; left: -2%; bottom: -0.14em; width: 104%; height: 0.3em; overflow: visible"><path d="M6 24 C 50 14, 110 20, 160 17 S 250 12, 294 19" fill="none" stroke="{A}" stroke-width="16" stroke-linecap="round"></path><path d="M22 30 C 90 22, 170 27, 284 23" fill="none" stroke="{A}" stroke-width="8" stroke-linecap="round" opacity="0.9"></path></svg></span>'
def topbar(d,right):
    return f'<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(243,238,228,0.25); padding-bottom: 14px"><div style="display: flex; align-items: center; gap: 12px"><img src="{fu(LOGO)}" alt="" style="width: 40px; height: 40px"><span style="font-family: \'Inter\', sans-serif; font-weight: 800; font-size: 26px; letter-spacing: -1px">coolbio·360</span></div><span style="font-size: 17px; font-weight: 700; letter-spacing: 4px; color: #9A958B">{right}</span></div>'
def phone(p,w,h,rank,score,A,first):
    pad=12 if first else 10; rad=56 if first else 48
    tiles=''.join(f'<img src="{fu(CAP+p["h"]+f"_{k}.jpg")}" alt="" style="width: 100%; aspect-ratio: 3 / 4; object-fit: cover; display: block">' for k in (1,2,3))
    tiles+=''.join('<div style="width: 100%; aspect-ratio: 3 / 4; background: #EEEBE6"></div>' for k in range(6))
    av=68 if first else 58
    lab_bg=A if first else '#F3EEE4'; sc_col=A if first else '#F3EEE4'
    return f'''<div style="text-align: center; margin-bottom: 14px; display: flex; justify-content: center; gap: 10px; align-items: center"><span style="background: {lab_bg}; color: #0B1631; font-weight: 700; font-size: {24 if first else 22}px; letter-spacing: 3px; padding: 5px 12px">No.{rank}</span><span style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: {30 if first else 26}px; color: {sc_col}">{score}</span></div>
<div style="width: {w}px; height: {h}px; box-sizing: border-box; border-radius: {rad}px; background: #0d0d0f; padding: {pad}px; box-shadow: 0 0 0 3px #c9c6bf, 0 36px 70px rgba(0,0,0,0.55)"><div style="width: 100%; height: 100%; border-radius: {rad-10}px; overflow: hidden; background: #FFFFFF; display: flex; flex-direction: column">
<div style="height: 44px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-family: 'Inter', sans-serif; font-weight: 800; font-size: 16px; letter-spacing: 4px; color: #9A958B">• • •</div>
<div style="display: flex; align-items: center; gap: 12px; padding: 4px 14px 0"><div style="width: {av}px; height: {av}px; border-radius: 50%; background: #E9E6E0; display: flex; align-items: center; justify-content: center; font-family: 'Inter', sans-serif; font-weight: 800; font-size: 28px; color: #9A958B; flex-shrink: 0">?</div><div style="flex-grow: 1; display: flex; flex-direction: column; gap: 7px"><div style="height: 9px; width: 80%; background: #E9E6E0; border-radius: 5px"></div><div style="height: 9px; width: 55%; background: #E9E6E0; border-radius: 5px"></div></div></div>
<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 14px 12px"><div style="height: 8px; width: 90%; background: #F0EDE8; border-radius: 4px"></div><div style="height: 8px; width: 70%; background: #F0EDE8; border-radius: 4px"></div><div style="height: 8px; width: 50%; background: #F0EDE8; border-radius: 4px"></div></div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px">{tiles}</div></div></div>'''
def cover(d):
    A=d['accent']; P={p['rank']:p for p in d['people']}
    body=f'''<div style="{BG.format(A=A)} position: relative; overflow: hidden">
<div style="position: absolute; left: 46px; right: 46px; top: 44px; display: flex; justify-content: space-between; font-size: 20px; font-weight: 700; letter-spacing: 4px; color: #9A958B"><span>THE BIO ISSUE</span><span>VOL. {d['vol']} · {d['tag']}</span></div>
<div style="position: absolute; left: 46px; right: 46px; top: 100px; text-align: center"><div style="display: inline-block; background: {A}; color: #0B1631; padding: 8px 18px; font-size: 22px; font-weight: 700; letter-spacing: 6px">THE PODIUM</div>
<h1 style="margin: 16px 0 0; font-family: 'Inter', sans-serif; font-weight: 700; font-size: {96 if len(d['word'])<6 else 84 if len(d['word'])<7 else 76}px; line-height: 0.95; letter-spacing: -4px; white-space: nowrap">The 5 Best {under(d['word'],A)} Bios</h1>
<div style="margin-top: 14px; font-style: italic; font-size: 32px; color: #D9D3C7">Three made the podium. Who’s No.1? Swipe to find out.</div></div>
<div style="position: absolute; left: 44px; top: 500px; width: 300px; transform: rotate(-7deg); transform-origin: 50% 100%">{phone(P[2],300,600,2,P[2]['score'],A,False)}</div>
<div style="position: absolute; right: 44px; top: 500px; width: 300px; transform: rotate(7deg); transform-origin: 50% 100%">{phone(P[3],300,600,3,P[3]['score'],A,False)}</div>
<div style="position: absolute; left: 334px; top: 446px; width: 360px">{phone(P[1],360,700,1,P[1]['score'],A,True)}</div>
<div style="position: absolute; left: 46px; right: 46px; bottom: 36px; display: flex; justify-content: space-between; align-items: center; border-top: 2px solid rgba(243,238,228,0.85); padding-top: 16px; background: transparent"><span style="font-size: 24px; font-weight: 500; color: #D9D3C7">{d['sub']}</span><span style="font-size: 22px; font-weight: 700; letter-spacing: 5px">SWIPE →</span></div></div>'''
    return page(body,f"{d['word']} Bios cover")
LAB=[('Personality',170,24,'middle'),('Clarity',284,79,'start'),('Call to action',312,202,'start'),('Details',233,302,'start'),('Photos',107,302,'end'),('Style',28,202,'end'),('Activity',56,79,'end')]
def pt(i,v):
    a=-math.pi/2+i*2*math.pi/7; r=120*v/10
    return f'{170+r*math.cos(a):.1f},{170+r*math.sin(a):.1f}'
def radar(p,A):
    vals=p['bio']+p['feed']
    rings=''.join(f'<polygon points="{" ".join(pt(i,s) for i in range(7))}" fill="none" stroke="rgba(243,238,228,{0.25 if s==10 else 0.14})" stroke-width="1"></polygon>' for s in (10,7.5,5,2.5))
    axes=''.join(f'<line x1="170" y1="170" x2="{pt(i,10).split(",")[0]}" y2="{pt(i,10).split(",")[1]}" stroke="rgba(243,238,228,0.14)"></line>' for i in range(7))
    poly=f'<polygon points="{" ".join(pt(i,v) for i,v in enumerate(vals))}" fill="{A}" fill-opacity="0.35" stroke="{A}" stroke-width="3" stroke-linejoin="round"></polygon>'
    labs=''.join(f'<text x="{x}" y="{y}" text-anchor="{an}" fill="{"#D9D3C7" if i<4 else "#F3EEE4"}" font-size="17" font-family="Hanken Grotesk, sans-serif">{n}</text>' for i,(n,x,y,an) in enumerate(LAB))
    aria=', '.join(f'{n.lower()} {r1(v)}' for (n,*_),v in zip(LAB,vals))
    return f'<svg role="img" aria-label="Score chart for @{p["h"]}: {aria}" viewBox="-80 0 500 320" style="width: 420px; height: 269px; flex-shrink: 0">{rings}{axes}{poly}{labs}</svg>'
def bar(n,v,col):
    return f'<div style="display: grid; grid-template-columns: 140px minmax(0, 1fr) 40px; gap: 12px; align-items: center; font-size: 19px"><span>{n}</span><div style="height: 6px; background: rgba(243,238,228,0.14)"><div style="width: {round(v*10)}%; height: 6px; background: {col}"></div></div><span style="font-family: \'Inter\', sans-serif; font-weight: 600; text-align: right">{r1(v)}</span></div>'
def bars(p,A):
    b=sum(p['bio'])/4; f=sum(p['feed'])/3
    h=lambda t,s,c,mt: f'<div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid rgba(243,238,228,0.25); padding-bottom: 4px{mt}"><span style="font-size: 15px; font-weight: 700; letter-spacing: 4px; color: #9A958B">{t}</span><span style="font-family: \'Inter\', sans-serif; font-weight: 700; font-size: 28px{c}">{r1(s)}</span></div>'
    out=h('THE BIO',b,f'; color: {A}','')+''.join(bar(n,v,A) for n,v in zip(['Personality','Clarity','Call to action','Details'],p['bio']))
    out+=h('THE FEED',f,'','; margin-top: 8px')+''.join(bar(n,v,'#F3EEE4') for n,v in zip(['Photos','Style','Activity'],p['feed']))
    return f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 9px">{out}</div>'
def profile(d,p):
    A=d['accent']; win=p['rank']==1; th=200 if win else 220
    tiles=''.join(f'<img src="{fu(CAP+p["h"]+f"_{k}.jpg")}" alt="" style="width: 100%; height: {th}px; object-fit: cover; display: block">' for k in (1,2,3))
    card=f'<div style="margin-top: 16px; background: #FFFFFF; border-radius: 18px; padding: 14px; box-shadow: {"0 0 0 4px "+A+", " if win else ""}0 30px 60px rgba(0,0,0,0.45)"><img src="{fu(CAP+p["h"]+"_head.png")}" alt="@{p["h"]} profile header" style="width: 100%; max-height: {280 if win else 300}px; object-fit: contain; object-position: left top; display: block"><div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px; margin-top: 8px">{tiles}</div></div>'
    chart=f'<div style="margin-top: 16px; display: flex; gap: 24px; align-items: center">{radar(p,A)}{bars(p,A)}</div>'
    quote=f'<div style="margin-top: {12 if win else 14}px; font-style: italic; font-size: 24px; line-height: 1.3; color: #E9E3D7">{p["v"]}</div>'
    sc=f'<div style="text-align: right"><div style="font-size: 15px; font-weight: 700; letter-spacing: 4px; color: #9A958B">COOL SCORE</div><div style="font-family: \'Inter\', sans-serif; font-weight: 700; font-size: 64px; line-height: 1; color: {A}">{p["score"]}</div></div>'
    if win:
        head=f'''<div style="display: flex; align-items: flex-end; gap: 24px; margin-top: 16px"><div style="flex-grow: 1"><div style="display: inline-block; background: {A}; color: #0B1631; padding: 6px 14px; font-size: 18px; font-weight: 700; letter-spacing: 5px">No.1 · THE WINNER</div>
<div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: {68 if len(d['word'])<6 else 58 if len(d['word'])<7 else 52}px; line-height: 0.95; letter-spacing: -3px; margin-top: 10px; white-space: nowrap">The Best {under(d['word'],A)} Bio</div>
<div style="font-size: 23px; color: #D9D3C7; margin-top: 10px"><b style="color: #F3EEE4">@{p['h']}</b> · {p['cat']}</div></div>
<div style="display: flex; align-items: center; gap: 14px"><span style="font-size: 92px; line-height: 1">🏆</span>{sc}</div></div>'''
        foot=f'<div style="margin: auto -40px 0; background: {A}; color: #0B1631; padding: 18px 40px; display: flex; justify-content: space-between; align-items: center"><span style="font-family: \'Inter\', sans-serif; font-weight: 800; font-size: 30px; letter-spacing: 1px">{p["congrats"]}</span><span style="font-size: 18px; font-weight: 700; letter-spacing: 4px">ONE MORE →</span></div>'
        body=f'<div style="{BG.format(A=A)} padding: 34px 40px 0; display: flex; flex-direction: column; overflow: hidden">{topbar(d,"THE LIST · "+d["tag"]+" · WINNER")}{head}{card}{chart}{quote}{foot}</div>'
    else:
        r=p['rank']
        head=f'''<div style="display: flex; align-items: flex-end; gap: 24px; margin-top: 18px"><span style="font-family: 'Inter', sans-serif; font-weight: 300; font-size: 130px; line-height: 0.8; letter-spacing: -6px">0{r}</span>
<div style="flex-grow: 1; padding-bottom: 4px"><div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 34px; letter-spacing: -1px">@{p['h']}</div><div style="font-size: 22px; color: #D9D3C7; margin-top: 4px">{p['cat']}</div></div>{sc}</div>'''
        foot=f'<div style="margin-top: auto; display: flex; justify-content: space-between; font-size: 16px; font-weight: 700; letter-spacing: 4px; color: #9A958B"><span>RANK 0{r} OF 05</span><span style="color: #F3EEE4">NEXT: No.{r-1} →</span></div>'
        body=f'<div style="{BG.format(A=A)} padding: 34px 40px 30px; display: flex; flex-direction: column; overflow: hidden">{topbar(d,"THE LIST · "+d["tag"]+f" · {6-r} / 5")}{head}{card}{chart}{quote}{foot}</div>'
    return page(body,f"{d['word']} Bios No.{p['rank']}")
def steal(d):
    A=d['accent']; s=d['steal']
    row=lambda i,t,l: f'<div style="display: grid; grid-template-columns: 56px minmax(0, 1fr) 190px; gap: 18px; align-items: center; padding: 20px 0; border-bottom: 1px solid rgba(243,238,228,0.14)"><span style="font-family: \'Inter\', sans-serif; font-weight: 300; font-size: 48px; line-height: 1">{i}</span><div style="font-size: 32px; line-height: 1.3">{t.replace("[","<span style=\"color: "+A+"; font-weight: 700\">[").replace("]","]</span>")}</div><span style="font-size: 16px; font-weight: 700; letter-spacing: 3px; color: #9A958B; text-align: right">{l}</span></div>'
    rows=''.join(row(i+1,t,l) for i,(t,l) in enumerate(s['lines']))
    body=f'''<div style="{BG.format(A=A)} padding: 34px 46px 40px; display: flex; flex-direction: column; overflow: hidden">{topbar(d,"THE LIST · "+d["tag"])}
<div style="margin-top: 40px"><span style="display: inline-block; background: {A}; color: #0B1631; padding: 8px 18px; font-size: 22px; font-weight: 700; letter-spacing: 6px">STEAL THIS BIO</span></div>
<h2 style="margin: 18px 0 0; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 84px; line-height: 0.95; letter-spacing: -4px">{s['h']}</h2>
<div style="margin-top: 16px; font-style: italic; font-size: 30px; color: #D9D3C7">Built from what our top 5 have in common. Fill the gaps, done.</div>
<div style="margin-top: 34px; border-top: 1px solid rgba(243,238,228,0.35)">{rows}</div>
<div style="margin-top: 26px; background: #FFFFFF; color: #000000; border-radius: 16px; padding: 22px 26px; box-shadow: 0 30px 60px rgba(0,0,0,0.45)"><div style="font-size: 15px; font-weight: 700; letter-spacing: 3px; color: #8A857B">EXAMPLE</div><div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 24px; margin-top: 8px">@{s['ex_h']}</div><div style="font-size: 25px; line-height: 1.4; margin-top: 6px">{'<br>'.join(s['ex'])}</div></div>
<div style="margin-top: auto; display: flex; align-items: flex-end; justify-content: space-between"><div><div style="font-size: 16px; font-weight: 700; letter-spacing: 4px; color: #9A958B">SAVE IT · NEXT LIST</div><div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 40px; letter-spacing: -1px; margin-top: 8px">{d['next']}</div></div><div style="background: #F3EEE4; color: #0B1631; padding: 22px 34px; font-size: 24px; font-weight: 700; letter-spacing: 5px">FOLLOW @COOLBIO360</div></div></div>'''
    return page(body,f"{d['word']} Bios steal this bio")
async def render(slug):
    d=json.load(open(B+f'/new/{slug}.json'))
    pages=[cover(d)]+[profile(d,p) for p in sorted(d['people'],key=lambda p:-p['rank'])]+[steal(d)]
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,h in enumerate(pages):
            f=OUT+f'{slug}_{i+1:02d}.html'; open(f,'w').write(h)
            await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(600)
            await pg.screenshot(path=OUT+f'coolbio360_{slug}_{i+1:02d}.jpg',type='jpeg',quality=92,clip={'x':0,'y':0,'width':1080,'height':1350})
        await b.close()
    print(slug,'ok')
if __name__=='__main__':
    for s in sys.argv[1:]: asyncio.run(render(s))
