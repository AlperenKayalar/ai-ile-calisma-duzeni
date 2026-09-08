# Süreci başka bir işte tekrarlama protokolü

**Amaç:** 8 Eylül'de ağırlık kazanan gerçek çalışma biçimini, başka bir kişinin kendi hesapları ve verileriyle uygulayabileceği bir teslim sürecine dönüştürmek.

Bu belge, [gerçek deneyimden](03-gercek-deneyim.md) çıkarılmış **önerilen standarttır**. Kullanıcının bütün adımları geçmişte bu tabloyla yürüttüğü veya başka bir işletmede uçtan uca doğrulandığı iddia edilmez.

## İşe başlama koşulları

İş sahibinin hedefi, kullanılabilecek kaynaklar, bir çalışma klasörü ve işi kabul edecek kişi belli olmalı. Mevcut dosya, profil ve yayınları önce oku. Yeni bir kopya ya da hesap oluşturmadan önce aynı işin var olup olmadığını kontrol et.

İlk uygulamada tek bir iş ve iki hedef çıktı yeterli. “Tek iş”, birkaç kişisel çalışmayı kullanan bir tanıtım işi de olabilir; tek kaynak dosyayla sınırlı değildir. 31 hesabı veya bütün geçmişi yeniden kurmak önkoşul değil. Mevcut bir çalışma alanıyla başlayabilir, AI dosyaya erişemiyorsa gerekli içeriği elle aktarabilirsin.

İlk pilotta brif, kaynak, çıktı, kabul ve devam bölümlerini tek dosyada tutabilirsin. İşe kendin basit bir kimlik ver; örneğin `PILOT-01`. Dosyaları ancak farklı kişiler yazacaksa veya içerik büyürse ayır. Yerel teslimin geri okuması, kaydedilen dosyanın yeniden açılmasıdır; insan kabulü ve dış platform kontrolü ayrı kalır.

## Roller

| Rol | Sorumluluk | Tek kişi çalışıyorsa |
|---|---|---|
| İş sahibi | Amacı, kapsam değişikliklerini, paylaşılacak bilgiyi ve teslim kabulünü belirler | Sensin |
| Yürütücü | Kaynakları okur, işi parçalara ayırır, uygular ve sonucu birleştirir | Ana AI çalışma oturumu |
| Yardımcı | Verilen sınırlı alt işi, belirtilen dosyada üretir | Ayrı ajan veya ayrı oturum; isteğe bağlı |
| Kontrol eden | Kabul ölçütlerini kaynak ve gerçek çıktıyla sınar | Sen veya bağımsız ikinci okuma |

Bir kişi birkaç rol üstlenebilir; kayıt yine “kararı kim verdi, işi kim yaptı, kim neyi kontrol etti?” sorularına yanıt vermeli. İkinci AI'nın onayı tek başına müşteri/insan kabulü değildir.

## Uygulama sırası

| Adım | Girdi | Yapılacak iş ve sorumlu | Çıktı | Geçiş ölçütü | Takılırsa |
|---|---|---|---|---|---|
| 0. Kapsamı sabitle | İş sahibinin talebi | Yürütücü talebi tek sonuç cümlesine çevirir; iş sahibi belirsiz kararları çözer | Görev brifi ve karar kaydı | Sonuç, hedef kitle ve bitiş ölçütü anlaşılır | Eksik kararı daralt; bağımsız kaynak okumasını sürdür |
| 1. Mevcut durumu çıkar | Dosyalar, ilgili konuşmalar, hesaplar | Yürütücü güncel kaynakları tarar; eski notlarla çelişkiyi korur | Kaynak envanteri ve başlangıç durumu | Her önemli kayıt için tarih, erişim ve dayanak var | Erişilemeyeni “bilinmiyor” işaretle; varmış/yokmuş gibi yazma |
| 2. Bir pilot seç | Envanter ve hedef | İş sahibi kapsamı seçer; yürütücü bir kaynak işini iki çıktıya bağlar | Dar pilot ve kabul listesi | Kullanılabilir kaynak ve kontrol yolu var | Kaynağı/çıktıyı küçült; geri alınamayacak işlemi pilot koşulu yapma |
| 3. Görevleri ayır | Pilot, kaynak ve kabul listesi | Yürütücü bağımsız alt işleri dağıtır; yazılacak alanları ayırır | Devir notları | Her alt işin girdisi, dosyası ve teslimi belli | Çakışan dosyada tek yazıcıya dön |
| 4. Uygula | Onaylanmış kapsam ve kaynak | Yürütücü/yardımcı metni, varlığı veya değişikliği üretir; mevcut işi günceller | Taslak veya çalışma çıktısı | Dosya var ve açılıyor; kaynak ilişkisi korunuyor | Hatanın son başarılı adımını kaydet, oradan devam et |
| 5. Geri oku ve doğrula | Gerçek çıktı ve kabul listesi | Kontrol eden kaynağı karşılaştırır; gerekliyse UI, dosya veya anlamlı test kullanır | Kabul kaydı ve düzeltmeler | Kritik maddeler geçti; belirsizler açık | “Tamamlandı” yazma; sorunlu adımı yeniden uygula |
| 6. Teslim et / yayımla | Kontrol edilmiş çıktı, belirli hedef ve yetki | Yürütücü izinli hedefe aktarır; sonucu yeniden açar | Teslim dosyası veya gerçek yayın adresi | Hedefteki sonuç görülmüş | Belirsiz yazma sonucunda yeniden göndermeden önce hedefi oku |
| 7. Kaydı devret | Sonuç, açık işler, ölçümler | Yürütücü tek iş kaydını ve kapanışı günceller | Devam notu, gerekirse takip talimatı | Yeni oturum ilk adımı tahmin etmeden bulabiliyor | Kayıp bağlantıyı düzelt; aynı işi ikinci kez açma |
| 8. Tekrarı değerlendir | İkinci uygulamanın gerçek sonucu | İş sahibi ve kontrol eden süreyi, hatayı ve bakım yükünü karşılaştırır | Protokol değişikliği veya korunacak yöntem | Başarı, maliyet ve sınır kaydı var | Kullanılmayan adımı çıkar; deneyi küçült |

Bir adımda zaten açık olan yetkiyi her seferinde yeniden sormak gerekmez. Yeni bütçe, farklı yayın hedefi veya işin amacını değiştiren karar ortaya çıkarsa bunu karar kaydına taşı.

## Tamamlanma durumlarını aynılaştırma

| Durum | Ne söyleyebilirsin? | Henüz ne söyleyemezsin? |
|---|---|---|
| Bulundu | Kaynak veya hesap kaydı var | Erişilebilir / doğru / güncel |
| Taslak hazır | Kontrol edilebilen çıktı var | Yayımlandı veya kabul edildi |
| Teknik kontrol geçti | Belirtilen kontrol başarılı | Her cihazda veya gerçek işte çalışıyor |
| İnsan kabulü alındı | İlgili kişi çıktıyı kabul etti | Dış platforma ulaştı |
| Hedefte doğrulandı | Sonuç hedefte yeniden açıldı | Ticari fayda oluştu |
| Fayda ölçüldü | Belirli dönem ve kapsamda veri var | Her kullanıcıda aynı sonuç çıkar |

## Hata halinde devam reçeteleri

**Oturum açılmıyor:** Metin/varlık hazırlığını tamamla. Hesap durumunu erişim bekliyor yap. Giriş işlemini tamamlanmış sayma.

**Kaydet dedikten sonra yanıt kayboldu:** Önce hedefi yeniden oku. Sonucun var olup olmadığını belirlemeden işlemi tekrar etme.

**İki kayıt çelişiyor:** Aynı konu ve yetki düzeyindeki güncel kanıtı esas al; eski durumu tarihsel olarak bırak. Bir asistanın tamamlandı cümlesi açık kullanıcı düzeltmesini geçersiz kılamaz.

**AI gereksiz yere kapsamı büyüttü:** Son kullanıcının amaç cümlesine dön. Yeni öneriyi mevcut işten ayrı etiketle. Özellikle “tüm araçları kur” gibi bir gereksinimi kendiliğinden ekleme.

**Yerel çıktı hazır, yayın yetkisi veya hedefi yok:** Teslimi yerel dosya olarak kaydet. Yayın adımını açık tut. İçeriği hazır olan iş ile yayımlanmış işi ayır.

**Takip çalışmadı:** Kaynak erişimini, çalışma koşullarını ve son koşu kaydını incele. Takip tanımının etkin görünmesi ile ilk gerçek koşunun başarıyla bitmesi farklı kabul maddeleri.

## İlk tekrarın kabulü

[Tam prova örneği](../ornekler/prova/akisin-tamami.md), her rolün ne üreteceğini gösterir. Kendi işinde bir pilotu tamamlamak için şu kayıtlar yeterlidir:

- Kapsam ve insan kararları.
- Kaynak envanteri, tarih ve eksikler.
- Bir ana çalışma çıktısı ve uyarlanmış iki teslim.
- Dayanak kontrolü ve varsa hedefte geri okuma.
- Tek iş kaydı, kapanış ve ölçüm sınırı.

Gerçek tekrarın başarısı, bu kayıtları başka bir kişinin senin sözlü açıklamana ihtiyaç duymadan izleyebilmesiyle sınanacak. Bu sürümdeki masa başı örnekler böyle bir dış kullanıcı pilotunun yerine geçmez.
