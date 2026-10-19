import re,os
from playwright.sync_api import sync_playwright
from PIL import Image
logo=re.sub(r'aria-hidden="true" focusable="false" ','',open('/home/claude/ig-build/logo.svg').read())
open('_r.html','w').write(open('post.html').read().replace('LOGO',logo))
os.makedirs('out',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+os.path.abspath('_r.html')); pg.wait_for_timeout(1500)
    n=pg.locator('section.s').count()
    for i in range(1,n+1):
        pg.locator(f'#s{i}').screenshot(path='_t.png')
        Image.open('_t.png').convert('RGB').resize((1080,1350),Image.LANCZOS).save(f'out/{i}.jpg','JPEG',quality=93)
    b.close()
ims=[Image.open(f'out/{i}.jpg').resize((360,450),Image.LANCZOS) for i in range(1,n+1)]
w=Image.new('RGB',(3*370,2*460),'white')
for k,im in enumerate(ims): w.paste(im,((k%3)*370,(k//3)*460))
w.save('sheet.jpg',quality=88)
