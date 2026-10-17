"""Render scene.html with query params to a PNG. Usage: python3 render.py out.png "w=2160&h=2700&..." """
import sys, base64, http.server, threading, functools, os
from playwright.sync_api import sync_playwright

root = os.path.dirname(os.path.abspath(__file__))
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
http.server.SimpleHTTPRequestHandler.log_message = lambda *a: None
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
port = srv.server_address[1]

jobs = [(sys.argv[i], sys.argv[i + 1]) for i in range(1, len(sys.argv), 2)]
with sync_playwright() as p:
    b = p.chromium.launch(args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
    for out, qs in jobs:
        params = dict(x.split("=") for x in qs.split("&") if x)
        w, h = int(params.get("w", 2160)), int(params.get("h", 2700))
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.on("console", lambda m: print("console:", m.text) if m.type == "error" else None)
        pg.goto(f"http://127.0.0.1:{port}/scene.html?{qs}")
        pg.wait_for_function("document.title==='READY'", timeout=240000)
        data = pg.evaluate("document.querySelector('canvas').toDataURL('image/png')")
        open(out, "wb").write(base64.b64decode(data.split(",")[1]))
        print("saved", out)
        pg.close()
    b.close()
srv.shutdown()
