import sys,glob
from PIL import Image
S='/tmp/claude-0/-home-claude/53dac568-2f59-5e8d-84bd-ba9717c4f02c/scratchpad/'
d,tag=sys.argv[1],sys.argv[2]
for slug in sys.argv[3:]:
    fs=sorted(glob.glob(f'{d}/coolbio360_{slug}_*.jpg'))
    ims=[Image.open(f).resize((432,540)) for f in fs]
    c=Image.new('RGB',(432*len(ims),540));[c.paste(im,(i*432,0)) for i,im in enumerate(ims)];c.save(S+f'{tag}_{slug}.jpg',quality=85)
