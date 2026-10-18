import glob,re,numpy as np
from PIL import Image
D='/tmp/claude-chrome-screenshots-vpeKgh/'
S=1568/1047
def f(i): 
    g=glob.glob(D+f'screenshot-*-{i}.png'); assert len(g)==1,(i,g); return g[0]
def maxrun(row):
    best=cur=0
    for v in row:
        cur=cur+1 if v else 0; best=max(best,cur)
    return best
for line in open('map.txt'):
    p=line.split()
    if len(p)<4: continue
    h,ti,gi=p[0],int(p[1]),int(p[2])
    m=re.search(r'top(\d+)',line); top=int(m.group(1)) if m else 400
    rtop=400 if gi in (3,5,7,9,11) else 380
    # header
    im=Image.open(f(ti)).convert('RGB'); a=np.asarray(im).astype(int)
    blue=(a[:,:,2]>220)&(a[:,:,0]<110)&(a[:,:,1]<120)
    cut=None
    for y in np.where(blue.sum(1)>300)[0]:
        if maxrun(blue[y])>300: cut=y-14; break
    if cut is None: cut=a.shape[0]
    nonw=(a[:cut].min(2)<235); ys=np.where(nonw.any(1))[0]; xs=np.where(nonw.any(0))[0]
    box=(max(xs[0]-24,0),max(ys[0]-24,0),min(xs[-1]+24,a.shape[1]),min(ys[-1]+24,cut))
    im.crop(box).save(f'cap/{h}_head.png')
    g=Image.open(f(gi)).convert('RGB')
    skip=1 if 'tile1blank' in line else 0
    for k in range(3):
        c=k+skip; x0=c*262*S; y0=max(0,(top-rtop)*S)
        g.crop((round(x0),round(y0),round(x0+261*S),round((top-rtop)*S+348*S))).save(f'cap/{h}_{k+1}.jpg',quality=92)
    print(h,box,top-rtop)
