# Uso: python3 shot.py <screenshot.png> <handle>
# Taglia sopra il pulsante Follow (striscia blu continua > 300px), toglie il bianco attorno, porta la larghezza a 1380 e salva shots/<handle>.png
import sys, numpy as np
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB'); a=np.asarray(im).astype(int)
blue=(a[:,:,2]>220)&(a[:,:,0]<110)&(a[:,:,1]<120)
cut=a.shape[0]
for y in np.where(blue.sum(1)>300)[0]:
    row=blue[y]; best=cur=0
    for v in row:
        cur=cur+1 if v else 0; best=max(best,cur)
    if best>300: cut=y-10; break
a2=a[:cut]; nonw=a2.min(2)<235; ys=np.where(nonw.any(1))[0]; xs=np.where(nonw.any(0))[0]
box=(max(xs[0]-24,0),max(ys[0]-24,0),min(xs[-1]+24,a.shape[1]),min(ys[-1]+24,cut))
c=im.crop(box)
if c.size[0]<1380:
    W=Image.new('RGB',(1380,c.size[1]),'white'); W.paste(c,(0,0)); c=W
c.save(f'shots/{sys.argv[2]}.png'); print(sys.argv[2],c.size)
