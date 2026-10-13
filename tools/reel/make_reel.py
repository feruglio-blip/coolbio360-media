# Reel "Winners of the Month": 3 telefoni a bouquet con i profili che scorrono. Uso: python3 make_reel.py config.json out.mp4
import asyncio, json, sys, os, subprocess, shutil
T=os.path.dirname(os.path.abspath(__file__))
FONTS='<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Hanken+Grotesk:ital,wght@0,500;0,700;1,400;1,500&display=swap" rel="stylesheet">'
def html(cfg):
    ph=''
    for i,p in enumerate(cfg['phones']):
        ph+=f'''<div class="ph" id="ph{i}"><div class="frame"><div class="scr"><img id="im{i}" src="file://{T}/{p['screen']}"><div class="status"><span>9:41</span><span>●●● ▮</span></div><div class="nav">⌂ &nbsp; ⌕ &nbsp; ⊕ &nbsp; ▷ &nbsp; ◯</div></div><div class="island"></div></div>
</div>'''
        tags=''.join(f'''<div class="tagp" id="tg{i}"><div class="cat" style="background:{p['accent']}">{p['cat']}</div><div class="sc"><span id="sc{i}">0.0</span></div><div class="hd">@{p['h']}</div></div>''' for i,p in enumerate(cfg['phones']))
    return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{box-sizing:border-box}} body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:linear-gradient(160deg,#1B1C1F 0%,#111726 55%,#0B1631 100%);font-family:'Hanken Grotesk',sans-serif;color:#F3EEE4}}
#frameb{{position:absolute;inset:0;border:26px solid {cfg['accent']}}}
#top{{position:absolute;left:80px;right:80px;top:120px}}
.kick{{font-size:24px;font-weight:700;letter-spacing:6px;color:#9A958B;display:flex;justify-content:space-between}}
.ttl{{font-family:Inter;font-weight:700;font-size:118px;line-height:.95;letter-spacing:-5px;margin-top:34px}}
.ul{{position:relative;display:inline-block}} .ul svg{{position:absolute;left:-2%;bottom:-.12em;width:104%;height:.3em;overflow:visible}}
.ph{{position:absolute;top:500px;width:420px;left:330px;transform-origin:50% 100%}}
.frame{{position:relative;width:420px;height:880px;border-radius:62px;background:#0d0d0f;padding:13px;box-shadow:0 0 0 3px #c9c6bf,0 40px 80px rgba(0,0,0,.6)}}
.scr{{position:relative;width:100%;height:100%;border-radius:50px;overflow:hidden;background:#fff}}
.scr img{{position:absolute;left:0;top:0;width:100%}}
.island{{position:absolute;top:28px;left:50%;width:110px;height:32px;margin-left:-55px;background:#000;border-radius:20px}}
.status{{position:absolute;top:0;left:0;right:0;height:62px;background:#fff;color:#000;font:600 17px Inter;display:flex;justify-content:space-between;align-items:center;padding:8px 34px 0}}
.nav{{position:absolute;bottom:0;left:0;right:0;height:64px;background:#fff;border-top:1px solid #ddd;color:#000;font-size:24px;display:flex;justify-content:center;align-items:center}}
#tags{{position:absolute;left:60px;right:60px;top:1470px;display:flex;justify-content:space-between}} .tagp{{width:310px;text-align:center}} .cat{{display:inline-block;color:#0B1631;font-weight:700;letter-spacing:5px;font-size:20px;padding:7px 16px}}
.sc{{font-family:Inter;font-weight:700;font-size:72px;letter-spacing:-3px;margin-top:10px;line-height:1}} .hd{{font-size:19px;font-weight:700;letter-spacing:2px;color:#9A958B;margin-top:8px}}
#end{{position:absolute;left:80px;right:80px;top:640px;opacity:0}}
.e1{{font-family:Inter;font-weight:700;font-size:150px;line-height:.95;letter-spacing:-6px}} .e2{{font-style:italic;font-size:60px;color:#D9D3C7;margin-top:30px}}
.btn{{display:inline-block;margin-top:90px;background:#F3EEE4;color:#0B1631;font-weight:700;letter-spacing:6px;font-size:34px;padding:26px 44px}}
#logo{{position:absolute;left:80px;bottom:90px;display:flex;align-items:center;gap:16px;font:800 40px Inter;letter-spacing:-1.5px}}
</style></head><body><div id="frameb"></div>
<div id="top"><div class="kick" id="k"><span>THE WINNERS</span><span>{cfg['month'].upper()}</span></div>
<div class="ttl" id="tt">{cfg['line1']}<br><span class="ul">{cfg['line2']}<svg viewBox="0 0 300 40" preserveAspectRatio="none"><path id="u1" d="M6 24 C 50 14, 110 20, 160 17 S 250 12, 294 19" fill="none" stroke="{cfg['accent']}" stroke-width="16" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/><path id="u2" d="M22 30 C 90 22, 170 27, 284 23" fill="none" stroke="{cfg['accent']}" stroke-width="8" stroke-linecap="round" opacity=".9" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg></span></div></div>
{ph}
<div id="tags">{tags}</div>
<div id="end"><div class="e1">Is your<br>bio next?</div><div class="e2">DM us your @. Next month it could be you.</div><div class="btn">FOLLOW @COOLBIO360</div></div>
<div id="logo"><img src="file://{T}/../assets/logo-coolbio360-trasparente.svg" style="width:62px;height:62px">coolbio·360</div>
<script>
const P={json.dumps(cfg['phones'])};
const cl=(x,a,b)=>Math.max(a,Math.min(b,x)); const ease=x=>1-Math.pow(1-cl(x,0,1),3); const io=x=>{{x=cl(x,0,1);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}};
const pose=[{{x:-262,r:-10,s:.84,z:1}},{{x:0,r:0,s:1,z:3}},{{x:262,r:10,s:.84,z:2}}];
function setT(t){{
 document.getElementById('k').style.opacity=ease(t/0.6);
 const tt=document.getElementById('tt'); tt.style.opacity=ease((t-.2)/.6); tt.style.transform=`translateY(${{(1-ease((t-.2)/.6))*40}}px)`;
 document.getElementById('u1').style.strokeDashoffset=1-io((t-.9)/.6); document.getElementById('u2').style.strokeDashoffset=1-io((t-1.3)/.5);
 const out=io((t-10.2)/.9);
 P.forEach((p,i)=>{{const el=document.getElementById('ph'+i); const st=.7+[0.25,0,0.5][i]; const k=ease((t-st)/.9);
  const q=pose[i]; const fl=Math.sin((t+i)*1.4)*8;
  el.style.zIndex=q.z; el.style.opacity=k*(1-out);
  el.style.transform=`translateX(${{q.x*k}}px) translateY(${{(1-k)*900+fl+out*120}}px) rotate(${{q.r*k}}deg) scale(${{q.s*(1-out*.15)}})`;
  const im=document.getElementById('im'+i); const H=im.naturalHeight*(394/1080); const max=Math.max(0,H-854+64);
  const sp=io((t-2.4-i*.3)/6.2); im.style.transform=`translateY(${{-sp*max}}px)`;
  const s=document.getElementById('sc'+i); const v=p.score*ease((t-2.6-i*.35)/1.6); s.textContent=v.toFixed(1);
  const tg=document.getElementById('tg'+i); tg.style.opacity=ease((t-2.2-i*.35)/.6)*(1-out);}});
 const e=document.getElementById('end'); const ek=ease((t-10.6)/.8); e.style.opacity=ek; e.style.transform=`translateY(${{(1-ek)*60}}px)`;
 document.getElementById('top').style.opacity=1-out;
}}
</script></body></html>'''
async def main(cfgp,outp):
    from playwright.async_api import async_playwright
    cfg=json.load(open(cfgp)); fps=cfg.get('fps',30); dur=cfg.get('dur',13.5)
    hp='/tmp/reel.html'; open(hp,'w').write(html(cfg))
    fr='/tmp/reel_frames'; shutil.rmtree(fr,ignore_errors=True); os.makedirs(fr)
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+hp); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(1500)
        n=int(fps*dur)
        for f in range(n):
            await pg.evaluate(f'setT({f/fps})')
            await pg.screenshot(path=f'{fr}/{f:05d}.jpg',type='jpeg',quality=90)
        await b.close()
    cmd=['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',f'{fr}/%05d.jpg']
    if cfg.get('audio'): cmd+=['-i',cfg['audio'],'-shortest','-c:a','aac','-b:a','192k','-af',f"afade=t=out:st={dur-1.5}:d=1.5"]
    cmd+=['-c:v','libx264','-pix_fmt','yuv420p','-profile:v','high','-crf','18','-movflags','+faststart',outp]
    subprocess.run(cmd,check=True)
if __name__=='__main__': asyncio.run(main(sys.argv[1],sys.argv[2]))
