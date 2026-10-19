#!/usr/bin/env node
// Adsaturn Instagram yayıncı — Instagram Graph API (resmi, ücretsiz)
// queue/ altındaki ONAYLI ve zamanı gelmiş gönderileri yayınlar, published/ altına taşır.
//
// Ortam değişkenleri:
//   IG_USER_ID        Instagram profesyonel hesap ID'si (zorunlu, DRY_RUN hariç)
//   IG_ACCESS_TOKEN   Erişim anahtarı (zorunlu, DRY_RUN hariç)
//   GRAPH_HOST        graph.facebook.com (Facebook Login / sistem kullanıcısı) veya graph.instagram.com (Instagram Login). Varsayılan: graph.facebook.com
//   GRAPH_VERSION     Varsayılan: v23.0
//   MEDIA_BASE_URL    Görsellerin herkese açık adresi. Varsayılan: https://raw.githubusercontent.com/<repo>/<branch>
//   DRY_RUN=1         API'ye hiçbir şey göndermez, sadece ne yapacağını yazar
//   NOW               Test için zaman (ISO). Varsayılan: şimdi

import fs from "node:fs";
import path from "node:path";

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const QUEUE = path.join(ROOT, "queue");
const PUBLISHED = path.join(ROOT, "published");
const DRY = process.env.DRY_RUN === "1";
const HOST = process.env.GRAPH_HOST || "graph.facebook.com";
const VER = process.env.GRAPH_VERSION || "v23.0";
const IG = process.env.IG_USER_ID;
const TOKEN = process.env.IG_ACCESS_TOKEN;
const NOW = process.env.NOW ? new Date(process.env.NOW) : new Date();
const MAX_PER_RUN = Math.max(1, Math.min(15, parseInt(process.env.MAX_PER_RUN || '1', 10) || 1)); // varsayılan 1: yanlışlıkla toplu paylaşımı önler

const repo = process.env.GITHUB_REPOSITORY || "OWNER/REPO";
const branch = process.env.GITHUB_REF_NAME || "main";
const BASE = (process.env.MEDIA_BASE_URL || `https://raw.githubusercontent.com/${repo}/${branch}`).replace(/\/$/, "");

const log = (...a) => console.log(new Date().toISOString(), ...a);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function api(method, endpoint, params = {}) {
  const url = new URL(`https://${HOST}/${VER}/${endpoint}`);
  const body = new URLSearchParams({ ...params, access_token: TOKEN });
  const res = method === "GET"
    ? await fetch(url + "?" + body.toString())
    : await fetch(url, { method, body });
  const json = await res.json().catch(() => ({}));
  if (!res.ok || json.error) {
    const e = json.error || {};
    throw new Error(`API ${endpoint}: ${e.message || res.status} (code ${e.code ?? "-"}, sub ${e.error_subcode ?? "-"})`);
  }
  return json;
}

async function waitReady(containerId, label) {
  for (let i = 0; i < 40; i++) {
    const { status_code, status } = await api("GET", containerId, { fields: "status_code,status" });
    if (status_code === "FINISHED") return;
    if (status_code === "ERROR" || status_code === "EXPIRED") throw new Error(`${label} konteyner hatası: ${status || status_code}`);
    await sleep(15000);
  }
  throw new Error(`${label} konteyneri zamanında hazır olmadı`);
}

function loadPosts() {
  if (!fs.existsSync(QUEUE)) return [];
  return fs.readdirSync(QUEUE, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => {
      const dir = path.join(QUEUE, d.name);
      const file = path.join(dir, "post.json");
      if (!fs.existsSync(file)) return null;
      try {
        return { id: d.name, dir, meta: JSON.parse(fs.readFileSync(file, "utf8")) };
      } catch (e) {
        log(`⚠️ ${d.name}/post.json okunamadı: ${e.message}`);
        return null;
      }
    })
    .filter(Boolean)
    .sort((a, b) => new Date(a.meta.publish_at) - new Date(b.meta.publish_at));
}

function validate(p) {
  const m = p.meta;
  const errs = [];
  if (!["image", "carousel", "reel", "story"].includes(m.type)) errs.push("type: image | carousel | reel | story olmalı");
  if (!m.publish_at || isNaN(new Date(m.publish_at))) errs.push("publish_at geçerli bir ISO tarih olmalı (örn. 2026-10-20T10:00:00+03:00)");
  if (!Array.isArray(m.media) || m.media.length === 0) errs.push("media: en az bir dosya adı");
  if (m.type === "carousel" && (m.media.length < 2 || m.media.length > 10)) errs.push("carousel 2-10 görsel ister");
  if (["image", "reel", "story"].includes(m.type) && m.media.length !== 1) errs.push(`${m.type} tek dosya ister`);
  for (const f of m.media || []) {
    if (!fs.existsSync(path.join(p.dir, f))) errs.push(`dosya yok: ${f}`);
    const ext = path.extname(f).toLowerCase();
    if (m.type !== "reel" && !(m.type === "story" && [".mp4", ".mov"].includes(ext)) && ![".jpg", ".jpeg"].includes(ext)) errs.push(`görseller JPEG olmalı: ${f}`);
  }
  if ((m.caption || "").length > 2200) errs.push("caption 2200 karakteri aşıyor");
  if (((m.caption || "").match(/#/g) || []).length > 30) errs.push("en fazla 30 hashtag");
  return errs;
}

const urlFor = (p, f) => `${BASE}/queue/${encodeURIComponent(p.id)}/${encodeURIComponent(f)}`;
const isVideo = (f) => [".mp4", ".mov"].includes(path.extname(f).toLowerCase());

async function publish(p) {
  const m = p.meta;
  const caption = m.caption || "";
  let creation;
  if (m.type === "image") {
    creation = await api("POST", `${IG}/media`, { image_url: urlFor(p, m.media[0]), caption, ...(m.alt_text ? { alt_text: m.alt_text } : {}) });
  } else if (m.type === "carousel") {
    const children = [];
    for (const f of m.media) {
      const c = await api("POST", `${IG}/media`, { image_url: urlFor(p, f), is_carousel_item: "true" });
      children.push(c.id);
    }
    creation = await api("POST", `${IG}/media`, { media_type: "CAROUSEL", children: children.join(","), caption });
    await waitReady(creation.id, "carousel");
  } else if (m.type === "reel") {
    creation = await api("POST", `${IG}/media`, { media_type: "REELS", video_url: urlFor(p, m.media[0]), caption, share_to_feed: "true" });
    await waitReady(creation.id, "reel");
  } else if (m.type === "story") {
    const f = m.media[0];
    creation = await api("POST", `${IG}/media`, isVideo(f)
      ? { media_type: "STORIES", video_url: urlFor(p, f) }
      : { media_type: "STORIES", image_url: urlFor(p, f) });
    if (isVideo(f)) await waitReady(creation.id, "story");
  }
  const pub = await api("POST", `${IG}/media_publish`, { creation_id: creation.id });
  let permalink = null;
  try { permalink = (await api("GET", pub.id, { fields: "permalink" })).permalink; } catch {}
  return { media_id: pub.id, permalink };
}

function moveToPublished(p, result) {
  fs.mkdirSync(PUBLISHED, { recursive: true });
  const target = path.join(PUBLISHED, p.id);
  fs.renameSync(p.dir, target);
  fs.writeFileSync(path.join(target, "result.json"), JSON.stringify({ ...result, published_at: new Date().toISOString() }, null, 2));
}

function markFailed(p, message) {
  p.meta.status = "failed";
  p.meta.last_error = message;
  p.meta.failed_at = new Date().toISOString();
  fs.writeFileSync(path.join(p.dir, "post.json"), JSON.stringify(p.meta, null, 2) + "\n");
}

async function main() {
  if (!DRY && (!IG || !TOKEN)) {
    console.error("IG_USER_ID ve IG_ACCESS_TOKEN tanımlı değil (GitHub → Settings → Secrets → Actions).");
    process.exit(1);
  }
  if (process.env.PAUSED === "1") { log("⏸  Yayın durduruldu (PAUSED=1)."); return; }

  const posts = loadPosts();
  log(`Kuyrukta ${posts.length} gönderi. Şu an: ${NOW.toISOString()}${DRY ? " [DRY RUN]" : ""}`);

  let done = 0, hadError = false;
  for (const p of posts) {
    const m = p.meta;
    const errs = validate(p);
    const tag = `[${p.id}] ${m.type}`;
    if (errs.length) { log(`❌ ${tag} geçersiz: ${errs.join("; ")}`); hadError = true; continue; }
    if (m.approved !== true) { log(`⏳ ${tag} onay bekliyor (approved: false)`); continue; }
    if (m.status === "failed") { log(`⛔ ${tag} daha önce başarısız oldu, elle kontrol gerek: ${m.last_error}`); continue; }
    if (new Date(m.publish_at) > NOW) { log(`🕒 ${tag} zamanı gelmedi (${m.publish_at})`); continue; }
    if (done >= MAX_PER_RUN) { log(`↪︎ ${tag} bir sonraki çalıştırmaya kaldı`); continue; }

    if (DRY) {
      log(`🧪 ${tag} yayınlanacaktı → ${m.media.map((f) => urlFor(p, f)).join(", ")}`);
      done++; continue;
    }
    try {
      log(`🚀 ${tag} yayınlanıyor…`);
      const result = await publish(p);
      moveToPublished(p, result);
      log(`✅ ${tag} yayınlandı: ${result.permalink || result.media_id}`);
      done++;
    } catch (e) {
      log(`❌ ${tag} başarısız: ${e.message}`);
      markFailed(p, e.message);
      hadError = true;
    }
  }
  if (hadError) process.exitCode = 1; // GitHub, başarısız çalıştırmada e-posta bildirimi gönderir
}

main();
