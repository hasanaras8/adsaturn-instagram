# Adsaturn Instagram içerik takvimi: 20 Ekim 2026 – 31 Aralık 2026
# Slayt tipleri: cover, point, list, compare, cta, holiday
# pillar: arama (Google Ads/SEO), sosyal (Meta), web, yz (yapay zekâ/ölçüm), ozel/mono (özel günler)

TAGS = {
    'arama': '#googleads #seo #dijitalpazarlama #adsaturn',
    'sosyal': '#metareklam #instagramreklam #sosyalmedyayönetimi #adsaturn',
    'web': '#webtasarım #kurumsalweb #dijitalpazarlama #adsaturn',
    'yz': '#yapayzeka #googleanalytics #dijitalpazarlama #adsaturn',
}
LINK = "Ücretsiz dijital analiz için profildeki bağlantıdan bize ulaşın."

POSTS = [
# ───────────── EKİM ─────────────
dict(date='2026-10-21T11:00', slug='google-ads-butce', pillar='arama', label='Google Ads',
 slides=[
  dict(t='cover', h='Google Ads bütçeniz <em>nereye</em> gidiyor?', sub='Paranın sessizce eridiği 4 yer'),
  dict(t='point', k='01', h='Alakasız aramalar', p='“Ücretsiz”, “iş ilanı”, “nasıl yapılır” gibi aramalar tıklama alır ama müşteri getirmez. Negatif anahtar kelimeler bunları dışarıda tutar.'),
  dict(t='point', k='02', h='Ölçülmeyen dönüşümler', p='Form, telefon ve WhatsApp tıklamaları kaydedilmiyorsa sistem neyi artırması gerektiğini bilemez.'),
  dict(t='point', k='03', h='Geniş konum ayarı', p='Hizmet vermediğiniz şehirlerde gösterilen reklam, bütçeyi müşteriniz olamayacak kişilere harcar.'),
  dict(t='point', k='04', h='Her reklam ana sayfaya', p='Aranan hizmeti anlatan ayrı bir sayfa yoksa ziyaretçi aradığını bulmak için uğraşmaz, geri döner.'),
  dict(t='cta', h='Hesabınızı birlikte <em>inceleyelim.</em>', btn='Ücretsiz hesap analizi'),
 ],
 caption="""Google Ads'te bütçe çoğu zaman tek seferde değil, küçük sızıntılarla erir.

En sık gördüğümüz dört neden: alakasız aramalarda çıkan reklamlar, ölçülmeyen dönüşümler, gereğinden geniş konum ayarı ve her reklamın ana sayfaya gönderilmesi.

Dördü de birkaç ayar ve doğru bir açılış sayfasıyla düzeltilebilir.

Hesabınıza birlikte bakalım. """ + LINK),

dict(date='2026-10-23T11:00', slug='meta-ilk-saniye', pillar='sosyal', label='Meta reklamları',
 slides=[
  dict(t='cover', h='Reklamınız ilk <em>saniyede</em> kazanır ya da kaybeder.'),
  dict(t='point', k='01', h='Akış durmaz', p='İnsanlar Instagram’da reklam izlemek için durmaz. Durduracak bir şey görürlerse dururlar.'),
  dict(t='point', k='02', h='Önce sorun, sonra marka', p='İlk karede logonuz değil, müşterinin kendini tanıdığı bir sorun ya da sahne olmalı.'),
  dict(t='point', k='03', h='Sessiz izlenir', p='Videoların büyük kısmı sesi kapalı izlenir. Ana mesaj ekranda yazılı olmalı.'),
  dict(t='point', k='04', h='Tek mesaj', p='Bir reklam tek bir şey söyler. Aynı anda üç teklif, hiçbirini akılda bırakmaz.'),
  dict(t='cta', h='Reklamlarınızı <em>durduran</em> hale getirelim.', btn='Ücretsiz reklam analizi'),
 ],
 caption="""Instagram ve Facebook'ta reklamınızın şansı ilk saniyedir. Kaydırma o kadar hızlı ki, ilk karede ilgi çekmeyen reklamın geri kalanı izlenmez.

İlk karede müşterinin tanıdığı bir sorunu gösterin, mesajı ekrana yazın ve tek bir teklifle çıkın.

Reklamlarınızı birlikte inceleyelim. """ + LINK),

dict(date='2026-10-26T11:00', slug='site-musteri-kaciriyor', pillar='web', label='Web sitesi',
 slides=[
  dict(t='cover', h='Siteniz müşteri <em>kaçırıyor</em> olabilir.', sub='Kontrol etmeniz gereken 5 işaret'),
  dict(t='list', h='Bu işaretlerden biri sizde de var mı?', items=[
     'Mobilde yazılar küçük, butonlar iç içe',
     'Telefon ve WhatsApp butonu ilk ekranda yok',
     'Sayfalar geç açılıyor',
     'Fiyat, süre ya da süreç hakkında bilgi yok',
     'Son güncelleme yıllar önce yapılmış']),
  dict(t='point', h='Ziyaretçi sormaz, gider', p='Aradığını bulamayan kişi size yazıp sormaz. Arama sonuçlarına geri dönüp bir sonraki siteye girer.'),
  dict(t='cta', h='Sitenizi birlikte <em>gözden</em> geçirelim.', btn='Ücretsiz site analizi'),
 ],
 caption="""Bir web sitesi müşteri kaybettiğini size söylemez. Ziyaretçi aradığını bulamayınca sessizce çıkar.

Mobilde zor okunan yazılar, ilk ekranda olmayan iletişim butonları, geç açılan sayfalar, fiyat ya da süreç hakkında bilgi eksikliği ve uzun süredir güncellenmemiş içerik en sık gördüğümüz işaretler.

Sitenize birlikte bakalım. """ + LINK),

dict(date='2026-10-28T11:00', slug='seo-mu-google-ads-mi', pillar='arama', label='Google Ads · SEO',
 slides=[
  dict(t='cover', h='SEO mu, <em>Google Ads</em> mi?'),
  dict(t='compare', h='İki yol, iki farklı hız', a=dict(title='Google Ads', items=['Aynı gün görünür','Tıklama başına ödenir','Bütçe durunca görünürlük biter','Hızlı test için uygun']),
       b=dict(title='SEO', items=['Sonuç birkaç ay sürer','Tıklama başına ödeme yok','Emek birikir, kalıcıdır','Güven ve marka için güçlü'])),
  dict(t='point', h='Çoğu zaman cevap ikisi', p='Google Ads bugünün müşterisini getirir, SEO yarının maliyetini düşürür. Oranı sektörünüz ve bütçeniz belirler.'),
  dict(t='cta', h='Sizin için doğru <em>dengeyi</em> bulalım.', btn='Ücretsiz dijital analiz'),
 ],
 caption="""“SEO mu yapalım, Google Ads mi?” en sık duyduğumuz soru.

Google Ads aynı gün sonuç verir ama bütçe durduğunda görünürlük de durur. SEO daha yavaş ilerler, karşılığında zamanla birikir ve tıklama başına ödeme istemez.

Çoğu işletme için doğru cevap ikisinin bir karışımıdır. Oranı birlikte belirleyelim. """ + LINK),

dict(date='2026-10-29T10:00', slug='29-ekim', pillar='ozel', label='',
 slides=[dict(t='holiday', kind='29ekim')],
 caption="""Cumhuriyetimizin 103. yılı kutlu olsun.

#29ekim #cumhuriyetbayramı #adsaturn"""),

# ───────────── KASIM ─────────────
dict(date='2026-11-02T11:00', slug='chatgpt-reklam', pillar='yz', label='Yapay zekâ',
 slides=[
  dict(t='cover', h='Müşterileriniz artık <em>ChatGPT’ye</em> de soruyor.'),
  dict(t='point', k='01', h='Arama alışkanlığı değişiyor', p='Ürün ya da hizmet araştırırken Google’ın yanında yapay zekâ asistanlarına soranların sayısı artıyor.'),
  dict(t='point', k='02', h='Orada da reklam var', p='ChatGPT’de reklamlar konuşmanın konusuyla ilgili olduğunda gösteriliyor. Henüz az markanın denediği yeni bir kanal.'),
  dict(t='point', k='03', h='Hazırlık sitenizden başlar', p='Asistanların sizi önerebilmesi için sitenizin hizmetlerinizi açık ve düzenli anlatması gerekir.'),
  dict(t='cta', h='Yapay zekâ aramalarında <em>görünür</em> olun.', btn='Ücretsiz dijital analiz'),
 ],
 caption="""İnsanlar artık yalnızca Google'da aramıyor. “Kadıköy'de iyi bir diş kliniği önerir misin?” gibi soruları ChatGPT'ye de soruyorlar.

ChatGPT'de reklam vermek artık mümkün. Ayrıca yapay zekâ asistanlarının sizi önermesi, sitenizin hizmetlerinizi ne kadar açık anlattığına bağlı.

İki tarafı da birlikte hazırlayalım. """ + LINK),

dict(date='2026-11-04T11:00', slug='olcum-altyapisi', pillar='yz', label='Ölçüm',
 slides=[
  dict(t='cover', h='Ölçmediğiniz reklamı <em>yönetemezsiniz.</em>'),
  dict(t='list', h='Reklam başlamadan kurulu olmalı', items=[
     'Google Analytics 4','Google Ads dönüşüm etiketi','Meta Pixel ve Conversions API',
     'Form, telefon ve WhatsApp tıklama olayları','Search Console bağlantısı']),
  dict(t='point', h='Ölçüm bütçeyi yönlendirir', p='Hangi reklamın satış getirdiğini bilmeden yapılan her değişiklik tahmindir.'),
  dict(t='cta', h='Ölçüm altyapınızı <em>kontrol</em> edelim.', btn='Ücretsiz ölçüm kontrolü'),
 ],
 caption="""Reklama başlamadan önce ilk işimiz ölçümü kurmaktır. Ölçüm olmadan reklam yayına girmez.

Google Analytics 4, Google Ads dönüşüm etiketi, Meta Pixel ve Conversions API, form ve telefon tıklama olayları, Search Console bağlantısı. Bunlar olmadan hangi reklamın işe yaradığını bilemezsiniz.

Altyapınızı birlikte kontrol edelim. """ + LINK),

dict(date='2026-11-06T11:00', slug='isletme-profili', pillar='arama', label='Google Haritalar',
 slides=[
  dict(t='cover', h='Google Haritalar’da <em>öne</em> çıkıyor musunuz?'),
  dict(t='list', h='İşletme profili kontrol listesi', items=[
     'Doğru kategori seçilmiş','Çalışma saatleri güncel','Gerçek fotoğraflar yüklenmiş',
     'Yorumlara yanıt veriliyor','Hizmetler ve açıklama eksiksiz','Web sitesi ve telefon doğru']),
  dict(t='point', h='“Yakınımdaki” aramaları', p='Yakınındaki bir işletmeyi arayan kişi çoğu zaman hemen aramak ya da gelmek ister. Bu aramalarda haritadaki ilk sonuçlar öne çıkar.'),
  dict(t='cta', h='Profilinizi birlikte <em>düzenleyelim.</em>', btn='Ücretsiz profil analizi'),
 ],
 caption="""“Yakınımdaki kuaför”, “en yakın veteriner”, “açık eczane”... Bu aramaların cevabı çoğu zaman Google Haritalar'da çıkar.

Google İşletme Profiliniz eksiksiz ve güncel değilse, yakınınızdaki müşteri rakibinize gider.

Kategori, çalışma saatleri, fotoğraflar, yorum yanıtları ve iletişim bilgileri. Profilinizi birlikte gözden geçirelim. """ + LINK),

dict(date='2026-11-09T11:00', slug='organik-mi-reklam-mi', pillar='sosyal', label='Sosyal medya',
 slides=[
  dict(t='cover', h='Organik paylaşım mı, <em>reklam</em> mı?'),
  dict(t='compare', h='İkisi farklı işler yapar', a=dict(title='Organik', items=['Takipçilerinize ulaşır','Marka sesi ve güven kurar','Ücretsiz ama zaman ister','Sonuç yavaş görünür']),
       b=dict(title='Reklam', items=['Sizi tanımayanlara ulaşır','Kitle seçilebilir','Bütçe ister','Sonuç hızlı ve ölçülebilir'])),
  dict(t='point', h='Biri vitrin, diğeri tabela', p='Reklamla gelen kişi profilinize bakar. Orada düzenli ve güncel bir hesap görmezse geri döner.'),
  dict(t='cta', h='İkisini birlikte <em>planlayalım.</em>', btn='Ücretsiz sosyal medya analizi'),
 ],
 caption="""Reklam sizi tanımayan insanlara ulaştırır. Organik paylaşımlar ise o insanlar profilinize geldiğinde güven verir.

Biri olmadan diğeri yarım kalır: reklamla gelen kişi boş ya da yıllardır güncellenmemiş bir hesap görürse takip etmeden çıkar.

Sosyal medya planınızı birlikte kuralım. """ + LINK),

dict(date='2026-11-10T09:05', slug='10-kasim', pillar='mono', label='',
 slides=[dict(t='holiday', kind='10kasim')],
 caption="""Ulu Önder Mustafa Kemal Atatürk'ü vefatının 88. yılında saygı, özlem ve minnetle anıyoruz.

#10kasım #atatürk"""),

dict(date='2026-11-13T11:00', slug='acilis-sayfasi', pillar='web', label='Web sitesi',
 slides=[
  dict(t='cover', h='İyi bir açılış sayfası <em>6 parçadan</em> oluşur.'),
  dict(t='list', h='Sayfada olması gerekenler', items=[
     'Ne sunduğunuzu söyleyen tek cümle','Ana eylem butonu ilk ekranda','Güven veren kanıt: yorum, referans, sertifika',
     'Sık sorulan soruların cevabı','Kısa ve kolay iletişim formu','Mobilde rahat okunan düzen']),
  dict(t='point', h='Reklam ile sayfa aynı dili konuşmalı', p='“Kombi bakımı” reklamına tıklayan kişi kombi bakımını anlatan bir sayfaya inmeli, genel bir ana sayfaya değil.'),
  dict(t='cta', h='Reklamınıza uygun sayfayı <em>kuralım.</em>', btn='Ücretsiz site analizi'),
 ],
 caption="""Reklama tıklayan kişi bir sayfaya iner ve birkaç saniye içinde karar verir: kalmak ya da çıkmak.

İyi bir açılış sayfası ne sunduğunu tek cümleyle söyler, ana butonu ilk ekranda gösterir, güven verir, soruları cevaplar ve iletişimi kolaylaştırır.

Reklamlarınıza uygun sayfaları birlikte hazırlayalım. """ + LINK),

dict(date='2026-11-16T11:00', slug='kelime-degil-niyet', pillar='arama', label='Google Ads · SEO',
 slides=[
  dict(t='cover', h='Kelimeye değil, <em>niyete</em> odaklanın.'),
  dict(t='point', k='01', h='Aynı kelime, farklı niyet', p='“Diş beyazlatma” yazan kişi fiyat da araştırıyor olabilir, evde yapılan yöntemleri de. Reklamınız hangisine cevap veriyor?'),
  dict(t='point', k='02', h='Karara yakın aramalar', p='“Fiyat”, “randevu”, “en yakın”, “hemen” gibi ifadeler genellikle karar vermek üzere olan kişiden gelir.'),
  dict(t='point', k='03', h='Bilgi arayan da değerli', p='Henüz karar vermemiş kişiye faydalı bir yazıyla ulaşmak, onu ileride müşteriniz yapabilir.'),
  dict(t='cta', h='Doğru aramaları <em>birlikte</em> seçelim.', btn='Ücretsiz anahtar kelime analizi'),
 ],
 caption="""Aynı kelimeyi yazan iki kişi aynı şeyi istemeyebilir. Biri satın almaya hazırdır, diğeri sadece bilgi topluyordur.

Google Ads'te bütçeyi karara yakın aramalara, SEO'da ise bilgi arayan kişiye cevap veren içeriklere ayırmak iki tarafı da verimli kılar.

Anahtar kelimelerinizi birlikte gözden geçirelim. """ + LINK),

dict(date='2026-11-18T11:00', slug='yeniden-hedefleme', pillar='sosyal', label='Meta reklamları',
 slides=[
  dict(t='cover', h='Sitenize girip çıkanlar <em>kaybolmadı.</em>'),
  dict(t='point', k='01', h='İlk ziyarette karar yok', p='Çoğu kişi fiyatlara bakar, başka sitelerle karşılaştırır ve sonra unutur.'),
  dict(t='point', k='02', h='Yeniden hatırlatın', p='Meta Pixel ile sitenizi ziyaret edenlere Instagram ve Facebook’ta yeniden ulaşabilirsiniz.'),
  dict(t='point', k='03', h='Aynı reklamı değil', p='Geri dönen kişiye soru cevaplayan, güven veren ya da süreli bir teklif sunan farklı bir reklam gösterin.'),
  dict(t='cta', h='Kaçan ziyaretçileri <em>geri</em> getirelim.', btn='Ücretsiz reklam analizi'),
 ],
 caption="""Sitenize girip bir şey almadan çıkan kişi kaybedilmiş bir müşteri değildir. Sadece henüz karar vermemiştir.

Yeniden hedefleme reklamlarıyla bu kişilere Instagram ve Facebook'ta tekrar ulaşabilir, ilk ziyarette aklında kalan soruları cevaplayabilirsiniz.

Kurulumunu birlikte yapalım. """ + LINK),

dict(date='2026-11-20T11:00', slug='hangi-kanal-satis', pillar='yz', label='Ölçüm',
 slides=[
  dict(t='cover', h='Hangi kanal gerçekten <em>satış</em> getiriyor?'),
  dict(t='point', k='01', h='Her platform kendini öne çıkarır', p='Google da Meta da satışı kendi hanesine yazar. Rakamları toplayınca gerçek satıştan fazlası çıkabilir.'),
  dict(t='point', k='02', h='Tek kaynak', p='Google Analytics 4 ve satış verileriniz, kanalları aynı terazide tartmanızı sağlar.'),
  dict(t='point', k='03', h='Haftalık değil, aylık bakın', p='Tek haftalık dalgalanmaya göre bütçe değiştirmek, iyi çalışan kampanyayı da bozabilir.'),
  dict(t='cta', h='Raporunuzu <em>sadeleştirelim.</em>', btn='Ücretsiz ölçüm kontrolü'),
 ],
 caption="""Google Ads paneli bir rakam söyler, Meta paneli başka bir rakam. İkisini toplayınca bazen kasaya girenden fazlası çıkar.

Bu yüzden tüm kanalları tek bir raporda, aynı ölçüyle değerlendiriyoruz. Bütçe kararları da bu rapora göre veriliyor.

Raporlamanızı birlikte kuralım. """ + LINK),

dict(date='2026-11-23T11:00', slug='kasim-indirim-hazirlik', pillar='sosyal', label='Kampanya',
 slides=[
  dict(t='cover', h='Kasım indirimlerine <em>hazır</em> mısınız?'),
  dict(t='list', h='Kampanya başlamadan önce', items=[
     'Kampanya sayfası ve indirim kodları hazır','Pixel ve dönüşüm takibi test edildi','Görseller ve metinler önceden onaylandı',
     'Yeniden hedefleme kitleleri oluşturuldu','Stok ve kargo süresi net','Günlük bütçe ve durdurma kuralları belirlendi']),
  dict(t='point', h='Son gün başlamayın', p='Reklamların bir öğrenme süreci var. Birkaç gün önce başlayan kampanya, yoğun günlerde daha verimli çalışır.'),
  dict(t='cta', h='Kampanyanızı <em>birlikte</em> kuralım.', btn='Ücretsiz kampanya planı'),
 ],
 caption="""Kasım indirim dönemi, yılın en kalabalık reklam dönemi. Hazırlıksız girilen kampanya, rakiplerle aynı anda daha pahalıya reklam vermek demek.

Sayfa, indirim kodları, ölçüm, görseller, kitleler ve bütçe kuralları kampanyadan önce hazır olmalı.

Kampanyanızı birlikte planlayalım. """ + LINK),

dict(date='2026-11-25T11:00', slug='mobil-site', pillar='web', label='Web sitesi',
 slides=[
  dict(t='cover', h='Müşterileriniz sitenize <em>telefondan</em> giriyor.'),
  dict(t='point', k='01', h='Başparmakla kullanılır', p='Butonlar kolayca dokunulacak büyüklükte, menüler sade olmalı.'),
  dict(t='point', k='02', h='Ağır görseller yavaşlatır', p='Sıkıştırılmamış fotoğraflar mobil bağlantıda sayfanın açılmasını geciktirir.'),
  dict(t='point', k='03', h='Tek dokunuşla iletişim', p='Telefon, WhatsApp ve yol tarifi butonları her sayfada kolayca ulaşılabilir olmalı.'),
  dict(t='cta', h='Sitenizi mobilde <em>test</em> edelim.', btn='Ücretsiz site analizi'),
 ],
 caption="""Sitenizi bilgisayardan değil, telefondan kontrol edin. Müşterilerinizin çoğu oradan bakıyor.

Küçük butonlar, geç açılan görseller ve bulunması zor iletişim bilgileri mobilde ziyaretçi kaybının en sık nedenleri.

Sitenizi birlikte mobilde test edelim. """ + LINK),

dict(date='2026-11-27T11:00', slug='black-friday-hatalar', pillar='sosyal', label='Kampanya',
 slides=[
  dict(t='cover', h='Black Friday’de en sık yapılan <em>4 hata</em>'),
  dict(t='point', k='01', h='Son gün başlamak', p='Rekabetin en yoğun olduğu gün reklam da pahalılaşır. Hazırlık birkaç gün önce başlamalı.'),
  dict(t='point', k='02', h='Herkese aynı reklam', p='Sitenizi daha önce ziyaret edenle sizi ilk kez görene aynı mesaj gösterilmemeli.'),
  dict(t='point', k='03', h='Ölçülmeyen kampanya', p='İndirim kodları ve satışlar takip edilmiyorsa hangi reklamın işe yaradığı bilinmez.'),
  dict(t='point', k='04', h='Belirsiz teklif', p='“Büyük indirim” yerine net oranı ve son tarihi yazın.'),
  dict(t='cta', h='Kampanyanızı <em>kontrol</em> edelim.', btn='Ücretsiz kampanya analizi'),
 ],
 caption="""Bugün Black Friday. Son dakikada kurulan kampanyalarda en sık gördüğümüz dört hata: geç başlamak, herkese aynı reklamı göstermek, sonuçları ölçmemek ve belirsiz teklifler.

Gelecek kampanyalarınızı birlikte planlayalım. """ + LINK),

dict(date='2026-11-30T11:00', slug='yapay-zeka-ozetleri', pillar='yz', label='Yapay zekâ · SEO',
 slides=[
  dict(t='cover', h='Google artık cevabı <em>kendisi</em> veriyor.'),
  dict(t='point', k='01', h='Yapay zekâ özetleri', p='Birçok aramada Google, sonuçların üstünde yapay zekâyla hazırlanmış bir özet gösteriyor.'),
  dict(t='point', k='02', h='Özette yer almak', p='Bu özetler, soruyu açık ve düzenli cevaplayan sayfalardan bilgi alır.'),
  dict(t='point', k='03', h='Ne yapmalı?', p='Sık sorulan soruları sitenizde net başlıklarla cevaplayın, yapılandırılmış veri ekleyin, içerikleri güncel tutun.'),
  dict(t='cta', h='Sitenizi yapay zekâ aramasına <em>hazırlayalım.</em>', btn='Ücretsiz SEO analizi'),
 ],
 caption="""Google'da birçok soru artık sonuç listesinden önce yapay zekâ özetiyle cevaplanıyor.

Bu özetlerde kaynak gösterilmek için sitenizin soruları açık ve düzenli cevaplaması gerekiyor. Net başlıklar, sık sorulan sorular, yapılandırılmış veri ve güncel içerik burada fark yaratıyor.

Sitenizi birlikte hazırlayalım. """ + LINK),

# ───────────── ARALIK ─────────────
dict(date='2026-12-02T11:00', slug='reklam-metni', pillar='arama', label='Google Ads',
 slides=[
  dict(t='cover', h='Tıklatan reklam metninde <em>neler</em> olur?'),
  dict(t='list', h='Metinde olması gerekenler', items=[
     'Aranan hizmetin adı','Şehir ya da bölge','Somut fayda: süre, garanti, kapsam',
     'Güven unsuru: deneyim, referans, yorumlar','Net eylem: ara, randevu al, teklif iste']),
  dict(t='point', h='Öğeleri boş bırakmayın', p='Site bağlantıları, açıklama satırları ve arama butonu reklamınızı büyütür, tıklanma ihtimalini artırır.'),
  dict(t='cta', h='Reklam metinlerinizi <em>yenileyelim.</em>', btn='Ücretsiz hesap analizi'),
 ],
 caption="""Arama sonuçlarında reklamınızın yanında birkaç rakip daha var. Kişi hangisine tıklayacağına birkaç saniyede karar veriyor.

Hizmetin adı, bölge, somut bir fayda, güven veren bir ayrıntı ve net bir eylem çağrısı bu kararı sizden yana çevirir.

Reklam metinlerinizi birlikte gözden geçirelim. """ + LINK),

dict(date='2026-12-04T11:00', slug='hedef-kitle', pillar='sosyal', label='Meta reklamları',
 slides=[
  dict(t='cover', h='Hedef kitleyi daraltmak her zaman <em>doğru</em> mu?'),
  dict(t='point', k='01', h='Fazla dar kitle pahalıdır', p='Çok sayıda ilgi alanı ve filtre eklemek, sistemin uygun kişiyi bulacağı alanı küçültür.'),
  dict(t='point', k='02', h='Görsel de hedefler', p='Meta reklamlarında reklamı kimin göreceğini büyük ölçüde görsel ve mesajın kendisi belirliyor.'),
  dict(t='point', k='03', h='Neyi sınırlamalı?', p='Konum, yaş ve dil gibi gerçek kısıtları koruyun. Gerisini test ederek genişletin.'),
  dict(t='cta', h='Kitlenizi <em>doğru</em> kuralım.', btn='Ücretsiz reklam analizi'),
 ],
 caption="""Meta reklamlarında hedef kitleyi ne kadar daraltırsanız o kadar iyi sonuç alacağınızı düşünmek kolay. Çoğu zaman tersi oluyor.

Gerçek kısıtları (konum, yaş, dil) koruyup gerisini sisteme ve görsellerinize bırakmak, daha düşük maliyetle daha çok uygun kişiye ulaşmanızı sağlayabilir.

Kitle ayarlarınızı birlikte inceleyelim. """ + LINK),

dict(date='2026-12-07T11:00', slug='llms-txt', pillar='web', label='Web sitesi · Yapay zekâ',
 slides=[
  dict(t='cover', h='Sitenizde <em>llms.txt</em> var mı?'),
  dict(t='point', k='01', h='Nedir?', p='Sitenizin ana dizinine konan, işletmenizi ve önemli sayfalarınızı yapay zekâ araçlarına özetleyen sade bir metin dosyası.'),
  dict(t='point', k='02', h='Ne işe yarar?', p='Yapay zekâ asistanları sitenizi okurken neyin önemli olduğunu bu dosyadan daha kolay anlar.'),
  dict(t='point', k='03', h='robots.txt’ten farkı', p='robots.txt neyin taranmayacağını söyler. llms.txt ise neyin önemli olduğunu anlatır.'),
  dict(t='cta', h='Sitenize <em>ekleyelim.</em>', btn='Ücretsiz site analizi'),
 ],
 caption="""llms.txt, sitenizi yapay zekâ araçlarına tanıtan küçük bir metin dosyası. Henüz yeni bir öneri ama yapay zekâ asistanlarının sitenizi doğru anlamasına yardımcı oluyor.

Kurduğumuz tüm sitelere ekliyoruz. Sitenizde yoksa birlikte hazırlayalım. """ + LINK),

dict(date='2026-12-09T11:00', slug='negatif-anahtar-kelime', pillar='arama', label='Google Ads',
 slides=[
  dict(t='cover', h='Reklamınız kimlere <em>gösterilmemeli?</em>'),
  dict(t='point', k='01', h='Negatif anahtar kelime', p='Belirlediğiniz kelimeleri içeren aramalarda reklamınızın çıkmasını engeller.'),
  dict(t='point', k='02', h='Bir örnek', p='Ücretli eğitim veren bir kurs için “bedava”, “pdf”, “iş ilanı” gibi kelimeler genellikle negatife eklenir.'),
  dict(t='point', k='03', h='Düzenli bakım', p='Arama terimleri raporu düzenli kontrol edilmeli, yeni alakasız aramalar listeye eklenmeli.'),
  dict(t='cta', h='Arama terimlerinizi <em>temizleyelim.</em>', btn='Ücretsiz hesap analizi'),
 ],
 caption="""Google Ads'te reklamınızın kime gösterileceği kadar, kime gösterilmeyeceği de önemli.

Negatif anahtar kelimeler, müşteriniz olmayacak kişilerin aramalarında reklamınızın çıkmasını engeller ve bütçenizi doğru aramalara bırakır.

Arama terimleri raporunuza birlikte bakalım. """ + LINK),

dict(date='2026-12-11T11:00', slug='tek-mesaj-gorsel', pillar='sosyal', label='Sosyal medya',
 slides=[
  dict(t='cover', h='Bir görsel, <em>bir mesaj.</em>'),
  dict(t='point', k='01', h='Göz önce neye bakmalı?', p='Her görselde tek bir odak olsun: ürün, yüz ya da tek bir cümle.'),
  dict(t='point', k='02', h='Az yazı', p='Başlık kısa olmalı. Ayrıntılar açıklamaya ya da sonraki sayfalara kalsın.'),
  dict(t='point', k='03', h='Tanınan bir dil', p='Aynı renkler ve yazı tipleri, kişinin sizi kaydırırken tanımasını sağlar.'),
  dict(t='cta', h='Görsel dilinizi <em>birlikte</em> kuralım.', btn='Ücretsiz sosyal medya analizi'),
 ],
 caption="""Akışta dikkat çeken görsellerin ortak noktası sade olmalarıdır: tek bir odak, kısa bir başlık ve tanıdık bir görsel dil.

Her şeyi tek görsele sığdırmaya çalışmak yerine bir mesaj seçin. Gerisi açıklamada ya da sonraki sayfalarda kalsın.

Görsel dilinizi birlikte oluşturalım. """ + LINK),

dict(date='2026-12-14T11:00', slug='2027-butce-plani', pillar='yz', label='Planlama',
 slides=[
  dict(t='cover', h='2027 bütçesini yapmadan <em>önce</em>'),
  dict(t='list', h='Bu yılın verisine sorun', items=[
     'Hangi kanal en düşük maliyetle müşteri getirdi?','Hangi aylarda talep arttı?','Hangi hizmet ya da ürün daha kârlı?',
     'Hangi reklamlar hiç sonuç getirmedi?','Siteye gelenlerin ne kadarı iletişime geçti?']),
  dict(t='point', h='Plan geçmiş veriyle başlar', p='Bütçeyi tahmine göre değil, bu yıl ölçtüğünüz sonuçlara göre dağıtın.'),
  dict(t='cta', h='2027 planınızı <em>birlikte</em> yapalım.', btn='Ücretsiz dijital analiz'),
 ],
 caption="""Yeni yılın pazarlama bütçesini yaparken en iyi kaynak, bu yılın verisi.

Hangi kanal müşteri getirdi, hangi aylar yoğundu, hangi reklamlar sonuç vermedi? Bu soruların cevabı 2027'de bütçenin nereye gideceğini belirler.

Planınızı birlikte hazırlayalım. """ + LINK),

dict(date='2026-12-16T11:00', slug='yerel-seo', pillar='arama', label='Yerel SEO',
 slides=[
  dict(t='cover', h='“Yakınımdaki” aramalarında <em>siz</em> var mısınız?'),
  dict(t='point', k='01', h='Tutarlı bilgiler', p='İşletme adı, adres ve telefon sitenizde, haritada ve rehberlerde aynı şekilde yazılmalı.'),
  dict(t='point', k='02', h='Bölge sayfaları', p='Birden fazla bölgeye hizmet veriyorsanız her bölge için gerçek bilgiler içeren ayrı sayfalar hazırlayın.'),
  dict(t='point', k='03', h='Yorumlar', p='Düzenli gelen ve yanıtlanan yorumlar hem güven verir hem de haritadaki görünürlüğünüzü destekler.'),
  dict(t='cta', h='Yerel görünürlüğünüzü <em>artıralım.</em>', btn='Ücretsiz yerel SEO analizi'),
 ],
 caption="""Yerel bir işletmeyseniz müşterilerinizin çoğu sizi “yakınımdaki” aramalarıyla bulur.

Tutarlı iletişim bilgileri, hizmet verdiğiniz bölgeler için ayrı sayfalar ve düzenli yanıtlanan yorumlar bu aramalarda öne çıkmanızı sağlar.

Yerel SEO durumunuza birlikte bakalım. """ + LINK),

dict(date='2026-12-18T11:00', slug='ajans-secerken', pillar='arama', label='Adsaturn',
 slides=[
  dict(t='cover', h='Ajans seçmeden önce <em>sorun.</em>'),
  dict(t='list', h='Cevabını bilmeniz gerekenler', items=[
     'Reklam hesapları kimin adına açılacak?','Sonuçlar hangi araçla ölçülecek?','Rapor ne sıklıkla gelecek?',
     'Bütçe kararlarını kim verecek?','Çalışma bitince verilerim bende kalacak mı?','Benzer işletmelerle çalıştınız mı?']),
  dict(t='point', h='Bizim cevabımız', p='Hesaplar sizin adınıza açılır. Ölçüm kurulmadan reklam yayına girmez. Tüm kanallar tek raporda toplanır.'),
  dict(t='cta', h='Tanışalım.', btn='Ücretsiz dijital analiz'),
 ],
 caption="""Bir ajansla çalışmaya başlamadan önce sorulması gereken birkaç soru var. Hesaplar kimin adına açılacak, sonuçlar nasıl ölçülecek, rapor ne sıklıkla gelecek, çalışma bittiğinde verileriniz sizde kalacak mı?

Bizde hesaplar sizin adınıza açılır, ölçüm kurulmadan reklam yayına girmez ve tüm kanallar tek raporda toplanır.

Tanışmak için """ + LINK[0].lower() + LINK[1:]),

dict(date='2026-12-21T11:00', slug='yil-sonu-site-bakimi', pillar='web', label='Web sitesi',
 slides=[
  dict(t='cover', h='Sitenize <em>yıl sonu</em> bakımı'),
  dict(t='list', h='Yeni yıldan önce', items=[
     'Kırık bağlantıları düzeltin','Eski kampanya ve fiyatları kaldırın','Çalışma saatlerini ve iletişim bilgilerini güncelleyin',
     'Alt bilgideki yılı 2027 yapın','Formları test edin','Yedek alın, eklentileri güncelleyin']),
  dict(t='point', h='Küçük ayrıntı, büyük güven', p='Alt bilgisinde iki yıl önceki tarih yazan bir site, ziyaretçiye “burası hâlâ açık mı?” diye düşündürür.'),
  dict(t='cta', h='Bakımı biz <em>yapalım.</em>', btn='Ücretsiz site analizi'),
 ],
 caption="""Yeni yıla girmeden sitenize kısa bir bakım yapmanın tam zamanı.

Kırık bağlantılar, geçmiş kampanyalar, eski çalışma saatleri, alt bilgideki eski yıl ve çalışmayan formlar ziyaretçinin güvenini sessizce azaltır.

Bakım listesini birlikte tamamlayalım. """ + LINK),

dict(date='2026-12-23T11:00', slug='son-adimda-vazgecme', pillar='sosyal', label='Tüketici davranışı',
 slides=[
  dict(t='cover', h='Müşteri neden son adımda <em>vazgeçer?</em>'),
  dict(t='point', k='01', h='Beklenmeyen maliyet', p='Kargo ya da ek ücret son ekranda çıkınca güven sarsılır.'),
  dict(t='point', k='02', h='Fazla soru', p='Her ek form alanı, devam etmek için bir neden daha ister.'),
  dict(t='point', k='03', h='Belirsizlik', p='Teslim süresi, iade ya da iptal koşulları belli değilse karar ertelenir.'),
  dict(t='point', k='04', h='Güven eksikliği', p='İlk kez alışveriş yapan kişi yorum, garanti ve gerçek iletişim bilgisi arar.'),
  dict(t='cta', h='Satın alma yolunuzu <em>inceleyelim.</em>', btn='Ücretsiz site analizi'),
 ],
 caption="""Sepete ekleyip almadan çıkan, formu doldurmaya başlayıp bırakan kişi aslında çok yaklaşmıştı.

Son adımda vazgeçmenin arkasında genellikle dört şey var: beklenmeyen maliyet, fazla soru, belirsizlik ve güven eksikliği. Dördü de sayfada yapılacak düzenlemelerle azaltılabilir.

Satın alma ya da başvuru adımlarınızı birlikte inceleyelim. """ + LINK),

dict(date='2026-12-25T11:00', slug='yapay-zeka-icerik', pillar='yz', label='Yapay zekâ',
 slides=[
  dict(t='cover', h='Yapay zekâ içerik yazar ama <em>sizi</em> tanımaz.'),
  dict(t='point', k='01', h='Hız kazandırır', p='Taslak, fikir listesi ve farklı başlık denemeleri için zaman kazandırır.'),
  dict(t='point', k='02', h='Deneyimi yazamaz', p='Müşterilerinizle yaşadığınız gerçek örnekler ve kendi bakış açınız ancak sizden gelir.'),
  dict(t='point', k='03', h='Kontrol şart', p='Yayına giden her metni doğruluk, marka dili ve yasal uygunluk açısından bir insan okumalı.'),
  dict(t='cta', h='İçerik sürecinizi <em>birlikte</em> kuralım.', btn='Ücretsiz içerik analizi'),
 ],
 caption="""Yapay zekâ araçları içerik üretimini hızlandırıyor. Ama işletmenizi, müşterilerinizi ve sizi farklı kılan deneyimi bilmiyorlar.

En iyi sonuç ikisini birlikte kullanınca çıkıyor: hız için yapay zekâ, doğruluk ve özgünlük için insan.

İçerik sürecinizi birlikte kuralım. """ + LINK),

dict(date='2026-12-28T11:00', slug='nasil-calisiyoruz', pillar='arama', label='Adsaturn',
 slides=[
  dict(t='cover', h='Adsaturn ile çalışmak <em>nasıl</em> başlar?'),
  dict(t='list', h='Dört adım', numbered=True, items=[
     'Ücretsiz analiz: sitenize, reklam ve sosyal medya hesaplarınıza bakarız.',
     'Plan: hangi kanalın hangi bütçeyle kullanılacağını birlikte belirleriz.',
     'Kurulum: ölçüm, kampanyalar ve gerekiyorsa site hazırlanır.',
     'Yönetim ve rapor: kampanyalar düzenli iyileştirilir, sonuçlar tek raporda paylaşılır.']),
  dict(t='cta', h='Ücretsiz analizle <em>başlayalım.</em>', btn='Ücretsiz dijital analiz'),
 ],
 caption="""Bizimle çalışmak ücretsiz bir analizle başlar. Sitenize, reklam ve sosyal medya hesaplarınıza bakar, neyin çalıştığını ve neyin eksik olduğunu anlatırız.

Ardından planı birlikte yapar, ölçümü ve kampanyaları kurar, sonuçları her ay tek bir raporda paylaşırız.

2027'ye birlikte başlamak için """ + LINK[0].lower() + LINK[1:]),

dict(date='2026-12-31T11:00', slug='yeni-yil', pillar='arama', label='',
 slides=[dict(t='holiday', kind='yeniyil')],
 caption="""2027'de sizi arayan müşterilerle buluşmanız dileğiyle. Yeni yılınız kutlu olsun.

#yeniyıl #2027 #adsaturn"""),
]
