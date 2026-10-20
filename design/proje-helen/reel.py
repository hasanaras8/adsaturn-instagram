import re, os, subprocess, shutil
from playwright.sync_api import sync_playwright
from mock import _sb, DEV_CSS

FPS, DUR = 30, 26
AD = re.sub(r'<title>.*?</title>', '', open('/home/claude/sadiye/adsaturn.svg').read()).replace('<svg ', '<svg class="ad" ', 1)

def phone(inner, w, x, y, rot=0, sbimg=None, pid=''):
    fs = w / 433
    bg, tx, lum = _sb(sbimg)
    ind = 'rgba(20,12,14,.8)' if lum > 140 else 'rgba(255,255,255,.85)'
    return f'''<div class="ph" id="{pid}" style="left:{x}px;top:{y}px;font-size:{fs}px;transform:rotate({rot}deg)">
  <i class="btn b1"></i><i class="btn b2"></i><i class="btn b3"></i><i class="btn b4"></i>
  <div class="bez"><div class="scr">
    <div class="sb" style="background:{bg};color:{tx}"><span class="tm">11:05</span><span class="ics">
      <svg viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx=".7"/><rect x="5" y="5.5" width="3" height="6.5" rx=".7"/><rect x="10" y="3" width="3" height="9" rx=".7"/><rect x="15" y="0" width="3" height="12" rx=".7"/></svg>
      <svg viewBox="0 0 16 12"><path d="M8 2.6c2.3 0 4.4.9 6 2.4l1.3-1.4A10.6 10.6 0 0 0 8 .6 10.6 10.6 0 0 0 .7 3.6L2 5c1.6-1.5 3.7-2.4 6-2.4Zm0 3.7c1.3 0 2.5.5 3.4 1.3l1.3-1.4A6.8 6.8 0 0 0 8 4.3 6.8 6.8 0 0 0 3.3 6.2l1.3 1.4c.9-.8 2.1-1.3 3.4-1.3Zm0 3.6c.5 0 .9.2 1.2.5L8 11.7 6.8 10.4c.3-.3.7-.5 1.2-.5Z"/></svg>
      <span class="bat"><b></b></span></span></div>
    <div class="di"></div>
    <div class="cnt">{inner}</div>
    <div class="hi" style="background:{ind}"></div>
  </div></div></div>'''

img = lambda src: f'<img src="{src}" style="position:absolute;left:0;top:0;width:390em;height:797em">'
CSS = DEV_CSS + '''
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:#F7F2E9;font-family:Inter,sans-serif;color:#17140F;-webkit-font-smoothing:antialiased}
.ph .sb{font-family:Inter,sans-serif!important}
.ph .cnt{position:absolute;left:0;top:47em;width:390em;height:797em;overflow:hidden}
.sc{position:absolute;inset:0;opacity:0;overflow:hidden}
.cap{position:absolute;left:90px;right:90px;top:200px;text-align:left}
.ey{font:600 30px Inter;letter-spacing:.24em;text-transform:uppercase;color:#95713A;display:flex;align-items:center;gap:18px}
.ey::before{content:"";width:56px;height:2px;background:currentColor}
h1,h2{font-family:"Cormorant Garamond",serif;font-weight:500;line-height:1.02;letter-spacing:-.01em}
h1{font-size:150px} h2{font-size:104px;margin-top:22px}
em{font-style:italic;color:#95713A}
.ad{height:56px;width:auto;color:currentColor}
.toggle{position:absolute;display:flex;align-items:center;justify-content:space-between;padding:0 14px;border-radius:999px;background:rgba(252,250,246,.97);box-shadow:0 20px 40px -12px rgba(30,20,5,.5);z-index:20}
.sun{border-radius:50%;background:radial-gradient(circle at 35% 35%,#ffe1a6,#e9a04e 70%)}
.moon{border-radius:50%;background:radial-gradient(circle at 35% 35%,#4a4136,#17140F 75%);box-shadow:inset -14px -7px 0 0 #0d0b08}
.ring{position:absolute;border:4px solid #B08A4E;border-radius:50%;z-index:30}
.tag{position:absolute;z-index:31;font:600 34px Inter;background:#FCFAF6;color:#95713A;border:2px solid rgba(149,113,58,.45);padding:14px 26px;border-radius:999px}
'''

PW = 640
S = f'''
<div class="sc" id="s1" style="background:#17140F">
  <img id="s1bg" src="img/DJI_20260417002726_0496_D-1920.webp" style="position:absolute;left:50%;top:0;height:1920px;width:auto;transform-origin:50% 60%">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,20,15,.55) 0%,rgba(23,20,15,0) 30%,rgba(23,20,15,0) 50%,rgba(23,20,15,.9) 88%)"></div>
  <div style="position:absolute;left:90px;top:120px;color:#FCFAF6">{AD}</div>
  <div id="s1t" style="position:absolute;left:90px;right:90px;bottom:220px;color:#FCFAF6">
    <div class="ey" style="color:#E4D2B0">Proje · Web sitesi · Mardin</div>
    <h1 style="margin-top:26px">Helen Olimpos <em style="color:#E4D2B0">Konağı</em></h1>
  </div>
</div>
<div class="sc" id="s2" style="background:linear-gradient(175deg,#FCFAF6,#EFE7D9)">
  <div class="cap"><div class="ey">helenolimposkonagi.com</div><h2>Taşın gölgesinde <em>bir web sitesi.</em></h2></div>
  {phone('<img id="long" src="m_long.png" style="position:absolute;left:0;top:0;width:390em;height:auto"><img id="hdr" src="hdr.png" style="position:absolute;left:0;top:0;width:390em;height:auto;opacity:0">', PW, (1080-PW)//2, 600, 0, 'm_light_rooms.png', 'p2')}
</div>
<div class="sc" id="s3" style="background:linear-gradient(160deg,#C29B5E,#B08A4E 50%,#8E6A35);color:#FCFAF6">
  <div class="cap"><div class="ey" style="color:#FBEBCB">Açık / koyu tema</div><h2>Gündüz taş rengi, <em style="color:#FBEBCB">gece konak ışığı.</em></h2></div>
  {phone(img('m_light_rooms.png'), 470, 40, 720, -5, 'm_light_rooms.png', 'p3a')}
  {phone(img('m_dark_rooms.png'), 470, 570, 720, 5, 'm_dark_rooms.png', 'p3b')}
  <div class="toggle" id="tg" style="left:420px;top:1230px;width:240px;height:110px"><div class="sun" style="width:82px;height:82px"></div><div class="moon" style="width:82px;height:82px"></div></div>
</div>
<div class="sc" id="s4" style="background:linear-gradient(175deg,#F7F2E9,#EFE7D9)">
  <div class="cap"><div class="ey">TR · EN · RU · AR · KU</div><h2>Beş dilde <em>aynı karşılama.</em></h2></div>
  {phone(img('m_light_en.png'), 400, 0, 820, -7, 'm_light_en.png', 'p4a')}
  {phone(img('m_light_ar.png'), 400, 680, 820, 7, 'm_light_ar.png', 'p4c')}
  {phone(img('m_light_hero2.png'), 440, 320, 760, 0, 'm_light_hero2.png', 'p4b')}
</div>
<div class="sc" id="s5" style="background:linear-gradient(175deg,#FCFAF6,#F7F2E9)">
  <div class="cap"><div class="ey">Rezervasyon</div><h2>Tarihi seçin, <em>gerisi WhatsApp’ta.</em></h2></div>
  {phone(img('m_light_hero.png'), PW, (1080-PW)//2, 590, 0, 'm_light_hero.png', 'p5')}
  <div class="ring" id="r1"></div><div class="tag" id="t1">Konağın müziği</div>
  <div class="ring" id="r2"></div><div class="tag" id="t2">WhatsApp</div>
</div>
<div class="sc" id="s6" style="background:radial-gradient(70% 45% at 100% 100%,#E4D2B0 0%,rgba(228,210,176,0) 70%),linear-gradient(175deg,#FCFAF6,#F7F2E9)">
  <div style="position:absolute;left:90px;top:200px">{AD}</div>
  <div style="position:absolute;left:90px;right:90px;top:460px">
    <h2 style="font-size:124px">İşletmenizin de böyle bir <em>sitesi</em> olsun.</h2>
    <div style="display:inline-block;margin-top:60px;background:#17140F;color:#F7F2E9;font:600 44px Inter;padding:34px 56px;border-radius:4px">Ücretsiz site analizi</div>
    <div style="font:600 46px Inter;margin-top:40px">adsaturn.com</div>
  </div>
  <div id="s6p" style="position:absolute;left:90px;right:90px;bottom:200px;height:560px;border-radius:24px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(40,25,10,.5)"><img src="img/DJI_20260417001301_0444_D-1920.webp" style="width:100%;height:100%;object-fit:cover;object-position:40% 55%"></div>
</div>'''

JS = '''
const SC=[['s1',0,4.2],['s2',3.8,10.2],['s3',9.8,14.2],['s4',13.8,18.2],['s5',17.8,22.2],['s6',21.8,26.5]];
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)); const ease=x=>x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2; const out=x=>1-Math.pow(1-x,3);
function place(ring,tag,ph,bx,by,r,side){const P=document.getElementById(ph).getBoundingClientRect();const fs=parseFloat(getComputedStyle(document.getElementById(ph)).fontSize);
  const x=P.left+(4.5+17+bx)*fs, y=P.top+(4.5+17+47+by)*fs; const R=r*fs;
  ring.style.left=(x-R)+'px'; ring.style.top=(y-R)+'px'; ring.style.width=ring.style.height=(2*R)+'px';
  tag.style.top=(y-34)+'px'; tag.style.right=(1080-(x-R)+26)+'px'; return R}
window.setT=function(t){
  for(const [id,a,b] of SC){const e=document.getElementById(id); const o=cl((t-a)/.4)*cl((b-t)/.4); e.style.opacity=o; e.style.display=o>0?'block':'none'}
  // s1
  let p=cl(t/4.2); document.getElementById('s1bg').style.transform=`translateX(-50%) scale(${1.14-0.12*ease(p)})`;
  document.getElementById('s1t').style.transform=`translateY(${40*(1-out(cl((t-.3)/1.2)))}px)`; document.getElementById('s1t').style.opacity=cl((t-.3)/1);
  // s2 scroll
  p=cl((t-4.6)/5.2); const sc=ease(p)*5200; document.getElementById('long').style.transform=`translateY(${-sc}em)`;
  document.getElementById('hdr').style.opacity=cl((sc-420)/80);
  document.getElementById('p2').style.transform=`translateY(${60*(1-out(cl((t-3.8)/.8)))}px)`;
  // s3
  p=out(cl((t-9.8)/.9)); document.getElementById('p3a').style.transform=`translateX(${-120*(1-p)}px) rotate(-5deg)`; document.getElementById('p3b').style.transform=`translateX(${120*(1-p)}px) rotate(5deg)`;
  // s4
  p=out(cl((t-13.8)/.9)); document.getElementById('p4a').style.transform=`translateY(${160*(1-p)}px) rotate(-7deg)`; document.getElementById('p4c').style.transform=`translateY(${160*(1-p)}px) rotate(7deg)`;
  document.getElementById('p4b').style.transform=`translateY(${90*(1-out(cl((t-14.1)/.9)))}px)`;
  // s5 rings
  const r1=document.getElementById('r1'),t1=document.getElementById('t1'),r2=document.getElementById('r2'),t2=document.getElementById('t2');
  place(r1,t1,'p5',343,495,34); place(r2,t2,'p5',343,687,34);
  const a1=cl((t-18.6)/.5), a2=cl((t-19.9)/.5); const pul=1+.08*Math.sin(t*6);
  r1.style.opacity=t1.style.opacity=a1; r2.style.opacity=t2.style.opacity=a2; r1.style.transform=`scale(${pul})`; r2.style.transform=`scale(${pul})`;
  // s6
  document.getElementById('s6p').style.transform=`translateY(${80*(1-out(cl((t-22)/1)))}px)`;
}'''

FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap">'
open('reel.html', 'w').write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8">{FONT}<style>{CSS}</style></head><body>{S}<script>{JS}</script></body></html>')

shutil.rmtree('frames', ignore_errors=True); os.makedirs('frames')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=1)
    pg.goto('file://' + os.path.abspath('reel.html'), wait_until='networkidle'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(1500)
    for i in range(FPS * DUR):
        pg.evaluate(f'setT({i / FPS})')
        pg.screenshot(path=f'frames/{i:04d}.jpg', type='jpeg', quality=92)
    b.close()

# müzik: 60. saniyeden 26 sn, giriş/çıkış yumuşatma, ses seviyesi -14 LUFS
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '60', '-t', str(DUR), '-i', 'muzik.mp3',
                '-af', f'afade=t=in:st=0:d=1.2,afade=t=out:st={DUR-2.5}:d=2.5,loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', 'audio.m4a'], check=True)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', 'frames/%04d.jpg', '-i', 'audio.m4a',
                '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'medium', '-movflags', '+faststart',
                '-c:a', 'aac', '-b:a', '192k', '-shortest', 'reel.mp4'], check=True)
print('ok')
