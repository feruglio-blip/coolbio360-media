# coolbio360 dal 6/11/2026: pacchetti "da copiare" e meme su foto aesthetic.
# Uso: python3 gen_pack.py packs.json [slug...]  (foto in tools/packs/bg/, output in tools/packs/out/)
import json,sys,os,asyncio,html,base64
B=os.path.dirname(os.path.abspath(__file__)); OUT=B+'/out/'; BG=B+'/bg/'
FONTS='<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;1,9..144,500&amp;family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">'
E=html.escape
EMO="'Inter','Noto Color Emoji',sans-serif"
def uri(f): return 'data:image/jpeg;base64,'+base64.b64encode(open(BG+f,'rb').read()).decode()
def page(body,img,blur=False,dark=.0):
    flt='filter:blur(28px) saturate(1.1);transform:scale(1.15);' if blur else ''
    return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>body{{margin:0}}*{{box-sizing:border-box}}</style></head><body>
<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:#222;font-family:{EMO};color:#fff">
<div style="position:absolute;inset:0;background:url({img}) center/cover;{flt}"></div>
<div style="position:absolute;inset:0;background:rgba(20,16,24,{dark})"></div>{body}</div></body></html>'''
def brand(): return '<div style="position:absolute;left:64px;bottom:52px;font-weight:800;font-size:28px;letter-spacing:-0.5px;text-shadow:0 2px 12px rgba(0,0,0,.35)">coolbio·360</div>'
def counter(i,n): return f'<div style="position:absolute;right:64px;bottom:56px;font-weight:600;font-size:22px;letter-spacing:3px;opacity:.85">{i} / {n}</div>'
def cover(p,n,img):
    b=f'''<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 40%,rgba(15,10,20,.78) 78%,rgba(15,10,20,.9) 100%)"></div>
<div style="position:absolute;left:64px;top:70px;font-weight:700;font-size:24px;letter-spacing:5px;text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.4)">{E(p.get('kicker','Copy · Paste · Post'))}</div>
<div style="position:absolute;right:64px;top:62px;background:#fff;color:#1d1a24;border-radius:999px;padding:12px 26px;font-weight:800;font-size:24px">SAVE IT ↓</div>
<div style="position:absolute;left:64px;right:64px;bottom:250px">
<div style="font-family:Fraunces,serif;font-weight:800;font-size:{p.get('tfs',112)}px;line-height:.98;letter-spacing:-3px">{p['title']}</div>
<div style="margin-top:28px;font-size:34px;line-height:1.35;opacity:.92">{E(p['sub'])}</div></div>
<div style="position:absolute;left:64px;bottom:150px;display:flex;gap:12px;flex-wrap:wrap">{''.join(f'<span style="background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.4);backdrop-filter:blur(8px);border-radius:999px;padding:10px 22px;font-size:24px;font-weight:600">{E(t)}</span>' for t in p.get('chips',[]))}</div>
{brand()}{counter(1,n)}'''
    return page(b,img)
def head(h,A,tag='screenshot it 📸'):
    return f'''<div style="position:absolute;left:64px;right:64px;top:70px;display:flex;justify-content:space-between;align-items:center">
<div style="font-family:Fraunces,serif;font-weight:800;font-size:58px;letter-spacing:-1px;text-shadow:0 2px 14px rgba(0,0,0,.3)">{E(h)}</div>
<div style="background:{A};color:#1d1a24;border-radius:999px;padding:10px 22px;font-weight:700;font-size:22px">{tag}</div></div>'''
def bios(p,s,i,n,img):
    A=p['accent']; items=s['bios']
    cards=''.join(f'''<div style="background:rgba(255,255,255,.88);color:#1d1a24;border-radius:28px;padding:24px 30px;box-shadow:0 10px 30px rgba(0,0,0,.18);display:flex;gap:22px;align-items:center">
<div style="flex:none;width:48px;height:48px;border-radius:50%;background:#1d1a24;color:#fff;font-weight:800;font-size:22px;display:flex;align-items:center;justify-content:center">{k+s.get('start',1)}</div>
<div style="font-size:{s.get('fs',38)}px;line-height:1.32;white-space:pre-line">{E(b)}</div></div>''' for k,b in enumerate(items))
    b=f'''{head(s['h'],A)}<div style="position:absolute;left:64px;right:64px;top:180px;bottom:130px;display:flex;flex-direction:column;justify-content:center;gap:20px">{cards}</div>{brand()}{counter(i,n)}'''
    return page(b,img,True,.25)
def meme(p,s,i,n,img):
    A=p['accent']
    rows=''.join(f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div style="background:rgba(255,255,255,.9);color:#1d1a24;border-radius:24px;padding:24px 26px;font-size:31px;line-height:1.3;white-space:pre-line">{E(a)}</div>
<div style="background:#1d1a24;color:#fff;border-radius:24px;padding:24px 26px;font-size:31px;line-height:1.3;font-weight:600;white-space:pre-line">{E(b)}</div></div>''' for a,b in s['rows'])
    hd=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;font-weight:800;font-size:22px;letter-spacing:4px;text-transform:uppercase"><div>{E(s.get("l","The bio says"))}</div><div>{E(s.get("r","What it means"))}</div></div>'
    b=f'''{head(s['h'],A,'be honest')}<div style="position:absolute;left:64px;right:64px;top:180px;bottom:130px;display:flex;flex-direction:column;justify-content:center;gap:18px">{hd}{rows}</div>{brand()}{counter(i,n)}'''
    return page(b,img,True,.3)
def cta(p,i,n,img):
    b=f'''<div style="position:absolute;left:64px;right:64px;top:250px;text-align:center">
<div style="font-family:Fraunces,serif;font-weight:800;font-size:100px;line-height:1;letter-spacing:-3px">{E(p.get('cta_h','Found your favourite?'))}</div>
<div style="margin-top:36px;font-size:38px;line-height:1.45;opacity:.95">{E(p.get('cta_t','Tell us the number in the comments.'))}</div>
<div style="margin:64px auto 0;display:flex;flex-direction:column;gap:18px;width:720px;color:#1d1a24">
<div style="background:#fff;border-radius:999px;padding:26px;font-weight:800;font-size:34px">📌 Save it for later</div>
<div style="background:rgba(255,255,255,.85);border-radius:999px;padding:26px;font-weight:700;font-size:32px">📤 Send it to a friend</div></div>
<div style="margin-top:76px;font-weight:800;font-size:34px">Follow @coolbio360 for a new pack every day ✨</div></div>
{counter(i,n)}'''
    return page(b,img,True,.35)
def build(p):
    img=uri(p['bg']); sl=p['slides']; n=len(sl)+2; pages=[cover(p,n,img)]
    for k,s in enumerate(sl):
        f={'bios':bios,'meme':meme}[s.get('type','bios')]; pages.append(f(p,s,k+2,n,img))
    pages.append(cta(p,n,n,img)); return pages
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
