# Generatore "One Person, Four Bios" da episodes.json (stesso template di ep. 1 e 2)
import json,math,os,sys,asyncio,html
B=os.path.dirname(os.path.abspath(__file__)); IMG='/home/claude/coolbio360-media/design/bios/'
OUT=B+'/out/'; os.makedirs(OUT,exist_ok=True)
FONTS='<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&amp;family=Inter:wght@400;600;700;800&amp;display=swap" rel="stylesheet">'
def page(b,t): return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(t)}</title>{FONTS}<style>body{{margin:0}}</style></head><body>{b}</body></html>'
def img(n): return 'file://'+IMG+n+'.jpg'
def sc(p): return round(sum(v for _,v in p['crit'])/5+1e-9,1)
def fmt(v): return '10' if v>=10 else f'{v:.1f}'
def pt(i,v):
    a=math.radians(-90+72*i); r=115*v/10; return f'{170+r*math.cos(a):.1f},{165+r*math.sin(a):.1f}'
LAB=[(170,26,'middle'),(302,122,'start'),(252,282,'start'),(88,282,'end'),(38,122,'end')]
def radar(p):
    col=p['radar']; rings=''.join(f'<polygon points="{" ".join(pt(i,s) for i in range(5))}" fill="none" stroke="rgba(255,255,255,{0.25 if s==10 else 0.12})"></polygon>' for s in (10,7.5,5))
    axes=''.join(f'<line x1="170" y1="165" x2="{pt(i,10).split(",")[0]}" y2="{pt(i,10).split(",")[1]}" stroke="rgba(255,255,255,0.12)"></line>' for i in range(5))
    poly=f'<polygon points="{" ".join(pt(i,v) for i,(_,v) in enumerate(p["crit"]))}" fill="{col}" fill-opacity="{0.3 if col.upper() in ("#FFFFFF","#E7E9EA") else 0.4}" stroke="{col}" stroke-width="3" stroke-linejoin="round"></polygon>'
    labs=''.join(f'<text x="{x}" y="{y}" text-anchor="{a}" fill="#CCCCCC" font-size="18" font-family="Inter, sans-serif">{n}</text>' for (n,_),(x,y,a) in zip(p['crit'],LAB))
    aria=', '.join(f'{n.lower()} {fmt(v)}' for n,v in p['crit'])
    return f'<svg role="img" aria-label="Score chart: {aria}" viewBox="-70 0 480 300" style="width: 380px; height: 238px; flex-shrink: 0">{rings}{axes}{poly}{labs}</svg>'
def bars(p):
    return '<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 12px">'+''.join(f'<div style="display: grid; grid-template-columns: 150px minmax(0, 1fr) 40px; gap: 12px; align-items: center; font-size: 20px"><span>{n}</span><div style="height: 6px; background: rgba(255,255,255,0.12)"><div style="width: {round(v*10)}%; height: 6px; background: {p["radar"]}"></div></div><span style="font-weight: 700; text-align: right">{fmt(v)}</span></div>' for n,v in p['crit'])+'</div>'
def chip(p,fs,pad,rad,extra=''):
    bd=';box-shadow: inset 0 0 0 2px rgba(255,255,255,0.6)' if p['bg'] in ('#000000','#111111') else ''
    return f'<span style="background: {p["bg"]}; color: {p["fg"]}; font-weight: 800; font-size: {fs}px; padding: {pad}; border-radius: {rad}px{bd}">{p["name"]}{extra}</span>'
def platform(e,i):
    p=e['plat'][i]; s=sc(p)
    card=f'<div style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-weight: 700; font-size: 30px">{p["who"]}</span><span style="font-size: 20px; color: #777777">{p.get("meta","")}</span></div>'
    if p.get('label'): card+=f'<div style="font-size: 19px; color: #777777; margin-top: 12px">{p["label"]}</div>'
    card+=f'<div style="font-size: {p.get("fs",27)}px; line-height: 1.38; margin-top: 8px; color: #222222">{p["bio"]}</div>'
    if p.get('foot'): card+=f'<div style="font-size: 19px; color: #777777; margin-top: 10px">{p["foot"]}</div>'
    b=f'''<div style="width: 1080px; height: 1350px; background: #111111; color: #F5F5F5; position: relative; overflow: hidden; font-family: 'Inter', sans-serif">
<img src="{img(p['img'])}" alt="" style="position: absolute; left: 0; top: 0; width: 1080px; height: 720px; object-fit: cover; object-position: center {p.get('pos',25)}%; display: block">
<div style="position: absolute; left: 40px; top: 40px">{chip(p,40,'10px 22px',12)}</div>
<span style="position: absolute; right: 40px; top: 48px; color: #FFFFFF; font-weight: 800; font-size: 22px; letter-spacing: 3px; background: rgba(17,17,17,0.6); padding: 8px 14px; border-radius: 8px">{i+1} / 4</span>
<div style="position: absolute; left: 50px; right: 50px; top: 540px; background: #FFFFFF; color: #111111; border-radius: 20px; padding: 26px 32px; box-shadow: 0 24px 60px rgba(0,0,0,0.5)">{card}</div>
<div style="position: absolute; left: 50px; right: 50px; top: 905px; display: flex; gap: 20px; align-items: center">{radar(p)}{bars(p)}</div>
<div style="position: absolute; left: 50px; right: 50px; bottom: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 30px; border-top: 1px solid rgba(255,255,255,0.25); padding-top: 18px"><div style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 600; font-size: 30px; line-height: 1.2">{p['joke']}</div><div style="text-align: right; flex-shrink: 0"><div style="font-size: 15px; font-weight: 800; letter-spacing: 4px; color: #999999">SCORE</div><div style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 80px; line-height: 1; color: {p['radar']}">{fmt(s)}</div></div></div></div>'''
    return page(b,f"{e['name']} {p['name']}")
def winner(e): return max(range(4),key=lambda i:sc(e['plat'][i]))
def cover(e):
    w=winner(e); tiles=''
    for i,p in enumerate(e['plat']):
        v='top' if i<2 else 'bottom'
        badge=(f'<span style="position: absolute; right: 22px; {v}: 22px; background: #FFFFFF; color: #111111; font-weight: 800; font-size: 34px; padding: 6px 16px; border-radius: 10px">{fmt(sc(p))} 🏆</span>' if i==w else f'<span style="position: absolute; right: 22px; {v}: 22px; background: rgba(14,14,14,0.78); color: #FFFFFF; font-weight: 800; font-size: 34px; padding: 6px 16px; border-radius: 10px">{fmt(sc(p))}</span>')
        tiles+=f'<div style="position: relative; overflow: hidden"><img src="{img(p["img"])}" alt="" style="width: 100%; height: 100%; object-fit: cover; object-position: center {p.get("pos",25)}%; display: block"><div style="position: absolute; left: 22px; {v}: 22px">{chip(p,28,"8px 16px",10)}</div>{badge}</div>'
    b=f'''<div style="width: 1080px; height: 1350px; background: #0E0E0E; position: relative; overflow: hidden; font-family: 'Inter', sans-serif">
<div style="position: absolute; inset: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-rows: repeat(2, minmax(0, 1fr)); gap: 4px">{tiles}</div>
<div style="position: absolute; left: 120px; right: 120px; top: 470px; background: #FFFFFF; color: #111111; padding: 34px 40px 30px; transform: rotate({e.get('rot',2)}deg); box-shadow: 0 30px 70px rgba(0,0,0,0.5); text-align: center">
<div style="font-weight: 800; font-size: 20px; letter-spacing: 6px; color: #666666">ONE PERSON, FOUR BIOS</div>
<div style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {e.get('tfs',70)}px; line-height: 0.95; letter-spacing: -2px; margin-top: 14px">{e['title']}</div>
<div style="font-size: 26px; margin-top: 18px; color: #333333">Swipe to see how we scored every {e['name']} →</div>
<div style="font-weight: 800; font-size: 18px; letter-spacing: 2px; color: #999999; margin-top: 18px">coolbio·360 · EP. {e['ep']:02d}</div></div></div>'''
    return page(b,f"{e['name']} cover")
def verdict(e):
    order=sorted(range(4),key=lambda i:-sc(e['plat'][i])); w=order[0]; rows=''
    for i in order:
        p=e['plat'][i]; s=sc(p)
        rows+=f'<div style="display: grid; grid-template-columns: 120px 200px minmax(0, 1fr) 110px; gap: 20px; align-items: center"><img src="{img(p["img"])}" alt="" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; object-position: center {p.get("pos",25)}%; display: block{"; box-shadow: 0 0 0 5px #FFFFFF" if i==w else ""}"><div style="text-align: center">{chip(p,26,"8px 14px",10," 🏆" if i==w else "")}</div><div style="height: 26px; background: rgba(255,255,255,0.10)"><div style="width: {round(s*10)}%; height: 26px; background: {p["radar"]}"></div></div><span style="font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: 54px; text-align: right">{fmt(s)}</span></div>'
    b=f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; background: #111111; color: #F5F5F5; padding: 60px 56px 50px; display: flex; flex-direction: column; overflow: hidden; font-family: 'Inter', sans-serif">
<div style="font-weight: 800; font-size: 20px; letter-spacing: 6px; color: #999999">THE VERDICT · {e['kicker']}</div>
<h2 style="margin: 24px 0 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 92px; line-height: 0.95; letter-spacing: -3px">{e['headline']}</h2>
<div style="margin-top: 14px; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 600; font-size: 38px; color: #BBBBBB">{e['sub']}</div>
<div style="margin-top: 46px; display: flex; flex-direction: column; gap: 22px">{rows}</div>
<div style="margin-top: 50px; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 54px; line-height: 1.02; letter-spacing: -1px">{e['tag']}</div>
<div style="margin-top: auto; display: flex; align-items: flex-end; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.25); padding-top: 20px"><div><div style="font-size: 16px; font-weight: 800; letter-spacing: 4px; color: #999999">NEXT EPISODE</div><div style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 40px; margin-top: 6px">{e['next']}</div></div><div style="text-align: right"><div style="font-weight: 800; font-size: 26px; letter-spacing: -0.5px">coolbio·360</div><div style="font-size: 18px; color: #999999; margin-top: 4px">{e['follow']}</div></div></div></div>'''
    return page(b,f"{e['name']} verdict")
async def main(eps):
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for e in eps:
            pages=[cover(e)]+[platform(e,i) for i in range(4)]+[verdict(e)]
            for k,h in enumerate(pages):
                f=OUT+f'ep{e["ep"]:02d}_{k}.html'; open(f,'w').write(h)
                await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(500)
                await pg.screenshot(path=OUT+f'coolbio360_fourbios_ep{e["ep"]:02d}_{k}.jpg',type='jpeg',quality=92,clip={'x':0,'y':0,'width':1080,'height':1350})
            print('ep',e['ep'],[ (p['name'],fmt(sc(p))) for p in e['plat']],'winner',e['plat'][winner(e)]['name'])
        await b.close()
if __name__=='__main__':
    E=json.load(open(B+'/episodes.json')); sel=[int(x) for x in sys.argv[1:]] or [e['ep'] for e in E]
    asyncio.run(main([e for e in E if e['ep'] in sel]))
