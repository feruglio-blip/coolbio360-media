# coolbio360 pacchetti v5: stesso sistema della v4 con più layout e sequenze diverse per post.
# Uso: python3 gen_pack5.py packs.json [slug...]   output in out5/
import json,sys,os,asyncio
import gen6_base as V
from gen6_base import E,NAVY,INK,CREAM,M,W,H,uri,grain,orbs,page,header,progress,num,title,sticker
B=os.path.dirname(os.path.abspath(__file__)); OUT=B+'/out5/'
def mix(c1,c2,t):
    a=[int(c1[i:i+2],16) for i in (1,3,5)]; b=[int(c2[i:i+2],16) for i in (1,3,5)]
    return '#'+''.join(f'{round(x+(y-x)*t):02x}' for x,y in zip(a,b))
def lum(c): r,g,b=[int(c[i:i+2],16)/255 for i in (1,3,5)]; return .3*r+.59*g+.11*b
NAVYBG=lambda: f'radial-gradient(120% 80% at 0% 0%,{INK} 0%,{NAVY} 60%)'
# chat: un'amica chiede, le caption sono le risposte
def chat(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',40),64); fs=40 if fs<50 else fs
    ask=s.get('ask','what should I caption this? 🥺')
    out=''.join(f'''<div style="align-self:flex-end;max-width:800px;background:linear-gradient(135deg,{A},{A2});color:{NAVY};border-radius:34px 34px 10px 34px;padding:18px 26px;display:flex;gap:18px;align-items:center;box-shadow:0 10px 26px rgba(0,0,0,.25)">
<span class="n" style="font-size:83px;line-height:.8;color:{NAVY}">{k+1}</span><span style="font-size:{fs}px;font-weight:600;line-height:1.25">{E(b)}</span></div>''' for k,b in enumerate(s['bios']))
    b=f'''{orbs(p,i,n)}{grain()}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],CREAM)}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:300px;display:flex;flex-direction:column;gap:26px">
<div style="display:flex;gap:16px;align-items:flex-end;margin-bottom:14px"><div style="width:150px;height:190px;border-radius:22px;background:url({img}) center/cover;flex:none"></div>
<div style="background:#2a3350;color:{CREAM};border-radius:34px 34px 34px 10px;padding:20px 28px;font-size:38px;font-weight:500">{E(ask)}</div></div>
{out}</div>{progress(i,n,A,'rgba(243,238,228,.18)')}'''
    return page(b,NAVYBG())
# bande: 5 fasce a tutta larghezza dal colore chiaro al blu
def spectrum(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',40),64)
    cols=[A,mix(A,A2,.5),A2,mix(A2,NAVY,.5),NAVY]; top=300; h=(1236-top)//5
    bands=''.join(f'''<div style="position:absolute;left:0;right:0;top:{top+k*h}px;height:{h+1}px;background:linear-gradient(90deg,{c}d9,{mix(c,NAVY,.12)}b3);backdrop-filter:blur(6px);display:flex;align-items:center;gap:30px;padding:0 {M}px;color:{NAVY if lum(c)>.55 else CREAM}">
<span class="n" style="font-size:182px;line-height:.8;width:120px">{k+1}</span><span style="font-family:Inter,'Noto Color Emoji';font-size:{fs}px;font-weight:700;line-height:1.15;max-width:760px">{E(b)}</span></div>''' for k,(b,c) in enumerate(zip(s['bios'],cols)))
    b=f'''{orbs(p,i,n,.5)}{grain(.07)}{header(i,n,NAVY)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],NAVY)}</div>
<div class="z">{bands}</div>{progress(i,n,NAVY,'rgba(11,22,49,.15)')}'''
    return page(b,f'linear-gradient(165deg,{CREAM},{mix(CREAM,A,.35)})')
# bento: griglia di riquadri diversi
def bento(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',40),60); fs=36 if fs<50 else fs
    tw,th,g=456,330,24
    tiles=[('title',NAVYBG(),CREAM),(0,f'linear-gradient(150deg,{A},{A2})',NAVY),(1,'photo',CREAM),(2,'#ffffff',NAVY),(3,f'linear-gradient(150deg,{A2},{mix(A2,NAVY,.45)})',CREAM),(4,f'linear-gradient(150deg,{mix(CREAM,A,.5)},{A})',NAVY)]
    html=''
    for k,(what,bg,fg) in enumerate(tiles):
        x=M+(k%2)*(tw+g); y=140+(k//2)*(th+g)
        style=f'position:absolute;left:{x}px;top:{y}px;width:{tw}px;height:{th}px;border-radius:{[44,24,24,44,24,44][k]}px;overflow:hidden;box-shadow:0 14px 30px rgba(11,22,49,.14);'
        if what=='title':
            html+=f'<div style="{style}background:{bg};padding:34px;display:flex;flex-direction:column;justify-content:flex-end">{title(s["h"],CREAM,78)}<div class="sub" style="font-size:26px;color:{A};margin-top:10px">Screenshot your favourite</div></div>'
        elif bg=='photo':
            html+=f'''<div style="{style}background:url({img}) center/cover"><div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 20%,{NAVY}cc)"></div>
<div style="position:absolute;left:30px;top:24px">{num(what+1,96,f"linear-gradient(180deg,#fff,{A})")}</div><div style="position:absolute;left:30px;right:30px;bottom:28px">{sticker(s["bios"][what],"#fff",NAVY,fs-2)}</div></div>'''
        else:
            html+=f'''<div style="{style}background:{bg};padding:28px 32px;display:flex;flex-direction:column;justify-content:space-between;color:{fg}">
<span class="n" style="font-size:143px;line-height:.8">{what+1}</span><span style="font-family:Inter,'Noto Color Emoji';font-size:{fs}px;font-weight:700;line-height:1.18">{E(s["bios"][what])}</span></div>'''
    b=f'''{orbs(p,i,n,.55)}{grain(.06)}<div class="z">{html}</div>{progress(i,n,NAVY,'rgba(11,22,49,.12)')}'''
    return page(b,f'linear-gradient(165deg,{CREAM},{mix(CREAM,A,.3)})')
# split: metà foto, metà lista
def split(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',40),60); fs=44 if fs<50 else fs
    rows=''.join(f'''<div style="display:flex;gap:18px;align-items:center">{num(k+1,124,f"linear-gradient(180deg,{A},{A2})")}<div>{sticker(b,CREAM,NAVY,fs)}</div></div>''' for k,b in enumerate(s['bios']))
    b=f'''<div style="position:absolute;left:0;top:0;bottom:0;width:430px;background:url({img}) center/cover;z-index:0"></div>
<div style="position:absolute;left:0;top:0;bottom:0;width:430px;background:linear-gradient(90deg,transparent 60%,{NAVY});z-index:0"></div>
{orbs(p,i,n,.6)}{grain()}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:390px;right:{M}px;top:170px">{title(s['h'],CREAM,62)}</div>
<div class="z" style="position:absolute;left:390px;right:{M}px;top:{340 if len(s['h'])<12 else 420}px;display:flex;flex-direction:column;gap:{44 if len(s['h'])<12 else 30}px">{rows}</div>{progress(i,n,A,'rgba(243,238,228,.18)')}'''
    return page(b,NAVY)
# commenti: la sezione commenti di Instagram
def comments(p,s,i,n,img):
    A,A2=p['accent'],p['A2']; fs=min(s.get('fs',40),56); fs=36 if fs<50 else fs
    likes=['12.4k','8.1k','6.9k','5.2k','3.7k']; names=['your_bestie','not_ur_ex','the.groupchat','mum_online','plot.twist']
    rows=''.join(f'''<div style="display:flex;gap:22px;align-items:flex-start">
<div style="flex:none;width:80px;text-align:center"><span class="n" style="font-size:143px;color:{A2};line-height:.8">{k+1}</span></div>
<div style="flex:1"><div style="font-size:24px;font-weight:700;color:#6b7280">{names[k]} <span style="font-weight:500">· {k+2}h</span></div>
<div style="font-size:{fs}px;font-weight:500;color:{NAVY};line-height:1.25;margin-top:4px">{E(b)}</div>
<div style="font-size:22px;font-weight:600;color:#9ca3af;margin-top:8px">Reply</div></div>
<div style="flex:none;text-align:center;color:{A2};font-size:34px;line-height:1">♥<div style="font-size:20px;font-weight:700;color:#6b7280;margin-top:6px">{likes[k]}</div></div></div>''' for k,b in enumerate(s['bios']))
    b=f'''<div style="position:absolute;inset:-40px;background:url({img}) center/cover;filter:blur(18px);z-index:0"></div>
<div style="position:absolute;inset:0;background:{NAVY}88;z-index:0"></div>
{orbs(p,i,n,.5)}{grain(.07)}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],CREAM)}</div>
<div class="z" style="position:absolute;left:36px;right:36px;top:300px;bottom:110px;background:#fff;border-radius:44px;padding:22px 40px;box-shadow:0 -10px 40px rgba(0,0,0,.25)">
<div style="width:90px;height:8px;border-radius:4px;background:#d1d5db;margin:0 auto 14px"></div>
<div style="text-align:center;font-weight:800;font-size:28px;color:{NAVY};margin-bottom:26px">Comments</div>
<div style="display:flex;flex-direction:column;gap:30px">{rows}</div></div>{progress(i,n,A,'rgba(243,238,228,.25)')}'''
    return page(b,NAVY)
def memechat(p,s,i,n,img):
    A,A2=p['accent'],p['A2']
    rows=''.join(f'''<div style="display:flex;flex-direction:column;gap:12px">
<div style="align-self:flex-start;max-width:760px;background:#2a3350;color:{CREAM};border-radius:34px 34px 34px 10px;padding:18px 26px;font-size:36px;font-weight:500">my bio says “{E(a)}”</div>
<div style="align-self:flex-end;max-width:760px;background:linear-gradient(135deg,{A},{A2});color:{NAVY};border-radius:34px 34px 10px 34px;padding:18px 26px;font-size:36px;font-weight:600;font-style:italic">translation: {E(b[0].lower()+b[1:])}</div></div>''' for a,b in s['rows'])
    b=f'''{orbs(p,i,n)}{grain()}{header(i,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">{title(s['h'],CREAM)}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:330px;display:flex;flex-direction:column;gap:34px">{rows}</div>{progress(i,n,A,'rgba(243,238,228,.18)')}'''
    return page(b,NAVYBG())
# copertine
def badge(p,size=230,rot=10):
    A,A2=p['accent'],p['A2']
    return f'''<div style="padding:{int(size*.08)}px {int(size*.15)}px {int(size*.1)}px;border-radius:26px;background:linear-gradient(150deg,{A},{A2});display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate({rot}deg);box-shadow:0 18px 40px rgba(0,0,0,.35);color:{NAVY}">
<span class="n" style="font-size:{int(size*.5)}px;line-height:.85">{p['badge'].split()[0]}</span><span style="font-weight:700;font-size:{int(size*.11)}px">{E(' '.join(p['badge'].split()[1:]))}</span></div>'''
def ex(p):
    s0=p['slides'][0]; return (s0['bios'][0],min(s0.get('fs',40),64)) if 'bios' in s0 else (s0['rows'][0][0],40)
def cover_arch(p,n,img):
    A,A2=p['accent'],p['A2']; l1,l2=p['t3'].split('|'); t,fs=ex(p)
    b=f'''{orbs(p,1,n)}{grain()}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:54px;display:flex;justify-content:space-between;align-items:center;color:{CREAM}">
<div style="display:flex;align-items:center;gap:12px"><img src="{V.LOGO}" style="width:42px;height:42px"><span style="font-weight:800;font-size:26px;letter-spacing:-1px">coolbio·360</span></div>
<span class="sub" style="font-size:28px">The copy-paste issue, vol. {p['vol']}</span></div>
<div class="z" style="position:absolute;right:{M}px;top:150px;width:560px;height:720px;border-radius:280px 280px 36px 36px;background:url({img}) center/cover;box-shadow:0 30px 60px rgba(0,0,0,.45)"></div>
<div class="z" style="position:absolute;left:{M}px;top:250px;transform:rotate(-5deg);max-width:520px">{sticker(t,'#fff',NAVY,fs,'box-shadow:0 14px 34px rgba(0,0,0,.3)')}</div>
<div class="z" style="position:absolute;left:{M+20}px;top:520px">{badge(p,210,-8)}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:900px">
<h1 class="d" style="margin:0;font-size:100px;line-height:.92;letter-spacing:-3px;color:{CREAM}">{E(l1)}<br><span style="background:linear-gradient(90deg,{A},{A2});-webkit-background-clip:text;background-clip:text;color:transparent">{E(l2)}</span></h1>
<div class="sub" style="margin-top:18px;font-size:32px;color:{CREAM};opacity:.9">{E(p['sub'])}</div></div>{progress(1,n,A,'rgba(243,238,228,.18)')}'''
    return page(b,NAVYBG())
def cover_type(p,n,img):
    A,A2=p['accent'],p['A2']; l1,l2=p['t3'].split('|'); t,fs=ex(p)
    b=f'''{orbs(p,1,n,.5)}{grain(.1)}{header(1,n,NAVY).replace(f'>1<span style="opacity:.45">/{n}</span>',f'>vol. {p["vol"]}<span></span>')}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px">
<h1 class="d" style="margin:0;font-size:{118 if len(l1)<15 else 90}px;line-height:.9;letter-spacing:-4px;color:{NAVY}">{E(l1)}<br><span style="color:{A2 if lum(A)>.6 else CREAM}">{E(l2)}</span></h1>
<div class="sub" style="margin-top:20px;font-size:34px;color:{NAVY};max-width:620px">{E(p['sub'])}</div></div>
<div class="z" style="position:absolute;right:60px;top:{640 if len(l1)<15 else 470}px;width:500px;height:{610 if len(l1)<15 else 700}px;background:#fff;padding:22px 22px 90px;transform:rotate(5deg);box-shadow:0 30px 60px rgba(11,22,49,.35)"><div style="width:100%;height:100%;background:url({img}) center/cover"></div></div>
<div class="z" style="position:absolute;right:120px;top:{1110 if len(l1)<15 else 1030}px;transform:rotate(5deg);max-width:520px">{sticker(t,NAVY,CREAM,fs)}</div>
<div class="z" style="position:absolute;left:{M+10}px;top:800px">{badge(p,260,-10).replace(f"linear-gradient(150deg,{A},{A2})",NAVY).replace(f"color:{NAVY}\">",f"color:{CREAM}\">",1)}</div>
{progress(1,n,NAVY,'rgba(11,22,49,.18)')}'''
    return page(b,f'linear-gradient(160deg,{A} 0%,{A2} 100%)')
def end_color(p,n,img):
    A,A2=p['accent'],p['A2']
    acts=[('Save it','for your next post'),('Send it','to the friend who needs it'),('Comment','which one is yours' if p['slug'].startswith('meme') else 'the number you picked')]
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:26px"><span class="n" style="font-size:195px;line-height:.8;color:{NAVY}">{k+1}</span><div><div class="d" style="font-size:62px;color:{NAVY};line-height:1">{a}</div><div class="sub" style="font-size:30px;color:{NAVY};opacity:.75;margin-top:4px">{b}</div></div></div>''' for k,(a,b) in enumerate(acts))
    b=f'''{orbs(p,n,n,.5)}{grain(.1)}{header(n,n,NAVY)}
<div class="z" style="position:absolute;right:-30px;top:560px;width:420px;height:520px;background:#fff;padding:18px 18px 70px;transform:rotate(-6deg);box-shadow:0 30px 60px rgba(11,22,49,.35)"><div style="width:100%;height:100%;background:url({img}) center/cover"></div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:160px">{title(p.get('cta_h','Found your favourite?'),NAVY,90)}</div>
<div class="z" style="position:absolute;left:{M}px;top:470px;display:flex;flex-direction:column;gap:40px">{rows}</div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;bottom:120px;display:flex;justify-content:space-between;align-items:center">
<span class="sub" style="font-size:32px;color:{NAVY}">A new pack every day</span>
<span style="background:{NAVY};color:{CREAM};font-weight:800;font-size:28px;padding:20px 34px;border-radius:999px">Follow @coolbio360</span></div>
{progress(n,n,NAVY,'rgba(11,22,49,.18)')}'''
    return page(b,f'linear-gradient(160deg,{A} 0%,{A2} 100%)')
COVERS={'photo':V.cover,'arch':cover_arch,'type':cover_type}
L={'stack':V.stack,'feature':V.feature,'ladder':V.ladder,'story':V.story,'meme':V.meme,'chat':chat,'spectrum':spectrum,'bento':bento,'split':split,'comments':comments,'memechat':memechat}
PLAN={'winter01':('photo',['chat','stack','spectrum']),'user01':('arch',['bento','split','story','ladder']),
      'emoji01':('type',['spectrum','bento','chat','feature']),'bday01':('arch',['comments','feature','split']),'meme01':('type',['meme','memechat'])}
def build(p):
    img=uri(p['bg']); sl=p['slides']; n=len(sl)+2; cv,seq=PLAN[p['slug']]
    pages=[COVERS[cv](p,n,img)]+[L[seq[k]](p,s,k+2,n,img) for k,s in enumerate(sl)]+[(end_color if cv=='type' else V.end)(p,n,img)]
    return pages
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
