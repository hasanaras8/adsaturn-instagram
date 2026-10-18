"""Render all posts from content.py into out/<date>_<slug>/N.jpg + post.json.
Usage: python3 build.py [slug ...]   (no args = all)"""
import json, os, re, sys, html
from playwright.sync_api import sync_playwright
from PIL import Image
from content import POSTS, TAGS

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGO = re.sub(r'aria-hidden="true" focusable="false" ', '', open('/home/claude/ig-build/logo.svg').read())
ACC = {'arama': '#ffb45e', 'sosyal': '#ff8a6b', 'web': '#8fd0ff', 'yz': '#c2adff', 'ozel': '#ff4a52', 'mono': '#f3f0ea'}
COVERS = ['cover', 'close', 'gap', 'far']
POINTS = ['close', 'gap', 'limb', 'far']

CSS = """
@font-face{font-family:Outfit;src:url(fonts/Outfit.ttf);font-weight:100 900}
@font-face{font-family:Serif;src:url(fonts/InstrumentSerif-Italic.ttf);font-style:italic}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;font-family:Outfit;-webkit-font-smoothing:antialiased}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;color:#f3f0ea;background:#050505 center/cover no-repeat}
.s::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,5,5,.72) 0%,rgba(5,5,5,.35) 42%,rgba(5,5,5,0) 62%);pointer-events:none}
.s::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.07;mix-blend-mode:screen;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.in{position:absolute;inset:0;padding:92px 88px;display:flex;flex-direction:column;z-index:1}
.logo{width:236px}.logo svg{width:100%;height:auto;display:block;color:#f3f0ea}
.top{display:flex;justify-content:space-between;align-items:center;font-size:27px;font-weight:500;color:#a19c94}
.lab{display:flex;align-items:center;gap:14px}
.lab i{width:12px;height:12px;border-radius:50%;background:var(--a);box-shadow:0 0 14px var(--a)}
h1{font-weight:600;font-size:var(--fs,104px);line-height:1.02;letter-spacing:-.04em;max-width:900px}
h2{font-weight:600;font-size:var(--fs,84px);line-height:1.04;letter-spacing:-.035em;max-width:900px}
h3{font-weight:600;font-size:68px;line-height:1.08;letter-spacing:-.03em;max-width:880px}
em{font-family:Serif;font-style:italic;font-weight:400;letter-spacing:-.01em;font-size:1.1em;color:var(--a)}
.k{font-family:Serif;font-style:italic;font-size:110px;line-height:1;color:var(--a);margin-bottom:18px}
p{font-size:38px;line-height:1.38;color:#d6d2cb;max-width:840px;margin-top:30px}
.sub{font-size:34px;color:#cfcac2;margin-top:30px}
.swipe{margin-top:40px;display:flex;align-items:center;gap:14px;font-size:30px;font-weight:500}
.swipe svg{width:56px}
ul{list-style:none;margin-top:44px}
li{display:flex;gap:26px;align-items:flex-start;font-size:41px;line-height:1.3;padding:28px 0;border-top:1px solid rgba(243,240,234,.14);color:#e9e5de}
li:last-child{border-bottom:1px solid rgba(243,240,234,.14)}
li b{flex:none;width:30px;height:30px;margin-top:8px;border-radius:50%;border:2.5px solid var(--a)}
li.n b{border:none;width:auto;height:auto;margin-top:-4px;font-family:Serif;font-style:italic;font-weight:400;font-size:52px;color:var(--a);min-width:44px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:48px}
.col{border:1.5px solid rgba(243,240,234,.18);border-radius:28px;padding:34px 32px;background:rgba(12,12,12,.6)}
.col.hl{border-color:var(--a)}
.col h4{font-size:50px;font-weight:600;letter-spacing:-.02em;margin-bottom:18px}
.col.hl h4{color:var(--a)}
.col div{font-size:34px;line-height:1.3;color:#d6d2cb;padding:20px 0;border-top:1px solid rgba(243,240,234,.12)}
.cta{margin-top:50px;align-self:flex-start;background:var(--a);color:#140c02;font-weight:600;font-size:38px;padding:26px 46px;border-radius:999px}
.url{margin-top:24px;font-size:34px}
.foot{margin-top:auto;font-size:26px;color:#a19c94}
.svc{margin-top:18px;font-size:27px;color:#a19c94}
.c{justify-content:center;text-align:left}
"""

def fs(text, big, mid, small):
    n = len(re.sub('<[^>]+>', '', text))
    return big if n <= 28 else mid if n <= 48 else small

def topbar(post, i, n):
    return f'<div class="top"><span class="lab"><i></i>{post["label"]}</span><span>{i} / {n}</span></div>'

def slide_html(post, idx, sl, n, pidx):
    p = post['pillar']
    t = sl['t']
    if t == 'cover':
        bg = f'{p}-{COVERS[pidx % len(COVERS)]}'
        sub = f'<div class="sub">{sl["sub"]}</div>' if sl.get('sub') else ''
        body = (f'<div class="logo">{LOGO}</div><h1 style="margin-top:64px;--fs:{fs(sl["h"],108,96,84)}px">{sl["h"]}</h1>{sub}'
                f'<div class="swipe">Kaydırın <svg viewBox="0 0 56 20"><path d="M0 10h52M42 2l10 8-10 8" fill="none" stroke="currentColor" stroke-width="3"/></svg></div>')
    elif t == 'point':
        bg = f'{p}-{POINTS[(idx + pidx) % len(POINTS)]}'
        k = f'<div class="k">{sl["k"]}</div>' if sl.get('k') else ''
        body = (topbar(post, idx + 1, n) + f'<div style="margin-top:70px">{k}<h2 style="--fs:{fs(sl["h"],84,74,66)}px">{sl["h"]}</h2>'
                f'<p>{sl["p"]}</p></div>')
    elif t == 'list':
        bg = f'{p}-plain'
        cls = 'n' if sl.get('numbered') else ''
        lis = ''.join(f'<li class="{cls}"><b>{(str(j+1)) if cls else ""}</b><span>{it}</span></li>' for j, it in enumerate(sl['items']))
        body = topbar(post, idx + 1, n) + f'<h3 style="margin-top:64px">{sl["h"]}</h3><ul>{lis}</ul>'
    elif t == 'compare':
        bg = f'{p}-plain'
        col = lambda c, hl: f'<div class="col{" hl" if hl else ""}"><h4>{c["title"]}</h4>' + ''.join(f'<div>{x}</div>' for x in c['items']) + '</div>'
        body = topbar(post, idx + 1, n) + f'<h3 style="margin-top:64px">{sl["h"]}</h3><div class="cmp">{col(sl["a"], True)}{col(sl["b"], False)}</div>'
    elif t == 'cta':
        bg = f'{p}-{"top" if (pidx % 2) else "far"}'
        body = (f'<div class="logo">{LOGO}</div><h2 style="margin-top:80px;--fs:{fs(sl["h"],92,80,70)}px">{sl["h"]}</h2>'
                f'<span class="cta">{sl["btn"]}</span><div class="url">adsaturn.com</div>'
                '<div class="svc">Google Ads · Meta Ads · SEO · Web tasarım</div>')
    elif t == 'holiday':
        kind = sl['kind']
        if kind == '29ekim':
            bg = 'ozel-cover'
            body = (f'<div class="logo">{LOGO}</div><div style="margin-top:70px"><div class="top" style="justify-content:flex-start">29 Ekim 1923</div>'
                    '<div style="font-family:Serif;font-style:italic;font-size:300px;line-height:.9;color:var(--a);margin-top:10px">103</div>'
                    '<h2 style="--fs:76px;margin-top:20px">Cumhuriyetimizin<br>103. yılı kutlu olsun.</h2></div>')
        elif kind == '10kasim':
            bg = 'mono-plain'
            body = (f'<div class="logo">{LOGO}</div><div style="margin:auto 0">'
                    '<div class="top" style="justify-content:flex-start">10 Kasım 1938</div>'
                    '<h2 style="--fs:80px;margin-top:34px;font-weight:500">Ulu Önder<br>Mustafa Kemal Atatürk’ü<br>saygı, özlem ve<br>minnetle anıyoruz.</h2></div>')
        else:  # yeniyil
            bg = 'arama-cover'
            body = (f'<div class="logo">{LOGO}</div><div style="margin-top:70px">'
                    '<div style="font-family:Serif;font-style:italic;font-size:280px;line-height:.9;color:var(--a)">2027</div>'
                    '<h2 style="--fs:80px;margin-top:24px">Yeni yılınız<br>kutlu olsun.</h2></div>')
        if kind == '10kasim':
            pass
    return f'<section class="s" id="s{idx+1}" style="--a:{ACC[p]};background-image:url(lib/{bg}.png)"><div class="in">{body}</div></section>'

def build(posts):
    os.makedirs('out', exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        for pidx, post in posts:
            n = len(post['slides'])
            secs = ''.join(slide_html(post, i, s, n, pidx) for i, s in enumerate(post['slides']))
            f = f'_post.html'
            open(f, 'w').write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{secs}</body></html>')
            pg.goto('file://' + os.path.join(ROOT, f)); pg.wait_for_timeout(700)
            d = f'out/{post["date"][:10]}_{post["slug"]}'; os.makedirs(d, exist_ok=True)
            media = []
            for i in range(n):
                pg.locator(f'#s{i+1}').screenshot(path='_tmp.png')
                Image.open('_tmp.png').convert('RGB').resize((1080, 1350), Image.LANCZOS).save(f'{d}/{i+1}.jpg', 'JPEG', quality=92)
                media.append(f'{i+1}.jpg')
            cap = post['caption'].strip()
            if post['pillar'] in TAGS:
                cap += '\n\n' + TAGS[post['pillar']]
            meta = {'type': 'carousel' if n > 1 else 'image', 'publish_at': post['date'] + ':00+03:00', 'approved': True,
                    'media': media, 'caption': cap}
            if n == 1:
                meta['alt_text'] = re.sub('<[^>]+>', ' ', post['caption'].split('\n')[0])
            json.dump(meta, open(f'{d}/post.json', 'w'), ensure_ascii=False, indent=2)
            print('ok', d, n)
        b.close()

if __name__ == '__main__':
    sel = sys.argv[1:]
    items = [(i, p) for i, p in enumerate(POSTS) if not sel or p['slug'] in sel]
    build(items)
