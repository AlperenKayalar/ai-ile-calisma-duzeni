---
name: kabul-kontrolu
description: Bir çıktıyı kaynağı ve kabul ölçütleriyle karşılaştırıp geçti / kaldı / sınanmadı sonuçlu kabul kaydı üretir. Bir taslak, teslim veya "tamamlandı" iddiası kontrol edilecekse, bir iş kapatılmadan önce veya kullanıcı kontrol, doğrulama ya da kabul kaydı istediğinde kullan.
---

# Kabul kontrolü

Kontrol edilecek iş veya dosya: $ARGUMENTS (boşsa sana verilen mesajda veya konuşmada adı geçen çıktıyı kullan)

Bu kontrolde bağımsız kontrol eden rolündesin. Kararını yalnız dosyalardaki kaynağa ve gerçek çıktıya dayandır. Çıktıyı üretmiş olmak ya da üreten oturumun özeti doğruluk kanıtı değildir; yöntemin amacı, üretenle kontrol edenin aynı yanılgıyı paylaşmasını önlemek. Çıktıyı bu konuşmada sen ürettiysen ve subagent kullanabiliyorsan kontrolü bir subagent'a ver, ona yalnız dosya yollarını ve kabul ölçütlerini ilet. Bunu yapamıyorsan kaynak ve çıktıyı baştan okuyarak kontrol et ve bu sınırı kayda yaz.

Kontrol ederken:

- Çıktıyı gerçekten aç: dosya, sayfa veya önizleme. Açamadığın çıktının sonucu "sınanmadı" olur.
- Kişi, iş, sayı, tarih, sonuç, link veya durum bildiren her iddiayı kaynaktaki dayanağına bağla. Dayanağı olmayanları ve dosyadan sınanamayan süreç iddialarını (ör. “yayımlanmadı”) kabul tablosunun altında ayrı listele.
- Her kabul ölçütü için nasıl kontrol ettiğini, gerçek gözlemini ve sonucu (geçti / kaldı / sınanmadı) yaz. Kabul ölçütleri brifte veya iş kaydında yazılı olanlardır; uzunluk gibi alıştırma hedeflerini ayrı satırlarda değerlendir.
- Durumları ayrı tut: taslak hazır, teknik kontrol geçti, insan kabulü alındı, hedefte doğrulandı. Biri diğerini kanıtlamaz. İnsan kabulü iş sahibine aittir; onu sen veremezsin.

Teslim: kabul tablosu (bu depoda `sablonlar/kabul-kaydi.md` biçimi), düzeltme için gereken en küçük değişiklikler ve genel durum. İlk kontrolde şablonun düzeltme alanına önerilerini yaz; tekrar kontrol sonucu düzeltme uygulandıktan sonra doldurulur. Kalan bir ölçütü diğerleri geçti diye kapatma. Düzeltmeyi uygulamak yerine öner; kontrol eden ile düzelten ayrı kalırsa ikinci kontrol anlam taşır.
