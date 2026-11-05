# 3 varianti di grafica per le classifiche Top 5 (copertina + slide profilo), da scegliere.
# Uso: python3 gen_top_var.py new/<slug>.json
import json,sys,os,asyncio,math
B=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,B+'/../packs')
import gen_pack6 as P6, gen6_base as V
from gen6_base import E,NAVY,INK,CREAM,M,W,H,grain,header
import gen_top6 as T
OUT=B+'/outvar/'
EXTRA='<link href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Big+Shoulders+Display:wght@900&amp;family=Archivo:wdth,wght@62..125,100..900&amp;display=swap" rel="stylesheet">'
LAB=['Personality','Clarity','Call to action','Details','Photos','Style','Activity']
NF={'a':"font-family:Anton,sans-serif;font-weight:400",'b':"font-family:Archivo,sans-serif;font-stretch:125%;font-weight:900",'c':"font-family:'Big Shoulders Display',sans-serif;font-weight:900"}
def N(v,k,size,col,extra=''): return f'<span style="{NF[v]};font-size:{size}px;line-height:.85;color:{col};letter-spacing:-.01em;{extra}">{k}</span>'
def radar(vals,col,line,lab,size=380,fill_op=.35):
    cx,cy,R=200,175,130
    def pt(i,s): a=-math.pi/2+i*2*math.pi/7; return f"{cx+R*s/10*math.cos(a):.1f},{cy+R*s/10*math.sin(a):.1f}"
    rings=''.join(f'<polygon points="{" ".join(pt(i,s) for i in range(7))}" fill="none" stroke="{line}" stroke-width="1.2"/>' for s in (10,7.5,5,2.5))
    axes=''.join(f'<line x1="{cx}" y1="{cy}" x2="{pt(i,10).split(",")[0]}" y2="{pt(i,10).split(",")[1]}" stroke="{line}"/>' for i in range(7))
    poly=f'<polygon points="{" ".join(pt(i,v) for i,v in enumerate(vals))}" fill="{col}" fill-opacity="{fill_op}" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>'
    labs=''
    for i,l in enumerate(LAB):
        a=-math.pi/2+i*2*math.pi/7; x=cx+(R+22)*math.cos(a); y=cy+(R+22)*math.sin(a)+6
        an='middle' if abs(math.cos(a))<.3 else ('start' if math.cos(a)>0 else 'end')
        labs+=f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{an}" font-size="17" font-family="Inter" font-weight="600" fill="{lab}">{l}</text>'
    return f'<svg viewBox="-70 0 540 350" style="width:{size}px;height:{size*350/540:.0f}px;flex:none">{rings}{axes}{poly}{labs}</svg>'
def bars(vals,v,col,track,fg):
    g1,g2=('THE BIO',vals[:4],LAB[:4]),('THE FEED',vals[4:],LAB[4:])
    out=''
    for name,vs,ls in (g1,g2):
        avg=sum(vs)/len(vs)
        out+=f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin:{0 if name=="THE BIO" else 18}px 0 6px"><span style="font-size:18px;font-weight:700;color:{fg};opacity:.7">{name.title()}</span>{N(v,f"{avg:.1f}",40,col)}</div>'
        out+=''.join(f'<div style="display:grid;grid-template-columns:150px 1fr 46px;gap:12px;align-items:center;margin:4px 0;font-size:18px;color:{fg}"><span>{l}</span><div style="height:9px;border-radius:5px;background:{track}"><div style="width:{x*10}%;height:9px;border-radius:5px;background:{col}"></div></div><span style="font-weight:700;text-align:right">{x:g}</span></div>' for l,x in zip(ls,vs))
    return f'<div style="flex:1">{out}</div>'
def page(b): return P6.page(b,NAVY).replace('</head>',EXTRA+'</head>',1)
def head_img(p): return T.b64(T.CAP+p['h']+'_head.png')
def phs(p,h=200): return ''.join(f'<div style="flex:1;height:{h}px;border-radius:20px;background:url({T.b64(T.CAP+p["h"]+f"_{k}.jpg")}) center/cover"></div>' for k in (1,2,3))
# A. Scoreboard: Anton, blu notte, tabellone
def A_profile(d,p,i,n):
    A,A2=d['accent'],d['A2']; vals=p['bio']+p['feed']
    b=f'''{grain()}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:130px;display:flex;align-items:flex-end;gap:26px;color:{CREAM}">
{N('a',p['rank'],250,A)}<div style="flex:1;padding-bottom:22px"><div class="sub" style="font-size:28px;color:{A}">No.{p['rank']} of 5</div>
<div style="font-family:Anton;font-size:60px;line-height:1;margin-top:4px">@{E(p['h'])}</div><div style="font-size:24px;opacity:.8;margin-top:6px">{E(p['cat'])}</div></div>
<div style="text-align:right;padding-bottom:18px"><div style="font-size:18px;font-weight:700;opacity:.7">Cool Score</div>{N('a',p['score'],120,A)}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:400px;background:#fff;border-radius:26px;padding:16px"><img src="{head_img(p)}" style="width:100%;max-height:290px;object-fit:cover;object-position:top;display:block;border-radius:12px"></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:740px;display:flex;gap:16px">{phs(p,170)}</div>
<div class="z" style="position:absolute;left:{M-20}px;right:{M}px;top:935px;display:flex;gap:20px;align-items:center">{radar(vals,A,'rgba(243,238,228,.2)','#D9D3C7',400)}{bars(vals,'a',A,'rgba(243,238,228,.15)',CREAM)}</div>
<div class="z sub" style="position:absolute;left:{M}px;right:{M}px;bottom:36px;font-size:26px;color:{CREAM};opacity:.9">{E(p['v'])}</div>'''
    return page(b)
def A_cover(d,n):
    A,A2=d['accent'],d['A2']; P={p['rank']:p for p in d['people']}
    def pod(r,x,y,sz):
        return f'''<div class="z" style="position:absolute;left:{x}px;top:{y}px;width:{sz}px;text-align:center"><div style="width:{sz}px;height:{sz}px;border-radius:50%;background:url({T.avatar(P[r]['h'],14)}) center/cover;box-shadow:0 0 0 6px {A}"></div>
<div style="margin-top:16px">{N('a',r,int(sz*.55),A)}<span style="font-family:Anton;font-size:{int(sz*.2)}px;color:{CREAM};margin-left:12px">{P[r]['score']}</span></div></div>'''
    b=f'''{grain()}{header(1,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px;color:{CREAM}"><div style="font-family:Anton;font-size:150px;line-height:.9;text-transform:uppercase">The 5 best<br><span style="color:{A}">{E(d['word'])} bios</span></div>
<div class="sub" style="font-size:32px;margin-top:16px">{E(d['sub'])}</div></div>
{pod(2,M,720,240)}{pod(1,(W-300)//2,640,300)}{pod(3,W-M-240,780,240)}'''
    return page(b)
# B. Magazine: Archivo espanso, crema chiaro
def B_profile(d,p,i,n):
    A,A2=d['accent'],d['A2']; vals=p['bio']+p['feed']
    b=f'''{grain(.06)}{header(i,n,NAVY)}
<div class="z" style="position:absolute;right:{M-10}px;top:110px">{N('b',p['rank'],300,A2,'opacity:.95')}</div>
<div class="z" style="position:absolute;left:{M}px;right:330px;top:160px;color:{NAVY}"><div class="sub" style="font-size:28px;color:{A2}">No.{p['rank']} of 5</div>
<div style="font-family:Archivo;font-stretch:112%;font-weight:800;font-size:54px;line-height:1.02;margin-top:6px;word-break:break-all">@{E(p['h'])}</div><div style="font-size:24px;opacity:.75;margin-top:8px">{E(p['cat'])}</div>
<div style="margin-top:18px;display:inline-flex;align-items:baseline;gap:12px;background:{NAVY};color:{CREAM};border-radius:18px;padding:10px 22px"><span style="font-size:18px;font-weight:700">Cool Score</span>{N('b',p['score'],52,A)}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:450px;background:#fff;border-radius:28px;padding:16px;box-shadow:0 20px 44px rgba(11,22,49,.14)"><img src="{head_img(p)}" style="width:100%;max-height:290px;object-fit:cover;object-position:top;display:block;border-radius:12px">
<div style="display:flex;gap:12px;margin-top:12px">{phs(p,160)}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:965px;display:flex;gap:24px;align-items:center;background:rgba(255,255,255,.6);border-radius:28px;padding:16px 26px 16px 0">{radar(vals,A2,'rgba(11,22,49,.15)','#4a4458',380,.3)}{bars(vals,'b',A2,'rgba(11,22,49,.1)',NAVY)}</div>
<div class="z sub" style="position:absolute;left:{M}px;right:{M}px;bottom:30px;font-size:25px;color:{NAVY}">{E(p['v'])}</div>'''
    return page(b)
def B_cover(d,n):
    A,A2=d['accent'],d['A2']; P={p['rank']:p for p in d['people']}
    cards=''.join(f'''<div style="flex:1;background:#fff;border-radius:28px;padding:18px;box-shadow:0 20px 40px rgba(11,22,49,.15);transform:translateY({[0,-60,30][k]}px)">
<div style="aspect-ratio:1;border-radius:20px;background:url({T.avatar(P[r]['h'],14)}) center/cover"></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:12px">{N('b',r,90,A2)}<span style="font-family:Archivo;font-stretch:112%;font-weight:800;font-size:34px;color:{NAVY}">{P[r]['score']}</span></div></div>''' for k,r in enumerate((2,1,3)))
    b=f'''{grain(.06)}{header(1,n,NAVY)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:160px;color:{NAVY}"><div style="font-family:Archivo;font-stretch:125%;font-weight:900;font-size:96px;line-height:.95;letter-spacing:-2px">The 5 best<br><span style="color:{A2}">{E(d['word'])}</span> bios</div>
<div class="sub" style="font-size:32px;margin-top:16px">{E(d['sub'])}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:720px;display:flex;gap:24px">{cards}</div>'''
    return page(b)
# C. Sport card: Big Shoulders pieno, carta da collezione su colore
def C_profile(d,p,i,n):
    A,A2=d['accent'],d['A2']; vals=p['bio']+p['feed']
    b=f'''{grain(.08)}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:56px;right:56px;top:120px;bottom:56px;border-radius:44px;padding:6px;background:linear-gradient(150deg,{A},{A2},{CREAM},{A})">
<div style="width:100%;height:100%;border-radius:40px;background:linear-gradient(170deg,{INK},{NAVY} 60%);padding:30px 34px;color:{CREAM};position:relative;overflow:hidden">
<div style="position:absolute;right:20px;top:-20px">{N('c',p['rank'],330,A,'opacity:.95')}</div>
<div class="sub" style="font-size:28px;color:{A}">No.{p['rank']} of 5</div>
<div style="font-family:'Big Shoulders Display';font-weight:900;font-size:76px;line-height:1;margin-top:2px;max-width:640px;word-break:break-all">@{E(p['h'])}</div>
<div style="font-size:24px;opacity:.8;margin-top:4px">{E(p['cat'])}</div>
<div style="position:relative;z-index:1;margin-top:22px;background:#fff;border-radius:22px;padding:12px"><img src="{head_img(p)}" style="width:100%;max-height:250px;object-fit:cover;object-position:top;display:block;border-radius:10px"></div>
<div style="display:flex;gap:12px;margin-top:14px">{phs(p,200)}</div>
<div style="display:flex;gap:16px;align-items:center;margin-top:10px">{radar(vals,A,'rgba(243,238,228,.2)','#D9D3C7',440)}
<div style="flex:1"><div style="font-size:18px;font-weight:700;opacity:.7">Cool Score</div>{N('c',p['score'],150,A)}
<div style="display:flex;gap:26px;margin-top:6px;font-size:19px"><div>Bio <b style="color:{A}">{sum(p['bio'])/4:.1f}</b></div><div>Feed <b style="color:{A}">{sum(p['feed'])/3:.1f}</b></div></div></div></div>
<div class="sub" style="font-size:28px;line-height:1.3;margin-top:10px">{E(p['v'])}</div></div></div>'''
    return page(b)
def C_cover(d,n):
    A,A2=d['accent'],d['A2']; P={p['rank']:p for p in d['people']}
    def card(r,x,y,w,rot):
        return f'''<div class="z" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);border-radius:30px;padding:5px;background:linear-gradient(150deg,{A},{A2},{CREAM});box-shadow:0 30px 60px rgba(0,0,0,.4)">
<div style="border-radius:26px;background:{NAVY};padding:16px;text-align:center"><div style="aspect-ratio:1;border-radius:18px;background:url({T.avatar(P[r]['h'],14)}) center/cover"></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:8px;padding:0 6px">{N('c',r,110,A)}<span style="font-family:'Big Shoulders Display';font-weight:900;font-size:50px;color:{CREAM}">{P[r]['score']}</span></div></div></div>'''
    b=f'''{grain(.08)}{header(1,n,NAVY)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px;color:{NAVY}"><div style="font-family:'Big Shoulders Display';font-weight:900;font-size:170px;line-height:.85;text-transform:uppercase">The 5 best<br>{E(d['word'])} bios</div>
<div class="sub" style="font-size:32px;margin-top:16px">{E(d['sub'])}</div></div>
{card(2,60,740,300,-8)}{card(3,W-360,760,300,8)}{card(1,(W-340)//2,660,340,0)}'''
    return page(b)
async def main(path):
    d=json.load(open(path)); os.makedirs(OUT,exist_ok=True)
    d['A2']=d.get('A2') or T.mix(d['accent'],'#7A2E1F',.45); d['hues']=[d['accent'],d['A2'],'#F2A7C8','#9D8CF2']
    P={p['rank']:p for p in d['people']}
    jobs={'A':[('d',A_cover),('d',A_profile)],'B':[('l',B_cover),('l',B_profile)],'C':[('a',C_cover),('d',C_profile)]}
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':W,'height':H})
        for v,js in jobs.items():
            for k,(tone,fn) in enumerate(js):
                P6.CTX.update(p=d,i=k+1,n=2,tones=[js[0][0],js[1][0]])
                h=fn(d,2) if k==0 else fn(d,P[2],2,7)
                f=OUT+f"{v}_{k+1}.html"; open(f,'w').write(h)
                await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(700)
                await pg.screenshot(path=OUT+f"var_{v}_{k+1}.jpg",type='jpeg',quality=90)
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1]))
