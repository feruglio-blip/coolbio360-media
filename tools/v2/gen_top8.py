# Classifiche Top 5, versione A rifinita: blu notte con gradiente panoramico più deciso (toni analoghi dell'accento),
# cornice accento attorno, avatar visibili, Anton per numeri e titoli, card con cornice chiara, ragnatela + barre in vetro.
# Uso: python3 gen_top8.py new/<slug>.json   output in out8/
import json,sys,os,asyncio
B=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,B+'/../packs')
import gen_pack6 as P6, gen6_base as V
from gen6_base import E,NAVY,INK,CREAM,M,W,H,grain,header
import gen_top6 as T, gen_top_var as TV
OUT=B+'/out8/'
EXTRA='<link href="https://fonts.googleapis.com/css2?family=Anton&amp;display=swap" rel="stylesheet">'
def N(k,size,col,extra=''): return f'<span style="font-family:Anton;font-size:{size}px;line-height:.86;color:{col};{extra}">{k}</span>'
def page(b,acc):
    h=P6.page(b,NAVY).replace('</head>',EXTRA+'</head>',1)
    frame=f'<div style="position:absolute;inset:0;border:22px solid {acc};z-index:9;pointer-events:none"></div>'
    i=h.rfind('</div></body>'); return h[:i]+frame+h[i:]
CARD=lambda: 'background:#fff;border-radius:30px;padding:14px;box-shadow:0 0 0 8px rgba(255,255,255,.18),0 30px 60px rgba(0,0,0,.45)'
GLASS='background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.22);border-radius:30px;backdrop-filter:blur(14px)'
def cover(d):
    A,A2=d['accent'],d['A2']; P={p['rank']:p for p in d['people']}
    def pod(r,x,y,sz):
        return f'''<div class="z" style="position:absolute;left:{x}px;top:{y}px;width:{sz}px;text-align:center">
<div style="width:{sz}px;height:{sz}px;border-radius:50%;background:url({T.avatar(P[r]['h'])}) center/cover;box-shadow:0 0 0 7px {d['strong'] if r==1 else 'rgba(243,238,228,.35)'},0 30px 60px rgba(0,0,0,.5)"></div>
<div style="margin-top:22px;display:flex;justify-content:center;align-items:baseline;gap:14px">{N(r,int(sz*.5),d['strong'] if r==1 else CREAM)}<span style="font-family:Anton;font-size:{int(sz*.2)}px;color:{CREAM};opacity:.85">{P[r]['score']}</span></div></div>'''
    b=f'''{grain()}{header(1,7,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px;color:{CREAM}">
<div class="sub" style="font-size:30px;color:{CREAM}">The bio issue, vol. {d['vol']}</div>
<div style="font-family:Anton;font-size:156px;line-height:.9;text-transform:uppercase;margin-top:10px">The 5 best<br><span style="color:{d['strong']}">{E(d['word'])} bios</span></div>
<div class="sub" style="font-size:32px;margin-top:18px;opacity:.9">{E(d['sub'])}</div></div>
{pod(2,M+10,790,250)}{pod(3,W-M-260,830,250)}{pod(1,(W-320)//2,720,320)}'''
    return page(b,d['strong'])
def statcol(name,vs,ls,S):
    rows=''.join(f'''<div style="display:grid;grid-template-columns:128px 150px 34px;gap:12px;align-items:center;height:30px;font-size:18px;color:{CREAM}"><span>{l}</span><div style="height:8px;border-radius:4px;background:rgba(243,238,228,.18)"><div style="width:{x*10}%;height:8px;border-radius:4px;background:{S}"></div></div><span style="font-weight:700;text-align:right">{x:g}</span></div>''' for l,x in zip(ls,vs))
    return f'''<div><div style="display:flex;justify-content:space-between;align-items:baseline;height:52px;border-bottom:1px solid rgba(243,238,228,.2);margin-bottom:8px"><span style="font-size:22px;font-weight:800;color:{CREAM}">{name}</span>{N(f"{sum(vs)/len(vs):.1f}",40,S)}</div>{rows}</div>'''
def profile(d,p,i):
    A,S=d['accent'],d['strong']; vals=p['bio']+p['feed']; win=p['rank']==1
    tiles=''.join(f'<div style="flex:1;aspect-ratio:3/4;background:url({T.b64(T.CAP+p["h"]+f"_{k}.jpg")}) center/cover"></div>' for k in (1,2,3))
    b=f'''<div style="position:absolute;left:0;right:0;top:0;height:470px;background:linear-gradient(180deg,{NAVY} 0%,{NAVY}f2 55%,{NAVY}00 100%);z-index:1"></div>
{grain()}{header(i,7,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:120px;bottom:40px;display:flex;flex-direction:column;justify-content:space-between">
<div style="display:flex;align-items:center;gap:26px;color:{CREAM}">
{N(p['rank'],190,S)}
<div style="flex:1;min-width:0"><div style="font-size:22px;font-weight:800;color:{CREAM};opacity:.85">{'THE WINNER 🏆' if win else 'No.'+str(p['rank'])+' of 5'}</div>
<div style="font-family:Anton;font-size:54px;line-height:1.04;margin-top:4px;word-break:break-all">@{E(p['h'])}</div>
<div class="sub" style="font-size:23px;line-height:1.28;margin-top:8px;opacity:.92">{E(p['v'])}</div></div>
<div style="flex:none;width:170px;text-align:center;border-left:1px solid rgba(243,238,228,.22);padding-left:18px">{N(p['score'],100,S)}<div style="font-size:16px;font-weight:800;letter-spacing:.5px;margin-top:10px;opacity:.85">Cool Score / 10</div></div></div>
<div style="background:#fff;border-radius:28px;padding:14px;box-shadow:0 0 0 8px rgba(255,255,255,.16),0 30px 60px rgba(0,0,0,.45)">
<img src="{T.b64(T.CAP+p['h']+'_head.png')}" style="width:100%;display:block">
<div style="display:flex;gap:4px;margin-top:10px">{tiles}</div></div>
<div style="display:flex;align-items:center;justify-content:center;gap:30px">{TV.radar(vals,S,'rgba(243,238,228,.3)','#E9E3D7',240)}<div style="display:flex;gap:30px;align-items:flex-start">{statcol('The Bio',p['bio'],TV.LAB[:4],S)}{statcol('The Feed',p['feed'],TV.LAB[4:],S)}</div></div></div>'''
    return page(b,d['strong'])
def steal(d):
    S=d['strong']; st=d['steal']
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:22px;padding:22px 0;border-bottom:2px solid #ECE6D6">{N(k+1,76,S,'width:44px;text-align:center')}<div style="flex:1"><div style="font-size:18px;font-weight:700;color:#9a948a">{l[1].capitalize()}</div><div style="font-size:30px;font-weight:600;color:#1c1c1e;margin-top:2px">{l[0]}</div></div></div>''' for k,l in enumerate(st['lines']))
    ex='<br>'.join(st['ex'])
    b=f'''{grain()}{header(7,7,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:130px;bottom:40px;display:flex;flex-direction:column;justify-content:space-between">
<div style="background:#FFFDF6;border-radius:40px;padding:34px 44px 40px;box-shadow:0 30px 70px rgba(0,0,0,.3);font-family:Inter">
<div style="display:flex;justify-content:space-between;font-size:28px;color:#E0A800;font-weight:500"><span>‹ Notes</span><span style="font-weight:700">Done</span></div>
<div style="font-family:Anton;font-size:64px;color:#1c1c1e;margin-top:12px;line-height:1">STEAL THIS BIO</div>
<div class="sub" style="font-size:26px;color:#6b6458;margin-top:8px">Built from what our top 5 have in common</div>
<div style="margin-top:6px">{rows}</div>
<div style="margin-top:20px;background:#fff;border:2px solid #ECE6D6;border-radius:24px;padding:18px 24px">
<div style="font-weight:800;font-size:24px;color:#111">{st['ex_h']}</div><div style="font-size:24px;line-height:1.42;color:#222;margin-top:4px">{ex}</div></div></div>
<div style="background:#fff;border-radius:30px;padding:22px 26px;display:flex;align-items:center;gap:22px;box-shadow:0 20px 50px rgba(0,0,0,.3)">
<img src="{V.LOGO}" style="width:90px;height:90px;border-radius:50%;background:{NAVY}">
<div style="flex:1"><div style="font-weight:800;font-size:30px;color:#111">coolbio360</div><div style="font-size:23px;color:#555;margin-top:4px;line-height:1.3">The best bios on Instagram, ranked<br>Follow for tomorrow's list</div></div>
<div style="background:#0095F6;color:#fff;font-weight:700;font-size:28px;padding:16px 38px;border-radius:14px">Follow</div></div></div>'''
    return page(b,S)
async def main(path):
    d=json.load(open(path)); os.makedirs(OUT,exist_ok=True); P={p['rank']:p for p in d['people']}
    A=d['accent']; d['A2']=T.mix(A,'#5A1E10',.5)
    import colorsys; r,g,b_=[int(A[k:k+2],16)/255 for k in (1,3,5)]; hh,ll,ss=colorsys.rgb_to_hls(r,g,b_); rr,gg,bb=colorsys.hls_to_rgb(hh,.6,1.0); d['strong']='#%02x%02x%02x'%(int(rr*255),int(gg*255),int(bb*255))
    d['hues']=[A,'#FF4D6D','#FFB45E','#9B2C6E']     # analoghi caldi: accento, corallo, ambra, prugna
    tones=['d']*7
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':W,'height':H})
        for i in range(1,8):
            P6.CTX.update(p=d,i=i,n=7,tones=tones)
            h=cover(d) if i==1 else (profile(d,P[7-i],i) if i<7 else steal(d))
            f=OUT+f"{d['slug']}_{i:02d}.html"; open(f,'w').write(h)
            await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(700)
            await pg.screenshot(path=OUT+f"coolbio360_{d['slug']}_{i:02d}.jpg",type='jpeg',quality=92)
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1]))
