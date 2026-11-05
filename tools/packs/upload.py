# Programma i pacchetti nella console Very Content Studio. Uso: python3 upload.py [dry]
import json,subprocess,sys,glob,os
B=os.path.dirname(os.path.abspath(__file__))
K=open('/tmp/claude-0/-home-claude/53dac568-2f59-5e8d-84bd-ba9717c4f02c/scratchpad/.vcs_key').read().strip()
PLAN=[('winter01','cb059','2026-11-06 12:00'),('user01','cb060','2026-11-07 12:00'),('emoji01','cb061','2026-11-08 12:00'),('bday01','cb062','2026-11-09 12:00'),('meme01','cb063','2026-11-10 12:00')]
P={p['slug']:p for p in json.load(open(B+'/packs.json'))}
for slug,ide,q in PLAN:
    p=P[slug]; files=sorted(glob.glob(f'{B}/out/coolbio360_{slug}_*.jpg'))
    title=p['title'].replace('<br>',' ')
    imgs=[{'alt':f'{title}, cover'}]+[{'alt':f"{title}: {s['h']}"} for s in p['slides']]+[{'alt':'Save it and send it to a friend'}]
    assert len(imgs)==len(files),slug
    dati={'profilo':'coolbio360','id_esterno':ide,'stato':'programmato','quando':q,'caption':p['caption'],'tema':p['tema'],
          'rubrica':'Bio translator' if slug.startswith('meme') else 'Copy & Paste','numero':slug,'immagini':imgs,
          'note':'Nuova direzione 6/11: contenuti da copiare su foto aesthetic'}
    if sys.argv[1:]==['dry']: print(ide,q,slug,len(files),len(p['caption'])); continue
    cmd=['curl','-s','-X','POST','-H','Authorization: Bearer '+K,'https://matteof141.sg-host.com/api/posts','-F','dati='+json.dumps(dati,ensure_ascii=False)]
    for f in files: cmd+=['-F','files[]=@'+f+';type=image/jpeg']
    r=subprocess.run(cmd,capture_output=True,text=True).stdout
    try:
        j=json.loads(r); x=j.get('post',j); print(ide,q,x.get('stato'),len(x.get('immagini') or []),x.get('errore') or j.get('errore') or '')
    except Exception: print(ide,'RISPOSTA',r[:300])
