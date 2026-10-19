#!/usr/bin/env node
// Facebook sayfasının kapak fotoğrafını depodaki bir görselle değiştirir.
// Kullanım: node scripts/fb-cover.mjs assets/facebook-kapak.jpg
import { fbPageInfo } from "./publish.mjs";
const file = process.argv[2];
const repo = process.env.GITHUB_REPOSITORY, branch = process.env.GITHUB_REF_NAME || "main";
const url = `https://raw.githubusercontent.com/${repo}/${branch}/${file}`;
const VER = process.env.GRAPH_VERSION || "v23.0";
const call = async (ep, params, token) => {
  const r = await fetch(`https://graph.facebook.com/${VER}/${ep}`, { method: "POST", body: new URLSearchParams({ ...params, access_token: token }) });
  const j = await r.json();
  if (j.error) throw new Error(`${ep}: ${j.error.message} (code ${j.error.code})`);
  return j;
};
try {
  const page = await fbPageInfo();
  const photo = await call(`${page.id}/photos`, { url, published: "false" }, page.access_token);
  await call(page.id, { cover: photo.id }, page.access_token);
  console.log(`✅ Kapak fotoğrafı güncellendi: ${page.name}`);
} catch (e) {
  console.error(`❌ Kapak güncellenemedi: ${e.message}`);
  process.exit(1);
}
