from playwright.sync_api import sync_playwright
U='https://sadiyeakoglubeauty.com/'
INIT="""try{localStorage.setItem('gz-consent','essential');localStorage.setItem('gz-theme','%s')}catch(e){}"""
HIDE="#privacy,.pv,[data-pv]{display:none!important} .rv{opacity:1!important;transform:none!important} .hdr.hide{transform:none!important}"
def ctx_for(b,mobile,theme):
    c=b.new_context(viewport={'width':390,'height':797} if mobile else {'width':1440,'height':900},
        device_scale_factor=3 if mobile else 2,locale='tr-TR',is_mobile=mobile,has_touch=mobile,reduced_motion='reduce',timezone_id='Europe/Istanbul',
        user_agent=('Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1' if mobile else None))
    c.add_init_script(INIT%theme); return c
def go(pg,url=U):
    pg.goto(url,wait_until='networkidle'); pg.add_style_tag(content=HIDE); pg.wait_for_timeout(1800)
def at(pg,sel,off=0):
    pg.evaluate(f"(()=>{{const e=document.querySelector('{sel}'); const y=e.getBoundingClientRect().top+window.scrollY+({off}); window.scrollTo(0,y); if(window.lenis) window.lenis.scrollTo(y,{{immediate:true}});}})()")
    pg.wait_for_timeout(1200)
with sync_playwright() as p:
    b=p.chromium.launch()
    for theme in ['light','dark']:
        for mobile in [True,False]:
            c=ctx_for(b,mobile,theme); pg=c.new_page(); pg.clock.set_fixed_time('2026-10-20T11:05:00+03:00'); go(pg)
            tag=('s' if mobile else 'd')+'_'+theme
            pg.screenshot(path=f'{tag}_hero.png')
            if mobile:
                for sel,off,name in [('#hizmetler',-60,'svc'),('#ilk-ziyaret',-60,'process'),('.rt-sec',-60,'ritual'),('#konular',-60,'konular'),('.offices-sec',-60,'offices')]:
                    at(pg,sel,off); pg.screenshot(path=f'{tag}_{name}.png')
                # advisor with selections
                c.close(); continue
                at(pg,'#danisman',0)
                try:
                    boxes=pg.locator('#danisman label, #danisman [role=checkbox], #danisman input[type=checkbox]')
                    n=boxes.count(); print('boxes',n)
                    for i in [0,1,4]:
                        pg.locator('#danisman input[type=checkbox]').nth(i).check(force=True)
                    pg.wait_for_timeout(800)
                except Exception as e: print('adv',e)
                at(pg,'#danisman',-60); pg.screenshot(path=f'{tag}_adv1.png')
                pg.evaluate("(()=>{const e=[...document.querySelectorAll('#danisman *')].find(x=>/SİZE UYGUN|Size uygun/i.test(x.textContent)&&x.children.length<4); if(e){const y=e.getBoundingClientRect().top+scrollY-120; scrollTo(0,y); if(window.lenis) lenis.scrollTo(y,{immediate:true});}})()")
                pg.wait_for_timeout(1200); pg.screenshot(path=f'{tag}_adv2.png')
            c.close()
    b.close()
