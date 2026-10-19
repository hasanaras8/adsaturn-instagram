from playwright.sync_api import sync_playwright
U='https://sadiyeakoglubeauty.com/'
HIDE="#privacy{display:none!important} .rv{opacity:1!important;transform:none!important}"
with sync_playwright() as p:
    b=p.chromium.launch()
    for theme in ['light','dark']:
        c=b.new_context(viewport={'width':390,'height':797},device_scale_factor=3,locale='tr-TR',is_mobile=True,has_touch=True,reduced_motion='reduce',timezone_id='Europe/Istanbul',
          user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1')
        c.add_init_script(f"try{{localStorage.setItem('gz-consent','essential');localStorage.setItem('gz-theme','{theme}')}}catch(e){{}}")
        pg=c.new_page(); pg.clock.set_fixed_time('2026-10-20T11:05:00+03:00'); pg.goto(U,wait_until='networkidle'); pg.add_style_tag(content=HIDE); pg.wait_for_timeout(1500)
        for k in ['leke','matlik','ozel']:
            el=pg.locator(f'.fd-o[data-c="{k}"]')
            if el.count()==0: el=pg.locator('.fd-o').nth({'leke':0,'matlik':1,'ozel':10}[k])
            el.first.evaluate("e=>e.click()")
            pg.wait_for_timeout(300)
        pg.wait_for_timeout(800)
        y=pg.evaluate("(()=>{const r=document.querySelector('.fd-res,.fd-out,[data-finder] aside,[data-finder] .fd-r')||[...document.querySelectorAll('[data-finder] *')].find(x=>/SİZE UYGUN/i.test(x.innerText||'')&&x.children.length>1);return r?r.getBoundingClientRect().top+scrollY-110:0})()")
        pg.evaluate(f"scrollTo(0,{y})"); pg.wait_for_timeout(1000); pg.screenshot(path=f's_{theme}_adv3.png')
        # also the opts list with checked boxes
        y2=pg.evaluate("document.querySelector('.fd-o').getBoundingClientRect().top+scrollY-260")
        pg.evaluate(f"scrollTo(0,{y2})"); pg.wait_for_timeout(800); pg.screenshot(path=f's_{theme}_adv4.png')
        c.close()
    b.close()
