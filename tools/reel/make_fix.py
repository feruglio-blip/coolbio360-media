# Reel "Fix this bio": bio prima, problemi evidenziati, bio riscritta che si scrive, punteggio che sale. Solo testo + musica.
# Uso: python3 make_fix.py config.json out.mp4
import asyncio, json, sys, os, subprocess, shutil
T=os.path.dirname(os.path.abspath(__file__))
FONTS='<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Hanken+Grotesk:ital,wght@0,500;0,700;1,400;1,500&display=swap" rel="stylesheet">'
def esc(s): return s.replace('&','&amp;').replace('<','&lt;')
def html(c):
    bl=''.join(f'<div class="bl" id="b{i}"><span class="mk" id="m{i}"></span><span class="tx">{esc(l)}</span></div>' for i,l in enumerate(c['before']))
    al=''.join(f'<div class="bl al" id="a{i}"></div>' for i,l in enumerate(c['after']))
    iss=''.join(f'<div class="iss" id="i{i}"><div class="x">✕</div><div><div class="il">{esc(x["label"])}</div><div class="id">{esc(x["note"])}</div></div></div>' for i,x in enumerate(c['issues']))
    dl=''.join(f'<div class="dl" id="d{i}"><span>{esc(x["k"])}</span><span class="dv">+{x["v"]:.1f}</span></div>' for i,x in enumerate(c['deltas']))
    A=c['accent']
    return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{box-sizing:border-box}} body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:linear-gradient(160deg,#1B1C1F 0%,#111726 55%,#0B1631 100%);font-family:'Hanken Grotesk',sans-serif;color:#F3EEE4}}
#frameb{{position:absolute;inset:0;border:26px solid {A}}}
#top{{position:absolute;left:80px;right:80px;top:120px}}
.kick{{font-size:24px;font-weight:700;letter-spacing:6px;color:#9A958B;display:flex;justify-content:space-between}}
.ttl{{font-family:Inter;font-weight:700;font-size:112px;line-height:.95;letter-spacing:-5px;margin-top:30px}}
.ul{{position:relative;display:inline-block}} .ul svg{{position:absolute;left:-2%;bottom:-.12em;width:104%;height:.3em;overflow:visible}}
#card{{position:absolute;left:80px;right:80px;top:560px;height:560px;background:#fff;border-radius:44px;color:#111;padding:48px 50px;box-shadow:0 40px 90px rgba(0,0,0,.55)}}
.hdr{{display:flex;align-items:center;gap:34px}}
.av{{width:150px;height:150px;border-radius:50%;padding:6px;background:conic-gradient(#F9CE34,#EE2A7B,#6228D7,#F9CE34)}}
.av div{{width:100%;height:100%;border-radius:50%;border:5px solid #fff;background:{c['avatar_bg']};display:flex;align-items:center;justify-content:center;font:700 64px Inter;color:#fff}}
.hn{{font:700 36px Inter;letter-spacing:-.5px}} .stats{{display:flex;gap:36px;margin-top:12px;font:500 25px Inter;color:#333}} .stats b{{font-weight:700;color:#111}}
.nm{{font:700 30px Inter;margin-top:34px}}
#bio{{position:relative;margin-top:10px}}
.bl{{position:relative;font:400 34px/1.42 Inter;color:#111;white-space:nowrap}}
.mk{{position:absolute;left:-8px;top:6px;height:38px;width:0;background:rgba(255,92,92,.28);border-radius:6px}}
.al{{position:absolute;left:0;opacity:1}}
.cur{{display:inline-block;width:3px;height:36px;background:#111;vertical-align:-5px;margin-left:2px}}
#lab{{position:absolute;top:-30px;left:50px;font:700 22px Inter;letter-spacing:5px;padding:12px 22px;color:#fff;background:#6B6B6B}}
#score{{position:absolute;top:-58px;right:40px;width:172px;height:172px;border-radius:50%;background:#0B1631;border:6px solid #FF5C5C;display:flex;flex-direction:column;align-items:center;justify-content:center}}
#sv{{font:800 64px Inter;letter-spacing:-3px;line-height:1;color:#F3EEE4}} .sl{{font:700 15px Inter;letter-spacing:4px;color:#9A958B;margin-top:6px}}
#below{{position:absolute;left:80px;right:80px;top:1270px}}
.iss{{position:absolute;left:0;right:0;display:flex;gap:24px;align-items:flex-start;opacity:0}}
.x{{flex:none;width:52px;height:52px;border-radius:50%;background:#FF5C5C;color:#0B1631;font:800 26px Inter;display:flex;align-items:center;justify-content:center;margin-top:4px}}
.il{{font:700 40px Inter;letter-spacing:-1px}} .id{{font-style:italic;font-size:32px;color:#C9C3B7;margin-top:6px}}
.dl{{position:absolute;left:0;right:0;display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid rgba(243,238,228,.15);padding:18px 0;font:600 40px Inter;opacity:0}}
.dv{{font:800 48px Inter;color:{A}}}
#end{{position:absolute;left:80px;right:80px;top:640px;opacity:0}}
.e1{{font-family:Inter;font-weight:700;font-size:150px;line-height:.95;letter-spacing:-6px}} .e2{{font-style:italic;font-size:58px;color:#D9D3C7;margin-top:30px}}
.btn{{display:inline-block;margin-top:90px;background:#F3EEE4;color:#0B1631;font-weight:700;letter-spacing:6px;font-size:34px;padding:26px 44px}}
#logo{{position:absolute;left:80px;bottom:90px;display:flex;align-items:center;gap:16px;font:800 40px Inter;letter-spacing:-1.5px}}
#ex{{position:absolute;right:80px;bottom:104px;font:700 18px Inter;letter-spacing:4px;color:#6F6A61}}
</style></head><body><div id="frameb"></div>
<div id="top"><div class="kick" id="k"><span>FIX THIS BIO</span><span>{esc(c['episode'])}</span></div>
<div class="ttl" id="tt">{esc(c['line1'])}<br><span class="ul">{esc(c['line2'])}<svg viewBox="0 0 300 40" preserveAspectRatio="none"><path id="u1" d="M6 24 C 50 14, 110 20, 160 17 S 250 12, 294 19" fill="none" stroke="{A}" stroke-width="16" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/><path id="u2" d="M22 30 C 90 22, 170 27, 284 23" fill="none" stroke="{A}" stroke-width="8" stroke-linecap="round" opacity=".9" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg></span></div></div>
<div id="card"><div id="lab">BEFORE</div><div id="score"><div id="sv">0.0</div><div class="sl">COOL SCORE</div></div>
<div class="hdr"><div class="av"><div>{esc(c['initial'])}</div></div><div><div class="hn">{esc(c['handle'])}</div><div class="stats"><span><b>{c['stats'][0]}</b> posts</span><span><b>{c['stats'][1]}</b> followers</span><span><b>{c['stats'][2]}</b> following</span></div></div></div>
<div class="nm">{esc(c['name'])}</div><div id="bio"><div id="bb">{bl}</div><div id="ab">{al}</div></div></div>
<div id="below">{iss}{dl}</div>
<div id="end"><div class="e1">Want yours<br>fixed?</div><div class="e2">{esc(c['end2'])}</div><div class="btn">FOLLOW @COOLBIO360</div></div>
<div id="logo"><img src="file://{T}/../assets/logo-coolbio360-trasparente.svg" style="width:62px;height:62px">coolbio·360</div>
<div id="ex">{esc(c.get('footnote',''))}</div>
<script>
const C={json.dumps(c)};
const cl=(x,a,b)=>Math.max(a,Math.min(b,x)); const ease=x=>1-Math.pow(1-cl(x,0,1),3); const io=x=>{{x=cl(x,0,1);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}};
const $=id=>document.getElementById(id);
const AF=C.after.map(s=>Array.from(s)); const tot=AF.reduce((a,b)=>a+b.length,0);
// posizioni verticali delle righe dopo
C.after.forEach((s,i)=>{{$('a'+i).style.top=(i*48)+'px'}});
const BL=Array.from(document.querySelectorAll('#bb .tx')).map(e=>e.offsetWidth);
function setT(t){{
 $('k').style.opacity=ease(t/.6);
 $('tt').style.opacity=ease((t-.2)/.6); $('tt').style.transform=`translateY(${{(1-ease((t-.2)/.6))*40}}px)`;
 $('u1').style.strokeDashoffset=1-io((t-.9)/.6); $('u2').style.strokeDashoffset=1-io((t-1.3)/.5);
 const ck=ease((t-.6)/.9); const out=io((t-22.0)/.8);
 $('card').style.opacity=ck*(1-out); $('card').style.transform=`translateY(${{(1-ck)*140-out*80}}px)`;
 // punteggio
 const s0=C.score_before, s1=C.score_after;
 let v=s0*ease((t-1.4)/1.2); if(t>17.4) v=s0+(s1-s0)*io((t-17.4)/1.6);
 $('sv').textContent=v.toFixed(1);
 const up=cl((t-17.4)/1.6,0,1); $('score').style.borderColor=up>.5?C.accent:'#FF5C5C';
 $('score').style.transform=`scale(${{1+Math.sin(cl((t-19.0)/.5,0,1)*Math.PI)*.12}})`;
 // problemi: evidenzia la riga e mostra la nota (uno alla volta)
 const w=[3.5,6.3,9.1];
 C.issues.forEach((x,i)=>{{const a=ease((t-w[i])/.5)*(1-ease((t-(w[i]+2.3))/.4)); const el=$('i'+i); el.style.opacity=a; el.style.transform=`translateY(${{(1-ease((t-w[i])/.5))*30}}px)`;
   x.lines.forEach(l=>{{const m=$('m'+l); const k=ease((t-w[i]-.1)/.4); const cur=parseFloat(m.dataset.k||0); m.style.width=Math.max(BL[l]+16)*(t<11.8?Math.max(k,0):0)+'px';}});}});
 // prima sparisce, dopo si scrive
 const fade=ease((t-11.6)/.4); $('bb').style.opacity=1-fade;
 const lab=$('lab'); if(t>11.9){{lab.textContent='AFTER'; lab.style.background=C.accent; lab.style.color='#0B1631'}} else {{lab.textContent='BEFORE'; lab.style.background='#6B6B6B'; lab.style.color='#fff'}}
 const n=Math.floor(tot*cl((t-12.2)/5.0,0,1)); let r=n;
 AF.forEach((ch,i)=>{{const k=Math.min(r,ch.length); r-=k; $('a'+i).innerHTML=ch.slice(0,k).join('').replace(/&/g,'&amp;').replace(/</g,'&lt;')+((k>0&&k<ch.length)||(i==AF.length-1&&k==ch.length&&n<tot)?'<span class="cur"></span>':'')+(k==ch.length&&i==AF.length-1&&t<17.6&&Math.floor(t*2)%2==0?'<span class="cur"></span>':'')}});
 // guadagni
 C.deltas.forEach((x,i)=>{{const st=17.8+i*.7; const el=$('d'+i); el.style.opacity=ease((t-st)/.4)*(1-out); el.style.top=(i*104)+'px'; el.style.transform=`translateX(${{(1-ease((t-st)/.4))*-40}}px)`;}});
 $('top').style.opacity=1-out;
 const e=$('end'); const ek=ease((t-22.5)/.8); e.style.opacity=ek; e.style.transform=`translateY(${{(1-ek)*60}}px)`;
}}
</script></body></html>'''
async def main(cfgp,outp):
    from playwright.async_api import async_playwright
    cfg=json.load(open(cfgp)); fps=cfg.get('fps',30); dur=cfg.get('dur',26)
    hp='/tmp/fix.html'; open(hp,'w').write(html(cfg))
    fr='/tmp/fix_frames'; shutil.rmtree(fr,ignore_errors=True); os.makedirs(fr)
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+hp); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(1500)
        only=os.environ.get('FRAMES')
        ts=[float(x) for x in only.split(',')] if only else [f/fps for f in range(int(fps*dur))]
        for f,t in enumerate(ts):
            await pg.evaluate(f'setT({t})')
            await pg.screenshot(path=f'{fr}/{f:05d}.jpg',type='jpeg',quality=90)
        await b.close()
    if os.environ.get('FRAMES'): print(fr); return
    cmd=['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',f'{fr}/%05d.jpg']
    if cfg.get('audio'): cmd+=['-i',cfg['audio'],'-shortest','-c:a','aac','-b:a','192k','-af',f"afade=t=in:d=0.3,afade=t=out:st={dur-1.5}:d=1.5"]
    cmd+=['-c:v','libx264','-pix_fmt','yuv420p','-profile:v','high','-crf','18','-movflags','+faststart',outp]
    subprocess.run(cmd,check=True)
if __name__=='__main__': asyncio.run(main(sys.argv[1],sys.argv[2]))
