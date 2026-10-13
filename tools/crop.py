from PIL import Image
import numpy as np, glob, sys
D='/tmp/claude-chrome-screenshots-fQ1X8e/'
def maxrun(row):
    best=cur=0
    for v in row:
        cur=cur+1 if v else 0; best=max(best,cur)
    return best
changed=[]
for line in open('gen/shots_map.txt'):
    p=line.split()
    if p[3]=='?': continue
    slug,h,f,idx,score=p
    fs=glob.glob(D+'screenshot-*-%s.png'%idx)
    im=Image.open(fs[0]).convert('RGB'); a=np.asarray(im).astype(int)
    blue=(a[:,:,2]>220)&(a[:,:,0]<110)&(a[:,:,1]<120)
    cand=np.where(blue.sum(1)>300)[0]
    cut=None
    for y in cand:
        if maxrun(blue[y])>300: cut=y-8; break
    nonw=(a[:cut].min(2)<235); ys=np.where(nonw.any(1))[0]; xs=np.where(nonw.any(0))[0]
    box=(max(xs[0]-24,0),max(ys[0]-24,0),min(xs[-1]+24,a.shape[1]),min(ys[-1]+24,cut))
    old=Image.open('cb/shots/'+h+'.png').size
    im.crop(box).save('cb/shots/'+h+'.png')
    new=(box[2]-box[0],box[3]-box[1])
    if old!=new: changed.append((slug,h,old,new))
for c in changed: print(c)
