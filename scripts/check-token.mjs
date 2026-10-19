#!/usr/bin/env node
// Erişim anahtarının çalıştığını ve yayın kotasını kontrol eder (paylaşım yapmaz).
const HOST = process.env.GRAPH_HOST || "graph.facebook.com";
const VER = process.env.GRAPH_VERSION || "v23.0";
const { IG_USER_ID: IG, IG_ACCESS_TOKEN: TOKEN } = process.env;

if (!IG || !TOKEN) { console.error("IG_USER_ID / IG_ACCESS_TOKEN eksik."); process.exit(1); }

const get = async (ep, fields) => {
  const u = `https://${HOST}/${VER}/${ep}?fields=${fields}&access_token=${encodeURIComponent(TOKEN)}`;
  const j = await (await fetch(u)).json();
  if (j.error) throw new Error(`${j.error.message} (code ${j.error.code})`);
  return j;
};

try {
  const acc = await get(IG, "username,followers_count,media_count");
  console.log(`✅ Bağlantı çalışıyor: @${acc.username} — ${acc.followers_count ?? "?"} takipçi, ${acc.media_count ?? "?"} gönderi`);
  try {
    const lim = await get(`${IG}/content_publishing_limit`, "quota_usage,config");
    const d = lim.data?.[0];
    if (d) console.log(`📊 Son 24 saatte API ile yayın: ${d.quota_usage}/${d.config?.quota_total ?? "?"}`);
  } catch (e) { console.log(`(kota okunamadı: ${e.message})`); }
} catch (e) {
  console.error(`❌ Anahtar/hesap hatası: ${e.message}\nAnahtarın süresi dolmuş olabilir — KURULUM.md 'Anahtarı yenileme' bölümüne bak.`);
  process.exit(1);
}

// Threads (tanımlıysa)
const TH = process.env.THREADS_ACCESS_TOKEN;
if (TH) {
  try {
    const j = await (await fetch(`https://graph.threads.net/v1.0/me?fields=username&access_token=${encodeURIComponent(TH)}`)).json();
    if (j.error) throw new Error(j.error.message);
    console.log(`✅ Threads bağlantısı çalışıyor: @${j.username}`);
  } catch (e) {
    console.error(`❌ Threads anahtarı hatası: ${e.message}`);
    process.exitCode = 1;
  }
}

// Facebook sayfası (FB_ENABLED=1 ise)
if (process.env.FB_ENABLED === "1") {
  try {
    const j = await get("me/accounts", "id,name,tasks,instagram_business_account");
    const page = (j.data || []).find((x) => x.instagram_business_account?.id === IG);
    if (!page) throw new Error(`Instagram'a bağlı sayfa görünmüyor (erişilen: ${(j.data || []).map((x) => x.name).join(", ") || "yok"})`);
    const canPost = (page.tasks || []).includes("CREATE_CONTENT");
    console.log(`${canPost ? "✅" : "❌"} Facebook sayfası: ${page.name}${canPost ? "" : " — içerik oluşturma yetkisi yok"}`);
    if (!canPost) process.exitCode = 1;
  } catch (e) {
    console.error(`❌ Facebook sayfası hatası: ${e.message}`);
    process.exitCode = 1;
  }
}
