---
name: is-brifi
description: Bir iş talebini AI ile Çalışma Düzeni protokolünün ilk adımlarına göre tek dosyalık iş kaydına çevirir - kapsam, kaynak envanteri, insan kararları, dar pilot ve kabul ölçütleri. Yeni bir iş başlarken, dağınık bir istek uygulanabilir göreve dönüştürülecekken veya kullanıcı brif çıkarmayı, kapsamı netleştirmeyi istediğinde kullan.
---

# İş brifi

Talep: $ARGUMENTS (boşsa konuşmadaki talebi kullan)

Amaç, talebi başka bir kişinin sözlü açıklamaya ihtiyaç duymadan izleyebileceği bir iş kaydına çevirmek. Kayıt bu depodaki `sablonlar/is-kaydi.md` biçimini izler; başka bir projedeysen aşağıdaki bölümler yeterli.

Önce mevcut olanı oku: ilgili dosyalar, önceki iş kayıtları, varsa son devam notu. Aynı iş zaten kayıtlıysa yeni kayıt açma, onu güncelle; iki kayıt aynı işin durumunu farklı gösterirse sonraki oturum hangisine güveneceğini bilemez.

Kayıtta bulunması gerekenler:

- **Brif:** tek cümlelik hedef, hedef kitle, kapsama dahil ve hariç olanlar, çıktılar ve konumları, yayın hedefi ve işlem yetkisi.
- **Kaynaklar:** her kaynağın konumu, biliniyorsa kendi tarihi, son kontrol tarihi ve erişim durumu (okundu / yalnız listede / erişilemedi). Erişemediğin kaynağı var veya yok diye değil, "bilinmiyor" diye yaz.
- **Kararlar:** iş sahibinin verdiği kararlar ile AI önerileri ayrı sütunlarda. Ücret, görünürlük, yayın hedefi, deneyim tarihi gibi kaynakta bulunmayan kararlar "karar bekliyor" listesine girer; yanına bu karara bağlı olmadan sürdürülebilecek işi yaz.
- **Pilot ve kabul:** tek iş; bir ana çıktı ve ondan uyarlanan en fazla iki teslim; en fazla beş gözlenebilir kabul ölçütü. Uzunluk gibi alıştırma hedefleri kabul ölçütü sayılmaz, brifte ayrı yazılır. Yayın, gönderim veya ödeme gibi geri alınamayacak bir işlem pilotun koşulu olmasın.

Kaydı kullanıcının belirttiği yere yaz. Konum belirtilmediyse ve bu public rehber deposunun içindeysen `work/` veya `private/` altına yaz (ikisi de .gitignore'da), çünkü kişisel iş kayıtları public pakete girmemeli.

Sonunda kullanıcıya üç şey söyle: kaydın yolu, iş sahibinin vermesi gereken kararlar ve ilk sonraki adım.
