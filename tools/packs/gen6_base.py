# coolbio360 pacchetti v4. Sistema: caption come testo con sfondo delle storie IG, numeri pieni Bricolage con gradiente,
# blu notte + crema + 2 toni per post, grana, sfera di luce a cavallo tra le slide, griglia fissa (margini 72, header, barra avanzamento).
# Uso: python3 gen_pack4.py packs.json [slug...]   output in out4/
import json,sys,os,asyncio,html,base64
B=os.path.dirname(os.path.abspath(__file__)); OUT=B+'/out4/'; BGD=B+'/bg/'
LOGO='file://'+os.path.abspath(B+'/../assets/logo-coolbio360-gradiente.svg')
FONTS='<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Inline+Display:wght@700..900&amp;family=Instrument+Serif:ital@0;1&amp;family=Archivo:wdth,wght@62..125,100..900&amp;family=Inter:wght@400;500;600;700;800&amp;family=Hanken+Grotesk:ital,wght@1,400;1,500&amp;display=swap" rel="stylesheet">'
E=html.escape
NAVY='#0B1631'; INK='#16255A'; CREAM='#F3EEE4'
M=72; W=1080; H=1350
OY=[0,360,1010,300,980,420,900,380]   # altezza della sfera sul confine tra slide i e i+1
def uri(f): return 'data:image/jpeg;base64,'+base64.b64encode(open(BGD+f,'rb').read()).decode()
CSS=f'''body{{margin:0}}*{{box-sizing:border-box}}
.s{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Inter,'Noto Color Emoji',sans-serif}}
.d{{font-family:Archivo,sans-serif;font-stretch:112%;font-weight:800}}
.n{{font-family:'Big Shoulders Inline Display',sans-serif;font-weight:900;font-style:normal;letter-spacing:-.01em;text-shadow:1px 1px 0 var(--sh),2px 2px 0 var(--sh),3px 3px 0 var(--sh),4px 4px 0 var(--sh),5px 5px 0 var(--sh),6px 6px 0 var(--sh),7px 7px 0 var(--sh)}}
.st{{display:inline;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:.1em .38em;border-radius:.28em;line-height:1.5;font-weight:600}}
.sub{{font-family:'Hanken Grotesk';font-style:italic}}
.z{{position:relative;z-index:2}}'''
def grain(op=.09):
    return f'<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:1;mix-blend-mode:overlay;opacity:{op};pointer-events:none"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>'
def orb(x,y,p,op=.75,r=430):
    return f'<div style="position:absolute;left:{x-r}px;top:{y-r}px;width:{2*r}px;height:{2*r}px;border-radius:50%;background:radial-gradient(circle,{p["accent"]} 0%,{p["A2"]} 28%,{p["A2"]}88 46%,transparent 70%);opacity:{op};z-index:0"></div>'
def orbs(p,i,n,op=.75):
    o=''
    if i>1: o+=orb(0,OY[(i-1)%len(OY)],p,op)
    if i<n: o+=orb(W,OY[i%len(OY)],p,op)
    return o
def page(body,bg):
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="s" style="background:{bg}">{body}</div></body></html>'
def header(i,n,fg):
    return f'''<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:54px;display:flex;justify-content:space-between;align-items:center;color:{fg}">
<div style="display:flex;align-items:center;gap:12px"><img src="{LOGO}" style="width:42px;height:42px"><span style="font-weight:800;font-size:26px;letter-spacing:-1px">coolbio·360</span></div>
<span class="d" style="font-size:28px;opacity:.8">{i}<span style="opacity:.45">/{n}</span></span></div>'''
def progress(i,n,on,off):
    seg=''.join(f'<div style="flex:1;height:6px;border-radius:3px;background:{on if k<i else off}"></div>' for k in range(n))
    return f'<div class="z" style="position:absolute;left:{M}px;right:{M}px;bottom:58px;display:flex;gap:10px">{seg}</div>'
def num(k,size,grad):
    import re as _r
    size=int(size*1.15); cols=_r.findall('#[0-9A-Fa-f]{6}',grad); fill=cols[0] if cols else '#ffffff'; shc=cols[-1] if len(cols)>1 else '#0B1631'
    if fill.lower()==NAVY.lower(): shc='#ffffff99'
    if fill.lower()=='#ffffff' or fill.lower()=='#fff': shc=cols[-1] if len(cols)>1 else NAVY
    d=max(4,size//24); shadow=','.join(f'{j}px {j}px 0 {shc}' for j in range(1,d+1))
    return f'<span class="n" style="font-size:{size}px;line-height:.82;color:{fill};text-shadow:{shadow};display:inline-block;padding-right:.06em">{k}</span>'
def igcard(dark=True):
    return f'''<div class="z" style="position:absolute;left:{M}px;right:{M}px;bottom:96px;background:#fff;border-radius:32px;padding:24px 28px;display:flex;align-items:center;gap:22px;box-shadow:0 20px 50px rgba(0,0,0,.28);font-family:Inter">
<img src="{LOGO}" style="width:96px;height:96px;border-radius:50%;background:{NAVY}">
<div style="flex:1"><div style="font-weight:800;font-size:30px;color:#111">coolbio360</div><div style="font-size:24px;color:#555;margin-top:4px;line-height:1.3">Copy-paste bios &amp; captions<br>A new pack every day</div></div>
<div style="background:#0095F6;color:#fff;font-weight:700;font-size:28px;padding:16px 40px;border-radius:14px">Follow</div></div>'''
def title(t,fg,size=80): return f'<h2 class="d" style="margin:0;font-size:{size}px;line-height:.92;letter-spacing:-2px;color:{fg}">{E(t)}</h2>'
def sticker(t,bg,fg,fs,extra=''): return f'<span class="st" style="background:{bg};color:{fg};font-size:{fs}px;{extra}">{E(t)}</span>'
# A. blu con luce: numeri a gradiente + caption crema
def stack(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',42),64)
    rows=''.join(f'''<div style="display:grid;grid-template-columns:150px 1fr;align-items:center;min-height:150px">
{num(k+1,150,f"linear-gradient(180deg,{A} 10%,{A2} 95%)")}<div>{sticker(b,CREAM,NAVY,fs)}</div></div>''' for k,b in enumerate(s['bios']))
    b=f'''{orbs(p,i,n)}{grain()}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],CREAM)}<div class="sub" style="margin-top:14px;font-size:30px;color:{A}">Screenshot the one that sounds like you</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:395px">{rows}</div>{progress(i,n,A,'rgba(243,238,228,.18)')}'''
    return page(b,f'radial-gradient(120% 80% at 0% 0%,{INK} 0%,{NAVY} 60%)')
# B. crema: la preferita gigante + le altre in griglia
def feature(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=s.get('fs',42); first,rest=s['bios'][0],s['bios'][1:]
    emo=fs>=60; big=110 if emo else (64 if len(first)<34 else 56); small=60 if emo else (38 if max(map(len,rest))<34 else 34)
    cards=''.join(f'''<div style="background:rgba(255,255,255,.72);border-radius:30px;padding:28px 30px;min-height:268px;display:flex;flex-direction:column;justify-content:space-between;gap:14px;box-shadow:0 12px 30px rgba(11,22,49,.10)">
{num(k+2,84,f"linear-gradient(180deg,{A2},{NAVY})")}<div style="font-family:Inter,'Noto Color Emoji';font-size:{small}px;font-weight:600;color:{NAVY};line-height:1.22">{E(b)}</div></div>''' for k,b in enumerate(rest))
    b=f'''{orbs(p,i,n,.55)}{grain(.06)}{header(i,n,NAVY)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px;display:flex;align-items:baseline;gap:18px"><span class="d" style="font-size:44px;color:{NAVY}">{E(s['h'])}</span><span class="sub" style="font-size:30px;color:{A2}">our favourite</span></div>
<div class="z" style="position:absolute;left:{M-6}px;top:230px">{num(1,250,f"linear-gradient(170deg,{A},{A2})")}</div>
<div class="z" style="position:absolute;left:260px;right:{M}px;top:230px;height:340px;display:flex;align-items:center"><div class="d" style="font-family:Archivo,'Noto Color Emoji';font-size:{big}px;line-height:1.05;letter-spacing:-1.5px;color:{NAVY}">{E(first) if emo else "“"+E(first)+"”"}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:610px;display:grid;grid-template-columns:1fr 1fr;gap:24px">{cards}</div>
{progress(i,n,NAVY,'rgba(11,22,49,.12)')}'''
    return page(b,f'linear-gradient(165deg,{CREAM} 0%,{CREAM} 45%,{A}66 100%)')
# C. colore pieno a gradiente: caption bianche, numeri blu pieni, allineamento a scala
def ladder(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',42),64)
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:22px;margin-left:{[0,70,140,70,0][k]}px;min-height:140px">
{num(k+1,124,f"linear-gradient(180deg,{NAVY},{INK})")}<div style="max-width:{760-[0,70,140,70,0][k]}px">{sticker(b,'#fff',NAVY,fs,'box-shadow:0 10px 24px rgba(11,22,49,.18)')}</div></div>''' for k,b in enumerate(s['bios']))
    b=f'''{orbs(p,i,n,.6)}{grain(.1)}{header(i,n,NAVY)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],NAVY)}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:345px">{rows}</div>{progress(i,n,NAVY,'rgba(11,22,49,.18)')}'''
    return page(b,f'linear-gradient(155deg,{A} 0%,{A2} 100%)')
# D. foto come una storia: caption sparse sulla foto
def story(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',42),60)
    pos=[(0,0),(120,0),(30,0),(150,0),(60,0)]
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:18px;margin-left:{pos[k][0]}px;transform:rotate({[-2,1.5,-1,2,-1.5][k]}deg)">
<span class="n" style="font-size:143px;line-height:.82;color:{A};filter:drop-shadow(0 6px 14px rgba(0,0,0,.45))">{k+1}</span><div style="max-width:{720-pos[k][0]}px">{sticker(b,'#fff',NAVY,fs,'box-shadow:0 10px 30px rgba(0,0,0,.25)')}</div></div>''' for k,b in enumerate(s['bios']))
    b=f'''<div style="position:absolute;inset:0;background:url({img}) center/cover;z-index:0"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,{NAVY}e0 0%,{NAVY}88 30%,{NAVY}99 60%,{NAVY}ee 100%);z-index:0"></div>
{orbs(p,i,n,.5)}{grain(.08)}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],CREAM)}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:360px;display:flex;flex-direction:column;gap:40px">{rows}</div>{progress(i,n,A,'rgba(243,238,228,.25)')}'''
    return page(b,NAVY)
def meme(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; light=(i%2==0); fg=NAVY if light else CREAM
    rows=''.join(f'''<div style="display:flex;flex-direction:column;gap:12px">
<div>{sticker('“'+a+'”','#fff' if light else CREAM,NAVY,46,'box-shadow:0 6px 18px rgba(11,22,49,.10)')}</div>
<div style="margin-left:150px"><span class="st sub" style="font-size:40px;font-weight:500;background:linear-gradient(90deg,{A},{A2});color:{NAVY}">{E(b)}</span></div></div>''' for a,b in s['rows'])
    b=f'''{orbs(p,i,n,.55 if light else .75)}{grain(.07)}{header(i,n,fg)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],fg)}<div class="sub" style="margin-top:14px;font-size:30px;color:{A2 if light else A}">What the bio says, and what it really means</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:400px;display:flex;flex-direction:column;gap:58px">{rows}</div>{progress(i,n,NAVY if light else A,'rgba(11,22,49,.12)' if light else 'rgba(243,238,228,.18)')}'''
    return page(b,f'linear-gradient(165deg,{CREAM} 0%,{CREAM} 50%,{A}55 100%)' if light else f'radial-gradient(120% 80% at 0% 0%,{INK} 0%,{NAVY} 60%)')
def cover(p,n,img):
    A,A2=p['accent'],p['A2']; l1,l2=p['t3'].split('|')
    s0=p['slides'][0]; ex=s0['bios'][0] if 'bios' in s0 else s0['rows'][0][0]
    b=f'''<div style="position:absolute;inset:0;background:url({img}) center/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,{NAVY}b0 0%,{NAVY}00 22%,{NAVY}10 45%,{NAVY}f0 74%,{NAVY} 100%)"></div>
{orbs(p,1,n,.6)}{grain(.09)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:54px;display:flex;justify-content:space-between;align-items:center;color:{CREAM}">
<div style="display:flex;align-items:center;gap:12px"><img src="{LOGO}" style="width:42px;height:42px"><span style="font-weight:800;font-size:26px;letter-spacing:-1px">coolbio·360</span></div>
<span class="sub" style="font-size:28px">The copy-paste issue, vol. {p['vol']}</span></div>
<div class="z" style="position:absolute;left:{M+40}px;top:300px;transform:rotate(-4deg);max-width:640px">{sticker(ex,'#fff',NAVY,min(s0.get('fs',40),64) if 'bios' in s0 else 40,'box-shadow:0 14px 34px rgba(0,0,0,.3)')}</div>
<div class="z" style="position:absolute;right:{M}px;top:560px;padding:18px 34px 22px;border-radius:26px;background:linear-gradient(150deg,{A},{A2});display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(10deg);box-shadow:0 18px 40px rgba(0,0,0,.35);color:{NAVY}">
<span class="n" style="font-size:124px;line-height:.85">{p['badge'].split()[0]}</span><span style="font-weight:700;font-size:26px">{E(' '.join(p['badge'].split()[1:]))}</span></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:{1350-470}px">
<h1 class="d" style="margin:0;font-size:96px;line-height:.92;letter-spacing:-3px;color:{CREAM}">{E(l1)}<br><span style="background:linear-gradient(90deg,{A},{A2});-webkit-background-clip:text;background-clip:text;color:transparent">{E(l2)}</span></h1>
<div class="sub" style="margin-top:22px;font-size:34px;color:{CREAM};opacity:.9">{E(p['sub'])}</div></div>
{progress(1,n,A,'rgba(243,238,228,.25)')}'''
    return page(b,NAVY)
def end(p,n,img):
    A,A2=p['accent'],p['A2']
    acts=[('Save it','for your next post'),('Send it','to the friend who needs it'),('Comment','which one is yours' if p['slug'].startswith('meme') else 'the number you picked')]
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:26px">{num(k+1,150,f"linear-gradient(180deg,{A},{A2})")}<div><div class="d" style="font-size:62px;color:{CREAM};line-height:1">{a}</div><div class="sub" style="font-size:30px;color:{A};margin-top:4px">{b}</div></div></div>''' for k,(a,b) in enumerate(acts))
    b=f'''{orbs(p,n,n)}{grain()}{header(n,n,CREAM)}
<div class="z" style="position:absolute;right:-40px;top:170px;width:360px;height:450px;background:url({img}) center/cover;border-radius:28px;transform:rotate(7deg);box-shadow:0 30px 60px rgba(0,0,0,.45)"></div>
<div class="z" style="position:absolute;left:{M}px;width:600px;top:170px">{title(p.get('cta_h','Found your favourite?'),CREAM,84)}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:500px;display:flex;flex-direction:column;gap:40px">{rows}</div>
{igcard()}
{progress(n,n,A,'rgba(243,238,228,.18)')}'''
    return page(b,f'radial-gradient(120% 80% at 0% 0%,{INK} 0%,{NAVY} 60%)')
def build(p):
    img=uri(p['bg']); sl=p['slides']; n=len(sl)+2; pages=[cover(p,n,img)]
    seq={2:[meme,meme],3:[stack,feature,ladder],4:[stack,feature,story,ladder]}[len(sl)]
    for k,s in enumerate(sl): pages.append(seq[k](p,s,k+2,n,img))
    pages.append(end(p,n,img)); return pages
async def main(path,slugs):
    P=json.load(open(path)); os.makedirs(OUT,exist_ok=True)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':W,'height':H})
        for p in P:
            if slugs and p['slug'] not in slugs: continue
            for k,h in enumerate(build(p)):
                f=OUT+f"{p['slug']}_{k+1:02d}.html"; open(f,'w').write(h)
                await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(500)
                await pg.screenshot(path=OUT+f"coolbio360_{p['slug']}_{k+1:02d}.jpg",type='jpeg',quality=92)
            print(p['slug'])
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1],sys.argv[2:]))
