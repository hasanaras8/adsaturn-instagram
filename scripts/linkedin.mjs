// LinkedIn şirket sayfası paylaşımı (Community Management API, Posts + Images API)
// Gerekli ortam değişkenleri:
//   LI_ORG_ID         Adsaturn şirket sayfasının sayısal kimliği
//   LI_ACCESS_TOKEN   veya LI_REFRESH_TOKEN + LI_CLIENT_ID + LI_CLIENT_SECRET (önerilen: her çalıştırmada yeni erişim anahtarı alınır)
import fs from "node:fs";
import path from "node:path";

const VERSION = process.env.LI_VERSION || "202509";
let token = null;

export const linkedinEnabled = () =>
  !!process.env.LI_ORG_ID && !!(process.env.LI_ACCESS_TOKEN || process.env.LI_REFRESH_TOKEN);

async function getToken() {
  if (token) return token;
  if (process.env.LI_REFRESH_TOKEN) {
    const r = await fetch("https://www.linkedin.com/oauth/v2/accessToken", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({
        grant_type: "refresh_token",
        refresh_token: process.env.LI_REFRESH_TOKEN,
        client_id: process.env.LI_CLIENT_ID || "",
        client_secret: process.env.LI_CLIENT_SECRET || "",
      }),
    });
    const j = await r.json().catch(() => ({}));
    if (!j.access_token) throw new Error(`LinkedIn anahtarı yenilenemedi: ${j.error_description || j.error || r.status}`);
    if (process.env.GITHUB_ACTIONS) console.log(`::add-mask::${j.access_token}`);
    token = j.access_token;
  } else token = process.env.LI_ACCESS_TOKEN;
  return token;
}

async function li(method, endpoint, body) {
  const r = await fetch(`https://api.linkedin.com/rest/${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${await getToken()}`,
      "LinkedIn-Version": VERSION,
      "X-Restli-Protocol-Version": "2.0.0",
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await r.text();
  if (!r.ok) throw new Error(`LinkedIn ${endpoint}: ${r.status} ${text.slice(0, 300)}`);
  return { json: text ? JSON.parse(text) : {}, headers: r.headers };
}

// LinkedIn "little text": ayrılmış karakterler kaçışlanır, #etiket hashtag şablonuna çevrilir
export function liText(s) {
  const esc = (x) => x.replace(/[\\|{}@\[\]()<>#*_~]/g, (c) => "\\" + c);
  return s
    .split(/(#[\p{L}\p{N}_]+)/u)
    .map((part) => (/^#[\p{L}\p{N}_]+$/u.test(part) ? `{hashtag|\\#|${part.slice(1)}}` : esc(part)))
    .join("");
}

async function uploadImage(file, owner) {
  const { json } = await li("POST", "images?action=initializeUpload", { initializeUploadRequest: { owner } });
  const { uploadUrl, image } = json.value;
  const up = await fetch(uploadUrl, {
    method: "PUT",
    headers: { Authorization: `Bearer ${await getToken()}` },
    body: fs.readFileSync(file),
  });
  if (!up.ok) throw new Error(`LinkedIn görsel yükleme: ${up.status}`);
  return image;
}

export async function publishLinkedIn(p) {
  const m = p.meta;
  if (!["image", "carousel"].includes(m.type)) return { skipped: `LinkedIn'de ${m.type} şimdilik desteklenmiyor` };
  const owner = `urn:li:organization:${process.env.LI_ORG_ID}`;
  const ids = [];
  for (const f of m.media.map((x) => x.replace(/\.(mp4|mov)$/i, ".jpg"))) ids.push(await uploadImage(path.join(p.dir, f), owner));
  const text = (m.linkedin_text || m.caption || "").slice(0, 2900);
  const content = ids.length > 1
    ? { multiImage: { images: ids.map((id) => ({ id, altText: (m.alt_text || "").slice(0, 120) })) } }
    : { media: { id: ids[0], altText: (m.alt_text || "").slice(0, 120) } };
  const { headers } = await li("POST", "posts", {
    author: owner,
    commentary: liText(text),
    visibility: "PUBLIC",
    distribution: { feedDistribution: "MAIN_FEED", targetEntities: [], thirdPartyDistributionChannels: [] },
    content,
    lifecycleState: "PUBLISHED",
    isReshareDisabledByAuthor: false,
  });
  const urn = headers.get("x-restli-id") || headers.get("x-linkedin-id");
  return { post_urn: urn, permalink: urn ? `https://www.linkedin.com/feed/update/${urn}/` : null };
}
