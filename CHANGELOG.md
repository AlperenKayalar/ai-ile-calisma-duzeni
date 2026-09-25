# Sürüm geçmişi

## 0.1.1 · 25 Eylül 2026

Bakım ve Claude Code eki. 8 Eylül deneyim kesiti ve 9 Eylül gözlemi değiştirilmedi.

- Yeni bölüm: [Protokolü Claude Code ile uygulamak](rehber/09-claude-ile-uygulama.md). Protokol parçalarının CLAUDE.md, skill, subagent, MCP, hooks ve zamanlanmış görev karşılıkları; Claude Opus 5.5 ve güncel modeller için komut yazımı. Kaynaklar 25 Eylül'de okunan resmî sayfalar.
- Üç taslak Claude Code skill'i: `/is-brifi`, `/kabul-kontrolu`, `/devir-notu` (`.claude/skills/`).
- Depoyu Claude ile düzenlerken korunacak kurallar için [CLAUDE.md](CLAUDE.md).
- [Komutlar](komutlar/README.md) güncel istem rehberine göre yeniden biçimlendirildi: girdi etiketlerle ayrıldı ve başa alındı, önemli kısıtların gerekçesi eklendi. İçerik ve sınırlar aynı.
- Eksik şablon eklendi: tek dosyalık [iş kaydı](sablonlar/is-kaydi.md) (protokoldeki `PILOT-01` düzeni).
- Yeni Komut 1 ve taslak skill'ler kurmaca demo üzerinde iki ayrı AI okuyucuyla denendi; çıkan belirsizlikler skill'lerde, Komut 1'de, iş kaydı ve kabul kaydı şablonlarında düzeltildi ([doğrulama notu](DOGRULAMA.md)).
- Otomatik dosya kontrolü: [araclar/kontrol.py](araclar/kontrol.py) ve GitHub Actions iş akışı. `SHA256SUMS.txt` yeniden üretildi; önceki listede `README.en.md` yoktu.
- GitHub için tekrar raporu ve düzeltme issue şablonları, pull request şablonu.
- Düzeltmeler: yayın akışındaki altı komut, komutlar dosyasındakilerle karışmaması için “yayın komutu” diye yeniden adlandırıldı; bölüm 06'daki olmayan “bağlantı kartı” yerine platform kartına bağlantı verildi; yayın dosyalarındaki GitHub yer tutucusu depo adresiyle dolduruldu; Runway bağlantısı yeni alan adına taşındı; README'ye dil bağlantısı eklendi; `.gitignore`'a Claude Code kişisel dosyaları eklendi.

## 0.1-en · 14 Eylül 2026

- Çalışan İngilizce dizin: [README.en.md](README.en.md). İçerik bağlantıları Türkçe dosyalara gider.

## 0.1 ek güncellemesi · 9 Eylül 2026

- Chrome'da açık yedi yardımcı aracın arayüz gözlemi, önerilen görevleri ve deneme sınırları.
- Ortak yardımcı görev kartı, devir komutu ve 10 dakikalık yayın uygulaması önerisi.
- Ana rehber, platformlar ve tekrar protokolüne bağlantılar.

Bu ek rehber içeriğini genişletir; araçlarda yeni üretim, hesap kurulumu, API/MCP/CLI bağlantısı veya sosyal yayın yapılmadı. `VERSION` 0.1 sürümünü göstermeye devam eder.

## 0.1 · 9 Eylül 2026

İlk rehber paketi. Kaynak kesiti 8 Eylül 2026, 23.57 İstanbul.

- 8 Eylül ağırlıklı gerçek süreç ve karar kronolojisi.
- Girdi, rol, çıktı, kabul ve hata halinde devam adımlarıyla uygulama protokolü.
- On çalışma şablonu, komutlar ve kurmaca tam prova.
- 60 dakikalık canlı yayın, altı bölüm ve 12 kısa içerik açısı.
- Bağımsız AI okuyucuyla yerel metin provası ve dosya kontrolleri.

Başka gerçek kullanıcıda uçtan uca tekrar, canlı platform testi ve karşılaştırmalı zaman/gelir kazanımı bu sürümde doğrulanmış değildir. Sürüm numarası uzak depo yayınının gerçekleştiğini tek başına göstermez.
