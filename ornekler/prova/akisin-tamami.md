# Uçtan uca masa başı prova

**Önerilen yöntemin doldurulmuş kurmaca örneği.** Gerçek hesap erişimi, canlı yayın veya dış kullanıcı pilotu değildir. Her adımın kaydını göstermek için hazırlanmıştır.

## 0. İş ve insan kararı

**İş kimliği:** DEMO-01.

**İş sahibi:** Deniz. **Yürütücü:** Bir AI çalışma oturumu. **Kontrol:** İş sahibinin kaynak karşılaştırması; isterse bağımsız ikinci AI okuması.

**Amaç:** Mevcut iki kişisel çalışmadan, kendini tutarlı anlatan bir ana profil ve iki metin taslağı üretmek; işi sonraki oturuma devretmek.

**İnsan kararı:** Hesaplara giriş ve yayın bu provanın dışında. Yeni site, ücretli abonelik veya müşteri bulma taahhüdü yok. Bunlar varsayımsal iş sahibinin bu örnek için verilmiş kararlarıdır.

## 1. Başlangıç ve kaynak envanteri

| Kaynak | Durum | Kullanılacak bilgi | Sınır |
|---|---|---|---|
| [Demo girdisi](../ilk-demo/girdi.md) | Metin erişilebilir | Kimlik, üç hizmet, iki kişisel çalışma, insan kararı | Gerçek müşteri ve gelir bilgisi yok |
| Gerçek portföy bağlantısı | Henüz yok | Yok | Link uydurulmayacak |
| Görseller | Bu provada verilmedi | Yok | Görsel kalite veya hak kontrolü yapıldı denmeyecek |

Başlangıçta üç farklı metin henüz üretilmemiş kabul edilir. Gerçek uygulamada mevcut metin varsa yeniden üretmeden önce okunur.

## 2. Pilot ve kabul listesi

Çıktılar: ana profil, 60–90 kelimelik portföy tanıtımı, en fazla 45 kelimelik kısa paylaşım, kabul notu ve devam notu. Uzunluklar alıştırma tercihidir.

Kabul: üç hizmet korunmalı; iki örnek kişisel çalışma kalmalı; müşteri/gelir iddiası uydurulmamalı; gerçek link olmadan link verilmemeli; her sonuç taslak olarak işaretlenmeli.

## 3. Görev dağılımı

| Alt iş | Sorumlu | Girdi | Teslim | Sınır |
|---|---|---|---|---|
| Ana profili çıkar | Yürütücü | Demo girdisi | Ana profil bölümü | Yeni biyografi veya deneyim ekleme |
| Metinleri uyarla | Yardımcı veya yürütücü | Ana profil + demo girdisi | Ayrı portföy ve kısa paylaşım taslağı | Kaynağı değiştirme |
| Kabulü denetle | Kontrol eden | Girdi + gerçek çıktı | Ölçüt tablosu | Taslağı yayın sanma |

Yardımcı kullanımı zorunlu değil. Aynı dosyaya eşzamanlı yazma yerine ayrı teslimler alınıp birleştirilir.

## 4. Uygulama

[Komut 1](../../komutlar/README.md) ve demo girdisini AI'ya ver. Gelen sonucu yeni bir çalışma dosyasına kaydet. [Beklenen çıktı](../ilk-demo/beklenen-cikti.md) önceden hazırlanmış karşılaştırma örneğidir; yeni denemenin başarılı olduğuna dair otomatik kanıt değildir.

Kaynakta olmayan bir iddia varsa üretim adımına dön. Örneğin “50 markanın satışlarını ikiye katladık” kabul edilemez; sayıyı küçültmek de çözüm değildir. İddia kaldırılır veya gerçek dayanak beklenir.

## 5. Örnek kabul kaydı

Aşağıdaki tablo yalnız paketteki **önceden yazılmış beklenen çıktının metin karşılaştırmasını** gösterir. Canlı hesabın kontrolü veya yeni bir kullanıcının çalışması değildir.

| Ölçüt | Gözlem | Sonuç |
|---|---|---|
| Üç hizmet korunuyor | Ana profil ve tanıtımda üçü de var | Geçti |
| Kişisel çalışmalar doğru anlatılıyor | Fincan ve lamba, kişisel/kavramsal diye belirtiliyor | Geçti |
| Müşteri/gelir/ödül uydurulmuyor | Böyle bir iddia yok | Geçti |
| Gerçek link uydurulmuyor | Linkin eksik olduğu yazıyor | Geçti |
| Taslak durumu ve sonraki adım var | Yerel taslak; iş sahibinin okuyup kontrol etmesi | Geçti |
| Görseller uygun | Görsel girdi yok | Sınanmadı |
| Gerçek kullanıcı kabulü | Kurmaca iş sahibi | Sınanmadı |
| Dış platformda görünürlük | Yayın kapsam dışı | Sınanmadı |

## 6. Teslim ve hata durumunda devam

Teslim, yerel metin dosyasıdır. Canlı yayın demosunda AI yanıt vermezse beklenen çıktıyı aç ve “önceden hazırlanmış örnek” diye belirt; kontrol adımını onun üzerinde göster. Yeni hesap veya bağlantı kurulumuna geçmek gerekmez.

Gerçek işte dış platforma yazılacaksa, bu aşamaya platform kartı ve iş sahibinin belirlediği hedef/yetki eklenir. Kaydetme sonucunu hedefte yeniden açıp doğrula. Belirsiz sonuçta körlemesine yeniden gönderme.

## 7. Doldurulmuş devam notu

**Yapılan:** Demo girdisinden ana profil ve iki metin hazırlanması örneklendi.

**Çıktı:** [Beklenen metin](../ilk-demo/beklenen-cikti.md).

**Kontrol:** Yukarıdaki beş metin ölçütü kaynakla karşılaştırıldı. Görsel, gerçek hesap ve iş sahibi kabulü sınanmadı.

**Açık kalan:** Kendi gerçek denemende kabul tablosunu yeniden doldurmak.

**İlk sonraki adım:** Gerçek iş sahibi metni okur; sonra gerekiyorsa kendi paylaşılabilir görsellerini ve hedef kanalını ekler.

**Mevcut kayıt:** DEMO-01. Yeni oturum bunun devamı olarak açılır, aynı iş yeniden oluşturulmaz.

## 8. Tekrar nasıl sınanacak?

Başka bir kişi kendi paylaşılabilir girdisiyle aynı sırayı uygular. Nerede ek açıklama istediğini, neyin yanlış üretildiğini, aktif emeğini ve kontrol sonucunu kaydeder. İlk dış kullanıcı pilotu tamamlanana kadar “başkalarında da profesyonel biçimde çalıştığı doğrulandı” denmez.
