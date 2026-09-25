# Kopyalanabilir görev komutları

Komutlar bu paket için yazılmış önerilerdir. Adı geçen girdiyi aynı sohbete, komuttaki etiketlerin arasına yapıştır; AI görmediği dosyayı bilemez. İlk üç komut bir işin hazırlık, üretim ve kontrol adımlarıdır.

**Biçim notu · 25 Eylül 2026.** Girdi, etiketlerle (`<girdi>…</girdi>`) talimattan ayrılır ve komutun başına konur; önemli kısıtların yanında nedeni yazar. Anthropic'in [güncel istem rehberi](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) bu üç alışkanlığı öneriyor: içeriği XML etiketleriyle ayırmak, uzun girdiyi talimatın üstüne koymak, talimatın gerekçesini vermek. “Adım adım düşün” veya “ÇOK ÖNEMLİ” gibi satırlar bilerek eklenmedi; nedeni [Claude bölümünde](../rehber/09-claude-ile-uygulama.md). Komutlar başka AI araçlarında da aynı biçimde kullanılabilir. Etiket adları Türkçe olabilir; önemli olan tutarlı olmaları.

## 1. Küçük demo: ana profil ve iki uyarlama

```text
<girdi>
[Demo girdisinin veya kendi paylaşılabilir bilgilerinin tamamı]
</girdi>

Yukarıdaki girdiden şu beş parçayı hazırla:
1. Ana profil, 2–4 kısa cümle: kimlik, hedef kitle, üç hizmet ve çalışma biçimi.
2. 60–90 kelimelik portföy tanıtımı.
3. En fazla 45 kelimelik sosyal paylaşım taslağı.
4. Eksik bilgiler ve kullanamayacağımız iddialar, ayrı bir liste halinde.
5. İşin durumu ve tek sonraki adım.

Metinler yalnız girdideki gerçeklere dayansın; kişisel çalışmalar kişisel
çalışma olarak anlatılsın. Kişi bu metinlerle kendini tanıtacak, uydurulmuş
müşteri, sonuç veya link ona zarar verir.
Uzunluklar alıştırmanın kabul ölçütüdür, platform limiti değildir. Kelimeleri
boşlukla ayrılmış birimler olarak say.
Sonuç yerel taslak olarak kalır: iş sahibi hesap açılmamasına ve hiçbir yere
gönderilmemesine karar verdi.
```

## 2. Uçtan uca bir işi yürüt

```text
<is_brifi>
[Görev brifi veya iş kaydı]
</is_brifi>

<kaynak_envanteri>
[Kaynak envanteri]
</kaynak_envanteri>

Bu işi brifteki kapsam içinde baştan sona yürüt.

Önce mevcut durumu, açık insan kararlarını ve kabul ölçütlerini kısaca özetle.
AI önerilerini öneri olarak etiketle; kararı iş sahibi verir.

İşi girdi, sorumlu, çıktı, kontrol ve hata halinde devam adımlarına ayır.
Bağımsız alt işleri yardımcılara verebilirsin; her birine somut bir teslim ve
ayrı bir dosya ver, çünkü aynı dosyaya veya aynı arayüze eşzamanlı yazmak
çakışma üretiyor. Yardımcı kullanamıyorsan adımları sırayla yap.

Başarı iddialarını kaynağa bağla. Çıktıyı kaydettikten sonra yeniden açıp
kontrol et. Taslak, teknik kontrol, insan kabulü ve yayın durumlarını ayrı yaz.
Eksik yetki veya bilgiye bağlı adımı açık bırak, bağımsız işleri tamamla.
Bir çıktıyı yeniden oluşturmadan önce hedefte zaten var olup olmadığına bak.

Sonunda tek bir devam notu bırak: teslimlerin yeri, kabul sonuçları, açık
kalanlar ve ilk sonraki adım.
```

## 3. Bağımsız kontrol

```text
<girdi>
[Kaynak girdi]
</girdi>

<cikti>
[Kontrol edilecek çıktı]
</cikti>

<kabul_olcutleri>
[Brifteki kabul ölçütleri]
</kabul_olcutleri>

Bu çıktının bağımsız kontrolünü yap. Çıktıyı kimin ürettiği, doğru olup
olmadığı hakkında bir şey söylemez; dayanak yalnız girdidir.

Önemli iddiaların her birini girdideki dayanağına bağla. Dayanağı olmayan
müşteri, sonuç, deneyim, tarih veya linki işaretle.
Her kabul ölçütünü geçti / kaldı / sınanmadı olarak değerlendir ve gözlemini yaz.
Sonucu düzeltmek için gereken en küçük değişiklikleri öner.
```

## 4. Haber veya araştırmadan içerik taslağı

```text
<soru>
[Araştırma sorun]
</soru>

<kaynaklar>
[Seçtiğin kaynaklar ve bağlantıları]
</kaynaklar>

Bu kaynaklardan bir paylaşım taslağı hazırla.
Önce kaynakta geçen bulguyu, sonra benim işim için yorumunu yaz; okuyucu
ikisini ayırt edebilmeli. Yayın tarihini ve olayın tarihini ayrı ver.
Kaynak iddiayı gerçekten desteklemiyorsa bunu belirt.
Taslak özgün olsun ve kaynağa bağlantı versin. Sonucu taslak olarak kaydet;
yayımlama kararı iş sahibinde.
```

## 5. Mevcut hesapları işe bağla

```text
<hesap_ve_arac_listesi>
[Hesap, profil ve araç kayıtların]
</hesap_ve_arac_listesi>

<secilen_is>
[Bu listenin hizmet edeceği tek iş]
</secilen_is>

Listeyi seçilen işe hizmet edecek biçimde düzenle.
Tekrarları birleştir. Her kayıt için ayrı sütunlarda göster: hangi işte
kullanıldığı, erişimin doğrulanıp doğrulanmadığı, profil durumu, içerik durumu
ve denenmiş somut işlem.
Yer imi veya açık sekme yalnız “bağlantı kayıtlı” düzeyidir; çalışan
entegrasyon sayılması için belirli bir işlemin gerçekten denenmiş olması gerekir.
Önceliği yeni hesap açmaya değil, seçilen işin tamamlanmasına ver.
```

## 6. Oturumu devret

```text
<oturum_kaydi>
[Bu oturumun çıktıları, kontrol sonuçları ve kararları. Aynı sohbette
devam ediyorsan boş bırakabilirsin.]
</oturum_kaydi>

Bu oturumu, yeni bir oturumun eski sohbeti okumadan devam edebileceği tek bir
devam notunda uzlaştır: amaç, üretilen gerçek çıktılar ve konumları, kontrol
sonuçları, insanın verdiği kararlar, açık işler ve yeni oturumun ilk adımı.
Henüz seçilmemiş AI önerilerini ayrı listele; onları görev taahhüdüne
dönüştürme.
```
