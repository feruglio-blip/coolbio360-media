# coolbio360 post da copiare, stile allineato alle classifiche (6/11): Bricolage Grotesque, numeri pieni senza ombra,
# cornice nel colore della serie, accento oro (sottolineatura a mano della parola chiave, etichette), copertine A/B/E/F.
# Uso: python3 gen_pack7.py packs.json [slug...]   output in out7/
import json,sys,os,asyncio,re,html
import gen_pack6 as P6, gen6_base as V, gen6_layouts as L5
from gen6_base import E,NAVY,INK,CREAM,M,W,H,grain,header,sticker
B=os.path.dirname(os.path.abspath(__file__)); OUT=B+'/out7/'
GOLD='#FFD23F'
BRIC='<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&amp;display=swap" rel="stylesheet">'
CSS=".d{font-family:'Bricolage Grotesque',sans-serif!important;font-stretch:100%!important;font-weight:800!important;letter-spacing:-.02em}\n.n{font-family:'Bricolage Grotesque',sans-serif!important;font-weight:800!important;text-shadow:none!important;letter-spacing:-.04em!important}"
def num(k,size,grad):
    cols=re.findall('#[0-9A-Fa-f]{6}',grad); col=cols[-1] if cols else '#FFFFFF'
    if len(cols)>1 and cols[-1].upper() in ('#4C6FD6','#7B55D9','#E05683','#F07A3C','#23A07E') and cols[0].upper()!=NAVY.upper(): col=cols[0]
    if col.lower() in (INK.lower(),): col=NAVY
    if '170deg' in grad and len(cols)>1: col=cols[-1]
    return f'<span class="n" style="font-size:{int(size*.95)}px;line-height:.82;color:{col};display:inline-block">{k}</span>'
V.num=num; L5.num=num
def under(word,col=GOLD):
    return f'<span style="position:relative;display:inline-block">{word}<svg viewBox="0 0 300 40" preserveAspectRatio="none" style="position:absolute;left:-2%;bottom:-0.08em;width:104%;height:0.24em;overflow:visible"><path d="M6 24 C 50 14, 110 20, 160 17 S 250 12, 294 19" fill="none" stroke="{col}" stroke-width="16" stroke-linecap="round"/><path d="M22 30 C 90 22, 170 27, 284 23" fill="none" stroke="{col}" stroke-width="8" stroke-linecap="round" opacity=".9"/></svg></span>'
def finish(h,p):
    h=h.replace('</head>',BRIC+f'<style>{CSS}</style></head>',1)
    # seconda riga del titolo: colore pieno + sottolineatura oro sulla prima parola
    k=h.find('<h1'); 
    if k>0:
        e=h.find('</h1>',k); seg=h[k:e]; w=E(p['uw'])
        j=seg.find('>'+w) if seg.find('>'+w)>=0 else seg.find(' '+w)
        if j>=0: j+=1; seg=seg[:j]+under(w)+seg[j+len(w):]
        h=h[:k]+seg+h[e:]
    return h
def cover_emoji(p,n,img):
    A,A2=p['accent'],p['A2']; l1,l2=p['t3'].split('|'); s0=p['slides'][0]['bios']
    big=''.join(f'<div style="font-size:{[230,190,210][k]}px;line-height:1;transform:rotate({[-8,6,-3][k]}deg);filter:drop-shadow(0 20px 30px rgba(0,0,0,.45))">{E(s0[k])}</div>' for k in range(3))
    b=f'''{grain()}{header(1,n,CREAM)}
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:150px;color:{CREAM}"><div class="sub" style="font-size:30px">The copy-paste issue, vol. {p['vol']}</div>
<h1 class="d" style="margin:12px 0 0;font-size:112px;line-height:.94;letter-spacing:-3px">{E(l1)}<br><span style="background:linear-gradient(90deg,{A},{A2});-webkit-background-clip:text;background-clip:text;color:transparent">{E(l2)}</span></h1>
<div class="sub" style="margin-top:18px;font-size:32px;opacity:.9">{E(p['sub'])}</div></div>
<div class="z" style="position:absolute;left:{M}px;right:{M}px;top:640px;display:flex;flex-direction:column;gap:26px;font-family:'Noto Color Emoji'">{big}</div>
<div class="z" style="position:absolute;right:{M+10}px;top:760px;transform:rotate(8deg);background:{GOLD};color:{NAVY};border-radius:22px;padding:14px 26px;text-align:center"><div class="n" style="font-size:96px;line-height:.9">{p['badge'].split()[0]}</div><div style="font-weight:800;font-size:24px">{E(' '.join(p['badge'].split()[1:]))}</div></div>'''
    return P6.page(b,NAVY)
L5.COVERS['emoji']=cover_emoji
PLAN={'winter01':('photo',['chat','stack','spectrum']),'user01':('arch',['bento','notes','story','ladder']),
      'emoji01':('type',['spectrum','bento','chat','feature']),'bday01':('photo',['comments','feature','notes']),'meme01':('type',['meme','memechat'])}
P6.PLAN.update(PLAN); P6.TONE['emoji']='d'
def build(p):
    return [finish(h,p) for h in P6.build(p)]
async def main(path,slugs):
    P=json.load(open(path)); os.makedirs(OUT,exist_ok=True)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':W,'height':H})
        for p in P:
            if slugs and p['slug'] not in slugs: continue
            for k,h in enumerate(build(p)):
                f=OUT+f"{p['slug']}_{k+1:02d}.html"; open(f,'w').write(h)
                await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(600)
                await pg.screenshot(path=OUT+f"coolbio360_{p['slug']}_{k+1:02d}.jpg",type='jpeg',quality=92)
            print(p['slug'])
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1],sys.argv[2:]))
