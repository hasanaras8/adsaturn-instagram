import re
logo=open('logo.svg').read()
logo=re.sub(r'<title>.*?</title>','',logo)
INK='#1d1733'
_orb=re.search(r'<ellipse class="lg-orbit".*?/>',open('logo.svg').read(),re.S).group(0)
ICON=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="8 8 226 126" style="width:100%;height:auto;display:block;overflow:visible">{_orb}</svg>'
def saturn(size, sph=('#ffd2a8','#ff8a4c','#e2562a'), ring=('#ff6b2c','#7b5cff'), tilt=-18, rid='a'):
    # vector saturn: back ring, sphere, front ring
    r=size*0.30; cx=cy=size/2; rx=size*0.48; ry=size*0.13
    g=f'''<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">
<defs><radialGradient id="s{rid}" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="{sph[0]}"/><stop offset=".55" stop-color="{sph[1]}"/><stop offset="1" stop-color="{sph[2]}"/></radialGradient>
<linearGradient id="r{rid}" x1="0" x2="1"><stop offset="0" stop-color="{ring[0]}"/><stop offset="1" stop-color="{ring[1]}"/></linearGradient>
<clipPath id="f{rid}"><rect x="-{size}" y="{cy}" width="{size*3}" height="{size}"/></clipPath>
<clipPath id="b{rid}"><rect x="-{size}" y="-{size}" width="{size*3}" height="{cy+size}"/></clipPath></defs>
<g transform="rotate({tilt} {cx} {cy})">
<g clip-path="url(#b{rid})"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#r{rid})" stroke-width="{size*0.018}" opacity=".55"/><ellipse cx="{cx}" cy="{cy}" rx="{rx*0.86}" ry="{ry*0.86}" fill="none" stroke="url(#r{rid})" stroke-width="{size*0.008}" opacity=".45"/></g>
<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#s{rid})"/>
<g clip-path="url(#f{rid})"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#r{rid})" stroke-width="{size*0.018}"/><ellipse cx="{cx}" cy="{cy}" rx="{rx*0.86}" ry="{ry*0.86}" fill="none" stroke="url(#r{rid})" stroke-width="{size*0.008}" opacity=".8"/></g>
</g></svg>'''
    return g

CSS=f'''
@font-face{{font-family:O;src:url(fonts/Outfit.ttf);font-weight:100 900}}
@font-face{{font-family:S;src:url(fonts/InstrumentSerif-Italic.ttf);font-style:italic}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:O;color:{INK};-webkit-font-smoothing:antialiased}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden}}
.in{{position:absolute;inset:0;padding:88px 84px;display:flex;flex-direction:column;z-index:2}}
.top{{display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:600;opacity:.75}}
.logo svg{{height:44px;width:auto;display:block;color:{INK}}}
.ey{{font-size:26px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--a);margin-top:56px}}
h1{{font-size:112px;line-height:.98;font-weight:700;letter-spacing:-.035em}}
h2{{font-size:80px;line-height:1.02;font-weight:700;letter-spacing:-.03em;margin-top:18px}}
em{{font-family:S;font-style:italic;font-weight:400;color:var(--a);letter-spacing:-.01em}}
p.l{{font-size:34px;line-height:1.42;margin-top:28px;max-width:880px;color:#3b3452}}
.card{{background:#fff;border-radius:34px;padding:34px 38px;box-shadow:0 18px 40px -22px rgba(40,20,60,.35)}}
.chip{{display:inline-block;font-size:24px;font-weight:600;padding:10px 20px;border-radius:999px;background:var(--soft);color:var(--a);margin:0 10px 10px 0}}
.btn{{display:inline-block;background:{INK};color:#fff;font-weight:700;font-size:36px;padding:28px 50px;border-radius:999px}}
.k{{font-family:S;font-style:italic;color:var(--a)}}
'''
def top(i): return f'<div class="top" style="min-height:44px"><div class="logo">{logo if i!=1 else ""}</div><span>{"" if i==1 else f"{i} / 10"}</span></div>'

S=[]
# 1 COVER
S.append(f'''<section class="s" style="--a:#e2501f;background:radial-gradient(90% 70% at 85% 80%,#ffb98a 0%,rgba(255,185,138,0) 70%),radial-gradient(70% 60% at 0% 0%,#ffe9a8 0%,rgba(255,233,168,0) 70%),linear-gradient(160deg,#fff4e4,#ffd9bf)">
<div style="position:absolute;left:84px;right:84px;top:720px;z-index:1;color:#000">{logo.replace('<svg ','<svg style="width:100%;height:auto;display:block;color:#000" ',1)}</div>
<div class="in">{top(1)}
<div class="ey">Dijital pazarlama ajansı · İstanbul</div>
<h1 style="margin-top:22px">Arayanı <em>yakalar,</em><br>habersizi<br><em>uyandırırız.</em></h1>
<div style="margin-top:auto;display:flex;align-items:center;gap:18px;font-size:34px;font-weight:700">Adsaturn’ü tanıyın <span style="display:inline-flex;width:72px;height:72px;border-radius:50%;background:{INK};color:#fff;align-items:center;justify-content:center;font-size:36px">→</span></div>
</div></section>''')

# 2 BIZ KIMIZ
rows=[('Google','Hangi kelime satıyor?','#2f6bff'),('Meta','Hangi kreatif durduruyor?','#e2501f'),('Site','Ziyaretçi nerede vazgeçiyor?','#10a38a')]
r=''.join(f'<div class="card" style="display:flex;align-items:center;gap:26px;margin-top:18px;padding:28px 34px"><span style="width:20px;height:20px;border-radius:50%;background:{c};flex:none;box-shadow:0 0 0 8px {c}22"></span><b style="font-size:32px;width:130px">{a}</b><span style="font-size:32px;color:#3b3452">{b}</span></div>' for a,b,c in rows)
S.append(f'''<section class="s" style="--a:#2f6bff;--soft:#e3ecff;background:linear-gradient(170deg,#eaf2ff,#d3e4ff)">
<div class="in">{top(2)}
<div class="ey">Biz kimiz?</div>
<h2>Reklam, SEO ve web sitesi <em>tek elden.</em></h2>
<p class="l">Reklam ayrı ajansta, SEO başka firmada, site bir yazılımcıdayken kimse bütün resmi görmez. Biz hepsini kurar, tek raporla ölçeriz.</p>
<div style="margin-top:38px">{r}</div>
<div style="margin-top:auto"><div style="font-size:24px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#2f6bff;margin-bottom:16px">Çalıştığımız sektörler</div>{''.join(f'<span class="chip" style="background:#fff">{x}</span>' for x in ['Otel & turizm','Hukuk','Sağlık & güzellik','Yerel esnaf','Restoran','Enerji','Eğitim','E-ticaret','Kurumsal'])}</div>
</div></section>''')

# 3 HIZMET EVRENI
rings=[('İç halka','Zemin','her şeyin indiği yer',['Web tasarım','E-ticaret taşıma','Ölçümleme'],'#2f6bff','#e3ecff'),
       ('Orta halka','Hasat','talep zaten var',['Google Ads','SEO','GEO','Harita kayıtları'],'#d97a00','#ffefd2'),
       ('Dış halka','Talep yaratma','kimse aramıyorken',['Meta Ads','TikTok Ads','ChatGPT Ads','Sosyal medya'],'#e2501f','#ffe2d6')]
def ringicon(n,c):
    return f'<svg width="96" height="96" viewBox="0 0 96 96"><circle cx="48" cy="48" r="12" fill="{c}"/>'+''.join(f'<circle cx="48" cy="48" r="{12+k*11}" fill="none" stroke="{c}" stroke-width="{4 if k==n else 2}" opacity="{1 if k==n else .3}"/>' for k in (1,2,3))+'</svg>'
c=''.join(f'''<div class="card" style="display:flex;gap:28px;align-items:flex-start;margin-top:26px;padding:42px 40px">{ringicon(i+1,col)}<div><div style="font-size:22px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:{col}">{a}</div><div style="font-size:42px;font-weight:700;margin-top:2px">{n} <span class="k" style="color:{col};font-size:36px;font-weight:400">· {t}</span></div><div style="margin-top:14px">{''.join(f'<span class="chip" style="background:{soft};color:{col}">{x}</span>' for x in it)}</div></div></div>''' for i,(a,n,t,it,col,soft) in enumerate(rings))
S.append(f'''<section class="s" style="--a:#d97a00;background:linear-gradient(170deg,#fff8e6,#ffe7b8)">
<div class="in">{top(3)}
<div class="ey">Hizmet evreni</div>
<h2 style="font-size:92px">On bir hizmet, <em>üç halka.</em></h2>
<div style="margin-top:20px">{c}</div>
<div style="margin-top:auto;font-size:26px;font-weight:600;color:#3b3452">Paket zorunluluğu yok. İhtiyacınız olanla başlarsınız.</div>
</div></section>''')

# 4 NEREDE TIKANIYORSUNUZ
cases=[('“Kimse markamı bilmiyor.”','Önce hatırlatmalısınız.',['Meta Ads','TikTok Ads']),
       ('“Aranıyoruz ama rakipler üstte.”','Talep var, başkası topluyor.',['Google Ads','SEO']),
       ('“Trafik var, satış yok.”','Sorun çoğu zaman indiği sayfada.',['Web tasarım','Ölçümleme']),
       ('“Reklam veriyoruz, ölçemiyoruz.”','Ölçüm bozuksa algoritma kör uçar.',['Ölçümleme','Google Ads'])]
c=''.join(f'''<div class="card" style="padding:38px 32px"><div class="k" style="font-size:60px;line-height:1">{i+1}</div><div style="font-size:35px;font-weight:700;margin-top:14px;line-height:1.2">{q}</div><div style="font-size:28px;color:#3b3452;margin-top:14px;line-height:1.35">{d}</div><div style="margin-top:22px">{''.join(f'<span class="chip" style="font-size:21px;padding:8px 16px">{x}</span>' for x in s)}</div></div>''' for i,(q,d,s) in enumerate(cases))
S.append(f'''<section class="s" style="--a:#e2501f;--soft:#ffe2d6;background:linear-gradient(170deg,#fff0ea,#ffd3c2)">
<div class="in">{top(4)}
<div class="ey">Teşhis</div>
<h2>Nerede <em>tıkanıyorsunuz?</em></h2>
<p class="l" style="font-size:30px">On bir hizmetin hepsine ihtiyacınız yok. Başlangıç noktası, durumunuza göre değişir.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:38px">{c}</div>
</div></section>''')

# 5 YONTEM
steps=[('Teşhis','Site, ölçüm, reklam hesapları ve rakipler incelenir.'),('Ölçüm','GA4, Tag Manager, Pixel ve Conversions API kurulur.'),('Küçük testler','Günlük bütçe, tek kanal, net bir hipotez.'),('Ölçekleme','İşe yarayan büyür, yaramayan kapanır. Bütçe kararı sizindir.'),('Tek rapor','Tüm kanallar aynı ekranda, aynı dille.')]
c=''.join(f'''<div style="display:flex;gap:30px;position:relative;padding-bottom:52px"><div style="flex:none;width:72px;height:72px;border-radius:50%;background:#fff;border:3px solid #10a38a;display:flex;align-items:center;justify-content:center;font-family:S;font-style:italic;font-size:40px;color:#10a38a;z-index:2">{i+1}</div><div style="padding-top:8px"><div style="font-size:46px;font-weight:700">{a}</div><div style="font-size:31px;color:#3b3452;margin-top:8px;line-height:1.35">{b}</div></div></div>''' for i,(a,b) in enumerate(steps))
S.append(f'''<section class="s" style="--a:#0e8c76;background:linear-gradient(170deg,#e8fbf4,#c5efe2)">
<div class="in">{top(5)}
<div class="ey">Yöntemimiz</div>
<h2 style="font-size:96px">Tahmin değil, <em>sıralama.</em></h2>
<div style="margin-top:80px;position:relative"><div style="position:absolute;left:35px;top:20px;bottom:60px;width:3px;background:#10a38a55"></div>{c}</div>
</div></section>''')

# 6 PSIKOLOJI
pr=[('Kayıptan kaçınma','İnsanlar kazanmaktan çok kaybetmemeye odaklanır.'),('Bilişsel yük','Zihin yorulunca karar ertelenir. Tek net çağrı kazandırır.'),('Sosyal kanıt','Gerçek yorum ve gerçek iş, en iyi reklam cümlesinden ikna edicidir.'),('Bağlam etkisi','Aynı mesaj, gösterildiği an ve yere göre farklı algılanır.')]
c=''.join(f'''<div class="card" style="padding:42px 36px"><div class="k" style="font-size:64px;line-height:1">{i+1}</div><div style="font-size:38px;font-weight:700;margin-top:14px">{a}</div><div style="font-size:29px;color:#3b3452;margin-top:14px;line-height:1.38">{b}</div></div>''' for i,(a,b) in enumerate(pr))
S.append(f'''<section class="s" style="--a:#6a4cf0;background:linear-gradient(170deg,#f2edff,#ddd2ff)">
<div class="in">{top(6)}
<div class="ey">Davranışsal pazarlama</div>
<h2>Reklam aslında bir <em>psikoloji</em> işidir.</h2>
<p class="l" style="font-size:30px">İnsanların neden tıkladığını, neden vazgeçtiğini ve neye güvendiğini her kampanyaya taşıyoruz.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px">{c}</div>
</div></section>''')

# 7 ORNEK
def cmp(lab,a,b,la=('Sıradan','İlkeye göre')):
    return f'''<div style="margin-top:34px"><div style="font-size:24px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#6a4cf0">{lab}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:14px">
<div class="card" style="background:#ffffffaa;box-shadow:none;border:2px dashed #c9bdf5"><div style="font-size:21px;font-weight:700;color:#8a82a6;letter-spacing:.08em;text-transform:uppercase">{la[0]}</div><div style="font-size:30px;margin-top:10px;color:#6b6585;line-height:1.3">{a}</div></div>
<div class="card" style="background:#6a4cf0;color:#fff"><div style="font-size:21px;font-weight:700;color:#d9d0ff;letter-spacing:.08em;text-transform:uppercase">{la[1]}</div><div style="font-size:30px;margin-top:10px;font-weight:600;line-height:1.3">{b}</div></div></div></div>'''
S.append(f'''<section class="s" style="--a:#6a4cf0;background:linear-gradient(170deg,#fbf9ff,#ebe4ff)">
<div class="in">{top(7)}
<div class="ey">Aynı bütçe, farklı sonuç</div>
<h2>Fark, <em>cümlenin</em> içinde.</h2>
{cmp('Kayıptan kaçınma','“Daha fazla müşteri kazanın.”','“Her gün kaçırdığınız müşterileri geri alın.”')}
{cmp('Bağlam etkisi','Arayana: “Kombi bakımı, Kadıköy. Hemen arayın.”','Kaydırana: “Kışın ilk soğuk sabahı kombiniz çalışacak mı?”',('Arama reklamı','Sosyal medya reklamı'))}
{cmp('Sosyal kanıt','“Sektörün en iyisiyiz.”','Gerçek müşteri yorumu ve yapılmış işin fotoğrafı.')}
</div></section>''')

# 8 SOZUMUZ
pm=[('Hesaplar sizin adınıza açılır','Google Ads, Analytics, Meta Business: mülkiyet sizde, biz iş ortağı erişimiyle çalışırız.'),('Önce ölçüm, sonra reklam','İlk iş her zaman ölçüm denetimi.'),('Tek ekip','Reklam, SEO ve sosyal medya için ayrı ayrı kişilerle konuşmazsınız.'),('Dürüst sınırlar','Bütçeniz bir kanal için yetersizse bunu baştan söyleriz.')]
c=''.join(f'''<div class="card" style="display:flex;gap:24px;margin-top:18px;padding:28px 32px"><span style="flex:none;width:52px;height:52px;border-radius:50%;background:#2f6bff;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700">✓</span><div><div style="font-size:33px;font-weight:700">{a}</div><div style="font-size:26px;color:#3b3452;margin-top:6px;line-height:1.35">{b}</div></div></div>''' for a,b in pm)
S.append(f'''<section class="s" style="--a:#2f6bff;background:linear-gradient(170deg,#eef7ff,#cfe6ff)">
<div class="in">{top(8)}
<div class="ey">Sözümüz</div>
<h2>Ajans değiştirirken canınızı yakanı <em>baştan</em> çözeriz.</h2>
<div style="margin-top:30px">{c}</div>
</div></section>''')

# 9 ASLA
nv=['Uydurma yorum, sahte sayaç ya da yapay aciliyet kullanmayız.','Gerçek olmayan sonuç vaat etmeyiz.','Reklam bütçenize dokunmayız; bütçe sizin kartınızdan doğrudan platforma gider.','Hukuk ve sağlık gibi sektörlerde kurala aykırı tanıtım yapmayız.']
c=''.join(f'''<div style="display:flex;gap:22px;align-items:flex-start;padding:24px 0;border-bottom:2px solid #1d173314"><span style="flex:none;width:46px;height:46px;border-radius:50%;border:3px solid #e2501f;color:#e2501f;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700">×</span><span style="font-size:31px;line-height:1.35;padding-top:2px">{x}</span></div>''' for x in nv)
S.append(f'''<section class="s" style="--a:#e2501f;background:linear-gradient(170deg,#fffaf0,#ffe9d6)">
<div class="in">{top(9)}
<div class="ey">Asla yapmadıklarımız</div>
<h2>Bazı şeyleri <em>hiç</em> yapmayız.</h2>
<div style="margin-top:26px">{c}</div>
<div class="card" style="margin-top:auto;background:#1d1733;color:#fff;display:flex;gap:24px;align-items:center"><div style="font-size:30px;line-height:1.35"><b>Ayrılmak isterseniz</b> erişimi kaldırmanız yeterli. Hesaplar zaten sizin.</div></div>
</div></section>''')

# 10 CTA
S.append(f'''<section class="s" style="--a:#e2501f;background:radial-gradient(80% 60% at 100% 0%,#ffc9a3 0%,rgba(255,201,163,0) 70%),radial-gradient(70% 60% at 0% 100%,#d9ccff 0%,rgba(217,204,255,0) 70%),linear-gradient(160deg,#fff3e6,#ffe0cc)">
<div style="position:absolute;right:84px;top:200px;width:460px;z-index:1;color:#000">{ICON}</div>
<div class="in">{top(10)}
<h2 style="margin-top:420px;font-size:92px">Önce mevcut durumunuza <em>bakalım.</em></h2>
<p class="l">Sitenizi, ölçüm kurulumunuzu ve reklam hesaplarınızı inceleyip nerede bütçe ya da trafik kaybettiğinizi yazılı olarak paylaşıyoruz. Ücretsiz ve taahhütsüz.</p>
<div style="margin-top:44px"><span class="btn">Ücretsiz dijital analiz</span></div>
<div style="margin-top:auto;font-size:30px;line-height:1.6;font-weight:600">adsaturn.com<br>info@adsaturn.com<br>WhatsApp +90 545 312 80 30</div>
</div></section>''')

open('post.html','w').write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(S)}</body></html>')

from playwright.sync_api import sync_playwright
from PIL import Image
import os
os.makedirs('out',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+os.path.abspath('post.html')); pg.wait_for_timeout(800)
    for i,el in enumerate(pg.query_selector_all('section'),1):
        el.screenshot(path='_t.png'); Image.open('_t.png').convert('RGB').resize((1080,1350),Image.LANCZOS).save(f'out/{i}.jpg',quality=92)
    b.close()
ims=[Image.open(f'out/{i}.jpg').resize((360,450)) for i in range(1,11)]
sh=Image.new('RGB',(360*5+40,450*2+10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%5)*368,(i//5)*460))
sh.save('sheet.jpg',quality=88)
