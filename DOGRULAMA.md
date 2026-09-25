# Bu paketin kontrolü

Bu not **rehber paketinin** kontrolünü anlatır. Gerçek deneyim bölümündeki 13 test, farklı bir iş olan yerel çalışma panosuna aittir.

## Bağımsız AI okuyucu provası

8 Eylül 2026'da, paketi yazan ana ajandan ayrı bir AI okuyucuya yalnız tekrar protokolü, kurmaca girdi ve komutlar verildi. Hazır beklenen çıktı ile tam prova dosyası verilmedi. Okuyucu ana profil, iki uyarlama, kaynak/karar kaydı, kabul tablosu ve devam notunu üretti.

Kaydedilmiş sonuç yeniden okunarak kontrol edildi. Portföy metni 69, kısa paylaşım 35 kelimeydi. Üç hizmet korundu, çalışmalar kişisel olarak anlatıldı, gerçek olmayan link ve ticari başarı iddiası eklenmedi. Bu sonuçlar küçük yerel metin alıştırmasına aittir.

Prova, talimatta iyileştirme gerektiren yerleri de gösterdi. “İki metin” başlığı “ana profil ve iki uyarlama” olarak düzeltildi. Tek işin birden fazla kaynak çalışma içerebileceği, ilk kaydın tek dosyada tutulabileceği, kelime sayma yöntemi ve kurmaca iş sahibi kabulünün sınırı açıklandı.

Son içerik incelemesinde canlı yayın komutunun hangi girdi metnini alacağı netleştirildi; küçük profil alıştırması ana protokolün isteğe bağlı alt çalışması olarak etiketlendi. Bu açıklama düzeltmelerinden sonra dosya kontrolleri yenilendi; tüm okuyucu provası ikinci kez koşturulmadı.

## Dosya kontrolleri

Depo içi Markdown bağlantıları, kod blokları ve örnek metinlerin uzunlukları kontrol edildi. Yayın akışının süreleri 60 dakikayı aralıksız kapsıyor. Kamu dosyalarında özel yerel yollar, e-posta adresleri, özel sohbet bağlantıları ve bilinen anahtar biçimleri için tarama yapıldı; ayrıca içerik insan verisi açısından okundu.

Otomatik örüntü taraması her tür hassas bilgiyi bulma garantisi değildir. Paket ham özel verileri temizleyerek değil, yöntemi yeniden yazarak ve kurmaca girdiler oluşturarak hazırlandı.

## Henüz sınanmayanlar

Başka bir gerçek kişinin kendi hesaplarıyla bütün süreci uygulaması, gerçek müşteri kabulü, canlı platform işlemleri, gelir etkisi ve karşılaştırmalı zaman kazancı bu derlemede sınanmadı. İlk dış kullanıcı pilotunda [kabul kaydı](sablonlar/kabul-kaydi.md) ve [fayda kaydı](sablonlar/fayda-kaydi.md) kullanılabilir.

## 9 Eylül Chrome eki

Yedi aracın mevcut sayfa içeriği salt okunur incelendi. Bu erişim gözlemi üretim veya entegrasyon testi değildir. Yeni yardımcılar bölümü ve görev kartı bağımsız AI okuyucu tarafından ayrıca incelendi; gözlem, önerilen görev ve gerçek çıktı ayrımı kontrol edildi. Devir komutu tarayıcı dışındaki erişim yollarını da kapsayacak biçimde düzeltildi.

Ekleme sırasında 36 dosyanın 32'si Markdown'dı; 98 depo içi bağlantı, kod bloğu dengesi ve seçili özel veri örüntüleri kontrol edildi. Kritik bulgu çıkmadı. Hesap/proje adresleri ve tarayıcı erişim belirteçleri kamu metnine taşınmadı. İlk okuyucu provası bu belge eklemesi için yeniden koşturulmadı; dış araçlara örnek üretim gönderilmedi.

## 25 Eylül 2026 bakımı

Dosya kontrolleri artık [araclar/kontrol.py](araclar/kontrol.py) ile tekrar çalıştırılabiliyor ve GitHub'da her değişiklikte otomatik koşuyor. Betik depo içi Markdown bağlantılarını, kod bloğu dengesini, bilinen özel veri örüntülerini (yerel kullanıcı yolu, e-posta, anahtar biçimleri, özel sohbet bağlantıları) ve `SHA256SUMS.txt` güncelliğini denetler. Kırık bağlantı ve kapanmamış kod bloğu içeren geçici bir test dosyasıyla hatayı yakaladığı görüldü. Bakım sonunda bütün dosyalarda hata çıkmadı. Önceki checksum listesinde `README.en.md` yoktu; liste yeniden üretildi.

Dış bağlantılar 25 Eylül'de yeniden açıldı. Resmî OpenAI ve Ollama belgeleri, Higgsfield, WASK ve Instantly yanıt verdi. Runway'in eski adresi kalıcı yönlendirmeyle yeni alan adına gidiyordu; bağlantı güncellendi. Lovable, Tripo ve Higgsfield CLI deposu otomatik istemciye erişim izni vermedi; bu, sayfaların kaldırıldığı anlamına gelmez ve bağlantılar değiştirilmedi.

Claude bölümündeki ürün bilgileri [kaynak notundaki](KAYNAKLAR.md) resmî sayfalardan okundu. Komutların yeni biçimi ve taslak skill'ler için yapılan ayrı okuyucu provası aşağıda.

## 25 Eylül 2026 okuyucu provası

Yeni Komut 1 ve üç taslak skill, bu oturumun modeli olan Claude Opus 5.5 ile çalışan iki ayrı AI okuyucuyla kurmaca demo üzerinde denendi. İki okuyucuya da beklenen çıktı ve tam prova verilmedi.

Birinci okuyucu yalnız protokolü, demo girdisini, Komut 1'i, `is-brifi` ve `devir-notu` skill'lerini ve iki şablonu kullandı; iş kaydı, Komut 1 çıktısı ve devam notu üretti. Ana profil 4 cümle ve 35 kelime, portföy tanıtımı 65, kısa paylaşım 40 kelimeydi. Sayılar ayrıca betikle yeniden sayıldı.

İkinci okuyucu yalnız `kabul-kontrolu` skill'ini, kabul kaydı şablonunu, demo girdisini ve birinci okuyucunun çıktısını gördü. Beş kabul ölçütünün ve üç uzunluk hedefinin hepsini “geçti” olarak değerlendirdi; dayanaksız müşteri, sonuç, sayı, tarih veya link bulmadı. Kaynakta olmayan iki ton ekini (“birlikte”, “şimdilik”) düşük riskli diye not etti. “Yayımlanmadı” gibi dosyadan sınanamayan süreç iddialarını ayrı tuttu. Çıktı dosyası kontrolden önce ve sonra aynıydı.

Prova, talimatlardaki belirsizlikleri de gösterdi ve şunlar düzeltildi: skill'deki pilot tanımı protokolün “bir ana çıktı ve iki uyarlama” ifadesiyle eşitlendi; uzunluklar kabul ölçütü değil alıştırma hedefi olarak adlandırıldı; Komut 1'e metinlerin şahsı eklendi; iş kaydı şablonuna pilot alanı ve iki tarih sütunu eklendi; devam notunun nereye yazılacağı netleşti; kabul kontrolünde iddia listesinin yeri, sınanamayan süreç iddiaları ve şablondaki düzeltme alanı açıklandı, şablondaki durum adı protokolle eşitlendi. Bu düzeltmelerden sonra prova yeniden koşturulmadı.

Sınanmayanlar: Claude Code'un skill'leri kendiliğinden tetiklemesi (okuyucular SKILL.md dosyalarını doğrudan okudu), claude.ai'ye yükleme, gerçek bir işte kullanım ve insan kabulü. Prova çıktıları kurmaca olduğu ve özel çalışma alanında üretildiği için pakete eklenmedi.
