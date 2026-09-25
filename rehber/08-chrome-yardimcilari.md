# Açık araçları çalışma arkadaşına dönüştür

**9 Eylül 2026 ek incelemesi.** Kullanıcının Chrome'da açık araçları da düzene katma isteği üzerine hazırlandı. Bu bölüm, 8 Eylül tarihli deneyim kesitine sonradan eklenen ayrı bir gözlemdir.

Ana yürütücü işi tarif eder, uygun araca sınırlı bir parça verir ve dönen sonucu aynı iş kaydında toplar. Görsel araca görsel brifi, video aracına hareket brifi, site aracına kullanıcı akışı gider. Sonucun kabulü iş sahibinde kalır.

## Gerçekte ne görüldü?

İnceleme sırasında Chrome'un sunduğu 10 açık sekmenin yedisi aşağıdaki yardımcı araçlardı. Diğer üçü mevcut GitHub sayfası, bir yazı önizlemesi ve boş sekmeydi. Bu anlık sayı, geçmişte kaydedilen hesap ve sekme toplamlarının güncellemesi değildir; tüm cihazlar veya profiller taranmadı.

Sekmelerin sayfa içeriği okundu. Bazı sekmeler doğrudan okunamayınca Chrome'un kendi arayüzünden seçilip incelendi. Üretim, gönderim, hesap kurulumu veya yeni bağlantı yapılmadı. Sekmeler açık bırakıldı.

| Araç | Bu oturumda görülen | Çalışma düzenindeki olası rol | Sonraki doğrulama |
|---|---|---|---|
| [Ollama](https://ollama.com/) | Hesap kullanım ekranı, yerel/bulut başlangıç açıklamaları | Küçük metinleri sınıflandırma, görev çıkarma veya ikinci okuma için model çalıştırma adayı | Bu makinede çalışan hizmet/model ve seçilen yolun yerel mi bulut mu olduğunu gerçek bir küçük görevle doğrula |
| [Higgsfield](https://higgsfield.ai/) | Hesap menüsü, varlık alanı, görsel/video ve MCP & CLI bağlantıları | Bir sahnenin görsel yönünü veya hareket varyantını üretme adayı | Seçilen üretim ekranı, kullanılacak kredi ve çıkan dosyanın brife uyumu |
| [Runway](https://runway.com/) | Hesap çalışma alanı, referans ekleme ve istem alanı, video/kampanya seçenekleri | Seçilmiş görsel veya klipten kısa video taslağı üretme adayı | Tek klibin üretilmesi, dışa aktarılması ve baştan sona kontrolü |
| [Tripo](https://www.tripo3d.ai/) | Hesapla karşılayan ana sayfa, görsel seçme, oluşturma ve 3D çalışma alanı | Görsel referanstan incelenebilir 3D taslak adayı | Dosyanın hedef 3D uygulamasında açılması, geometri ve ölçek kontrolü |
| [Lovable](https://lovable.dev/) | Mevcut portföy şablonu projesi ve önizleme; kişiselleştirme sorusu açık | Tek bir web akışını prototipleme adayı | Şablon içeriğini kaynakla değiştirme, bağlantı ve mobil görünümü deneme |
| [WASK](https://www.wask.co/) | İşletme adı, kategori, büyüklük, reklam harcaması ve telefon isteyen başlangıç formu; devam düğmesi pasif | Hesap kurulumu sonrası reklam hazırlığı ve ölçüm yardımcısı adayı | Gerçek işletme bilgileri, hesap/ölçüm erişimi ve belirli kampanya görevi |
| [Instantly](https://instantly.ai/) | Başlangıç akışının ilk adımı; “nasıl buldun?” sorusu, devam düğmesi pasif | Hesap kurulumu sonrası müşteri erişimi hazırlığı adayı | Gönderici erişimi, belirli alıcılar ve onaylı mesajla kontrollü kullanım |

Lovable önizlemesindeki örnek kişi ve stüdyo metinleri henüz kullanıcıya ait içerik sayılmadı. WASK ve Instantly'nin başlangıç ekranlarına ulaşılması kampanya veya gönderim bağlantısının hazır olduğunu göstermiyor. Ollama'nın web hesabı da bilgisayarda yerel model çalıştığını göstermiyor.

Bu tablo bir fiyat veya ürün sıralaması değildir. Görülen arayüz, bu hesap ve tarihteki durumdur. Tam hesap adresleri, özel proje bağlantıları, erişim belirteçleri ve ham ekran dökümleri eğitim paketine alınmadı.

## Yardımcıya verilecek iş

Her satır aşağıda **önerilen denemedir**; bu incelemede üretilmiş çıktı değildir. İlk işte ihtiyacı karşılayan tek aracı seçmek yeterli.

| Yardımcı | Verilecek girdi | İstenecek teslim | Kontrol edenin bakacağı şey |
|---|---|---|---|
| Ollama | Kısa paylaşılabilir metin ve çıkarılacak alanlar | Görev/etiket önerileri ve belirsizler | Kaynakta olmayan görev eklenmiş mi; kullanılan model ve yerel/bulut yolu kayıtlı mı? |
| Higgsfield | Sahne, amaç, izinli referans, korunacak ürün özellikleri | Tek görsel veya hareket varyantı | Ürün biçimi, kadraj, ışık ve brif tutarlılığı |
| Runway | Seçilmiş görsel/klip, hareket tarifi, hedef süre ve kadraj | Tek kısa klip | Başlangıç/orta/son tutarlılığı, ürün bozulması ve gerçek dosya süresi |
| Tripo | Referans görsel, kullanım amacı ve hedef uygulama | Açılabilen 3D taslak | Geometri, eksik parçalar, ölçek ve hedef kullanıma uygunluk |
| Lovable | Doğrulanmış metin/varlıklar, tek kullanıcı görevi | Tıklanabilir tek akış | Metinlerin kaynağı, buton hedefleri, mobil görünüm, boş/hata durumları |
| WASK | Kampanya amacı, kitle, teklif, açılış sayfası ve ölçüm planı | Kampanya hazırlığı veya erişilebilir raporun incelemesi | Tıklama, talep ve satışın ayrı ölçülmesi; sonuç iddiasının rapora dayanması |
| Instantly | Seçilmiş alıcı kapsamı, doğrulanmış bağlam ve hizmet teklifi | İncelenebilir mesaj taslağı | Yanlış kişiselleştirme, uydurulmuş temas geçmişi ve gönderim kapsamı |

Tek bir görev kaydı kullan: **girdi → araç → gerçek çıktı → kontrol → kabul → sonraki adım**. [Yardımcı görev kartını](../sablonlar/yardimci-gorev-karti.md) mevcut iş kaydına ekleyebilirsin. Platform başına ayrı görev sistemi kurmak gerekmez.

## Erişim yolunu açık yaz

**Tarayıcı üzerinden çalışma:** Yürütücü mevcut oturumu açar, görünür alanlarla çalışır ve sonucu geri okur. Bu incelemede yedi aracın yalnız ekranları okunabildi.

**API, MCP veya CLI üzerinden çalışma:** Kurulu bağlantı, doğru hesap, yetki kapsamı, çalıştırılan görev ve geri alınan çıktı ayrıca doğrulanır. Bir sitede “MCP” menüsü görünmesi, ana yürütücünün o aracı çağırabildiği anlamına gelmez. Bu incelemede yedi araç için yeni API/MCP/CLI bağlantısı kurulmadı veya sınanmadı.

**Elle aktarım:** Otomatik yol yoksa iş sahibi aynı brifi araca verebilir ve çıkan dosyayı geri getirebilir. Çıktı aynı kabul listesiyle denetlenir.

9 Eylül'de ayrıca okunan [Higgsfield bağlantı belgesi](https://higgsfield.ai/mcp) ve [resmî CLI deposu](https://github.com/higgsfield-ai/cli), hesapla giriş ve üretim işi devri yollarını açıklıyor. İlk adres kurulum sayfasıdır; doğrudan MCP sunucu adresi olarak doğrulanmadı. [Ollama Cloud belgesi](https://docs.ollama.com/cloud) ise yerel istemci üzerinden bulut modeli kullanımını da açıklıyor: komutun bilgisayarda çalışması, modelin bilgisayarda çalıştığını tek başına göstermez. Bu belgeler bağlantı için başlangıç kaynağıdır; bu makinede başarılı çağrı kanıtı değildir.

Yeni üretim başlamadan model/işlev, görünür maliyet ve deneme sayısını belirle. Mevcut yetki kapsamında ilerle; yeni harcama, farklı veri paylaşımı, alıcı veya yayın hedefi kararını iş sahibinden al. Mesaj taslağı, gönderilmiş mesaj; önizleme, yayımlanmış site; 3D dosya, denenmiş fiziksel baskı değildir.

## Canlı yayında uygulanabilecek 10 dakikalık bölüm

Bu bir **yayın önerisi**; yapılmış yayın veya üretim testi değildir.

1. **0–2 dakika:** Tek işi göster: “Bu paylaşılabilir kaynak görselden kısa bir ürün hareketi hazırlayacağız.” Kaynağın kullanım iznini ve bitti ölçütünü belirt.
2. **2–4 dakika:** Aynı kartta araç seçimi, hareket brifi, süre, kadraj ve deneme sınırını doldur. Hesap ayarları yerine görev alanını göster.
3. **4–7 dakika:** Erişimi ve maliyeti önceden doğrulanmış tek araçta denemeyi yürüt. İşlem yetişmezse durumu “üretim bekliyor” olarak göster; önceden hazırlanmış örneği açıkça etiketle.
4. **7–9 dakika:** Gerçek çıktıyı kaynağıyla karşılaştır. Bozulmayı veya eksikliği izleyiciye göster; kabul kararını gerekçelendir.
5. **9–10 dakika:** Dosyayı, kontrolü ve sonraki adımı aynı iş kaydına bağla.

Bu bölüm mevcut [60 dakikalık yayında](../yayin/01-ilk-yayin.md) bir uygulama bölümünün yerine kullanılabilir; toplam süreyi kendiliğinden uzatmaz. Çıkarılacak kısa içerik: “Yedi açık araçtan bu iş için birini nasıl seçtim?”
