# Protokolü Claude Code ile uygulamak

**25 Eylül 2026 eki.** Bu bölüm, [tekrar protokolünü](07-tekrar-edilebilir-protokol.md) Claude Code'da ve Claude Opus 5.5 gibi güncel modellerle nasıl kuracağını anlatır. Etiketi: **deneyimden çıkarılan standart + resmî belge.** 8 Eylül kaydındaki ana yürütücü Codex masaüstüydü; aynı protokolün Claude Code'da gerçek bir işle uçtan uca tekrarı bu sürümde kaydedilmedi. Ürün bilgileri aşağıda bağlantısı verilen resmî sayfalardan 25 Eylül 2026'da okundu; arayüz, model ve ücretler değişebilir.

Claude Code şart değil. Komutlar ve şablonlar herhangi bir AI sohbetinde çalışır. Claude Code, aynı kayıtları dosya olarak tutmayı, tekrar eden adımları komutlaştırmayı ve bağımsız kontrolü ayrı bir bağlama vermeyi kolaylaştırır.

## Protokolün parçaları Claude Code'da neye karşılık gelir?

| Protokol parçası | Claude Code karşılığı | Dikkat edilecek |
|---|---|---|
| Ana profil ve çalışma kuralları | [CLAUDE.md](https://code.claude.com/docs/en/memory): proje kökünde durur, her oturumun başında okunur | Resmî belge dosyayı 200 satırın altında tutmayı öneriyor; uzadıkça uyum düşüyor. Depoya girmeyecek kişisel tercihler `CLAUDE.local.md` dosyasına yazılır ve `.gitignore`'a eklenir. |
| Tekrar eden komut | [Skill](https://code.claude.com/docs/en/skills): `.claude/skills/<ad>/SKILL.md`, `/ad` ile çağrılır; Claude uygun durumda kendisi de yükleyebilir | [Araç bölümündeki](06-arac-ve-baglanti.md) kural geçerli: elle iki kez çalışmış işi skill'e çevir. |
| Yardımcı rolü | [Subagent](https://code.claude.com/docs/en/sub-agents): kendi bağlam penceresinde çalışır, ana konuşmanın geçmişini görmez | Tek yazıcı kuralı değişmez. Yardımcıya araştırma, okuma veya ayrı dosyaya taslak ver; ortak dosyayı ana yürütücü birleştirir. |
| Bağımsız kontrol eden | Ayrı bir subagent veya `context: fork` ile çalışan skill | Kontrol eden, üreten oturumun özetini değil dosyaların kendisini okumalı. |
| Bağlantı düzeyleri | [MCP](https://code.claude.com/docs/en/mcp) ile dış araç ve verilere erişim | [Sistem haritasındaki](02-sistem-haritasi.md) dört düzey aynen geçerli: bağlantının kurulması, belirli bir işin yapılabildiğini göstermez. |
| Metinle söylenen kural | [Hooks](https://code.claude.com/docs/en/hooks-guide): belirli anlarda her zaman çalışan kullanıcı komutları | Unutulmaması gereken kontrolü (ör. commit öncesi dosya kontrolü) talimat yerine hook'a bağlamak daha güvenilir. |
| Takip | [Zamanlanmış görevler](https://code.claude.com/docs/en/scheduled-tasks): masaüstü görevleri bilgisayar açıkken, `/loop` oturum açıkken, [Routines](https://code.claude.com/docs/en/routines) Anthropic bulutunda çalışır | Routines araştırma önizlemesinde ve yerel dosyalara erişmez. İlk gerçek koşunun sonucunu görmeden "takip çalışıyor" yazma. |
| Devam notu | Uzun işlerde durum dosyası ve git geçmişi | Anthropic'in [istem rehberi](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) çok oturumlu işlerde ilerleme notu dosyası ve git ile durum takibini öneriyor; bu, protokolün kapanış notuyla aynı fikir. |

## Bu depoda hazır gelenler

| Dosya | Ne işe yarar? | Durum |
|---|---|---|
| [CLAUDE.md](../CLAUDE.md) | Bu rehber deposunu Claude ile düzenlerken korunacak kurallar: üç etiket ayrımı, kanıtsız iddia yasağı, özel veri, değişiklik sonrası kontrol | Depo bakımı için; kendi işin için örnek olarak okuyabilirsin |
| `/is-brifi` ([SKILL.md](../.claude/skills/is-brifi/SKILL.md)) | Talebi tek dosyalık [iş kaydına](../sablonlar/is-kaydi.md) çevirir: kapsam, kaynak, karar, pilot, kabul ölçütü | Taslak |
| `/kabul-kontrolu` ([SKILL.md](../.claude/skills/kabul-kontrolu/SKILL.md)) | Çıktıyı kaynak ve kabul ölçütleriyle karşılaştırır, geçti / kaldı / sınanmadı tablosu üretir | Taslak |
| `/devir-notu` ([SKILL.md](../.claude/skills/devir-notu/SKILL.md)) | Yeni oturumun eski sohbeti okumadan devam edebileceği devam notunu yazar | Taslak |
| [araclar/kontrol.py](../araclar/kontrol.py) | Bağlantı, kod bloğu, özel veri örüntüsü ve checksum kontrolü; GitHub'da her değişiklikte otomatik çalışır | Bakım aracı |

Skill'ler [komutların](../komutlar/README.md) ve şablonların skill biçimidir. **Taslak** etiketi şu anlama gelir: talimatlar kurmaca demo üzerinde ayrı bir AI okuyucuyla denendi ([doğrulama notu](../DOGRULAMA.md)); gerçek bir işte iki kez elle çalıştırılma kuralı henüz tamamlanmadı ve Claude'un skill'i kendiliğinden tetiklemesi sınanmadı. İlk gerçek kullanımında kabul kaydı tut.

Kendi projende kullanmak için `.claude/skills/` altındaki klasörleri kendi projenin `.claude/skills/` klasörüne veya bütün projelerde geçerli olması için `~/.claude/skills/` altına kopyala. Frontmatter yalnız `name` ve `description` alanlarını içerdiği için resmî belgeye göre claude.ai'ye skill olarak yüklemeye de uygun; yükleme denenmedi. Kontrolün her seferinde ayrı bir bağlamda çalışmasını istersen Claude Code'da `kabul-kontrolu` frontmatter'ına `context: fork` satırını ekleyebilirsin; bu satır claude.ai yüklemesinde hata verir.

## Güncel modellerle komut yazmak

Aşağıdaki öneriler Anthropic'in [genel istem rehberinden](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) ve [Claude Opus 5.5 istem notlarından](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) alındı. Paketin [komutları](../komutlar/README.md) 25 Eylül'de bu önerilere göre yeniden biçimlendirildi; içerikleri ve sınırları aynı kaldı.

**Düşünme derinliği ayarla yönetilir, cümleyle değil.** Claude Opus 5.5'te düşünme her zaman açıktır ve ne kadar düşüneceğini effort düzeyi belirler; varsayılanı `medium`. Claude Code'da düzey `/effort` ile değiştirilir ([model ayarları](https://code.claude.com/docs/en/model-config)). “Adım adım düşün” veya “derin düşün” satırları gereksizdir; resmî not, sohbet ürünlerinde bu tür satırları kaldırmanın yanıtı hızlandırdığını, kaliteyi belirgin biçimde düşürmediğini söylüyor. Daha az düşünüp daha hızlı yanıt vermesini istiyorsan önce effort düzeyini düşür; resmî nota göre bu, istem cümlelerinden daha güvenilir çalışıyor.

**Akıl yürütmeyi yanıtta yazdırmaya çalışma, dayanağı iste.** Opus 5.5'te modelin iç akıl yürütmesini yanıt metninde yeniden yazdırmaya zorlayan istekler reddedilebiliyor. Protokolün istediği zaten başka bir şey: her önemli iddianın hangi kaynağa dayandığını göstermek. “Nasıl düşündüğünü yaz” yerine “bu cümlenin dayanağını kaynaktan göster” iste.

**Kısıtın nedenini yaz.** Rehber, talimatın gerekçesini vermenin modelin amacı daha iyi anlamasını sağladığını belirtiyor. “Link uydurma” yerine “Kişi bu metinle kendini tanıtacak; uydurulmuş link ona zarar verir” daha iyi genellenir. Paketteki gerçek sınırlar (uydurma yok, izinsiz yayın yok, insan kararı AI önerisinden ayrı) kalır; değişen yalnız anlatım.

**Baskı dili kullanma.** “ÇOK ÖNEMLİ”, “MUTLAKA” gibi vurgular eski modellerde eksik tetiklenmeyi telafi etmek için yazılıyordu. Resmî rehber, Opus 4.5 ve 4.6'nın sistem talimatına öncekilerden daha duyarlı olduğunu ve bu vurguların artık gereğinden fazla tetiklemeye yol açabileceğini yazıyor; önerisi düz talimat. Düz cümleyle yaz.

**Ne istediğini yaz, girdiyi ayır.** Yasak listesi yerine istenen sonucu tarif et. Girdiyi `<girdi>` gibi etiketlerle talimattan ayır; uzun girdiyi talimatın üstüne koy. Resmî rehber, soruyu sona koymanın özellikle çok belgeli girdilerde yanıt kalitesini artırdığını belirtiyor.

**Kapsamı dar tut.** Rehber, istenmeyen iyileştirme ve özellik eklenmemesini öneriyor. Bu, protokoldeki “AI gereksiz yere kapsamı büyüttü” reçetesiyle aynı: son kullanıcı amacına dön, yeni öneriyi ayrı etiketle.

**Subagent'ı gerektiğinde kullan.** Resmî öneri: paralel yürüyebilen, ayrı bağlam isteyen veya birbirinden bağımsız işlerde subagent; basit, sıralı veya tek dosyalık işte doğrudan çalışma. Rehbere göre Opus 4.6 ve Opus 5 subagent'a öncekilerden daha kolay iş veriyor; gereksiz dağıtım görürsen ne zaman yardımcı kullanılacağını açıkça yaz.

## İlk deneme

1. Bu depoyu klonla ve Claude Code'u depo klasöründe aç. Kişisel iş kayıtlarını `work/` altında tut; bu klasör `.gitignore`'da.
2. `/is-brifi` ile [demo girdisini](../ornekler/ilk-demo/girdi.md) iş kaydına çevir.
3. [Komut 1](../komutlar/README.md) ile metinleri üret ve dosyaya kaydet.
4. Yeni bir oturumda `/kabul-kontrolu` ile çıktıyı kontrol et; sonucu [beklenen çıktıyla](../ornekler/ilk-demo/beklenen-cikti.md) karşılaştır.
5. `/devir-notu` ile kapat. Ertesi gün yalnız bu notla başlamayı dene.

Aynı akışı kendi paylaşılabilir işinle tekrarladığında nerede takıldığını [tekrar raporuyla](https://github.com/AlperenKayalar/ai-ile-calisma-duzeni/issues/new?template=tekrar-raporu.md) paylaşabilirsin.
