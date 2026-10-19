#!/usr/bin/env node
// Daha önce Instagram'da yayınlanmış bir gönderiyi Threads'e de gönderir.
// Kullanım: THREADS_ACCESS_TOKEN=... node scripts/threads-post.mjs <published/ altındaki klasör adı>
import fs from "node:fs";
import path from "node:path";
import { publishThreads } from "./publish.mjs";

const id = process.argv[2];
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const dir = path.join(ROOT, "published", id || "");
if (!id || !fs.existsSync(path.join(dir, "post.json"))) { console.error(`published/${id} bulunamadı`); process.exit(1); }
if (!process.env.THREADS_ACCESS_TOKEN) { console.error("THREADS_ACCESS_TOKEN tanımlı değil"); process.exit(1); }
const resFile = path.join(dir, "result.json");
const result = fs.existsSync(resFile) ? JSON.parse(fs.readFileSync(resFile, "utf8")) : {};
if (result.threads?.media_id) { console.log(`Zaten Threads'te: ${result.threads.permalink}`); process.exit(0); }
const meta = JSON.parse(fs.readFileSync(path.join(dir, "post.json"), "utf8"));
try {
  result.threads = await publishThreads({ id, dir, folder: "published", meta });
  console.log(`🧵 Threads: ${result.threads.permalink || result.threads.media_id || result.threads.skipped}`);
} catch (e) {
  result.threads = { error: e.message };
  console.error(`❌ Threads başarısız: ${e.message}`);
  process.exitCode = 1;
}
fs.writeFileSync(resFile, JSON.stringify(result, null, 2));
