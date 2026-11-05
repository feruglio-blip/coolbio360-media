# coolbio360 pacchetti v3: grafica brand con slide di tipo diverso e una linea continua tra le slide
# Uso: python3 gen_pack3.py packs.json [slug...]   output in out3/
import json,sys,os,asyncio
import gen_pack2 as G
from gen_pack2 import E,CREAM,GREY,SOFT,NAVY,FONTS,LOGO,under,uri
B=os.path.dirname(os.path.abspath(__file__)); OUT=B+'/out3/'
def page(body,A,bg=None,fg=CREAM):
    bgc=bg or 'linear-gradient(160deg,#1B1C1F 0%,#111726 55%,#0B1631 100%)'
    st=f"width:1080px;height:1350px;box-sizing:border-box;border:26px solid {A};background:{bgc};color:{fg};font-family:'Hanken Grotesk','Noto Color Emoji',sans-serif;position:relative;overflow:hidden"
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>body{{margin:0}}*{{box-sizing:border-box}}</style></head><body><div style="{st}">{body}</div></body></html>'
# linea a mano che esce a destra e rientra a sinistra della slide successiva alla stessa altezza
def thread(i,col,y=1170):
    y=1222
    ph=[0,40,-30,25,-40,30][i%6]
    d=f"M-30 {y} C 200 {y-36+ph/2}, 380 {y+34}, 540 {y+ph/3} S 860 {y-34}, 1110 {y}"
    return f'<svg style="position:absolute;left:-26px;top:-26px;width:1080px;height:1350px;pointer-events:none" viewBox="0 0 1080 1350"><path d="{d}" fill="none" stroke="{col}" stroke-width="10" stroke-linecap="round"/></svg>'
def topbar(right,fg=CREAM,line='rgba(243,238,228,0.25)',logo=True):
    lg=f'<img src="{LOGO}" style="width:40px;height:40px">' if logo else ''
    return f'''<div style="position:absolute;left:46px;right:46px;top:40px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid {line};padding-bottom:14px;color:{fg}">
<div style="display:flex;align-items:center;gap:12px">{lg}<span style="font-family:Inter;font-weight:800;font-size:26px;letter-spacing:-1px">coolbio·360</span></div>
<span style="font-size:18px;font-weight:700;letter-spacing:4px;opacity:.75">{E(right)}</span></div>'''
def pill(t,bg,fg): return f'<div style="display:inline-block;background:{bg};color:{fg};padding:7px 16px;font-size:20px;font-weight:700;letter-spacing:5px">{t}</div>'
def foot(l,r,col): return f'<div style="position:absolute;left:46px;right:46px;bottom:40px;display:flex;justify-content:space-between;font-size:20px;font-weight:700;letter-spacing:4px;color:{col}"><span>{l}</span><span>{r}</span></div>'
FS=lambda s,d: s.get('fs',d)
# 1. note su fondo crema, card storte con nastro
def notes(p,s,i,n,img):
    A=p['accent']; rot=[-2.2,1.6,-1.2,2.0,-1.6]; off=[0,90,20,110,40]
    cards=''.join(f'''<div style="position:relative;width:850px;margin-left:{off[k]}px;transform:rotate({rot[k]}deg);background:#fff;padding:26px 30px 24px;box-shadow:0 14px 30px rgba(11,22,49,.16);display:flex;gap:22px;align-items:center">
<div style="position:absolute;top:-12px;left:50%;width:110px;height:26px;margin-left:-55px;background:{A};opacity:.75;transform:rotate({-rot[k]*2}deg)"></div>
<span style="flex:none;font-family:Inter;font-weight:800;font-size:30px;color:{NAVY};background:{A};width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center">{k+1}</span>
<span style="font-family:Inter,'Noto Color Emoji';font-weight:600;font-size:{min(FS(s,40),56)}px;color:{NAVY};line-height:1.2">{E(b)}</span></div>''' for k,b in enumerate(s['bios']))
    b=f'''{topbar(f"{p['tag']} · {i-1} / {n-2}",NAVY,'rgba(11,22,49,.2)')}
<div style="position:absolute;left:46px;right:46px;top:140px;color:{NAVY}">{pill('SCREENSHOT IT 📸',NAVY,CREAM)}
<h2 style="margin:16px 0 0;font-family:Inter;font-weight:700;font-size:76px;line-height:1;letter-spacing:-3px">{E(s['h'])}</h2></div>
<div style="position:absolute;left:46px;right:46px;top:335px;display:flex;flex-direction:column;gap:28px">{cards}</div>
{thread(i,NAVY)}{foot('SAVE IT','NEXT →','#6b6458')}'''
    return page(b,A,CREAM,NAVY)
# 2. foto a tutto schermo con la preferita gigante
def photohero(p,s,i,n,img):
    A=p['accent']; first,rest=s['bios'][0],s['bios'][1:]
    mini=''.join(f'<div style="display:flex;gap:14px;align-items:baseline;font-size:{min(FS(s,40)-8,40)}px;font-family:Inter,\'Noto Color Emoji\';font-weight:500;line-height:1.2"><span style="font-weight:300;color:{A}">{k+2}</span><span>{E(b)}</span></div>' for k,b in enumerate(rest))
    b=f'''<div style="position:absolute;inset:0;background:url({img}) center/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,22,49,.55) 0%,rgba(11,22,49,.05) 30%,rgba(11,22,49,.6) 44%,rgba(11,22,49,.96) 60%)"></div>
{topbar(f"{p['tag']} · {i-1} / {n-2}")}
<div style="position:absolute;left:46px;right:46px;top:140px"><h2 style="margin:0 0 14px;font-family:Inter;font-weight:700;font-size:76px;line-height:1;letter-spacing:-3px;text-shadow:0 4px 20px rgba(0,0,0,.4)">{E(s['h'])}</h2>{pill('SCREENSHOT IT 📸',A,NAVY)}</div>
<div style="position:absolute;left:46px;right:46px;top:620px">{pill('★ OUR FAVOURITE',CREAM,NAVY)}<div style="margin-top:16px; font-family:Inter,'Noto Color Emoji';font-weight:800;font-size:{s.get('hfs',72)}px;line-height:1.02;letter-spacing:-3px"><span style="background:linear-gradient(transparent 58%,{A}aa 58%);padding:0 6px">{E(first)}</span></div></div>
<div style="position:absolute;left:46px;right:46px;top:880px;display:grid;grid-template-columns:1fr 1fr;gap:16px 34px">{mini}</div>
{thread(i,A,1200)}{foot('SAVE IT','NEXT →',SOFT)}'''
    return page(b,A)
# 3. fondo accento, numeri giganti a zigzag
def zigzag(p,s,i,n,img):
    A=p['accent']
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:22px;{'flex-direction:row-reverse;text-align:right;' if k%2 else ''}height:160px">
<span style="flex:none;font-family:Inter;font-weight:800;font-size:190px;line-height:1;color:transparent;-webkit-text-stroke:3px {NAVY};width:150px;text-align:center">{k+1}</span>
<span style="font-family:Inter,'Noto Color Emoji';font-weight:700;font-size:{FS(s,44)}px;color:{NAVY};line-height:1.15;max-width:760px">{E(b)}</span></div>''' for k,b in enumerate(s['bios']))
    b=f'''{topbar(f"{p['tag']} · {i-1} / {n-2}",NAVY,'rgba(11,22,49,.25)')}
<div style="position:absolute;left:46px;right:46px;top:135px;color:{NAVY};display:flex;justify-content:space-between;align-items:flex-end">
<h2 style="margin:0;font-family:Inter;font-weight:800;font-size:80px;line-height:1;letter-spacing:-3.5px">{E(s['h'])}</h2>{pill('SCREENSHOT IT 📸',NAVY,A)}</div>
<div style="position:absolute;left:46px;right:46px;top:270px;display:flex;flex-direction:column">{rows}</div>
{thread(i,NAVY,1180)}{foot('SAVE IT','NEXT →',NAVY)}'''
    return page(b,NAVY,A,NAVY)
# 4. lista blu classica con foto ritagliata che sporge
def navylist(p,s,i,n,img):
    A=p['accent']
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:26px;padding:24px 0;border-bottom:1px solid rgba(243,238,228,.18)">
<div style="flex:none;width:56px;font-family:Inter;font-weight:300;font-size:56px">{k+1}</div>
<div style="flex:1;font-family:Inter,'Noto Color Emoji';font-size:{min(FS(s,42),52)}px;font-weight:500;color:{A};line-height:1.25">{E(b)}</div></div>''' for k,b in enumerate(s['bios']))
    b=f'''<div style="position:absolute;right:-60px;top:110px;width:330px;height:410px;background:url({img}) center/cover;transform:rotate(8deg);border:6px solid {CREAM};box-shadow:0 20px 40px rgba(0,0,0,.4)"></div>
{topbar(f"{p['tag']} · {i-1} / {n-2}")}
<div style="position:absolute;left:46px;width:640px;top:150px">{pill('SCREENSHOT IT 📸',A,NAVY)}
<h2 style="margin:18px 0 0;font-family:Inter;font-weight:700;font-size:76px;line-height:1;letter-spacing:-3px">{E(s['h'])}</h2>
<div style="margin-top:12px;font-style:italic;font-size:28px;color:{SOFT}">Pick one, post it, done.</div></div>
<div style="position:absolute;left:46px;right:46px;top:470px;border-top:1px solid rgba(243,238,228,.25)">{rows}</div>
{thread(i,A,1210)}{foot('SAVE IT','NEXT →',GREY)}'''
    return page(b,A)
def meme(p,s,i,n,img):  # meme: alterna crema e blu
    A=p['accent']; light=(i%2==0); fg=NAVY if light else CREAM
    rows=''.join(f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;padding:34px 0;border-bottom:1px solid {'rgba(11,22,49,.15)' if light else 'rgba(243,238,228,.18)'};align-items:center">
<div style="font-family:Inter,'Noto Color Emoji';font-size:38px;font-weight:600;line-height:1.2">“{E(a)}”</div>
<div style="font-size:35px;font-style:italic;line-height:1.3;{'background:'+A+';color:'+NAVY+';padding:12px 18px;transform:rotate(-1.5deg)' if light else 'color:'+A}">{E(b)}</div></div>''' for a,b in s['rows'])
    b=f'''{topbar(f"{p['tag']} · {i-1} / {n-2}",fg,'rgba(11,22,49,.2)' if light else 'rgba(243,238,228,.25)')}
<div style="position:absolute;left:46px;right:46px;top:150px;color:{fg}">{pill('BE HONEST',NAVY if light else A,CREAM if light else NAVY)}
<h2 style="margin:18px 0 0;font-family:Inter;font-weight:700;font-size:76px;line-height:1;letter-spacing:-3px">{E(s['h'])}</h2>
<div style="margin-top:30px;display:grid;grid-template-columns:1fr 1fr;gap:28px;font-size:18px;font-weight:700;letter-spacing:4px;opacity:.6;padding-bottom:12px">THE BIO SAYS<span>WHAT IT MEANS</span></div>{rows}</div>
{thread(i,NAVY if light else A,1200)}{foot('SEND IT TO A FRIEND','NEXT →',fg)}'''
    return page(b,A,CREAM if light else None,fg)
def cover(p,n,img):
    h=G.cover(p,n,img); return h.replace('</div></body>',thread(1,p['accent'],1190)+'</div></body>',1) if False else h
def cta(p,n,img):
    h=G.cta(p,n,img)
    h=h.replace('TOMORROW</div><div style="font-family:Inter;font-weight:700;font-size:38px;margin-top:6px">','</div><div style="font-family:Inter;font-weight:700;font-size:38px;margin-top:6px">')
    return h[:h.rfind('</div></body>')]+thread(n,p['accent'],1210)+'</div></body></html>'
CYCLE=[notes,photohero,zigzag,navylist]
def build(p):
    img=uri(p['bg']); sl=p['slides']; n=len(sl)+2
    c=G.cover(p,n,img); c=c[:c.rfind('</div></body>')]+thread(1,p['accent'],1230)+'</div></body></html>'
    pages=[c]
    for k,s in enumerate(sl):
        f=meme if s.get('type')=='meme' else CYCLE[k%len(CYCLE)]
        pages.append(f(p,s,k+2,n,img))
    pages.append(cta(p,n,img)); return pages
async def main(path,slugs):
    P=json.load(open(path)); os.makedirs(OUT,exist_ok=True)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for p in P:
            if slugs and p['slug'] not in slugs: continue
            for k,h in enumerate(build(p)):
                f=OUT+f"{p['slug']}_{k+1:02d}.html"; open(f,'w').write(h)
                await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(400)
                await pg.screenshot(path=OUT+f"coolbio360_{p['slug']}_{k+1:02d}.jpg",type='jpeg',quality=92)
            print(p['slug'])
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1],sys.argv[2:]))
