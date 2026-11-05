# coolbio360 pacchetti "Copy & Paste" con la grafica del brand (blu notte, cornice accento, Inter + Hanken Grotesk, sottolineatura a mano, telefono)
# Uso: python3 gen_pack2.py packs.json [slug...]   foto in bg/, output in out2/
import json,sys,os,asyncio,html,base64
B=os.path.dirname(os.path.abspath(__file__)); OUT=B+'/out2/'; BGD=B+'/bg/'
LOGO='file://'+os.path.abspath(B+'/../assets/logo-coolbio360-gradiente.svg')
FONTS='<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&amp;family=Hanken+Grotesk:ital,wght@0,400;0,500;0,700;1,400;1,500&amp;display=swap" rel="stylesheet">'
E=html.escape
CREAM='#F3EEE4'; GREY='#9A958B'; SOFT='#D9D3C7'; NAVY='#0B1631'
def frame(A): return f"width:1080px;height:1350px;box-sizing:border-box;border:26px solid {A};background:linear-gradient(160deg,#1B1C1F 0%,#111726 55%,#0B1631 100%);color:{CREAM};font-family:'Hanken Grotesk','Noto Color Emoji',sans-serif;position:relative;overflow:hidden"
def page(body,A): return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>body{{margin:0}}*{{box-sizing:border-box}}</style></head><body><div style="{frame(A)}">{body}</div></body></html>'
def uri(f): return 'data:image/jpeg;base64,'+base64.b64encode(open(BGD+f,'rb').read()).decode()
def under(word,A):
    return f'<span style="position:relative;display:inline-block">{word}<svg aria-hidden="true" viewBox="0 0 300 40" preserveAspectRatio="none" style="position:absolute;left:-2%;bottom:-0.14em;width:104%;height:0.3em;overflow:visible"><path d="M6 24 C 50 14, 110 20, 160 17 S 250 12, 294 19" fill="none" stroke="{A}" stroke-width="16" stroke-linecap="round"/><path d="M22 30 C 90 22, 170 27, 284 23" fill="none" stroke="{A}" stroke-width="8" stroke-linecap="round" opacity="0.9"/></svg></span>'
def topbar(right):
    return f'''<div style="position:absolute;left:46px;right:46px;top:40px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(243,238,228,0.25);padding-bottom:14px">
<div style="display:flex;align-items:center;gap:12px"><img src="{LOGO}" style="width:40px;height:40px"><span style="font-family:Inter;font-weight:800;font-size:26px;letter-spacing:-1px">coolbio·360</span></div>
<span style="font-size:18px;font-weight:700;letter-spacing:4px;color:{GREY}">{E(right)}</span></div>'''
def title_html(p): return E(p['t2']).replace(E(p['uw']),under(E(p['uw']),p['accent']),1).replace('|','<br>')
def phone(img,line,A):
    return f'''<div style="width:420px;height:760px;border-radius:60px;background:#0d0d0f;padding:13px;box-shadow:0 0 0 3px #c9c6bf,0 36px 70px rgba(0,0,0,.55)">
<div style="width:100%;height:100%;border-radius:48px;overflow:hidden;background:#fff;display:flex;flex-direction:column;color:#1d1a24;font-family:Inter,'Noto Color Emoji'">
<div style="height:40px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;letter-spacing:4px;color:{GREY}">• • •</div>
<div style="display:flex;align-items:center;gap:10px;padding:2px 16px 10px"><div style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,{A},#0B1631)"></div><div style="font-weight:700;font-size:17px">you</div><div style="margin-left:auto;font-weight:800;color:{GREY}">···</div></div>
<div style="height:440px;background:url({img}) center/cover"></div>
<div style="padding:12px 16px 0;font-size:24px;letter-spacing:6px">♡ ◯ ➢</div>
<div style="padding:8px 16px;font-size:20px;line-height:1.35"><b>you</b> {E(line)}</div></div></div>'''
def cover(p,n,img):
    A=p['accent']; first=p['slides'][0]
    line=first['bios'][0] if 'bios' in first else first['rows'][0][0]
    b=f'''<div style="position:absolute;left:46px;right:46px;top:44px;display:flex;justify-content:space-between;font-size:20px;font-weight:700;letter-spacing:4px;color:{GREY}"><span>THE COPY-PASTE ISSUE</span><span>VOL. {p['vol']} · {E(p['tag'])}</span></div>
<div style="position:absolute;left:46px;right:46px;top:100px;text-align:center">
<div style="display:inline-block;background:{A};color:{NAVY};padding:8px 18px;font-size:22px;font-weight:700;letter-spacing:6px">{E(p.get('kicker','COPY · PASTE · POST').upper())}</div>
<h1 style="margin:18px 0 0;font-family:Inter;font-weight:700;font-size:{p.get('tfs',84)}px;line-height:1;letter-spacing:-3.5px">{title_html(p)}</h1>
<div style="margin-top:16px;font-style:italic;font-size:32px;color:{SOFT}">{E(p['sub'])}</div></div>
<div style="position:absolute;left:50%;top:{p.get('ptop',455)}px;transform:translateX(-50%) rotate(-3deg)">{phone(img,line,A)}</div>
<div style="position:absolute;left:46px;right:46px;bottom:36px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid rgba(243,238,228,.85);padding-top:16px;background:linear-gradient(transparent,#0B1631 30%)"><span style="font-size:24px;font-weight:500;color:{SOFT}">{E(p.get('foot','Save it now, thank us later'))}</span><span style="font-size:22px;font-weight:700;letter-spacing:5px">SWIPE →</span></div>'''
    return page(b,A)
def listslide(p,s,i,n):
    A=p['accent']; fs=s.get('fs',44)
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:26px;padding:34px 0;border-bottom:1px solid rgba(243,238,228,.18)">
<div style="flex:none;width:56px;font-family:Inter;font-weight:300;font-size:56px;color:{CREAM}">{k+1}</div>
<div style="flex:1;font-family:Inter,'Noto Color Emoji';font-size:{fs}px;font-weight:500;color:{A};line-height:1.25">{E(b)}</div></div>''' for k,b in enumerate(s['bios']))
    b=f'''{topbar(f"{p['tag']} · {i-1} / {n-2}")}
<div style="position:absolute;left:46px;right:46px;top:150px">
<div style="display:inline-block;background:{A};color:{NAVY};padding:7px 16px;font-size:20px;font-weight:700;letter-spacing:5px">SCREENSHOT IT 📸</div>
<h2 style="margin:18px 0 0;font-family:Inter;font-weight:700;font-size:72px;line-height:1;letter-spacing:-3px">{E(s['h'])}</h2>
<div style="margin-top:12px;font-style:italic;font-size:28px;color:{SOFT}">{E(s.get('sub','Pick one, post it, done.'))}</div>
<div style="margin-top:34px;border-top:1px solid rgba(243,238,228,.25)">{rows}</div></div>
<div style="position:absolute;left:46px;right:46px;bottom:40px;display:flex;justify-content:space-between;font-size:20px;font-weight:700;letter-spacing:4px;color:{GREY}"><span>SAVE IT</span><span>NEXT →</span></div>'''
    return page(b,A)
def memeslide(p,s,i,n):
    A=p['accent']
    rows=''.join(f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;padding:36px 0;border-bottom:1px solid rgba(243,238,228,.18);align-items:center">
<div style="font-family:Inter,'Noto Color Emoji';font-size:38px;font-weight:500;color:{CREAM};line-height:1.25">“{E(a)}”</div>
<div style="font-size:36px;font-style:italic;color:{A};line-height:1.3">{E(b)}</div></div>''' for a,b in s['rows'])
    b=f'''{topbar(f"{p['tag']} · {i-1} / {n-2}")}
<div style="position:absolute;left:46px;right:46px;top:150px">
<div style="display:inline-block;background:{A};color:{NAVY};padding:7px 16px;font-size:20px;font-weight:700;letter-spacing:5px">BE HONEST</div>
<h2 style="margin:18px 0 0;font-family:Inter;font-weight:700;font-size:72px;line-height:1;letter-spacing:-3px">{E(s['h'])}</h2>
<div style="margin-top:34px;display:grid;grid-template-columns:1fr 1fr;gap:28px;font-size:18px;font-weight:700;letter-spacing:4px;color:{GREY};padding-bottom:12px;border-bottom:1px solid rgba(243,238,228,.25)"><span>THE BIO SAYS</span><span>WHAT IT MEANS</span></div>{rows}</div>
<div style="position:absolute;left:46px;right:46px;bottom:40px;display:flex;justify-content:space-between;font-size:20px;font-weight:700;letter-spacing:4px;color:{GREY}"><span>SEND IT TO A FRIEND</span><span>NEXT →</span></div>'''
    return page(b,A)
def cta(p,n,img):
    A=p['accent']
    b=f'''{topbar(f"{p['tag']} · THE END")}
<div style="position:absolute;left:46px;right:46px;top:170px">
<div style="display:inline-block;background:{A};color:{NAVY};padding:7px 16px;font-size:20px;font-weight:700;letter-spacing:5px">YOUR TURN</div>
<h2 style="margin:18px 0 0;font-family:Inter;font-weight:700;font-size:92px;line-height:.98;letter-spacing:-4px">{E(p.get('cta_h','Found your favourite?'))}</h2>
<div style="margin-top:20px;font-style:italic;font-size:34px;color:{SOFT};line-height:1.35">{E(p.get('cta_t','Tell us the number in the comments.'))}</div>
<div style="margin-top:50px;display:flex;gap:24px;align-items:stretch">
<div style="width:420px;height:540px;border:4px solid {CREAM};background:url({img}) center/cover;transform:rotate(-3deg)"></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:34px;font-size:40px">
<div><span style="font-family:Inter;font-weight:300;font-size:54px;margin-right:18px">1</span><b style="color:{A}">Save</b> it for later</div>
<div><span style="font-family:Inter;font-weight:300;font-size:54px;margin-right:18px">2</span><b style="color:{A}">Send</b> it to a friend</div>
<div><span style="font-family:Inter;font-weight:300;font-size:54px;margin-right:18px">3</span><b style="color:{A}">Comment</b> your pick</div></div></div></div>
<div style="position:absolute;left:46px;right:46px;bottom:40px;display:flex;justify-content:space-between;align-items:flex-end">
<div><div style="font-size:18px;font-weight:700;letter-spacing:4px;color:{GREY}">TOMORROW</div><div style="font-family:Inter;font-weight:700;font-size:38px;margin-top:6px">{E(p.get('next','A new pack, every day'))}</div></div>
<div style="background:{CREAM};color:{NAVY};padding:20px 26px;font-family:Inter;font-weight:700;font-size:24px;letter-spacing:3px">FOLLOW @COOLBIO360</div></div>'''
    return page(b,A)
def build(p):
    img=uri(p['bg']); sl=p['slides']; n=len(sl)+2; pages=[cover(p,n,img)]
    for k,s in enumerate(sl): pages.append((memeslide if s.get('type')=='meme' else listslide)(p,s,k+2,n))
    pages.append(cta(p,n,img)); return pages
async def main(path,slugs):
    P=json.load(open(path)); os.makedirs(OUT,exist_ok=True)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for p in P:
            if slugs and p['slug'] not in slugs: continue
            pages=build(p)
            for k,h in enumerate(pages):
                f=OUT+f"{p['slug']}_{k+1:02d}.html"; open(f,'w').write(h)
                await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(400)
                await pg.screenshot(path=OUT+f"coolbio360_{p['slug']}_{k+1:02d}.jpg",type='jpeg',quality=92)
            print(p['slug'],len(pages))
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1],sys.argv[2:]))
