# Uso: python3 shot.py <screenshot.png> <handle>  -> ritaglia il bianco attorno e salva shots/<handle>.png
import sys, numpy as np
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB'); a=np.asarray(im).astype(int)
nonw=a.min(2)<235; ys=np.where(nonw.any(1))[0]; xs=np.where(nonw.any(0))[0]
box=(max(xs[0]-24,0),max(ys[0]-24,0),min(xs[-1]+24,a.shape[1]),min(ys[-1]+24,a.shape[0]))
c=im.crop(box)
if c.size[0]<1380:
    W=Image.new('RGB',(1380,c.size[1]),'white'); W.paste(c,(0,0)); c=W
c.save(f'shots/{sys.argv[2]}.png'); print(sys.argv[2],c.size)
