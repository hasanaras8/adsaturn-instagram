import re, os
from playwright.sync_api import sync_playwright
from PIL import Image

AD = re.sub(r'<title>.*?</title>', '', open('adsaturn.svg').read()).replace('<svg ', '<svg class="ad" ', 1)

def phone(img, w, x, y, rot=0, z=1, dark=False, cls=''):
    """Gerçekçi iPhone 16 Pro: titanyum çerçeve, Dynamic Island, durum çubuğu, ana ekran çizgisi.
    Ekran 390x844 pt; görüntü 390x797 (durum çubuğu 47 pt üstte)."""
    fs = w / 433  # 1em = 1 iPhone noktası (dış genişlik 433 pt kabul)
    sb_bg = '#0f0b0c' if dark else '#f6f1ec'
    sb_tx = '#f6eee9' if dark else '#1a1214'
    ind = 'rgba(255,255,255,.85)' if dark else 'rgba(20,12,14,.85)'
    return f'''<div class="ph {cls}" style="left:{x}px;top:{y}px;font-size:{fs}px;transform:rotate({rot}deg);z-index:{z}">
  <i class="btn b1"></i><i class="btn b2"></i><i class="btn b3"></i><i class="btn b4"></i>
  <div class="bez"><div class="scr">
    <div class="sb" style="background:{sb_bg};color:{sb_tx}"><span class="tm">11:05</span>
      <span class="ics"><svg viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx=".7"/><rect x="5" y="5.5" width="3" height="6.5" rx=".7"/><rect x="10" y="3" width="3" height="9" rx=".7"/><rect x="15" y="0" width="3" height="12" rx=".7"/></svg>
      <svg viewBox="0 0 16 12"><path d="M8 2.6c2.3 0 4.4.9 6 2.4l1.3-1.4A10.6 10.6 0 0 0 8 .6 10.6 10.6 0 0 0 .7 3.6L2 5c1.6-1.5 3.7-2.4 6-2.4Zm0 3.7c1.3 0 2.5.5 3.4 1.3l1.3-1.4A6.8 6.8 0 0 0 8 4.3 6.8 6.8 0 0 0 3.3 6.2l1.3 1.4c.9-.8 2.1-1.3 3.4-1.3Zm0 3.6c.5 0 .9.2 1.2.5L8 11.7 6.8 10.4c.3-.3.7-.5 1.2-.5Z"/></svg>
      <span class="bat"><b></b></span></span></div>
    <div class="di"></div>
    <img src="{img}">
    <div class="hi" style="background:{ind}"></div>
  </div></div></div>'''

def laptop(img, w, x, y, z=1):
    return f'''<div class="lap" style="left:{x}px;top:{y}px;width:{w}px;z-index:{z}">
  <div class="lid"><div class="cam"></div><div class="win">
    <div class="bar"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i>
      <span class="url"><svg viewBox="0 0 10 12"><path d="M2 5V3.5a3 3 0 0 1 6 0V5h.5c.6 0 1 .4 1 1v5c0 .6-.4 1-1 1h-7c-.6 0-1-.4-1-1V6c0-.6.4-1 1-1H2Zm1.2 0h3.6V3.5a1.8 1.8 0 0 0-3.6 0V5Z"/></svg>sadiyeakoglubeauty.com</span></div>
    <img src="{img}"></div></div>
  <div class="base"><i></i></div></div>'''

CSS = '''
@font-face{font-family:F;src:url(fonts/fraunces-latin-wght-normal.woff2);font-weight:100 900;unicode-range:U+0000-00FF,U+0131,U+2000-206F}
@font-face{font-family:F;src:url(fonts/fraunces-latin-ext-wght-normal.woff2);font-weight:100 900;unicode-range:U+0100-02BA}
@font-face{font-family:F;src:url(fonts/fraunces-latin-wght-italic.woff2);font-style:italic;font-weight:100 900;unicode-range:U+0000-00FF,U+0131,U+2000-206F}
@font-face{font-family:F;src:url(fonts/fraunces-latin-ext-wght-italic.woff2);font-style:italic;font-weight:100 900;unicode-range:U+0100-02BA}
@font-face{font-family:I;src:url(fonts/inter-tight-latin-wght-normal.woff2);font-weight:100 900;unicode-range:U+0000-00FF,U+0131,U+2000-206F}
@font-face{font-family:I;src:url(fonts/inter-tight-latin-ext-wght-normal.woff2);font-weight:100 900;unicode-range:U+0100-02BA}
:root{--cream:#f6f1ec;--paper:#fdfaf7;--ink:#1a1214;--ink2:#4a3c3f;--terra:#8f4434;--terra2:#a9563f;--rose:#e2ad94;--blush:#f2dcd2}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#fff;font-family:I;-webkit-font-smoothing:antialiased;color:var(--ink)}
.s{width:1080px;height:1350px;position:relative;overflow:hidden}
.in{position:absolute;inset:0;padding:84px;display:flex;flex-direction:column;z-index:5;pointer-events:none}
.top{display:flex;justify-content:space-between;align-items:center}
.ad{height:46px;width:auto;display:block;color:currentColor}
.pg{font-size:23px;font-weight:600;letter-spacing:.08em;opacity:.6}
.ey{font-size:23px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--terra);display:flex;align-items:center;gap:16px;margin-top:58px}
.ey::before{content:"";width:44px;height:1.5px;background:currentColor}
h1,h2{font-family:F;font-weight:380;letter-spacing:-.02em;line-height:1.02}
h1{font-size:118px} h2{font-size:82px;margin-top:22px}
em{font-style:italic;color:var(--terra)}
p{font-size:31px;line-height:1.45;margin-top:24px;max-width:860px;color:var(--ink2)}
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px;max-width:900px}
.chips span{font-size:24px;font-weight:600;padding:12px 22px;border-radius:999px;background:var(--paper);border:1.5px solid rgba(143,68,52,.25);color:var(--terra)}
/* iPhone */
.ph{position:absolute;width:433em;height:882em;border-radius:74em;padding:4.5em;
  background:linear-gradient(135deg,#d8d2cb 0%,#a9a29a 18%,#efebe6 34%,#9d968e 52%,#e6e1db 70%,#b3aca4 88%,#dcd6cf 100%);
  box-shadow:0 60em 90em -30em rgba(60,25,20,.45),0 20em 40em -20em rgba(60,25,20,.35),inset 0 0 0 1em rgba(255,255,255,.5)}
.ph .bez{width:100%;height:100%;border-radius:70em;background:#050505;padding:17em;box-shadow:inset 0 0 0 1.5em #2a2a2a}
.ph .scr{width:390em;height:844em;border-radius:55em;overflow:hidden;position:relative;background:#000}
.ph .scr img{position:absolute;left:0;top:47em;width:390em;height:797em;display:block}
.ph .sb{position:absolute;left:0;top:0;width:390em;height:47em;display:flex;justify-content:space-between;align-items:center;padding:8em 28em 0 46em;font-family:I;font-weight:600}
.ph .sb .tm{font-size:16.5em;letter-spacing:-.01em}
.ph .ics{display:flex;align-items:center;gap:6em}
.ph .ics svg{height:11.5em;width:auto;fill:currentColor}
.ph .bat{width:25em;height:12em;border:1.2em solid currentColor;border-radius:3.5em;opacity:.95;position:relative;display:inline-block;padding:1.5em}
.ph .bat b{display:block;width:78%;height:100%;background:currentColor;border-radius:.1em}
.ph .bat::after{content:"";position:absolute;right:-3.5em;top:30%;width:1.8em;height:40%;background:currentColor;border-radius:0 1em 1em 0}
.ph .di{position:absolute;left:50%;top:11em;width:125em;height:36em;margin-left:-62.5em;border-radius:20em;background:#000;z-index:3}
.ph .hi{position:absolute;left:50%;bottom:8em;width:136em;height:5em;margin-left:-68em;border-radius:3em;z-index:3}
.ph .btn{position:absolute;width:5em;border-radius:2em;background:linear-gradient(90deg,#8e877f,#d9d3cc,#9a938b)}
.ph .b1{left:-3.5em;top:120em;height:32em}.ph .b2{left:-3.5em;top:180em;height:60em}.ph .b3{left:-3.5em;top:255em;height:60em}.ph .b4{right:-3.5em;top:205em;height:95em}
/* laptop */
.lap{position:absolute}
.lap .lid{background:#0b0b0c;border-radius:26px 26px 8px 8px;padding:22px 20px 26px;box-shadow:0 40px 80px -30px rgba(60,25,20,.5),inset 0 0 0 2px #2b2b2e;position:relative}
.lap .cam{position:absolute;left:50%;top:8px;width:8px;height:8px;margin-left:-4px;border-radius:50%;background:#1d1d22}
.lap .win{border-radius:8px;overflow:hidden;background:#fff}
.lap .bar{height:34px;background:#ebe7e3;display:flex;align-items:center;gap:8px;padding:0 14px;position:relative}
.lap .bar i{width:11px;height:11px;border-radius:50%}
.lap .url{position:absolute;left:50%;transform:translateX(-50%);height:22px;padding:0 16px;border-radius:7px;background:#fdfbf9;font:500 13px/22px I;color:#555;display:flex;align-items:center;gap:6px}
.lap .url svg{height:10px;fill:#777}
.lap img{display:block;width:100%}
.lap .base{height:24px;margin:0 -70px;background:linear-gradient(#e2ded9,#b5b0aa 70%,#8e8984);border-radius:0 0 30px 30px;position:relative}
.lap .base i{position:absolute;left:50%;top:0;width:190px;height:9px;margin-left:-95px;background:#a7a29c;border-radius:0 0 10px 10px}
.toggle{position:absolute;display:flex;align-items:center;justify-content:space-between;padding:0 12px;border-radius:999px;background:rgba(253,250,247,.95);box-shadow:0 20px 40px -12px rgba(40,10,10,.5);z-index:20}
.sun{border-radius:50%;background:radial-gradient(circle at 35% 35%,#ffe1a6,#f3a35c 70%)}
.moon{border-radius:50%;background:radial-gradient(circle at 35% 35%,#4a3a48,#1a1214 75%);box-shadow:inset -12px -6px 0 0 #0f0b0c}
.btnc{display:inline-block;margin-top:40px;align-self:flex-start;background:var(--ink);color:var(--cream);font:600 34px/1 I;padding:28px 46px;border-radius:999px}
.list{margin-top:30px;display:flex;flex-direction:column;gap:14px}
.list div{display:flex;gap:18px;align-items:baseline;font-size:29px;color:var(--ink2)}
.list b{font:italic 400 34px F;color:var(--terra);width:44px;flex:none}
'''

S = []
# 1 KAPAK
S.append(f'''<section class="s" style="background:radial-gradient(70% 55% at 85% 95%,#eab8a0 0%,rgba(234,184,160,0) 70%),radial-gradient(60% 50% at 0% 0%,#fff6ec 0%,rgba(255,246,236,0) 70%),linear-gradient(170deg,#f8efe8,#efd9cc)">
{phone('s_light_hero.png',420,560,610,6,2)}
{phone('s_dark_hero.png',420,150,650,-7,3,True)}
<div class="toggle" style="left:440px;top:1075px;width:200px;height:92px"><div class="sun" style="width:68px;height:68px"></div><div class="moon" style="width:68px;height:68px"></div></div>
<div class="in"><div class="top">{AD}<span class="pg" style="letter-spacing:.2em;color:var(--terra);opacity:1">PROJE</span></div>
<div class="ey">Web sitesi · Mersin Yenişehir</div>
<h1 style="margin-top:22px">Sadiye Akoğlu <em>Beauty</em></h1>
<p style="margin-top:22px">Bir güzellik salonunun web sitesi. Cildin gündüzü de var, gecesi de.</p></div></section>''')

# 2 MASAÜSTÜ
S.append(f'''<section class="s" style="background:linear-gradient(175deg,var(--paper),var(--cream) 60%,#efe3da)">
{laptop('d_light_hero.png',840,120,640,2)}
{phone('s_light_offices.png',240,780,690,0,3)}
<div class="in"><div class="top">{AD}<span class="pg">2 / 7</span></div>
<div class="ey">sadiyeakoglubeauty.com</div>
<h2>Salonu tanıyıp <em>randevu</em> alacağınız tek adres.</h2>
<p>Masaüstünde geniş, telefonda tek elle kullanılan bir site. Ara, randevu al ve WhatsApp her ekranda bir dokunuş uzaklıkta.</p></div></section>''')

# 3 GÜNDÜZ / GECE
S.append(f'''<section class="s" style="background:linear-gradient(160deg,#a9563f,#8f4434 55%,#6f3226);color:var(--cream)">
{phone('s_light_hero.png',370,100,545,-5,2)}
{phone('s_dark_hero.png',370,610,545,5,2,True)}
<div class="toggle" style="left:440px;top:905px;width:200px;height:92px"><div class="sun" style="width:68px;height:68px"></div><div class="moon" style="width:68px;height:68px"></div></div>
<div class="in" style="color:var(--cream)"><div class="top" style="color:var(--cream)">{AD}<span class="pg">3 / 7</span></div>
<div class="ey" style="color:#f2cbb8">Gündüz / Gece</div>
<h2>Bir dokunuşla <em style="color:#f2cbb8">gece ritüeli.</em></h2>
<p style="color:rgba(246,238,233,.88)">Sağ üstteki düğme siteyi gece hâline çevirir: görseller değişir, gündüz koruma rutini yerini gece onarım rutinine bırakır.</p></div></section>''')

# 4 CİLT DANIŞMANI
S.append(f'''<section class="s" style="background:linear-gradient(175deg,#f8e9e1,#f2dcd2 60%,#ecccbd)">
{phone('s_light_adv4.png',375,110,550,-4,2)}
{phone('s_light_adv3.png',375,595,530,4,3)}
<div class="in"><div class="top">{AD}<span class="pg">4 / 7</span></div>
<div class="ey">Cilt Danışmanı</div>
<h2>Cildinizi en çok <em>ne</em> düşündürüyor?</h2>
<p>Konuyu seçin, size uygun olabilecek bakımlar nedenleriyle listelensin. Kesin plan salonda, cilde bakarak yapılır.</p></div></section>''')

# 5 HİZMETLER
chips = ''.join(f'<span>{c}</span>' for c in ['Cilt Bakımı','Peeling Bakımları','Göz Çevresi','Kaş & Kirpik','Bölgesel İncelme','Saç Bakımı'])
S.append(f'''<section class="s" style="background:linear-gradient(175deg,var(--paper),var(--cream))">
{phone('s_light_konular.png',370,130,540,-3,2)}
{phone('s_light_svc.png',370,590,515,3,3)}
<div class="in"><div class="top">{AD}<span class="pg">5 / 7</span></div>
<div class="ey">Hizmetler</div>
<h2>Altı alan, <em>15</em> uygulama.</h2>
<div class="chips">{chips}</div></div></section>''')

# 6 SÜREÇ
S.append(f'''<section class="s" style="background:linear-gradient(170deg,#efe3da,#e6d2c6)">
{phone('s_light_process.png',400,600,470,3,2)}
<div class="in"><div class="top">{AD}<span class="pg">6 / 7</span></div>
<div class="ey">İlk ziyaret</div>
<h2 style="font-size:74px">Önce <em>dinliyor</em>,<br>sonra uyguluyor.</h2>
<div class="list" style="max-width:470px">
<div><b>1</b>Ücretsiz ön görüşme</div><div><b>2</b>Kişiye özel plan</div><div><b>3</b>Hijyen protokolü</div><div><b>4</b>Evde devam eden rutin</div></div>
<p style="max-width:450px;font-size:27px">Plan netleşmeden uygulamaya geçilmez; fiyat bu plana göre açıkça paylaşılır.</p></div></section>''')

# 7 CTA
S.append(f'''<section class="s" style="background:radial-gradient(70% 50% at 100% 100%,#eab8a0 0%,rgba(234,184,160,0) 70%),linear-gradient(170deg,var(--paper),var(--cream) 60%,#efd9cc)">
<div style="position:absolute;right:84px;bottom:170px;width:520px;height:500px;border-radius:28px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(60,25,20,.5);z-index:2"><img src="face.jpg" style="width:100%;height:100%;object-fit:cover;object-position:center 30%"></div>
<div class="in"><div class="top">{AD}<span class="pg">7 / 7</span></div>
<h2 style="margin-top:120px;font-size:92px">İşletmenizin de böyle bir <em>sitesi</em> olsun.</h2>
<span class="btnc">Ücretsiz site analizi</span>
<div style="font-size:32px;font-weight:600;margin-top:28px">adsaturn.com</div>
<div style="margin-top:auto;font-size:28px;color:var(--ink2)">Siteyi gezin: <b style="color:var(--terra)">sadiyeakoglubeauty.com</b></div></div></section>''')

open('post.html', 'w').write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(S)}</body></html>')
os.makedirs('out', exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto('file://' + os.path.abspath('post.html')); pg.wait_for_timeout(1500)
    for i, el in enumerate(pg.query_selector_all('section'), 1):
        el.screenshot(path='_t.png')
        Image.open('_t.png').convert('RGB').resize((1080, 1350), Image.LANCZOS).save(f'out/{i}.jpg', quality=92)
    b.close()
ims = [Image.open(f'out/{i}.jpg').resize((360, 450)) for i in range(1, 8)]
sh = Image.new('RGB', (368 * 7, 450), 'white')
for i, im in enumerate(ims): sh.paste(im, (i * 368, 0))
sh.save('sheet.jpg', quality=88)
print('ok')
