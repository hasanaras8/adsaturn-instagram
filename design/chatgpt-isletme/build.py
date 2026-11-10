import re
LOGO=re.sub(r'aria-hidden="true" focusable="false" ','',open('logo.svg').read())
CHK='<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'
CSS='''@font-face{font-family:O;src:url(Outfit.ttf);font-weight:100 900}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:O;-webkit-font-smoothing:antialiased;background:#fff}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;color:#16131f;background:#f7f4ef}
.s:before{content:"";position:absolute;width:900px;height:900px;border-radius:50%;right:-320px;top:-260px;background:radial-gradient(circle,#e4dcff 0%,rgba(228,220,255,0) 68%)}
.s:after{content:"";position:absolute;width:820px;height:820px;border-radius:50%;left:-300px;bottom:-300px;background:radial-gradient(circle,#ffe3cf 0%,rgba(255,227,207,0) 68%)}
.in{position:relative;z-index:1;height:100%;padding:84px 84px;display:flex;flex-direction:column}
.logo{width:220px;color:#16131f}.logo svg{width:100%;height:auto;display:block}
.top{display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:500;color:#6f6a7c}
.lab{display:flex;align-items:center;gap:12px}.lab i{width:12px;height:12px;border-radius:50%;background:#6d4cff}
.k{font-size:30px;font-weight:600;color:#6d4cff;letter-spacing:.06em;margin-top:52px}
h1{font-size:92px;line-height:1.02;letter-spacing:-.04em;font-weight:650;margin-top:56px}
h2{font-size:72px;line-height:1.05;letter-spacing:-.035em;font-weight:650;margin-top:14px}
.hl{color:#6d4cff}
.lead{font-size:33px;line-height:1.35;color:#4b4658;margin-top:22px;max-width:860px}
.card{background:#fff;border-radius:34px;box-shadow:0 30px 80px rgba(60,40,140,.13),0 4px 14px rgba(0,0,0,.05);border:1px solid #ece8f4}
.bub{border-radius:28px;padding:24px 30px;font-size:30px;line-height:1.35}
.q{align-self:flex-end;background:#6d4cff;color:#fff;border-bottom-right-radius:8px;max-width:640px}
.a{background:#fff;border:1px solid #ece8f4;border-bottom-left-radius:8px;box-shadow:0 10px 30px rgba(60,40,140,.08);max-width:760px;color:#2a2535}
.a b{color:#6d4cff}
.prof{padding:36px}
.ph{display:flex;align-items:center;gap:24px}
.av{width:96px;height:96px;border-radius:26px;background:linear-gradient(135deg,#7c5cff,#b18cff);color:#fff;font-size:46px;font-weight:700;display:grid;place-items:center;flex:none}
.nm{font-size:42px;font-weight:650;letter-spacing:-.02em;display:flex;align-items:center;gap:12px}
.ck{width:36px;height:36px;border-radius:50%;background:#2f80ff;display:grid;place-items:center;flex:none}.ck svg{width:22px}
.ct{font-size:26px;color:#6f6a7c;margin-top:4px}
.badge{display:inline-flex;align-items:center;gap:8px;font-size:22px;font-weight:600;padding:8px 16px;border-radius:999px;background:#eaf2ff;color:#2f6fe0}
.rows{margin-top:26px;border-top:1px solid #efecf4}
.row{display:flex;justify-content:space-between;align-items:center;padding:20px 0;border-bottom:1px solid #efecf4;font-size:27px}
.row span{color:#8a8597}.row b{font-weight:550;color:#221e2c}
.btn{margin-top:26px;background:#16131f;color:#fff;text-align:center;font-size:28px;font-weight:600;padding:24px;border-radius:20px}
.ex{position:absolute;right:28px;top:28px;font-size:20px;color:#8a8597;background:#f3f1f7;padding:6px 14px;border-radius:999px}
.field{border:2px solid #e5e1ee;border-radius:18px;padding:16px 22px;margin-top:14px}
.field small{display:block;font-size:20px;color:#8a8597}.field div{font-size:28px;font-weight:500;margin-top:2px}
.field.on{border-color:#6d4cff;box-shadow:0 0 0 6px rgba(109,76,255,.12)}
.cur{display:inline-block;width:3px;height:30px;background:#6d4cff;vertical-align:-5px;margin-left:3px}
.step{display:flex;align-items:center;gap:18px;font-size:28px;font-weight:500;padding:14px 0}
.dot{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;flex:none;background:#22b07d}.dot svg{width:22px}
.dot.w{background:#fff;border:3px solid #6d4cff}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:22px}
.st{background:#faf8fd;border:1px solid #efecf4;border-radius:24px;padding:24px}
.st small{font-size:23px;color:#8a8597}.st .n{font-size:58px;font-weight:650;letter-spacing:-.03em;margin-top:4px}.st .up{font-size:22px;color:#22b07d;font-weight:600}
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:16px}.chips span{font-size:24px;padding:10px 20px;border-radius:999px;background:#f1edff;color:#4b35c4;font-weight:500}
.cta{margin-top:44px;align-self:flex-start;background:#6d4cff;color:#fff;font-weight:600;font-size:36px;padding:26px 46px;border-radius:999px}
.url{font-size:32px;margin-top:22px;font-weight:500}
.svc{font-size:25px;color:#6f6a7c;margin-top:10px}
'''
def prof_card(extra_style=''):
    return f'''<div class="card prof" style="{extra_style}"><div class="ph"><div class="av">Ö</div><div><div class="nm">Örnek Diş Kliniği <span class="ck">{CHK}</span></div><div class="ct">Diş kliniği · Kadıköy, İstanbul</div></div></div>
<div style="margin-top:20px"><span class="badge">✓ Sahiplenilmiş profil</span></div>
<div class="rows"><div class="row"><span>Çalışma saatleri</span><b>Hafta içi 09:00–19:00</b></div><div class="row"><span>Hizmetler</span><b>İmplant, ortodonti, beyazlatma</b></div><div class="row"><span>Web sitesi</span><b>ornekklinik.com</b></div></div>
<div class="btn">İşletmeyle sohbet et</div></div>'''
def top(i): return f'<div class="top"><span class="lab"><i></i>Yapay zekâ · ChatGPT</span><span>{i} / 5</span></div>'
S=[]
S.append(f'''<div class="in"><div class="logo">{LOGO}</div><h1>ChatGPT’de işletmeniz <span class="hl">nasıl</span> görünüyor?</h1><p class="lead">Artık bunu siz yönetebilirsiniz.</p>
<div style="margin-top:44px;display:flex;flex-direction:column;gap:18px"><div class="bub q">Kadıköy’de iyi bir diş kliniği önerir misin?</div>
<div class="bub a">Bölgede öne çıkan seçeneklerden biri <b>Örnek Diş Kliniği</b>. Profiline göz atabilirsiniz ↓</div></div>
<div style="margin-top:24px;position:relative">{prof_card("transform:scale(.86);transform-origin:top left;width:1060px")}</div></div>''')
S.append(f'''<div class="in">{top(2)}<div class="k">01 · SAHİPLENİN</div><h2>Bilgilerinizi kendiniz güncelleyin.</h2><p class="lead">Business Hub’da işletmenizi bulun, doğrulayın, bilgilerinizi düzeltin.</p>
<div class="card" style="margin-top:42px;padding:38px;position:relative"><span class="ex">Business Hub</span>
<div class="step"><span class="dot">{CHK}</span>İşletmeyi bul</div><div class="step"><span class="dot">{CHK}</span>Sahipliği doğrula</div><div class="step"><span class="dot w"></span>Bilgileri güncelle</div>
<div class="field"><small>İşletme adı</small><div>Örnek Diş Kliniği</div></div>
<div class="field on"><small>Çalışma saatleri</small><div>Hafta içi 09:00–19:00, Cumartesi 10:00–16:00<span class="cur"></span></div></div>
<div class="field"><small>Hizmetler</small><div>İmplant, ortodonti, beyazlatma</div></div>
<div class="btn" style="background:#6d4cff">Kaydet</div></div></div>''')
S.append(f'''<div class="in">{top(3)}<div class="k">02 · ÖLÇÜN</div><h2>ChatGPT’de ne kadar anıldığınızı görün.</h2>
<div class="card" style="margin-top:46px;padding:38px;position:relative"><span class="ex">Örnek görünüm</span><div style="font-size:30px;font-weight:600">İçgörüler · Son 28 gün</div>
<div class="stats"><div class="st"><small>Anılma</small><div class="n">1.248</div><div class="up">▲ %18</div></div><div class="st"><small>Site tıklaması</small><div class="n">312</div><div class="up">▲ %11</div></div></div>
<svg viewBox="0 0 860 180" style="width:100%;margin-top:24px"><defs><linearGradient id="g" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#6d4cff" stop-opacity=".25"/><stop offset="1" stop-color="#6d4cff" stop-opacity="0"/></linearGradient></defs><path d="M0 150 L70 140 L140 145 L210 120 L280 126 L350 100 L420 108 L490 82 L560 88 L630 60 L700 66 L770 38 L860 30 L860 180 L0 180Z" fill="url(#g)"/><path d="M0 150 L70 140 L140 145 L210 120 L280 126 L350 100 L420 108 L490 82 L560 88 L630 60 L700 66 L770 38 L860 30" fill="none" stroke="#6d4cff" stroke-width="5" stroke-linejoin="round"/></svg>
<div style="font-size:26px;font-weight:600;margin-top:22px">Keşif konuları</div><div class="chips"><span>implant fiyatları</span><span>acil diş hekimi</span><span>diş beyazlatma</span><span>çocuk diş hekimi</span></div></div></div>''')
S.append(f'''<div class="in">{top(4)}<div class="k">03 · YAKINDA</div><h2>Business Agent müşterilerinize cevap verir.</h2><p class="lead">Şimdilik yalnızca ABD’de. Hazırlığı bugünden yapmak gerekiyor.</p>
<div class="card" style="margin-top:40px;padding:0;overflow:hidden"><div style="display:flex;align-items:center;gap:18px;padding:26px 32px;border-bottom:1px solid #efecf4"><div class="av" style="width:64px;height:64px;font-size:30px;border-radius:18px">Ö</div><div><div style="font-size:30px;font-weight:600;display:flex;gap:10px;align-items:center">Örnek Diş Kliniği <span class="ck" style="width:28px;height:28px">{CHK}</span></div><div style="font-size:22px;color:#8a8597">İşletme asistanı · Yapay zekâ</div></div></div>
<div style="padding:30px 32px;display:flex;flex-direction:column;gap:18px;background:#fbfaf8"><div class="bub q" style="font-size:28px">İmplant ile köprü arasındaki fark ne?</div>
<div class="bub a" style="font-size:28px">İmplant eksik dişin yerine kemiğe yerleştirilen tek bir yapay köktür; köprü ise komşu dişlerden destek alır. Hangisinin uygun olduğu muayeneyle belirlenir. Randevu bilgisi ister misiniz?</div></div></div></div>''')
S.append(f'''<div class="in" style="justify-content:center"><div class="logo" style="width:300px">{LOGO}</div><h2 style="margin-top:70px;font-size:88px">Profilinizi <span class="hl">birlikte</span> kuralım.</h2><p class="lead">Sahiplenme, bilgi düzeltme ve ölçüm kurulumu tek elden.</p>
<span class="cta">Ücretsiz dijital analiz</span><div class="url">adsaturn.com</div><div class="svc">Google Ads · Meta Ads · SEO · ChatGPT Ads</div></div>''')
html='<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>'+CSS+'</style></head><body>'+''.join(f'<section class="s" id="s{i+1}">{x}</section>' for i,x in enumerate(S))+'</body></html>'
open('post.html','w').write(html)
from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file:///home/claude/ig2/post.html'); pg.wait_for_timeout(800)
    for i in range(5):
        pg.locator(f'#s{i+1}').screenshot(path='t.png')
        Image.open('t.png').convert('RGB').resize((1080,1350),Image.LANCZOS).save(f'{i+1}.jpg',quality=92)
    b.close()
ims=[Image.open(f'{i}.jpg').resize((432,540)) for i in range(1,6)]
c=Image.new('RGB',(432*5+40,540),'white')
for i,im in enumerate(ims): c.paste(im,(i*442,0))
c.save('preview.jpg',quality=90)
