#!/usr/bin/env node
// Daha önce Instagram'da yayınlanmış bir gönderiyi Threads'e de gönderir.
// Kullanım: THREADS_ACCESS_TOKEN=... node scripts/threads-post.mjs <published/ altındaki klasör adı>
import fs from "node:fs";
import path from "node:path";
import { publishThreads } from "./publish.mjs";

// "all" verilirse Instagram'daki yayın sırasıyla (eskiden yeniye) Threads'te olmayan hepsi gönderilir.
const arg = process.argv[2];
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const PUB = path.join(ROOT, "published");
if (!arg) { console.error("klasör adı veya 'all' gerekli"); process.exit(1); }
if (!process.env.THREADS_ACCESS_TOKEN) { console.error("THREADS_ACCESS_TOKEN tanımlı değil"); process.exit(1); }
const readRes = (id) => { const f = path.join(PUB, id, "result.json"); return fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, "utf8")) : {}; };
let ids = arg === "all"
  ? fs.readdirSync(PUB).filter((d) => fs.existsSync(path.join(PUB, d, "post.json")))
      .sort((a, b) => new Date(readRes(a).published_at || 0) - new Date(readRes(b).published_at || 0))
  : arg.split(",");
const started = Date.now();
for (const id of ids) {
  const dir = path.join(PUB, id);
  if (!fs.existsSync(path.join(dir, "post.json"))) { console.error(`published/${id} bulunamadı`); process.exitCode = 1; continue; }
  const result = readRes(id);
  if (result.threads?.media_id) { console.log(`↷ ${id} zaten Threads'te`); continue; }
  if (Date.now() - started > 30 * 60 * 1000) { console.log(`⏱ süre doldu, ${id} ve sonrası bir sonraki çalıştırmada`); break; }
  const meta = JSON.parse(fs.readFileSync(path.join(dir, "post.json"), "utf8"));
  try {
    result.threads = await publishThreads({ id, dir, folder: "published", meta });
    console.log(`🧵 ${id}: ${result.threads.permalink || result.threads.media_id || result.threads.skipped}`);
    fs.writeFileSync(path.join(dir, "result.json"), JSON.stringify(result, null, 2));
  } catch (e) {
    console.error(`❌ ${id} Threads başarısız: ${e.message} — sıra bozulmasın diye durduruldu`);
    process.exitCode = 1;
    break;
  }
}
