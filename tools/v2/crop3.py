# Ritagli dalla ricerca del 6/11 (zoom Chrome): intestazione + 3 post
import glob,numpy as np
from PIL import Image
D='/tmp/claude-chrome-screenshots-owv5MH/'
def f(i): g=glob.glob(D+f'screenshot-*-{i}.png'); assert len(g)==1,(i,g); return g[0]
MAP={'bettyandbloom':(2,11),'house_of_flores_':(4,6),'bloome.x':(8,10),'floralsbyhoor':(12,13),'aprilflowers239':(14,15),
'esccandles':(16,23),'lostfond':(18,19),'spe_candle':(24,25),'wildnaturecandles':(26,27),'misneachremedies':(28,29),
'geesbeautycheltenham':(30,31),'shonaelunedbeauty':(32,33),'bymillicent_':(34,35),'homey.nailbeauty':(36,37),'by_oliviamcdonald':(38,39)}
for h,(hi,gi) in MAP.items():
    im=Image.open(f(hi)).convert('RGB')
    if im.width<900: im=im.resize((941,int(im.height*941/im.width)),Image.LANCZOS)
    a=np.asarray(im).astype(int); ink=(a.min(2)<225); rows=ink.any(1)
    # togli l'ultima riga di testo se tocca il bordo basso (tagliata)
    H=len(rows); y=H-1
    if rows[-3:].any():
        while y>0 and rows[y]: y-=1
    cut=y+1 if rows[-3:].any() else H
    ys=np.where(rows[:cut])[0]; xs=np.where(ink[:cut].any(0))[0]
    box=(max(xs[0]-28,0),max(ys[0]-24,0),min(xs[-1]+28,im.width),min(ys[-1]+20,cut))
    im.crop(box).save(f'cap/{h}_head.png')
    g=Image.open(f(gi)).convert('RGB'); s=g.width/941
    for k,(x0,x1) in enumerate([(0,290),(293,591),(594,891)]):
        g.crop((int(x0*s),0,int(x1*s),int(397*s))).save(f'cap/{h}_{k+1}.jpg',quality=92)
    print(h,box,im.size)
