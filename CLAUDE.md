# AI ile Çalışma Düzeni — Claude için çalışma notu

Bu depo, Alperen Kayalar'ın 8 Eylül 2026 deneyiminden çıkarılmış Türkçe bir süreç rehberidir: işi tarif et, uygula, doğrula, devret. Kod değil, public ve CC BY 4.0 lisanslı bir doküman paketi. Okuyucu, protokolü kendi hesapları ve verileriyle tekrar edebilmeli.

## Harita

- `README.md` giriş; `README.en.md` İngilizce dizin (içerik linkleri Türkçe dosyalara gider).
- `rehber/` bölümler. `03` gerçek deneyim, `07` tekrar protokolü (paketin omurgası), `09` Claude Code ile uygulama.
- `sablonlar/` doldurulacak kayıtlar; `komutlar/` kopyalanabilir istemler; `ornekler/` tamamen kurmaca (Deniz / Örnek Atölye).
- `yayin/` canlı yayın akışı ve seri planı (öneri; yapılmış yayın kaydı değil).
- `KAYNAKLAR.md` kaynak kodları (K1–K10) ve tarihli resmî ürün kaynakları; `DOGRULAMA.md` neyin nasıl kontrol edildiği.
- `.claude/skills/` protokolün üç adımının taslak skill'leri; `araclar/kontrol.py` dosya kontrolleri.

## Yazarken korunacak ayrımlar

Paketin değeri iddialarının dürüstlüğünde; okuyucu bir cümlenin kanıtlı mı, öneri mi, kurmaca mı olduğunu her zaman ayırt edebilmeli.

- Her yeni metin üç etiketten birine girer: **gerçek deneyim** (kaydı var), **bu deneyimden çıkarılan standart/öneri**, **kurmaca örnek**. Hangisi olduğu metinde görünür.
- Tamamlanma durumları ayrı kalır: bulundu, taslak hazır, teknik kontrol geçti, insan kabulü alındı, hedefte doğrulandı, fayda ölçüldü (`rehber/07` tablosu). Biri diğerinin kanıtı sayılmaz.
- Sınanmayanı "sınanmadı" diye yaz. Yeni bir deneme yaptıysan DOGRULAMA.md'ye ne yapıldığını ve neyin yeniden koşturulmadığını ekle.
- Güncel ürün özelliği iddiası, açılıp okunmuş resmî kaynağa ve tarihe bağlanır; kaynak KAYNAKLAR.md'ye eklenir. Fiyat ve model adı gibi hızlı değişen bilgiyi yalnız kaynağıyla ve tarihiyle ver.
- `rehber/03` ve KAYNAKLAR'daki 8 Eylül kesiti tarihsel kayıttır. İçeriğini sonradan değiştirme; düzeltme gerekirse tarihli ek not düş.
- Tarihlerde saat dilimi İstanbul'dur.

## Özel veri

Public pakete hesap adresi, e-posta, telefon, müşteri bilgisi, ham sohbet bağlantısı, anahtar veya oturum verisi girmez. Örnek gerekiyorsa kurmaca veri kullan. `araclar/kontrol.py` bilinen biçimleri tarar ama her şeyi yakalamaz; metni ayrıca oku.

## Dil ve üslup

Türkçe yaz; teknik terimleri İngilizce orijinaliyle bırak. Sade, doğrudan cümleler; dolgu, pazarlama dili ve "AI yazmış" tonu yok. Bağlantılar görünür ve tıklanabilir olsun. İngilizce dizin (`README.en.md`) Türkçe README'deki tabloyla eşleşmeli.

## Değişiklikten sonra

1. `python3 araclar/kontrol.py --guncelle` çalıştır: bağlantıları, kod bloklarını, özel veri örüntülerini denetler ve `SHA256SUMS.txt`'yi yeniler. Hata varsa düzelt.
2. `CHANGELOG.md`'ye tarihli satır ekle. Sürüm değişiyorsa `VERSION`, README ve YAYINLAMA.md'yi birlikte güncelle.
3. Yeni dosya eklediysen README tablolarına (TR ve EN) ve ilgili `README`'ye bağla.

Dosya silmeden veya yeniden adlandırmadan önce Alperen'e sor; diğer sitelerden ve yayın açıklamalarından bu yollara bağlantı verilmiş olabilir.
