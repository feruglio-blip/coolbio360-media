# Classifiche Top 5 con la grafica nuova (gradiente panoramico, numeri a maglia, card profilo vere).
# Uso: python3 gen_top6.py new/<slug>.json   output in out6/
import json,sys,os,asyncio,base64,io
B=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,B+'/../packs')
import gen_pack6 as P6, gen6_base as V
from gen6_base import E,NAVY,INK,CREAM,M,W,H,grain,header,num,title,sticker
from PIL import Image, ImageFilter
CAP=B+'/cap/'; OUT=B+'/out6/'
def mix(c1,c2,t):
    a=[int(c1[i:i+2],16) for i in (1,3,5)]; b=[int(c2[i:i+2],16) for i in (1,3,5)]
    return '#'+''.join(f'{round(x+(y-x)*t):02x}' for x,y in zip(a,b))
def b64(path,fmt='PNG',im=None):
    if im is None: return f'data:image/{"png" if path.endswith("png") else "jpeg"};base64,'+base64.b64encode(open(path,'rb').read()).decode()
    bio=io.BytesIO(); im.save(bio,fmt,quality=90); return f'data:image/{fmt.lower()};base64,'+base64.b64encode(bio.getvalue()).decode()
def avatar(h,blur=0):
    import numpy as np
    im=Image.open(CAP+h+'_head.png').convert('RGB'); w,hh=im.size
    arr=np.asarray(im).astype(int)[:, :int(hh*.84)]
    ys,xs=np.where(np.abs(arr-255).sum(axis=2)>60)
    x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max(); d=min(x1-x0,y1-y0); cx,cy=(x0+x1)/2,(y0+y1)/2
    r=d/2*0.8                                     # dentro il cerchio: niente bordo bianco
    a=im.crop((int(cx-r),int(cy-r),int(cx+r),int(cy+r))).resize((320,320))
    if blur: a=a.filter(ImageFilter.GaussianBlur(blur))
    return b64('',fmt='JPEG',im=a)
LAB=['Personality','Clarity','Call to action','Details','Photos','Style','Activity']
def cover(d,n):
    A,A2=d['accent'],d['A2']; P={p['rank']:p for p in d['people']}
    def pod(r,x,y,sz):
        p=P[r]
        return f'''<div class="z" style="position:absolute;left:{x}px;top:{y}px;width:{sz}px;text-align:center">
<div style="width:{sz}px;height:{sz}px;border-radius:50%;background:url({avatar(p['h'],14)}) center/cover;box-shadow:0 0 0 8px {CREAM},0 24px 50px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center"><span class="d" style="font-size:{int(sz*.42)}px;color:#fff;text-shadow:0 4px 20px rgba(0,0,0,.4)">?</span></div>
<div style="margin-top:22px;display:flex;justify-content:center;align-items:flex-end;gap:14px">{num(r,int(sz*.62),f"linear-gradient(180deg,{A},{A2})")}<span class="d" style="font-size:{int(sz*.2)}px;color:{CREAM}">{p['score']}</span></div></div>'''
    b=f'''{grain()}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:54px;display:flex;justify-content:space-between;align-items:center;color:{CREAM}">
<div style="display:flex;align-items:center;gap:12px"><img src="{V.LOGO}" style="width:42px;height:42px"><span style="font-weight:800;font-size:26px;letter-spacing:-1px">coolbio·360</span></div>
<span class="sub" style="font-size:28px">The bio issue, vol. {d['vol']}</span></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">
<h1 class="d" style="margin:0;font-size:104px;line-height:.9;letter-spacing:-3px;color:{CREAM}">The 5 best<br><span style="color:{A}">{E(d['word'])} bios</span> {d.get('emoji','')}</h1>
<div class="sub" style="margin-top:20px;font-size:32px;color:{CREAM};opacity:.9">{E(d['sub'])}.<br>Who made No.1?</div></div>
{pod(2,M,640,250)}{pod(1,(W-320)//2,560,320)}{pod(3,W-M-250,700,250)}'''
    return P6.page(b,NAVY)
def profile(d,p,i,n,tone):
    A,A2=d['accent'],d['A2']; fg=NAVY if tone in 'la' else CREAM
    vals=p['bio']+p['feed']
    stats=''.join(f'<div style="text-align:center"><div style="font-size:15px;font-weight:600;opacity:.75;line-height:1.1;height:34px">{l}</div>{num(f"{v:g}",44,(f"linear-gradient(180deg,{NAVY},{INK})" if tone=="a" else f"linear-gradient(180deg,{A if tone!=chr(108) else A2},{A2})"))}</div>' for l,v in zip(LAB,vals))
    phs=''.join(f'<div style="flex:1;height:220px;border-radius:22px;background:url({b64(CAP+p["h"]+f"_{k}.jpg")}) center/cover;box-shadow:0 12px 26px rgba(0,0,0,.18)"></div>' for k in (1,2,3))
    winner=p['rank']==1
    b=f'''{grain()}{header(i,n,fg)}
<div class="z" style="position:absolute;left:{M-6}px;top:120px">{num(p['rank'],260,f"linear-gradient(180deg,{NAVY if tone=='a' else A},{A2})")}</div>
<div class="z" style="position:absolute;left:300px;right:{M}px;top:150px;color:{fg}">
<div class="sub" style="font-size:30px;opacity:.85">{'The winner' if winner else 'No.'+str(p['rank'])+' of 5'}</div>
<div class="d" style="font-size:52px;letter-spacing:-1.5px;margin-top:6px;word-break:break-all">@{E(p['h'])}</div>
<div style="font-size:26px;margin-top:8px;opacity:.8">{E(p['cat'])}</div></div>
<div class="z" style="position:absolute;right:{M}px;top:120px;text-align:right;color:{fg}"></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:420px;display:flex;flex-direction:column;gap:24px">
<div style="position:relative;background:#fff;border-radius:30px;padding:18px 18px 14px;box-shadow:0 24px 50px rgba(0,0,0,.25)">
<img src="{b64(CAP+p['h']+'_head.png')}" style="width:100%;max-height:330px;object-fit:cover;object-position:top;display:block;border-radius:14px">
<div style="position:absolute;right:22px;top:-46px;background:{NAVY if tone!='d' else A};color:{CREAM if tone!='d' else NAVY};border-radius:22px;padding:12px 24px;text-align:center;box-shadow:0 14px 30px rgba(0,0,0,.3)"><div style="font-size:16px;font-weight:700;opacity:.8">Cool Score</div><div class="d" style="font-size:58px;line-height:1">{p['score']}</div></div></div>
<div style="display:flex;gap:20px">{phs}</div>
<div class="sub" style="font-size:30px;line-height:1.3;color:{fg}">{E(p['v'])}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;bottom:44px;display:grid;grid-template-columns:repeat(7,1fr);gap:8px;color:{fg}">{stats}</div>'''
    return P6.page(b,NAVY)
def steal(d,i,n):
    A,A2=d['accent'],d['A2']; st=d['steal']
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:22px;padding:22px 0;border-bottom:2px solid #ECE6D6">{num(k+1,80,f"linear-gradient(180deg,{A2},{NAVY})")}<div style="flex:1"><div style="font-size:19px;font-weight:700;color:#9a948a">{l[1].capitalize()}</div><div style="font-size:32px;font-weight:600;color:#1c1c1e;margin-top:2px">{l[0]}</div></div></div>''' for k,l in enumerate(st['lines']))
    ex='<br>'.join(st['ex'])
    b=f'''{grain()}{header(i,n,NAVY)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:140px;background:#FFFDF6;border-radius:40px;padding:30px 44px;box-shadow:0 30px 70px rgba(0,0,0,.25);font-family:Inter">
<div style="display:flex;justify-content:space-between;font-size:30px;color:#E0A800;font-weight:500"><span>‹ Notes</span><span style="font-weight:700">Done</span></div>
<div class="d" style="font-family:Archivo,'Noto Color Emoji';font-size:58px;color:#1c1c1e;margin-top:16px;letter-spacing:-1.5px;line-height:1">Steal this bio</div>
<div class="sub" style="font-size:28px;color:{A2};margin-top:10px">Built from what our top 5 have in common</div>
<div style="margin-top:10px">{rows}</div>
<div style="margin-top:26px;background:#fff;border:2px solid #ECE6D6;border-radius:24px;padding:22px 26px">
<div style="font-weight:800;font-size:26px;color:#111">{st['ex_h']}</div><div style="font-size:26px;line-height:1.45;color:#222;margin-top:6px">{ex}</div></div></div>
{V.igcard()}'''
    return P6.page(b,NAVY)
def build(d):
    n=7; tones=['d','l','d','l','d','a','l']
    d['A2']=d.get('A2') or mix(d['accent'],'#7A2E1F',.45); d['hues']=d.get('hues') or [d['accent'],d['A2'],'#F2A7C8','#9D8CF2']
    d['slug']=d['slug']; P={p['rank']:p for p in d['people']}; pages=[]
    for i in range(1,n+1):
        P6.CTX.update(p=d,i=i,n=n,tones=tones)
        if i==1: pages.append(cover(d,n))
        elif i<=6: pages.append(profile(d,P[7-i],i,n,tones[i-1]))
        else: pages.append(steal(d,i,n))
    return pages
async def main(path):
    d=json.load(open(path)); os.makedirs(OUT,exist_ok=True)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':W,'height':H})
        for k,h in enumerate(build(d)):
            f=OUT+f"{d['slug']}_{k+1:02d}.html"; open(f,'w').write(h)
            await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(600)
            await pg.screenshot(path=OUT+f"coolbio360_{d['slug']}_{k+1:02d}.jpg",type='jpeg',quality=92)
        await b.close()
    print(d['slug'])
if __name__=='__main__': asyncio.run(main(sys.argv[1]))
