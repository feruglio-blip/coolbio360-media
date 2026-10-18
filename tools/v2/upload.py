import json,subprocess,sys,os
SP='/tmp/claude-0/-home-claude/53dac568-2f59-5e8d-84bd-ba9717c4f02c/scratchpad/'
K=open(SP+'.vcs_key').read().strip()
CAL={e['immagini'][0].split('/')[-2]:e for e in json.load(open('/home/claude/coolbio360-media/calendario_coolbio360.json'))}
order=['petsit01','baker01','lash01','bar01','cookie01','massage01','truck01','embroid01','cart01','balloon01','vintage01']
days=['2026-10-%d'%d for d in range(19,30)]
posts=[]
n=40
for slug,day in zip(order,days):
    d=json.load(open(f'new/{slug}.json')); e=CAL[slug]
    cap=e['didascalia'].replace(', ranked by our editors.','. Scored on 7 criteria, from the bio to the feed.')
    cap=cap.replace('\n\nWhich one is your favourite?','\n\n📌 Last slide: a bio template you can steal. Save it.\n\nWhich one is your favourite?')
    assert 'Scored on 7' in cap and '📌' in cap, slug
    ppl=sorted(d['people'],key=lambda p:-p['rank'])
    imgs=[{'alt':f"The 5 best {d['word'].lower()} bios, cover"}]+[{'alt':f"No.{p['rank']} @{p['h']}, Cool Score {p['score']}",'tag':[{'username':p['h'],'x':0.5,'y':0.42}]} for p in ppl]+[{'alt':'Steal this bio template'}]
    files=[f'out/coolbio360_{slug}_{i:02d}.jpg' for i in range(1,8)]
    no1=[p['h'] for p in ppl if p['rank']==1][0]
    posts.append(dict(id=f'cb{n:03d}',quando=day+' 12:00',caption=cap,tema=e['tema'],rubrica='Top 5',numero='Vol. '+d['vol'],collaboratori=[no1],immagini=imgs,files=files)); n+=1
EP={1:('Office worker',SP+'finali/ep1/bios_%d.jpg','2026-10-19 21:00'),2:('University student',SP+'finali/ep2/leo_%d.jpg','2026-10-20 21:00')}
CAPS=json.load(open('caps_bios.json'))
for ep,(tema,pat,q) in EP.items():
    posts.append(dict(id=f'cb{n:03d}',quando=q,caption=CAPS[str(ep)],tema=tema,rubrica='One Person, Four Bios',numero='Ep. %02d'%ep,collaboratori=[],immagini=[{'alt':f'One Person, Four Bios episode {ep}, slide {i+1}'} for i in range(6)],files=[pat%i for i in range(6)])); n+=1
if sys.argv[1:]==['dry']:
    for p in posts: print(p['id'],p['quando'],p['tema'],p['numero'],len(p['files']),p['collaboratori'],len(p['caption']))
    sys.exit()
for p in posts:
    dati={'profilo':'coolbio360','id_esterno':p['id'],'stato':'programmato','quando':p['quando'],'caption':p['caption'],'tema':p['tema'],'rubrica':p['rubrica'],'numero':p['numero'],'immagini':p['immagini']}
    if p['collaboratori']: dati['collaboratori']=p['collaboratori']
    cmd=['curl','-s','-X','POST','-H','Authorization: Bearer '+K,'https://matteof141.sg-host.com/api/posts','-F','dati='+json.dumps(dati,ensure_ascii=False)]
    for f in p['files']: cmd+=['-F','files[]=@'+f+';type=image/jpeg']
    r=subprocess.run(cmd,capture_output=True,text=True).stdout
    try:
        j=json.loads(r); x=j.get('post',j); print(p['id'],p['quando'],x.get('stato'),x.get('id'),len(x.get('immagini') or []),x.get('errore') or j.get('errore') or '')
    except Exception: print(p['id'],'RISPOSTA',r[:300])
