# İlk yayın: Son birkaç gündeki işi tekrar uygulanabilir bir sürece çevirmek

**Yayının konusu:** Özellikle 8 Eylül 2026 konuşmaları ve son 3–4 gündeki kurulum deneyimi üzerinden, bir işin kapsamını belirlemekten sonucunu kontrol edip devretmeye kadar nasıl yürütüldüğünü göstermek.

**İzleyicinin kazanımı:** Kendi işinde tekrar kullanabileceği yedi adım: **kapsam ve brif → kaynak envanteri → insan kararları → görev dağıtımı → uygulama → geri okuma ve kabul → devir**.

Bu yedi başlık yayındaki anlatımın omurgasıdır. Ayrıntılı protokol pilot seçimini, kontrol edilen çıktının teslimini veya izinli yayını ve gerçek tekrarın değerlendirilmesini ayrıca açar. Prova sırasında teslim edilen dosya da yeniden açılır; dış platformda yayın yapılmayan örnekte yayın tamamlandı diye kaydedilmez.

**Sürümün durumu:** Gerçek çalışmalar aşağıdaki kaynak bölümünde anlatılıyor. Bunlardan çıkarılan [tekrar edilebilir protokol](../rehber/07-tekrar-edilebilir-protokol.md), bu paket için hazırlanmış profesyonel uygulama önerisidir. Başka bir kişinin kendi işinde yaptığı ilk uçtan uca tekrar henüz sınanmadı. Yayındaki kurmaca prova, bu sınamayı yapılmış saydırmaz.

Teknik bilgisi sınırlı biri veya küçük bir ekip, dosyaları bir metin düzenleyicide açarak ve erişebildiği bir AI sohbetini kullanarak yayını takip edebilir. Ek araç aboneliği gerekmez. AI erişimi yoksa önceden hazırlanmış prova üzerinden aynı kararlar ve kontroller gösterilir.

## İlk 90 saniye: Okunabilir açılış

> Son birkaç gündür web siteleri, hesaplar ve AI araçlarıyla oldukça yoğun bir çalışma yaptık. Özellikle bugün sosyal medya, haber, reklam ve iş platformlarıyla ilgili birçok parçayı bir araya getirdik. Profilleri hazırladık, hangi hesabın ne durumda olduğunu topladık, yaptığımız işleri ve kullanılan dosyaları birbirine bağladık.
>
> Bu düzen işimi ve hayatımı kolaylaştırdı; nasıl kurduğumu birlikte göstermek istiyorum. Bunu paylaşmak istememin nedeni de şu: Belki sizin de elinizde birçok hesap, yarım kalmış iş ve nereden devam edeceğinizi bilmediğiniz notlar var. Bizim yaşadığımız süreci, kendi işinize uygulayabileceğiniz kadar açık hale getirmek istiyorum.
>
> Önce gerçekten ne yaptığımızı ve hangi kısmın hâlâ açık olduğunu göstereceğim. Sonra kurmaca bir örnekte aynı adımları sırayla uygulayacağız: işi tarif edeceğiz, kaynakları toplayacağız, kararları vereceğiz, işi parçalara ayıracağız, bir çıktı üreteceğiz, sonucu yeniden okuyup kontrol edeceğiz ve devam kaydı bırakacağız.
>
> Burada gösterdiğim tekrar yöntemi henüz başka bir kişinin işi üzerinde baştan sona sınanmadı. Bugün elimizdeki deneyimden çıkarılmış ilk profesyonel öneriyi birlikte prova ediyoruz. Dosyaları GitHub’dan alıp kendi işinizde deneyebileceksiniz. Yayın sonunda elinizde, hangi işi nasıl yürüttüğünüzü ve nereden devam edeceğinizi gösteren bir kayıt olsun istiyorum.

## Ekranda kullanılacak paket

Yalnızca kamuya hazırlanmış bu paketin bulunduğu pencereyi paylaş. Gerçek hesaplara giriş yapmak yerine aşağıdaki deneyim özeti ve kurmaca kayıtlar gösterilir. Bildirimleri kapat; AI demosu için boş bir konuşma aç. Dosyaları yerelde de açık tut.

| Dosya | Yayındaki görevi |
| --- | --- |
| [Gerçek deneyim](../rehber/03-gercek-deneyim.md) | Son günlerin çalışmasını doğrulanan sonuçları ve açık kalanlarıyla anlatmak |
| [Tekrar edilebilir protokol](../rehber/07-tekrar-edilebilir-protokol.md) | Yedi aşamanın girdisini, kararını ve bitiş koşulunu göstermek |
| [Akışın tamamı — kurmaca prova](../ornekler/prova/akisin-tamami.md) | Kapsamdan devre kadar tek örnek üzerinde çalışmak ve bağlantı aksarsa devam etmek |
| [Görev brifi](../sablonlar/gorev-brifi.md) | Provanın iş tanımını kaydetmek |
| [Ana profil](../sablonlar/ana-profil.md) ve [platform kartı](../sablonlar/platform-karti.md) | Prova gerektiriyorsa uygulama aşamasının bir alt çıktısını hazırlamak |
| [Kapanış](../sablonlar/kapanis.md) | Sonucu, kanıtı, eksikleri ve sonraki ilk adımı devretmek |
| [Kısa profil demosu](../ornekler/ilk-demo/girdi.md) ve [beklenen çıktı](../ornekler/ilk-demo/beklenen-cikti.md) | Profil uyarlama adımını ayrıca göstermek gerekirse kullanmak |

Prova dosyasının bir çalışma kopyasını aç. AI'ya [girdi.md](../ornekler/ilk-demo/girdi.md) dosyasının tamamını ve prova dosyasındaki **“0. İş ve insan kararı”** bölümünü birlikte ver. Bir link yapıştırmak, bağlantıdaki metnin okunduğunu garanti etmez; düz sohbette bu iki metni kopyala. Önce kendi karar ve çıktıları üzerinde çalış, ardından hazır örnekle karşılaştır. Kopyaya eklenen yeni varsayımlar kurmaca diye etiketlenir. Kaynak paketteki gerçek deneyim kayıtları bu provaya göre değiştirilmez.

## 60 dakikalık akış

| Süre | Ekranda yapılan iş | Somut sonuç |
| --- | --- | --- |
| 00:00–05:00 | Açılış; deneyim, önerilen yöntem ve kurmaca prova ayrımını açıkla. | Yayının amacı ve iddiaların sınırı |
| 05:00–15:00 | Aşağıdaki gerçek süreci adım adım deneyim dosyasından göster. | Son birkaç günlük işten çıkarılmış beş ders |
| 15:00–20:00 | Provanın girdisini oku; Yayın komutu 1 ile kapsamı ve brifi çıkar. | Neyi bitireceği belli bir iş |
| 20:00–26:00 | Yayın komutu 2 ile kaynakları ve insan kararlarını ayır; örnekte gerekli kararları açıkça ver. | Kullanılabilir kaynaklar, eksikler ve karar kaydı |
| 26:00–32:00 | Yayın komutu 3 ile bağımlılıkları ve görev dağıtımını yaz. | Kimin neyi, hangi sırayla yapacağı |
| 32:00–43:00 | Yayın komutu 4 ile provanın ana profil ve iki metin görevini sırayla uygula; çıktıları dosyaya aktar. | Açılabilen, incelenebilir üç metin |
| 43:00–53:00 | Yayın komutu 5 ile çıktıyı yeniden açıp kaynak ve kabul koşullarıyla karşılaştır; bir hatayı düzelt; örnekteki teslim dosyasını aç. | Kabul ve teslim sonucu veya açık kalma nedeni |
| 53:00–58:00 | Yayın komutu 6 ile devir kaydı yaz; önceki sohbeti okumadan ilk sonraki adımı bulmayı dene. | Sonraki oturumun başlayabileceği kayıt |
| 58:00–60:00 | İzleyiciye kendi tekrarını nasıl başlatacağını göster; kaynak bağlantısını hatırlat. | Kendi işi için tek bir brif yazma adımı |

Zaman daralırsa uygulamanın ikinci çıktısını hazır provadan göster. Kapsamı, insan kararını, geri okumayı ve devri koru. Canlı yayında tüm hesapları veya bütün düzeni yeniden kurmayı vaat etme; bir işin tam döngüsünü göster.

## Gerçek süreci adım adım anlatmak: 10 dakika

Bu bölüm [gerçek deneyim kaydının](../rehber/03-gercek-deneyim.md) anlatımıdır. Başlangıçta 5 Eylül'deki neden/kanıt beklentisini ve 6 Eylül'deki dört gönderilik taslak paketi kısaca göster; önceki hazırlığın yeni işe girdi olduğunu anlat. Ardından aşağıdaki beş parçaya geç. Bu sıralama deneyimi açıklamak içindir; bütün işlemlerin tarihsel olarak tam bu sırada gerçekleştiği iddiası taşımaz.

| Gösterilecek örnek | Söylenecek ana nokta | Tekrara taşınacak ders |
| --- | --- | --- |
| Hesap ve profillerden kalıcı iş kayıtlarına genişleyen kapsam | “İhtiyaç çalışırken büyüdü. Hesapların durumunu, yapılan işi ve sonraki adımı birlikte takip etmemiz gerekti.” | Kapsam değişince brifi ve bitiş koşulunu güncelle. |
| 31 hesap kaydı, 30 ayrı hesap platformu ve 11 araç kaydı | “Bu sayılar envanteri anlatıyor. Araç kayıtlarının 10’unda erişim ölçülmemiş; listede olması çalıştığını kanıtlamıyor.” | Keşfedilen, erişilen, hazırlanmış ve sonucu ölçülmüş kayıtları ayır. |
| Bir gerçek portföy vakasının yedi mevcut platform kaydıyla eşleştirilmesi | “Aynı kaynak dosyaları farklı hedeflerde takip ettik. Yedi ayrı proje üretildiğini veya yedisinin bu turda ilk kez yayımlandığını söylemiyoruz.” | Kaynak, türev ve hedef kaydı arasındaki bağı koru; belirsiz sonuçta yeniden göndermeden mevcut kaydı kontrol et. |
| Mevcut görev, proje, hesap ve varlık kayıtlarını okuyan yerel pano | “Pano için ayrı bir görev veritabanı açılmadı; mevcut kayıtlar görünür hale getirildi. 13 yerel kontrol geçti.” | Bir görünüm hazırlarken hangi kaydın asıl kaynak olduğunu açık tut; yerel testin kapsamını yaz. |
| Kaydedilmiş takip rutini ve açık kabul adımları | “09.00/19.00 takibi kayıtlı ve etkin; ilk planlı koşunun tamamlandığı henüz kanıtlanmış değil. Dijital kalite kontrolü ile fiziksel baskı kabulü de ayrı.” | Yapılandırma, fiilî çalışma ve nihai kabul için ayrı kanıt iste; açık işi devir kaydında bırak. |

İnsan kararını görünür kılmak için kapsam dışına çıkarılan platformun kendiliğinden tekrar görev listesine dönmemesi örneğini anlat. Görev dağıtımında bağımsız araştırma ve taslakların ayrılabildiğini, aynı tarayıcı arayüzünü eşzamanlı değiştirmenin ise çakışma yarattığını belirt. İzleyici bu yöntemi tek AI sohbetiyle de uygulayabilir; birden çok ajan şart değildir.

## Prova komutları

Bu altı komut yayın akışına özeldir; [komutlar dosyasındaki](../komutlar/README.md) numaralı komutlarla karıştırmamak için “yayın komutu” diye anılır. Köşeli parantezli alanlara belirtilen metni yapıştır. Senaryo için [kurmaca prova dosyasını](../ornekler/prova/akisin-tamami.md) esas al; Deniz / Örnek Atölye’ye kaynakta bulunmayan müşteri, gelir veya başarı ekleme. Her komut önceki aşamanın insan tarafından kontrol edilmiş kaydını kullanır.

### Yayın komutu 1 — Kapsam ve brif

```text
Aşağıdaki kurmaca senaryoda yapılacak işi netleştir.
Şu başlıklarla kısa bir brif oluştur:
Amaç | Başlangıç durumu | Kapsama dahil işler | Kapsam dışı işler |
Beklenen çıktılar | Bitti diyebilmek için gereken kanıt | Açık sorular.

Kaynakta karar verilmemiş konuyu karar verilmiş gibi yazma.
Kapsamı yeni araçlar veya yeni hesaplar ekleyerek büyütme.
Çıktı hazırlamayı, platformda yayımlamayı ve sonucunu ölçmeyi ayrı aşamalar olarak yaz.

SENARYO GİRDİSİ:
[ilk-demo/girdi.md dosyasının tamamı + akisin-tamami.md içindeki 0. İş ve insan kararı bölümü]
```

**Beklenen çıktı:** Yapılacak iş ve kapsam dışı konular anlaşılır. Bitiş koşulu “AI cevap verdi” şeklinde kalmaz; açılıp kontrol edilebilecek bir sonuç ister.

### Yayın komutu 2 — Kaynak envanteri ve insan kararları

```text
Aşağıdaki brif ve senaryo için iki kısa tablo çıkar.

1. Kaynak | Hangi işte kullanılacak | Bilinen durum | Eksik bilgi.
2. Verilmesi gereken insan kararı | Seçenekler | Kararı vermeden ilerleyebilen iş.

Hesap veya araç listesinde bulunmak erişim kanıtı değildir.
Bir bilgi kaynağını, ondan türetilen çıktıdan ayır.
Kişisel kavramsal çalışmayı müşteri işi gibi gösterme.
Tercih, kapsam, dışarıya yayın veya çelişen bilgi konusunda kullanıcı adına karar uydurma.
Eksik bilgi gerektirmeyen işleri belirt.

KONTROL EDİLMİŞ BRİF VE SENARYO:
[Önceki brif ve senaryo girdisi]
```

**Beklenen çıktı:** Kaynaklar ve eksikler görünür. Sunucu örnekteki kararları yüksek sesle verir ve kaydeder: “Bu provada şu çıktıyı hazırlıyoruz; yayın aşaması kapsamda değil.” Gerçek hayatta karar zaten verilmişse yeniden onay istemek yerine mevcut kararın kaydı kullanılır.

### Yayın komutu 3 — Görev dağıtımı

```text
Aşağıdaki kontrol edilmiş brif, kaynak envanteri ve insan kararlarından görev planı çıkar.
En fazla beş görev kullan.

Her görev için yaz:
Görev | Sorumlu rol | Girdi | Önce tamamlanması gereken iş |
Teslim edilecek çıktı | Kabul kontrolü.

Bağımsız araştırma veya taslak işleri ayrılabilir.
Aynı dosyayı veya aynı hesap arayüzünü değiştiren işlere tek sorumlu ata.
Karar ve kabul sorumlusu insan olsun; AI araştırma, taslak veya uygulama desteği verebilir.
Ek ajan veya araç gerektirmeden sırayla yürütülebilecek plan yaz.

KAYITLAR:
[Kontrol edilmiş brif, envanter ve karar kaydı]
```

**Beklenen çıktı:** Bir sonraki görev seçilebilir; çıktının hangi kaynaktan geleceği ve kimin kontrol edeceği belli olur.

### Yayın komutu 4 — Uygulama

```text
Aşağıdaki görev planında girdileri hazır olan ilk uygulama görevini yap.
Yalnızca bu görevin kabul edilen kapsamı içinde üret.
Bir kaydı veya platformu gerçekten değiştirmediysen değiştirdiğini söyleme.
Görsel verilmediyse görmüş gibi değerlendirme.

Yanıtın:
1. Görevin doğrudan kullanılabilecek çıktısı.
2. Kullanılan kaynakların kısa listesi.
3. Eksikler ve kontrol edilmesi gereken noktalar.

GÖREV VE GİRDİLER:
[Seçilmiş görev, brif ve görev için gereken kaynaklar]
```

**Beklenen çıktı:** Planın tanımladığı somut taslak oluşur. Tam provada önce ana profil, ardından 60–90 kelimelik portföy tanıtımı ve en fazla 45 kelimelik kısa paylaşım hazırlanır. Komut gerektiğinde sıradaki görev için yeniden kullanılır. Bu uzunluklar demo tercihidir. Sunucu çıktıları çalışma kaydına alır ve tekrar açar; ardından kabul ve devir aşamalarına geçer.

### Yayın komutu 5 — Geri okuma ve kabul

```text
Aşağıdaki kaydedilmiş çıktıyı brifin kabul koşulları ve kaynaklarla karşılaştır.
Şu tabloyu oluştur:
Koşul | Çıktıda görülen kanıt | Sonuç: geçti / kaldı / ölçülmedi | Gerekli işlem.

Sadece gerçekten verilen veya yeniden okunmuş sonucu değerlendir.
Kaynakta olmayan müşteri, ticari sonuç veya tamamlanma iddiasını işaretle.
Taslağın hazır olması, dış platformda yayında olması ve sonuç vermesi ayrı durumlardır.
Herhangi birini diğerinin kanıtı sayma.
Son karar için insanın bakması gereken noktayı belirt.

KABUL KOŞULLARI, KAYNAKLAR VE YENİDEN AÇILMIŞ ÇIKTI:
[Brifin ilgili bölümü, kaynak ve kaydedilmiş çıktı]
```

**Beklenen çıktı:** Kaynakla eşleşen çıktı kabul edilir veya açık kalma nedeni yazılır. AI’ın değerlendirmesini sunucu kaynak ve dosyayla karşılaştırır.

Hata oluşmadıysa **kasıtlı hatalı örnek** etiketiyle bir devir satırı göster: “Tanıtım dosyası hazırlandı; bütün hesaplar güncellendi ve iş tamamlandı.” Kaynak yalnızca yerel taslağı destekliyorsa düzelt: “Tanıtım taslağı hazırlandı ve dosyada kontrol edildi. Hesaplara uygulama yapılmadı; kapsamda bulunan sonraki işlem açık.”

### Yayın komutu 6 — Devir

```text
Aşağıdaki gerçek prova sonuçlarından kısa bir devir kaydı oluştur:
Tamamlanan iş | Çıktının dosyası veya görüldüğü yer | Yapılan kontrol |
İnsan kararı | Açık kalan | Sonraki tek adım | Yeniden bakılması gereken kaynak.

Sadece gerçekten tamamlanan işleri tamamlandı olarak yaz.
Planlı bir kontrolün kurulmasını, o kontrolün fiilen çalışmasıyla karıştırma.
Bu kayıt okununca bütün eski sohbeti açmadan ilk sonraki işe başlanabilsin.
Sonunda, eksik bilgi yüzünden ilk adıma başlanamıyorsa bunu açıkça belirt.

PROVADA GERÇEKLEŞENLER:
[Yayında yapılan işler, kaydedilmiş çıktı ve kabul kontrolünün sonucu]
```

**Beklenen çıktı:** Yeni bir oturumda neyin hazır, neyin açık olduğu ve nereden devam edileceği anlaşılır. Son iki dakikada brifi kapatıp yalnızca devir kaydından ilk işi bulmayı dene. Bu küçük kontrol, başka birinin bağımsız tekrarının yerine geçmez.

## Bağlantı veya AI aksarsa

Bir denemeden sonra yerelde açık olan [tam prova dosyasına](../ornekler/prova/akisin-tamami.md) geç:

> “Canlı yanıt şu anda gelmiyor. Bu örneğin önceden hazırlanmış provası açık. Aynı karar ve kabul adımlarını onun üzerinde uygulayarak devam edeceğim.”

O anki aşamanın bölümünü göster. Kapsam aşamasındaysan bir dışarıda bırakılan işi, envanterdeysen bir eksik kaynağı, dağıtımda bir bağımlılığı, uygulamada gerçek çıktıyı seç. Kabulde kaynağı ve çıktı satırını karşılaştır. Devirde kaydı, yayında gerçekten yapılanlara göre değiştir. Hazır provayı o anda üretilmiş veya gerçek hesaplara uygulanmış gibi sunma.

## İzleyicinin ilk gerçek tekrarı

> “Kendi işinizde sık sık yarım kalan tek bir görevi seçin. Önce amacını, elinizdeki kaynakları ve bittiğinde neyi görmeniz gerektiğini yazın. Sonra bu yedi aşamayı izleyin. Hangi aşamada durduğunuzu, hangi kararı sizin vermeniz gerektiğini ve neyin eksik kaldığını kaydedin. Bu yöntemin işe yarayan ve değişmesi gereken taraflarını gerçek tekrarlarla görebileceğiz.”

Yayın açıklamasına depo bağlantısı eklenir: [github.com/AlperenKayalar/ai-ile-calisma-duzeni](https://github.com/AlperenKayalar/ai-ile-calisma-duzeni). İzleyicinin başlangıç dosyası [tekrar edilebilir protokol](../rehber/07-tekrar-edilebilir-protokol.md), karşılaştırma dosyası [kurmaca tam prova](../ornekler/prova/akisin-tamami.md) olur.
