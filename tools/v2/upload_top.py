# Carica le liste test fasce follower in console come "da_approvare". Uso: python3 upload_top.py [dry]
import json,subprocess,sys
K=open('/tmp/claude-0/-home-claude/53dac568-2f59-5e8d-84bd-ba9717c4f02c/scratchpad/.vcs_key').read().strip()
PLAN=[('florist02','cb069','2026-11-07 18:00'),('candle01','cb070','2026-11-08 18:00'),('nails02','cb071','2026-11-09 18:00')]
TAGS={'florist02':'#florist #floristuk #floraldesign #bouquet #weddingflowers #smallbusiness #instagrambio #bioideas',
      'candle01':'#candlemaker #soycandles #candlesuk #handpoured #smallbusinessuk #shopsmall #instagrambio #bioideas',
      'nails02':'#nailtech #nailsuk #biab #nailart #russianmanicure #beautysalon #instagrambio #bioideas'}
for slug,ide,q in PLAN:
    d=json.load(open(f'new/{slug}.json')); P=sorted(d['people'],key=lambda p:p['rank'])
    w=d['word'].lower()+('s' if not d['word'].endswith('s') else '')
    rank='\n'.join(f"{p['rank']}. @{p['h']} · {p['score']}" for p in P)
    cap=(f"The 5 best {d['word'].lower()} bios on Instagram right now {d['emoji']}\n\n{d['sub']}, all active in the last 3 weeks. Scored on 7 criteria, from the bio to the feed.\n\n"
         f"{rank}\n\n📌 Last slide: a bio template you can steal. Save it.\n\nWhich one would you follow? Tell us in the comments 👇\n\n{TAGS[slug]}")
    files=[f'out8_beams/coolbio360_{slug}_{i:02d}.jpg' for i in range(1,8)]
    imgs=[{'alt':f"The 5 best {d['word'].lower()} bios, cover"}]+[{'alt':f"No.{p['rank']} @{p['h']}, Cool Score {p['score']}",'tag':[{'username':p['h'],'x':0.5,'y':0.42}]} for p in sorted(P,key=lambda p:-p['rank'])]+[{'alt':'Steal this bio template'}]
    dati={'profilo':'coolbio360','id_esterno':ide,'stato':'da_approvare','quando':q,'caption':cap,'tema':d['word']+'s','rubrica':'Top 5','numero':'Vol. '+d['vol'],
          'immagini':imgs,'collaboratori':[P[0]['h']],'note':f"Test fascia follower: {d['band']}. Grafica nuova (fasci, accento oro, Bricolage)"}
    if sys.argv[1:]==['dry']: print(ide,q,len(files),len(cap)); print(cap[:400]); continue
    cmd=['curl','-s','-X','POST','-H','Authorization: Bearer '+K,'https://matteof141.sg-host.com/api/posts','-F','dati='+json.dumps(dati,ensure_ascii=False)]
    for f in files: cmd+=['-F','files[]=@'+f+';type=image/jpeg']
    r=subprocess.run(cmd,capture_output=True,text=True).stdout
    try: j=json.loads(r); x=j.get('post',j); print(ide,q,x.get('stato'),len(x.get('immagini') or []),x.get('errore') or j.get('errore') or '', json.dumps(j.get('controlli',''))[:200])
    except Exception: print(ide,'RISPOSTA',r[:300])
