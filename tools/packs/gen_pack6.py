# coolbio360 pacchetti v6: gradiente panoramico unico che attraversa tutte le slide (tagliato a 1080 per slide),
# numeri Instrument Serif corsivo, titoli Archivo espanso, niente barre di avanzamento, niente numeri nei cerchi.
# Uso: python3 gen_pack6.py packs.json [slug...]   output in out6/
import json,sys,os,asyncio,random
import gen6_base as V, gen6_layouts as L5
B=os.path.dirname(os.path.abspath(__file__)); OUT=B+'/out6/'
W,H,NAVY,CREAM=V.W,V.H,V.NAVY,V.CREAM
CTX={}
TONE={'stack':'d','chat':'d','split':'d','notes':'d','memechat':'d','story':'d','comments':'d','end':'d','arch':'d','photo':'d',
      'feature':'l','bento':'l','spectrum':'l','meme':'l','ladder':'a','type':'a','end_color':'a'}
def panorama():
    p,i,n,tones=CTX['p'],CTX['i'],CTX['n'],CTX['tones']; A,A2=p['accent'],p['A2']; hues=p['hues']
    col={'d':NAVY,'l':CREAM,'a':A}
    stops=[]
    for k,t in enumerate(tones):
        c=col[t]; stops+= [f'{c} {k*W+W*.3:.0f}px',f'{c} {k*W+W*.7:.0f}px']
    base=f'linear-gradient(90deg,{",".join(stops)})'
    rnd=random.Random(p['slug']); blobs=''
    for k in range(n+1):            # una macchia grande su ogni confine + una dentro ogni slide
        for j,(x,y,r) in enumerate([(k*W+rnd.randint(-120,120),rnd.randint(150,1200),rnd.randint(380,560)),(k*W+W/2+rnd.randint(-250,250),rnd.choice([rnd.randint(-100,250),rnd.randint(1050,1400)]),rnd.randint(260,420))]):
            if k==n and j==1: continue
            c=hues[(k*2+j)%len(hues)]; t=tones[min(max(int(x//W),0),n-1)]
            op={'d':.85,'l':.55,'a':.6}[t]
            blobs+=f'<div style="position:absolute;left:{x-r:.0f}px;top:{y-r:.0f}px;width:{2*r}px;height:{2*r}px;border-radius:50%;background:radial-gradient(circle,{c} 0%,{c}cc 25%,{c}55 50%,transparent 70%);opacity:{op};filter:blur(30px)"></div>'
    return f'<div style="position:absolute;top:0;left:{-(i-1)*W}px;width:{n*W}px;height:{H}px;background:{base};z-index:0">{blobs}</div>'
def page(body,bg):
    pan=panorama() if CTX else ''
    return f'<!doctype html><html><head><meta charset="utf-8">{V.FONTS}<style>{V.CSS}</style></head><body><div class="s" style="background:{NAVY};--sh:{CTX["p"]["A2"] if CTX else NAVY}">{pan}{body}</div></body></html>'
for M_ in (V,L5):
    M_.page=page; M_.orbs=lambda *a,**k:''; M_.progress=lambda *a,**k:''
PLAN={'winter01':('photo',['chat','stack','spectrum']),'user01':('arch',['bento','notes','story','ladder']),
      'emoji01':('type',['spectrum','bento','chat','feature']),'bday01':('arch',['comments','feature','notes']),'meme01':('type',['meme','memechat'])}
def build(p):
    img=V.uri(p['bg']); sl=p['slides']; n=len(sl)+2; cv,seq=PLAN[p['slug']]
    endk='end_color' if cv=='type' else 'end'
    tones=[TONE[cv]]+[TONE[x] for x in seq]+[TONE[endk]]
    names=[cv]+seq+[endk]; pages=[]
    for i,name in enumerate(names,1):
        CTX.update(p=p,i=i,n=n,tones=tones)
        if i==1: h=L5.COVERS[cv](p,n,img)
        elif i==n: h=(L5.end_color if endk=='end_color' else V.end)(p,n,img)
        else: h=L5.L[name](p,sl[i-2],i,n,img)
        pages.append(h)
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
