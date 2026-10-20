import re, os
from playwright.sync_api import sync_playwright
from PIL import Image
from mock import phone, laptop, DEV_CSS

AD = re.sub(r'<title>.*?</title>', '', open('/home/claude/sadiye/adsaturn.svg').read()).replace('<svg ', '<svg class="ad" ', 1)

CSS = '''
:root{--s50:#FCFAF6;--s100:#F7F2E9;--s200:#EFE7D9;--s300:#E2D6C2;--stone:#D3C4AC;--ink:#17140F;--ink7:#3B342A;--ink5:#6C6253;--gold:#B08A4E;--gold6:#95713A;--gold2:#E4D2B0}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#fff;font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased;color:var(--ink)}
.s{width:1080px;height:1350px;position:relative;overflow:hidden}
.in{position:absolute;inset:0;padding:84px;display:flex;flex-direction:column;z-index:5;pointer-events:none}
.top{display:flex;justify-content:space-between;align-items:center}
.ad{height:46px;width:auto;display:block;color:currentColor}
.pg{font-size:23px;font-weight:600;letter-spacing:.08em;opacity:.6}
.ey{font-size:22px;font-weight:600;letter-spacing:.24em;text-transform:uppercase;color:var(--gold6);display:flex;align-items:center;gap:16px;margin-top:56px}
.ey::before{content:"";width:44px;height:1.5px;background:currentColor}
h1,h2{font-family:"Cormorant Garamond",serif;font-weight:500;letter-spacing:-.01em;line-height:1}
h1{font-size:124px} h2{font-size:86px;margin-top:20px}
em{font-style:italic;color:var(--gold6)}
p{font-size:30px;line-height:1.45;margin-top:22px;max-width:880px;color:var(--ink7)}
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px;max-width:900px}
.chips span{font-size:23px;font-weight:600;padding:11px 20px;border-radius:999px;background:var(--s50);border:1.5px solid rgba(149,113,58,.35);color:var(--gold6)}
.photo{position:absolute;border-radius:22px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(40,25,10,.5)}
.photo img{width:100%;height:100%;object-fit:cover;display:block}
.toggle{position:absolute;display:flex;align-items:center;justify-content:space-between;padding:0 12px;border-radius:999px;background:rgba(252,250,246,.97);box-shadow:0 20px 40px -12px rgba(30,20,5,.5);z-index:20}
.sun{border-radius:50%;background:radial-gradient(circle at 35% 35%,#ffe1a6,#e9a04e 70%)}
.moon{border-radius:50%;background:radial-gradient(circle at 35% 35%,#4a4136,#17140F 75%);box-shadow:inset -12px -6px 0 0 #0d0b08}
.btnc{display:inline-block;margin-top:40px;align-self:flex-start;background:var(--ink);color:var(--s100);font:600 34px/1 Inter;padding:28px 46px;border-radius:4px;letter-spacing:.02em}
.note{position:absolute;z-index:30;display:flex;align-items:center;gap:14px;font:600 24px Inter;color:var(--ink)}
.note i{display:block;height:2px;background:var(--gold6)}
.note b{background:var(--s50);border:1.5px solid rgba(149,113,58,.4);padding:10px 18px;border-radius:999px;color:var(--gold6)}
''' + DEV_CSS + '.ph .sb{font-family:Inter,sans-serif!important}.note{right:195px}.note i{flex:1}'

S = []
# 1 KAPAK
S.append(f'''<section class="s" style="background:radial-gradient(70% 50% at 100% 100%,#E4D2B0 0%,rgba(228,210,176,0) 70%),linear-gradient(175deg,var(--s50),var(--s100) 55%,var(--s200))">
{laptop('d_light_hero.png',820,70,700,2)}
{phone('m_light_rooms.png',250,790,640,0,3)}
<div class="in"><div class="top">{AD}<span class="pg" style="letter-spacing:.24em;color:var(--gold6);opacity:1">PROJE</span></div>
<div class="ey">Web sitesi · Mardin</div>
<h1 style="margin-top:20px">Helen Olimpos <em>Konağı</em></h1>
<p>Mardin’de taş bir konağın web sitesi. Ovaya bakan on bir oda, beş dil ve konağın kendi müziği.</p></div></section>''')

# 2 ODALAR
rooms = ''.join(f'<div class="photo" style="position:relative;width:186px;height:140px;border-radius:14px"><img src="img/{f}"></div>'
                for f in ['afrodit-12-1024x768.webp','apollon20-1024x768.webp','artemis15-1024x768.webp','dionisos4-1024x768.webp'])
S.append(f'''<section class="s" style="background:linear-gradient(175deg,var(--s50),var(--s100))">
{phone('m_light_rooms.png',360,120,560,-3,2)}
{phone('m_light_zeus.png',360,600,530,3,3)}
<div class="in"><div class="top">{AD}<span class="pg">2 / 7</span></div>
<div class="ey">Odalar</div>
<h2>Olimpos’un on bir tanrısı, <em>on bir oda.</em></h2>
<p>Her odanın kendi sayfası var: kapasite, kat, yatak, manzara ve olanaklar tek bakışta.</p></div></section>''')

# 3 GÜNDÜZ / GECE
S.append(f'''<section class="s" style="background:linear-gradient(160deg,#C29B5E,#B08A4E 50%,#8E6A35);color:var(--s100)">
{phone('m_light_rooms.png',370,100,545,-5,2)}
{phone('m_dark_rooms.png',370,610,545,5,2)}
<div class="toggle" style="left:440px;top:905px;width:200px;height:92px"><div class="sun" style="width:68px;height:68px"></div><div class="moon" style="width:68px;height:68px"></div></div>
<div class="in" style="color:var(--s100)"><div class="top">{AD}<span class="pg">3 / 7</span></div>
<div class="ey" style="color:#FBEBCB">Açık / Koyu tema</div>
<h2>Gündüz taş rengi, <em style="color:#FBEBCB">gece konak ışığı.</em></h2>
<p style="color:rgba(252,250,246,.9)">Üstteki düğmeyle site koyu temaya geçer; gece bakanın gözünü yormaz.</p></div></section>''')

# 4 BEŞ DİL
S.append(f'''<section class="s" style="background:linear-gradient(175deg,var(--s100),var(--s200))">
{phone('m_light_en.png',300,40,640,-7,2)}
{phone('m_light_hero2.png',320,380,600,0,4)}
{phone('m_light_ar.png',300,740,640,7,3)}
<div class="in"><div class="top">{AD}<span class="pg">4 / 7</span></div>
<div class="ey">TR · EN · RU · AR · KU</div>
<h2>Beş dilde <em>aynı karşılama.</em></h2>
<p>Türkçe, İngilizce, Rusça, Arapça ve Kürtçe. Arapça sürüm sağdan sola okunur.</p></div></section>''')

# 5 REZERVASYON + MÜZİK
S.append(f'''<section class="s" style="background:radial-gradient(60% 45% at 0% 100%,#E4D2B0 0%,rgba(228,210,176,0) 70%),linear-gradient(175deg,var(--s50),var(--s100))">
{phone('m_light_hero.png',400,580,460,0,2)}
<div class="note" style="left:84px;top:958px"><b>Konağın müziği</b><i></i></div>
<div class="note" style="left:84px;top:1135px"><b>WhatsApp</b><i></i></div>
<div class="note" style="left:84px;top:1194px"><b>Tek dokunuşla arama</b><i></i></div>
<div class="in"><div class="top">{AD}<span class="pg">5 / 7</span></div>
<div class="ey">Rezervasyon</div>
<h2 style="font-size:80px">Tarihi seçin, <em>gerisi WhatsApp’ta.</em></h2>
<p style="max-width:470px">Giriş, çıkış, kişi ve oda sayısı hazır bir mesaj olarak gider; onay WhatsApp ya da telefonla gelir.</p>
<p style="max-width:470px;font-size:27px;margin-top:18px">Sağ alttaki düğme konağın müziğini açar.</p></div></section>''')

# 6 MARDİN
S.append(f'''<section class="s" style="background:linear-gradient(175deg,var(--s100),var(--s200))">
<div class="photo" style="left:84px;top:640px;width:430px;height:560px;z-index:1"><img src="img/mardinsultanisadomes.jpg" style="object-position:60% 50%"></div>
{phone('m_light_cevre.png',370,600,520,3,2)}
<div class="in"><div class="top">{AD}<span class="pg">6 / 7</span></div>
<div class="ey">Mardin rehberi</div>
<h2>Kapının önünde <em>açık hava müzesi.</em></h2>
<p>Ulu Cami’den Zinciriye Medresesi’ne yürüme süreleriyle 20 durak; her biri kendi sayfasında.</p></div></section>''')

# 7 CTA
S.append(f'''<section class="s" style="background:radial-gradient(70% 50% at 100% 100%,#E4D2B0 0%,rgba(228,210,176,0) 70%),linear-gradient(170deg,var(--s50),var(--s100) 60%)">
<div class="photo" style="right:84px;bottom:170px;width:600px;height:470px;z-index:2"><img src="img/DJI_20260417001301_0444_D-1920.webp" style="object-position:40% 55%"></div>
<div class="in"><div class="top">{AD}<span class="pg">7 / 7</span></div>
<h2 style="margin-top:120px;font-size:96px">İşletmenizin de böyle bir <em>sitesi</em> olsun.</h2>
<span class="btnc">Ücretsiz site analizi</span>
<div style="font-size:32px;font-weight:600;margin-top:28px">adsaturn.com</div>
<div style="margin-top:auto;font-size:28px;color:var(--ink7)">Siteyi gezin: <b style="color:var(--gold6)">helenolimposkonagi.com</b></div></div></section>''')

FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap">'
open('post.html', 'w').write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8">{FONT}<style>{CSS}</style></head><body>{"".join(S)}</body></html>')
os.makedirs('out', exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto('file://' + os.path.abspath('post.html'), wait_until='networkidle'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(1200)
    for i, el in enumerate(pg.query_selector_all('section'), 1):
        el.screenshot(path='_t.png')
        Image.open('_t.png').convert('RGB').resize((1080, 1350), Image.LANCZOS).save(f'out/{i}.jpg', quality=92)
    b.close()
ims = [Image.open(f'out/{i}.jpg').resize((360, 450)) for i in range(1, 8)]
sh = Image.new('RGB', (368 * 7, 450), 'white')
for i, im in enumerate(ims): sh.paste(im, (i * 368, 0))
sh.save('sheet.jpg', quality=88)
print('ok')
