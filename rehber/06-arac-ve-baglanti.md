# Araçları gerektiğinde ekle

İlk demo, kullanabildiğin bir AI sohbetinde metinleri yapıştırarak tamamlanabilir. Bir ücretli plan listesi veya tüm araçları kurma zorunluluğu yoktur. Mevcut hesabının sınırları yine geçerlidir.

Bu bölüm 8 Eylül deneyimindeki Codex kurulumunu anlatır. Aynı protokolün Claude Code ve güncel Claude modelleriyle kurulumu [ayrı bölümde](09-claude-ile-uygulama.md).

## Codex ile yerel dosya çalışması

Bu deneyimde Codex masaüstü uygulaması kullanıldı. Güncel resmî başlangıç sayfası masaüstü ve web seçeneklerini anlatıyor; geliştirici için Codex CLI ve editör eklentisine de yönlendiriyor. Kurulumda ürün adını ve hesabında görünen seçenekleri bu kaynaktan kontrol et. [Resmî başlangıç](https://learn.chatgpt.com/docs/quickstart).

Başlamak için demo klasörünü bir çalışma alanında aç, AI'ya okuyacağı dosyayı ve yazacağı yeni sonucu açıkça belirt. Sonucu önce kendin açıp oku. Tüm bilgisayarı kapsayan erişim, bu alıştırmanın önkoşulu değildir.

## Skill ne zaman anlamlı?

Skill, tekrar eden bir işin talimatlarını ve gerektiğinde kaynaklarını bir araya getirir. Codex ve ChatGPT'nin resmî belgelerinde yeniden kullanılabilir iş akışlarının yazım biçimi olarak tanımlanır. Paketle dağıtım için plugin kullanılabilir. [Resmî skill belgesi](https://learn.chatgpt.com/docs/build-skills).

Bu paketteki komutları önce elle uygula. Aynı girdiden aynı tür çıktıyı iki kez alabildiğinde, “ne zaman kullanılacak, ne okuyacak, ne üretecek, nasıl kontrol edilecek?” sözleşmesini yaz. 25 Eylül 2026'dan itibaren depoda protokolün üç adımı için taslak Claude Code skill'leri var; durumları ve kurulumları [Claude bölümünde](09-claude-ile-uygulama.md). Otomatik kurulan bir plugin içermez.

## Bağlantı nasıl eklenir?

MCP, modele başka araçların ve kaynakların erişimini sağlar. Yerel istemci bağlantılarıyla webdeki plugin araçlarının kurulum ve erişim biçimleri farklı olabilir. [Resmî MCP belgesi](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).

Önce tek bir işi tanımla: örneğin seçtiğin bir belgeden bilgi okumak. Kullandığın uygulamanın bağlantı arayüzünden ilgili hizmeti bağla; istenen erişimin bu işe uygun olduğunu kontrol et. AI'dan yalnız seçtiğin örnek kaydı okumasını iste. Gerçek sonuç dönünce [platform kartındaki](../sablonlar/platform-karti.md) AI erişim yöntemi ve denenen işlem alanlarına tarih ve kapsamla yaz. Bir okuma testi, yazma veya otomasyonun da çalıştığını göstermez.

Bağlantı yoksa aynı alıştırma için paylaşılabilir metni dışa aktarabilir ya da elle yapıştırabilirsin. Anahtarları, oturum verilerini veya kişisel yapılandırma dosyalarını eğitim deposuna koyma.

## Zamanlanmış takip

Önce takip komutunu normal bir oturumda dene. Çıktının ne zaman bildirim gerektireceğini belirt. Yerel dosyalarla çalışan zamanlanmış görevlerde bilgisayarın açık, uygulamanın çalışır ve kaynak projenin erişilebilir olması gerekir; web görevlerinin yerel klasöre erişimi aynı değildir. [Resmî zamanlanmış görevler belgesi](https://learn.chatgpt.com/docs/automations?surface=app).

Bu bir **takip talimatı taslağıdır**, kurulmuş otomasyon değildir:

> Seçtiğim iş listesini kontrol et. Yalnız yeni tamamlanma, gerçek hata, anlamlı değişiklik veya benden gereken bir karar varsa bildir. Değişiklik yoksa sessiz kal. Kaynağa erişemediğinde “değişiklik yok” deme; erişim sorununu belirt. Aynı işi ikinci kez oluşturma. Son kontrol zamanını kaydet.

Takvimi kurarken saat dilimini, kaynak konumunu ve durdurma yolunu belirt. İlk gerçek koşunun çıktısını görmeden “otomasyon çalışıyor” diye işaretleme.

Bu bölümün resmî kaynakları 8 Eylül 2026'da açılarak kontrol edildi. Arayüz, erişim ve ücretler değişebileceğinden sabit fiyat veya model adı verilmedi.
