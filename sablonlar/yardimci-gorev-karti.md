# Yardımcı görev kartı

Bu kartı mevcut iş kaydının içine kopyalayabilirsin. İlk doldurma sırasında sonuç alanlarını boş/bekliyor tut. Özel hesap bilgileri kendi çalışma alanında kalır.

## İş ve devir

- İş kimliği / amaç: [tek iş ve beklenen sonuç]
- Ana yürütücü / iş sahibi: [roller]
- Yardımcı araç / üstleneceği parça: [sınırlı görev]
- Girdi ve kullanım kapsamı: [kaynak dosya, araca verilebilecek içerik]
- İstenecek çıktı: [dosya türü, süre/boyut/adet]
- Korunacak özellikler: [metin, ürün biçimi, marka, vb.]
- Kabul ölçütleri: [gerçek çıktı üzerinde bakılacak üç madde]

## Erişim ve deneme

- Erişim yolu: [tarayıcı / elle aktarım / API / MCP / CLI]
- Gözlem tarihi ve kanıtı: [hangi ekran veya kontrollü işlem görüldü?]
- Erişim durumu: [sekme bulundu / arayüz okundu / görev denendi / çıktı geri alındı]
- Kullanılan işlev/model: [bilinmiyorsa bilinmiyor]
- Veri paylaşımı, kredi/harcama sınırı ve en fazla deneme: [işin mevcut yetkisi]
- Gerçekte yapılan işlem: [henüz yok veya açık tarif]

## Sonuç ve devam

- Çıktının yeri: [gerçek dosya veya erişilebilir hedef; henüz yoksa yok]
- Teknik kontrol: [geçti / kaldı / sınanmadı; kanıt]
- İnsan kabulü: [bekliyor / kabul / düzeltme; kim, ne zaman]
- Yayın/gönderim: [yok / taslak / hedefte doğrulandı]
- Süre ve maliyet: [ölçüm veya ölçülmedi]
- Tek sonraki adım: [ne, kimde, hangi girdiye bağlı]

## Kopyalanabilir devir komutu

```text
Bu görev kartındaki işi yap. Yalnız belirtilen girdiyi kullan ve istenen
çıktıyı üret. Korunacak özellikleri değiştirme. Kaynak eksikse açıkça yaz.

Erişim ve maliyeti seçilen erişim yolunda doğrula. Mevcut yetki kapsamındaki
işleri yürüt; yeni bütçe, veri paylaşımı veya yayın/gönderim kararı ekleme.
İşlem sonucunu görmeden tamamlandı deme. Çıktıyı geri aç, kabul ölçütlerini
geçti/kaldı/sınanmadı olarak değerlendir. Dosyayı ve tek sonraki adımı
aynı görev kartına bağla.
```
