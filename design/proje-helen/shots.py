from playwright.sync_api import sync_playwright
from cap import ctx, go, U
EAGER="""async()=>{document.querySelectorAll('img').forEach(i=>{i.loading='eager'; if(i.dataset.src&&!i.src) i.src=i.dataset.src});
for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}
scrollTo(0,0); await Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r;setTimeout(r,4000)})));}"""
FILL="""(()=>{const L=(document.documentElement.lang||'tr').slice(0,2); const fmt={tr:['13 Kas 2026','15 Kas 2026'],en:['Nov 13, 2026','Nov 15, 2026'],ar:['13 نوفمبر 2026','15 نوفمبر 2026'],ru:['13 нояб. 2026','15 нояб. 2026'],ku:['13 Nov 2026','15 Nov 2026']}[L]||['13.11.2026','15.11.2026'];
 [...document.querySelectorAll('input[type=date]')].slice(0,2).forEach((d,i)=>{d.type='text'; d.value=fmt[i];});
 const sel=[...document.querySelectorAll('select')]; if(sel[0]&&sel[0].options.length>1){sel[0].selectedIndex=1; sel[0].dispatchEvent(new Event('change',{bubbles:true}))} })()"""
def at_text(pg,txt,off=-90,*a):
    pg.evaluate(f"""(()=>{{const e=[...document.querySelectorAll('h1,h2,h3,.eyebrow,span,p')].find(x=>x.textContent.trim().startsWith({txt!r}));
      if(!e) return 0; const y=e.getBoundingClientRect().top+scrollY+({off}); scrollTo(0,y); return 1}})()""")
    pg.wait_for_timeout(900)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--lang=tr-TR'])
    for theme in ['light','dark']:
        for mobile in [True,False]:
            c=ctx(b,mobile,theme); pg=c.new_page(); go(pg); pg.evaluate(EAGER); pg.evaluate(FILL); pg.wait_for_timeout(800)
            t=('m' if mobile else 'd')+'_'+theme
            pg.screenshot(path=f'{t}_hero.png')
            if mobile:
                pg.add_style_tag(content='.fab,.leftfab{display:none!important}')
                pg.evaluate("(()=>{const h=document.querySelector('.hero__title');scrollTo(0,h.getBoundingClientRect().top+scrollY-330)})()"); pg.wait_for_timeout(800)
                pg.screenshot(path=f'{t}_hero2.png')
                pg.add_style_tag(content='.fab,.leftfab{display:none!important}')
                at_text(pg,'Odalarımız','x',-80) if False else None
                pg.evaluate("scrollTo(0,0)")
            if mobile and theme=='light':
                for txt,name,off in [('Konak Hakkında','about',-80),('Odalarımız','rooms',-80),('Hizmetler','svc',-80),('Galeri','gal',-80),('Çevre','cevre',-80),('Mardin’de bir gece','cta',-200)]:
                    at_text(pg,txt,off); pg.screenshot(path=f'{t}_{name}.png')
                for path,name in [('oda/zeus-kral-odasi/','zeus'),('galeri/','galeri'),('en/','en'),('ar/','ar')]:
                    go(pg,U+path); pg.evaluate(EAGER); pg.evaluate(FILL); pg.wait_for_timeout(600)
                    if name in ('en','ar'):
                        pg.add_style_tag(content='.fab,.leftfab{display:none!important}')
                        pg.evaluate("(()=>{const h=document.querySelector('.hero__title');scrollTo(0,h.getBoundingClientRect().top+scrollY-330)})()"); pg.wait_for_timeout(800)
                    else: pg.add_style_tag(content='.fab,.leftfab{display:none!important}')
                    pg.screenshot(path=f'{t}_{name}.png')
            if mobile and theme=='dark':
                for txt,name in [('Odalarımız','rooms'),('Hizmetler','svc')]:
                    at_text(pg,txt,-80); pg.screenshot(path=f'{t}_{name}.png')
            c.close()
    b.close()
