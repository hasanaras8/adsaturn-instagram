from PIL import Image
def _sb(img):
    im=Image.open(img).convert('RGB'); w,h=im.size
    px=[im.getpixel((x,y)) for x in range(0,w,7) for y in range(0,12)]
    r=sum(p[0] for p in px)//len(px); g=sum(p[1] for p in px)//len(px); b=sum(p[2] for p in px)//len(px)
    lum=0.299*r+0.587*g+0.114*b
    return f'rgb({r},{g},{b})', ('#1a1410' if lum>140 else '#f7f2e9'), lum
URL='helenolimposkonagi.com'
def phone(img, w, x, y, rot=0, z=1, dark=False, cls=''):
    """Gerçekçi iPhone 16 Pro: titanyum çerçeve, Dynamic Island, durum çubuğu, ana ekran çizgisi.
    Ekran 390x844 pt; görüntü 390x797 (durum çubuğu 47 pt üstte)."""
    fs = w / 433  # 1em = 1 iPhone noktası (dış genişlik 433 pt kabul)
    sb_bg, sb_tx, lum = _sb(img)
    ind = 'rgba(20,12,14,.8)' if lum>140 else 'rgba(255,255,255,.85)'
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
      <span class="url"><svg viewBox="0 0 10 12"><path d="M2 5V3.5a3 3 0 0 1 6 0V5h.5c.6 0 1 .4 1 1v5c0 .6-.4 1-1 1h-7c-.6 0-1-.4-1-1V6c0-.6.4-1 1-1H2Zm1.2 0h3.6V3.5a1.8 1.8 0 0 0-3.6 0V5Z"/></svg>{URL}</span></div>
    <img src="{img}"></div></div>
  <div class="base"><i></i></div></div>'''
DEV_CSS='''/* iPhone */
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
'''
