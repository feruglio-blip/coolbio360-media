# Caroselli "guide" (tips) di coolbio·360. Uso: python3 tools/gen_guide.py score01
import asyncio, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import *

def pts_badge(n,A): return f'<div style="background:{A};color:#0B1631;padding:10px 22px;font-size:26px;font-weight:700;letter-spacing:5px">{n} PTS</div>'
def bullets(items,A):
    return ''.join(f'<div style="display:flex;gap:20px;align-items:baseline;padding:18px 0;border-bottom:1px solid rgba(243,238,228,0.12);font-size:34px;line-height:1.3"><div style="color:{A};font-weight:700;min-width:34px">{s}</div><div>{t}</div></div>' for s,t in items)

def g_cover(c):
    A=c['accent']
    inner=f'''<div style="display:flex;justify-content:space-between;margin-top:18px;font-size:20px;font-weight:700;letter-spacing:4px;color:#9A958B"><div>THE BIO ISSUE</div><div>{c['kicker']}</div></div>
<div style="margin-top:80px;display:flex;align-items:flex-end;justify-content:space-between"><div style="background:{A};color:#0B1631;padding:10px 22px;font-size:26px;font-weight:700;letter-spacing:6px">THE GUIDE</div>{emobox(c['emoji'],190,180,130,10,A)}</div>
<div style="margin-top:30px;font-family:'Inter',sans-serif;font-weight:700;font-size:150px;line-height:0.95;letter-spacing:-6px">{c['t1']}</div>
<div style="font-family:'Inter',sans-serif;font-weight:700;font-size:150px;line-height:0.95;letter-spacing:-6px">{hand(c['t2'],A)}</div>
<div style="font-family:'Hanken Grotesk';font-style:italic;font-size:80px;line-height:1.1;color:#D9D3C7;margin-top:30px">{c['t3']}</div>
<div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid rgba(243,238,228,0.85);padding-top:24px"><div style="font-size:31px;font-weight:500;line-height:1.4;max-width:640px;color:#D9D3C7">{c['sub']}</div><div style="font-size:24px;font-weight:700;letter-spacing:5px">SWIPE →</div></div>'''
    return wrap(A,inner,48)

def g_overview(c):
    A=c['accent']
    rows=''.join(f'''<div style="display:flex;align-items:center;gap:28px;padding:26px 0;border-bottom:1px solid rgba(243,238,228,0.14)">
<div style="font-family:'Inter',sans-serif;font-weight:300;font-size:110px;line-height:0.8;width:90px">{p}</div>
<div style="flex:1"><div style="font-family:'Inter',sans-serif;font-weight:700;font-size:48px;letter-spacing:-1.5px">{n}</div><div style="font-size:28px;color:#9A958B;margin-top:6px">{q}</div></div>
<div style="display:flex;gap:8px">{''.join(f'<div style="width:26px;height:26px;background:{A if i<int(p) else "rgba(243,238,228,0.14)"}"></div>' for i in range(3))}</div></div>''' for p,n,q in c['criteria'])
    inner=header(f"THE GUIDE · {c['tag']}")+f'''<div style="margin-top:50px;{LBL}">THE COOL SCORE</div>
<div style="font-family:'Inter',sans-serif;font-weight:700;font-size:96px;line-height:0.95;letter-spacing:-4px;margin-top:14px">Four things.<br>Ten points.</div>
<div style="margin-top:40px;border-top:1px solid rgba(243,238,228,0.35)">{rows}</div>
{verdict(c['overview_line'],40)}{footer('HOW WE SCORE','SWIPE →')}'''
    return wrap(A,inner)

def g_criterion(c,k,i,n):
    A=c['accent']
    inner=header(f"THE GUIDE · {c['tag']} · {i} / {n}")+f'''<div style="display:flex;align-items:flex-end;justify-content:space-between;margin-top:40px">
<div><div style="{LBL}">CRITERION 0{i}</div><div style="font-family:'Inter',sans-serif;font-weight:700;font-size:110px;line-height:0.95;letter-spacing:-5px;margin-top:10px">{k['name']}</div></div>{pts_badge(k['pts'],A)}</div>
<div style="font-family:'Hanken Grotesk';font-style:italic;font-size:46px;line-height:1.2;color:#E9E3D7;margin-top:22px">{k['question']}</div>
<div style="margin-top:28px;border-top:1px solid rgba(243,238,228,0.35)">{bullets(k['rules'],A)}</div>
<div style="margin-top:30px;font-size:18px;font-weight:700;letter-spacing:4px;color:#9A958B">FULL MARKS · @{k['h'].upper()}</div>
<div style="margin-top:14px;background:#FFFFFF;border-radius:18px;padding:18px;box-shadow:0 30px 60px rgba(0,0,0,0.45);display:flex;justify-content:center"><img src="file://{T}/shots/{k['h']}.png" style="display:block;max-width:100%;max-height:360px;height:auto"></div>
{footer(k['why'],'NEXT →')}'''
    return wrap(A,inner)

def g_end(c):
    A=c['accent']
    inner=header(f"THE GUIDE · {c['tag']}")+f'''<div style="margin-top:70px;font-family:'Inter',sans-serif;font-weight:700;font-size:120px;line-height:0.95;letter-spacing:-5px">Score your<br>own bio.</div>
<div style="margin-top:22px;font-family:'Hanken Grotesk';font-style:italic;font-size:50px;line-height:1.15;color:#D9D3C7">{c['end_line']}</div>
<div style="margin-top:50px;border-top:1px solid rgba(243,238,228,0.35)">{bullets([("☐",x) for x in c['checklist']],A)}</div>
<div style="margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between"><div style="font-size:30px;line-height:1.35;max-width:560px;color:#D9D3C7">Want our verdict? <b style="color:#F3EEE4">DM us your @</b> and we rate it.</div>
<div style="background:#F3EEE4;color:#0B1631;padding:18px 34px;font-size:24px;font-weight:700;letter-spacing:4px">SAVE THIS POST</div></div>'''
    return wrap(A,inner,48)

async def main(slugs):
    from playwright.async_api import async_playwright
    data=json.load(open(T+'/data/guides.json'))
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for c in data:
            if slugs and c['slug'] not in slugs: continue
            n=len(c['criteria_detail'])
            slides=[g_cover(c),g_overview(c)]+[g_criterion(c,k,i,n) for i,k in enumerate(c['criteria_detail'],1)]+[g_end(c)]
            os.makedirs(T+'/out',exist_ok=True)
            for i,h in enumerate(slides,1):
                hp=f"/tmp/cbg_{c['slug']}_{i}.html"; open(hp,'w').write(h)
                await pg.goto('file://'+hp); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(800)
                await pg.screenshot(path=f"{T}/out/coolbio360_{c['slug']}_{i:02d}.jpg",type='jpeg',quality=92,clip={'x':0,'y':0,'width':1080,'height':1350})
        await b.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1:]))
