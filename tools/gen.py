import asyncio, sys, json, os, html as H
import pathlib
T=str(pathlib.Path(__file__).resolve().parent)
B=T
LOGO='file://'+T+'/assets/logo-coolbio360-trasparente.svg'
FONTS='<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Hanken+Grotesk:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">'
ROOT='width: 1080px; height: 1350px; box-sizing: border-box; border: 30px solid {A}; background: linear-gradient(160deg, #1B1C1F 0%, #111726 55%, #0B1631 100%); font-family: \'Hanken Grotesk\', sans-serif; color: #F3EEE4; overflow: hidden; display: flex; flex-direction: column; padding: 40px 48px {PB}px'
LBL='font-size: 19px; font-weight: 700; letter-spacing: 4px; color: #9A958B'
def header(right):
    return f'''<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(243, 238, 228, 0.35); padding-bottom: 18px">
<div style="display: flex; align-items: center; gap: 12px"><img src="{LOGO}" style="width: 56px; height: 56px; display: block"><div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 36px; letter-spacing: -1.5px">coolbio·360</div></div>
<div style="{LBL}">{right}</div></div>'''
def table(cat,strg):
    return f'''<div style="display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; padding: 14px 0; border-top: 1px solid rgba(243, 238, 228, 0.35); border-bottom: 1px solid rgba(243, 238, 228, 0.12)"><div style="{LBL}">CATEGORY</div><div style="font-size: 28px">{cat}</div></div>
<div style="display: flex; justify-content: space-between; padding: 14px 0; border-bottom: 1px solid rgba(243, 238, 228, 0.35)"><div style="{LBL}">STRENGTHS</div><div style="font-size: 28px">{strg}</div></div></div>'''
def shot(handle,winner,A):
    o=f'outline: 4px solid {A}; outline-offset: 8px; ' if winner else ''
    return f'''<div style="margin-top: 40px; font-size: 18px; font-weight: 700; letter-spacing: 4px; color: #9A958B">AS SEEN ON INSTAGRAM · @{handle.upper()}</div>
<div style="margin-top: 14px; background: #FFFFFF; border-radius: 18px; padding: 18px; box-shadow: 0 30px 60px rgba(0, 0, 0, 0.45); {o}display: flex; justify-content: center"><img src="file://{T}/shots/{handle}.png" style="display: block; max-width: 100%; max-height: 360px; height: auto"></div>'''
def verdict(t,fs=44): return f'<div style="margin-top: 24px; font-family: \'Hanken Grotesk\'; font-style: italic; font-size: {fs}px; line-height: 1.2; color: #E9E3D7">{t}</div>'
def footer(l,r): return f'<div style="margin-top: auto; display: flex; justify-content: space-between; {LBL}"><div>{l}</div><div style="color: #F3EEE4">{r}</div></div>'
def emobox(e,w,h,fs,bar,A): return f'<div style="display: flex; flex-direction: column; width: {w}px"><div style="height: {h}px; border: 1px solid rgba(243, 238, 228, 0.16); display: flex; align-items: center; justify-content: center; font-size: {fs}px">{e}</div><div style="height: {bar}px; background: {A}"></div></div>'
def wrap(A,inner,pb=44): return '<!doctype html><html><head><meta charset="utf-8">'+FONTS+'<style>body{margin:0}</style></head><body><div style="'+ROOT.format(A=A,PB=pb)+'">'+inner+'</div></body></html>'

def hand(title,A):
    w,rest=(title.rsplit(' ',1)+[''])[:2]
    svg=(f'<svg viewBox="0 0 300 40" preserveAspectRatio="none" style="position:absolute;left:-2%;bottom:-0.13em;width:106%;height:0.3em;overflow:visible">'
         f'<path d="M6 24 C 50 14, 110 20, 160 17 S 250 12, 294 19" fill="none" stroke="{A}" stroke-width="16" stroke-linecap="round"/>'
         f'<path d="M22 30 C 90 22, 170 27, 284 23" fill="none" stroke="{A}" stroke-width="8" stroke-linecap="round" opacity="0.9"/></svg>')
    return f'<span style="position:relative;display:inline-block">{w}{svg}</span> {rest}'
def cover(c):
    A=c['accent']
    inner=f'''<div style="display: flex; justify-content: space-between; margin-top: 18px; font-size: 20px; font-weight: 700; letter-spacing: 4px; color: #9A958B"><div>THE BIO ISSUE</div><div>VOL. {c['vol']} · {c['tag']}</div></div>
<div style="margin-top: 80px; display: flex; align-items: flex-end; justify-content: space-between"><div style="background: {A}; color: #0B1631; padding: 10px 22px; font-size: 26px; font-weight: 700; letter-spacing: 6px">THE LIST</div>{emobox(c['emoji'],190,180,130,10,A)}</div>
<div style="margin-top: 30px; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 150px; line-height: 0.95; letter-spacing: -6px">The 5 Best</div>
<div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 150px; line-height: 0.95; letter-spacing: -6px">{hand(c['title'],A)}</div>
<div style="font-family: 'Hanken Grotesk'; font-style: italic; font-weight: 400; font-size: 80px; line-height: 1.1; color: #D9D3C7; margin-top: 30px">on Instagram right now</div>
<div style="margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; border-top: 2px solid rgba(243, 238, 228, 0.85); padding-top: 24px"><div style="font-size: 31px; font-weight: 500; line-height: 1.4; max-width: 640px; color: #D9D3C7">{c['sub']} Ranked from No. 5 to No. 1 by our editors.</div><div style="font-size: 24px; font-weight: 700; letter-spacing: 5px">SWIPE →</div></div>'''
    return wrap(A,inner,48)
def rank(c,p):
    A=c['accent']; r=p['rank']
    nxt='NEXT: THE WINNER →' if r==2 else f'NEXT: No. {r-1} →'
    inner=header(f"THE LIST · {c['tag']} · {r} / 5")+f'''<div style="display: flex; align-items: flex-end; justify-content: space-between; margin-top: 36px">
<div style="font-family: 'Inter', sans-serif; font-weight: 300; font-size: 230px; line-height: 0.8; letter-spacing: -14px">0{r}</div>
<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px; padding-bottom: 6px"><div style="font-size: 18px; font-weight: 700; letter-spacing: 4px; color: #9A958B">COOL SCORE</div><div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 100px; line-height: 0.9; letter-spacing: -4px">{p['score']}</div></div>
{emobox(p['emoji'],160,150,96,9,A)}</div>'''+shot(p['h'],False,A)+'<div style="margin-top: 34px">'+table(p['cat'],p['str'])+'</div>'+verdict(p['v'])+footer(f'RANK 0{r} OF 05',nxt)
    return wrap(A,inner)
def winner(c,p):
    A=c['accent']
    inner=header(f"THE LIST · {c['tag']} · WINNER")+f'''<div style="display: flex; align-items: flex-end; justify-content: space-between; margin-top: 36px">
<div style="display: flex; flex-direction: column; gap: 14px"><div style="align-self: flex-start; background: {A}; color: #0B1631; padding: 8px 20px; font-size: 22px; font-weight: 700; letter-spacing: 6px">No. 1 · COOL SCORE {p['score']}</div>
<div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 112px; line-height: 0.95; letter-spacing: -5px">The Best<br>{c['single']}</div></div>{emobox('🏆',170,160,104,10,A)}</div>'''+shot(p['h'],True,A)+'<div style="margin-top: 44px">'+table(p['cat'],p['str'])+'</div>'+verdict(p['v'],40)+footer(p['congrats'],'ONE MORE →')
    return wrap(A,inner)
def end(c):
    A=c['accent']; n=c['next']
    row=lambda a,b,last=False: f'<div style="display: flex; justify-content: space-between; padding: 16px 0; {"border-top: 1px solid rgba(243, 238, 228, 0.35); " if a=="Personality" else ""}border-bottom: 1px solid rgba(243, 238, 228, {"0.35" if last else "0.12"}); font-size: 30px"><div>{a}</div><div style="color: #9A958B">{b}</div></div>'
    inner=header(f"THE LIST · {c['tag']}")+f'''<div style="margin-top: 90px; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 132px; line-height: 0.95; letter-spacing: -6px">Is your bio<br>next?</div>
<div style="margin-top: 22px; font-family: 'Hanken Grotesk'; font-style: italic; font-size: 52px; line-height: 1.15; color: #D9D3C7">Tag us in your stories or send it by DM.</div>
<div style="margin-top: 70px; display: flex; flex-direction: column"><div style="{LBL}; padding-bottom: 14px">HOW WE PICK</div>{row('Personality','Does it sound like a person?')}{row('Clarity','Do we get it in 3 seconds?')}{row('Call to action','Do we know what to do next?',True)}</div>
<div style="margin-top: auto; display: flex; align-items: flex-end; justify-content: space-between"><div style="display: flex; flex-direction: column; gap: 10px"><div style="{LBL}">NEXT LIST</div><div style="display: flex; align-items: center; gap: 22px">{emobox(n[1],96,90,56,7,n[2])}<div style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 56px; letter-spacing: -2px">{n[0]}</div></div></div>
<div style="background: #F3EEE4; color: #0B1631; padding: 18px 34px; font-size: 24px; font-weight: 700; letter-spacing: 4px">FOLLOW @COOLBIO360</div></div>'''
    return wrap(A,inner,48)

async def main(only=None):
    from playwright.async_api import async_playwright
    data=json.load(open(T+'/data/'+(os.environ.get('DATA') or 'data.json')))
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for c in data:
            if only and c['slug'] not in only: continue
            slides=[]
            if 'people' in c:
                ps=sorted(c['people'],key=lambda p:-p['rank'])
                slides=[cover(c)]+[rank(c,p) for p in ps if p['rank']>1]+[winner(c,[p for p in ps if p['rank']==1][0])]
            slides.append(end(c))
            start=7 if 'people' not in c else 1
            for i,h in enumerate(slides,start):
                hp=f"/tmp/cb_{c['slug']}_{i}.html"; open(hp,'w').write(h)
                await pg.goto('file://'+hp); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(800)
                os.makedirs(T+"/out",exist_ok=True); out=f"{T}/out/coolbio360_{c['slug']}_{i:02d}.jpg"
                await pg.screenshot(path=out,type='jpeg',quality=92,clip={'x':0,'y':0,'width':1080,'height':1350}); print(out)
        await b.close()
if __name__=="__main__": asyncio.run(main(sys.argv[1:] or None))
