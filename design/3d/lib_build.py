import subprocess, sys
PILLARS = {
 'arama': 'col=ffb15c&rim=ffa04a&keyc=ffc89a',
 'sosyal':'col=ff7d5e&rim=ff6448&keyc=ffb39c',
 'web':   'col=7fcbff&rim=58aaff&keyc=bfe0ff',
 'yz':    'col=b9a2ff&rim=9a7cff&keyc=d6c9ff',
 'ozel':  'col=ff3b45&rim=e3202d&keyc=ffb0a8',
 'mono':  'col=e9e6df&rim=bfbab2&keyc=e9e6df&glow=0.9',
}
PRESETS = {
 'cover':'dist=11.5&camy=1.2&offy=0.27&offx=0.12&tiltx=0.28&tiltz=-0.42&spin=0',
 'close':'dist=5.2&camy=0.35&offy=0.32&offx=-0.05&tiltx=0.12&tiltz=-0.22&spin=1.0',
 'gap':  'dist=8.5&camy=0.9&offy=0.22&offx=-0.12&tiltx=0.3&tiltz=0.35&spin=0&gap0=0.9&gapl=0.9',
 'top':  'dist=0.6&camy=10.5&offy=0.26&fov=34&tiltx=0&tiltz=0&spin=0.6',
 'far':  'dist=15&camy=1.6&offy=0.27&offx=0.1&tiltx=0.28&tiltz=-0.42&spin=0',
 'limb': 'dist=3.0&camy=0.2&offy=0.64&offx=0.32&tiltx=0.22&tiltz=-0.3&spin=0.4&rw=0.3&ringr=2.6',
 'plain':'planet=0&dist=7&camy=0.4&offy=0.44&tiltx=0.1&tiltz=-0.12&spin=2.0',
}
BASE='w=2160&h=2700&key=1.9&bloom=0.75&glow=1.35'
only = sys.argv[1:]
args=[]
for p,pc in PILLARS.items():
  for k,kq in PRESETS.items():
    name=f'{p}-{k}'
    if only and name not in only: continue
    args += [f'lib/{name}.png', f'{BASE}&{pc}&{kq}']
subprocess.run(['python3','render.py',*args],check=True,stdout=subprocess.DEVNULL)
