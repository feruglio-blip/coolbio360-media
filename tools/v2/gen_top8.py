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
<div style="width:{sz}px;height:{sz}px;border-radius:50%;background:url({T.avatar(P[r]['h'])}) center/cover;box-shadow:0 0 0 7px {A if r==1 else CREAM},0 0 0 14px rgba(255,255,255,.12),0 30px 60px rgba(0,0,0,.5)"></div>
<div style="margin-top:22px;display:flex;justify-content:center;align-items:baseline;gap:14px">{N(r,int(sz*.5),A if r==1 else CREAM)}<span style="font-family:Anton;font-size:{int(sz*.2)}px;color:{CREAM};opacity:.85">{P[r]['score']}</span></div></div>'''
    b=f'''{grain()}{header(1,7,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px;color:{CREAM}">
<div class="sub" style="font-size:30px;color:{A}">The bio issue, vol. {d['vol']}</div>
<div style="font-family:Anton;font-size:156px;line-height:.9;text-transform:uppercase;margin-top:10px">The 5 best<br><span style="background:linear-gradient(90deg,{A},{d['hues'][1]});-webkit-background-clip:text;background-clip:text;color:transparent">{E(d['word'])} bios</span></div>
<div class="sub" style="font-size:32px;margin-top:18px;opacity:.9">{E(d['sub'])}</div></div>
{pod(2,M+10,790,250)}{pod(3,W-M-260,830,250)}{pod(1,(W-320)//2,720,320)}'''
    return page(b,A)
def profile(d,p,i):
    A,A2=d['accent'],d['A2']; vals=p['bio']+p['feed']; win=p['rank']==1
    hl=d['hues'][1]
    phs=''.join(f'<div style="flex:1;height:140px;border-radius:20px;background:url({T.b64(T.CAP+p["h"]+f"_{k}.jpg")}) center/cover;box-shadow:0 0 0 5px rgba(255,255,255,.14),0 18px 34px rgba(0,0,0,.35)"></div>' for k in (1,2,3))
    b=f'''{grain()}{header(i,7,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:128px;display:flex;align-items:flex-end;gap:26px;color:{CREAM}">
{N(p['rank'],250,A,f'background:linear-gradient(180deg,{A},{hl});-webkit-background-clip:text;background-clip:text;color:transparent')}
<div style="flex:1;padding-bottom:24px"><div class="sub" style="font-size:28px;color:{A}">{'The winner 🏆' if win else 'No.'+str(p['rank'])+' of 5'}</div>
<div style="font-family:Anton;font-size:62px;line-height:1.02;margin-top:4px;word-break:break-all">@{E(p['h'])}</div><div style="font-size:24px;opacity:.8;margin-top:6px">{E(p['cat'])}</div></div>
<div style="text-align:right;padding-bottom:20px"><div style="font-size:18px;font-weight:700;opacity:.75">Cool Score</div>{N(p['score'],116,A)}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:420px;{CARD()}"><img src="{T.b64(T.CAP+p['h']+'_head.png')}" style="width:100%;max-height:320px;object-fit:cover;object-position:top;display:block;border-radius:16px"></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:772px;display:flex;gap:18px">{phs}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:1018px;display:flex;gap:6px;align-items:center;padding:6px 26px 6px 0;{GLASS}">{TV.radar(vals,A,'rgba(243,238,228,.25)','#E9E3D7',310)}{TV.bars(vals,'a',A,'rgba(243,238,228,.16)',CREAM)}</div>
<div class="z sub" style="position:absolute;left:{M}px;right:{M}px;top:938px;font-size:26px;line-height:1.25;color:{CREAM};opacity:.92">{E(p['v'])}</div>'''
    return page(b,A)
def steal(d):
    A=d['accent']; h=T.steal(d,7,7); h=h.replace('</head>',EXTRA+'</head>',1)
    i=h.rfind('</div></body>'); return h[:i]+f'<div style="position:absolute;inset:0;border:22px solid {A};z-index:9;pointer-events:none"></div>'+h[i:]
async def main(path):
    d=json.load(open(path)); os.makedirs(OUT,exist_ok=True); P={p['rank']:p for p in d['people']}
    A=d['accent']; d['A2']=T.mix(A,'#5A1E10',.5)
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
