#!/usr/bin/env node
// Threads uzun ömürlü anahtarı (60 gün) yeniler; yeni anahtarı yalnızca dosyaya yazar, ekrana basmaz.
// Kullanım: THREADS_ACCESS_TOKEN=... node scripts/threads-refresh.mjs <çıktı dosyası>
import fs from "node:fs";
const t = process.env.THREADS_ACCESS_TOKEN, out = process.argv[2];
if (!t || !out) { console.error("THREADS_ACCESS_TOKEN ve çıktı dosyası gerekli"); process.exit(1); }
const r = await fetch(`https://graph.threads.net/refresh_access_token?grant_type=th_refresh_token&access_token=${encodeURIComponent(t)}`);
const j = await r.json().catch(() => ({}));
if (!r.ok || !j.access_token) { console.error(`❌ Threads anahtarı yenilenemedi: ${j.error?.message || r.status}. Yeni anahtar üretmek gerekiyor.`); process.exit(1); }
console.log(`::add-mask::${j.access_token}`);
fs.writeFileSync(out, j.access_token, { mode: 0o600 });
console.log(`✅ Threads anahtarı yenilendi, ${Math.round((j.expires_in || 0) / 86400)} gün geçerli.`);
