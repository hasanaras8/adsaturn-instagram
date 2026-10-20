import sys
from playwright.sync_api import sync_playwright
U='https://helenolimposkonagi.com/'
HIDE="#cc,.ccbtn,.totop{display:none!important} .rv{opacity:1!important;transform:none!important}"
def ctx(b,mobile,theme):
    c=b.new_context(viewport={'width':390,'height':797} if mobile else {'width':1440,'height':900},device_scale_factor=3 if mobile else 2,
        locale='tr-TR',timezone_id='Europe/Istanbul',is_mobile=mobile,has_touch=mobile,reduced_motion='reduce',
        user_agent=('Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1' if mobile else None))
    c.add_init_script(f"try{{localStorage.setItem('hok_consent',JSON.stringify({{necessary:true,analytics:false,marketing:false,ts:Date.now()}}));localStorage.setItem('hok_theme','{theme}');localStorage.setItem('hok_cc_later','1')}}catch(e){{}}")
    return c
def go(pg,url=U):
    pg.clock.set_fixed_time('2026-10-20T11:05:00+03:00')
    pg.goto(url,wait_until='networkidle'); pg.add_style_tag(content=HIDE); pg.wait_for_timeout(1800)
if __name__=='__main__':
    with sync_playwright() as p:
        b=p.chromium.launch(); c=ctx(b,True,'light'); pg=c.new_page(); go(pg)
        pg.screenshot(path='m_full.png',full_page=True); b.close()
