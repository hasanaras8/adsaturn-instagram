# Adsaturn Instagram Otomatik Paylaşım — Kurulum

**Ne yapar:** `queue/` klasörüne konan, **onaylanmış** (`"approved": true`) ve **zamanı gelmiş** gönderileri `@adsaturn.official` hesabına Instagram'ın resmi API'si üzerinden paylaşır. GitHub Actions her saat kuyruğu kontrol eder. Bilgisayarının açık olması gerekmez.

**Maliyet:** 0 TL. Instagram Graph API ücretsiz, GitHub Actions'ın public repolar için ücretsiz dakikası fazlasıyla yeter.

**Desteklenen formatlar:** tek görsel, carousel (2–10 görsel), Reels (video), Story.

---

## 1. Instagram hesabını hazırla (2 dk)

1. Instagram uygulaması → Ayarlar → **Hesap türü ve araçlar** → **Profesyonel hesaba geç** → **İşletme**. (Zaten işletme hesabıysa geç.)
2. Hesabın bir **Facebook Sayfası**na bağlı olduğundan emin ol (Meta Business Suite → Ayarlar → Instagram hesapları).

## 2. GitHub reposunu oluştur (3 dk)

1. GitHub'da yeni repo: **`adsaturn-instagram`** — **Public** seç.
   - Neden public: Instagram görseli bir **herkese açık URL**'den çeker. Repo public olunca görseller `raw.githubusercontent.com` üzerinden otomatik erişilebilir olur.
   - Gizli tutmak istersen: repo private olsun, görselleri `adsaturn.com/ig/...` gibi bir klasöre yükleriz ve `MEDIA_BASE_URL` değişkenini ayarlarız (bunu sonra konuşabiliriz).
2. Bu paketteki tüm dosyaları repoya yükle (gizli `.github` klasörü dahil). Mac'te Terminal:
   ```bash
   cd ~/Desktop/File/Claude\ Hasan/adsaturn-instagram
   git init && git add -A && git commit -m "ilk kurulum"
   git branch -M main
   git remote add origin https://github.com/KULLANICI_ADIN/adsaturn-instagram.git
   git push -u origin main
   ```

## 3. Meta erişim anahtarını al (10–15 dk) — önerilen yol: süresiz anahtar

Kendi hesabın ve kendi uygulaman olduğu için **App Review gerekmez.**

1. **developers.facebook.com** → Uygulamalarım → **Uygulama oluştur** → kullanım durumu: *Diğer* → tür: **İşletme** → ad: `Adsaturn Publisher` → Business portföyü olarak Adsaturn'ü seç.
2. Uygulama panelinde **Instagram** ürününü (Facebook Login ile Instagram API) ekle.
3. **business.facebook.com** → Ayarlar → Kullanıcılar → **Sistem kullanıcıları** → *Ekle* → ad: `adsaturn-bot`, rol: **Yönetici**.
4. Bu sistem kullanıcısına **Varlık ata**:
   - Uygulamalar → `Adsaturn Publisher` → tam kontrol
   - Sayfalar → Adsaturn Sayfası → içerik oluşturma
   - Instagram hesapları → `adsaturn.official` → içerik
5. Sistem kullanıcısı → **Yeni token oluştur** → uygulama: `Adsaturn Publisher` → süre: **Asla sona ermez** → izinler:
   `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, `business_management`
6. Çıkan token'ı kopyala (bir daha gösterilmez).
7. **Instagram hesap ID'sini bul:** tarayıcıda aç (TOKEN yerine yapıştır):
   ```
   https://graph.facebook.com/v23.0/me/accounts?fields=name,instagram_business_account&access_token=TOKEN
   ```
   Sonuçtaki `instagram_business_account.id` değeri (17841… ile başlar) senin **IG_USER_ID**'n.

> Token'ı ve ID'yi bana sohbette yapıştırma — doğrudan bir sonraki adımda GitHub'a gir.

## 4. GitHub'a gizli bilgileri gir (2 dk)

Repo → **Settings → Secrets and variables → Actions**

**Secrets** sekmesi → *New repository secret*:
| Ad | Değer |
|---|---|
| `IG_USER_ID` | 3. adımdaki 17841… ID |
| `IG_ACCESS_TOKEN` | 3. adımdaki token |

**Variables** sekmesi (isteğe bağlı):
| Ad | Değer | Ne işe yarar |
|---|---|---|
| `PAUSED` | `1` | **Acil durdurma.** Tüm paylaşımları anında durdurur. `0` yapınca devam eder. |
| `GRAPH_HOST` | `graph.instagram.com` | Sadece "Instagram Login" yoluyla token aldıysan. Sistem kullanıcısı yolunda **girme**. |

## 5. Test et (1 dk)

Repo → **Actions** → *Instagram yayıncı* → **Run workflow** → "Deneme modu" işaretli kalsın → çalıştır.
Log'da `Kuyrukta 1 gönderi … onay bekliyor` görürsen kurulum tamam. Hiçbir şey paylaşılmaz.

Bağlantıyı da doğrulamak için: Deneme modunun işaretini kaldırmadan önce bana haber ver, ilk gerçek paylaşımı birlikte yapalım.

---

## Günlük kullanım

Her gönderi `queue/` altında kendi klasörüdür:

```
queue/
  2026-10-20_hizmet-google-ads/
    post.json
    1.jpg
```

`post.json`:
```json
{
  "type": "image",
  "publish_at": "2026-10-20T10:00:00+03:00",
  "approved": false,
  "media": ["1.jpg"],
  "alt_text": "Görsel açıklaması (erişilebilirlik)",
  "caption": "Gönderi metni…\n\n#adsaturn"
}
```

| Alan | Değerler |
|---|---|
| `type` | `image` · `carousel` (2–10 jpg) · `reel` (mp4/mov) · `story` |
| `publish_at` | Türkiye saatiyle: `+03:00` ekli ISO tarih |
| `approved` | `false` → bekler · `true` → zamanı gelince paylaşılır |

**Akış:** Ben gönderileri hazırlayıp `approved: false` olarak kuyruğa koyarım → sen bakarsın → onayladıklarını `true` yaparsın (ya da bana "onayla" dersin) → zamanı gelince otomatik paylaşılır → `published/` klasörüne taşınır, linki `result.json`'a yazılır.

**Güvenlik önlemleri**
- Onaylanmamış gönderi asla paylaşılmaz.
- Her saat en fazla **1** gönderi paylaşılır (yanlışlıkla toplu paylaşım olmaz).
- Hata olursa gönderi `failed` olarak işaretlenir, tekrar denenmez; GitHub sana e-posta atar.
- `PAUSED=1` ile her şey anında durur.
- Her pazartesi token otomatik kontrol edilir.

## Bilinmesi gerekenler
- Görseller **JPEG** olmalı, en-boy oranı 4:5 ile 1.91:1 arası (önerilen 1080×1350).
- GitHub'ın zamanlayıcısı bazen 5–30 dk gecikebilir; paylaşım saati "yaklaşık"tır.
- Instagram API sınırı: 24 saatte 100 gönderi (bizim plan haftada 3).
- Public repoda kuyruktaki görseller paylaşılmadan önce de teknik olarak erişilebilir durumdadır.

## Anahtarı yenileme
Sistem kullanıcısı token'ı süresizdir. Instagram şifresi değişirse veya izin kaldırılırsa geçersiz olur: 3. adımın 5. maddesinden yeni token al, GitHub'daki `IG_ACCESS_TOKEN`'ı güncelle.
