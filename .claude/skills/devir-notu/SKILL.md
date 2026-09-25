---
name: devir-notu
description: Oturum sonunda, yeni bir oturumun eski sohbeti okumadan devam edebileceği devam notu yazar. Kullanıcı günü veya işi kapatmak, devretmek ya da kaldığı yerden sonra devam etmek istediğinde, uzun bir işte bağlam dolmadan önce veya iş başka bir kişiye ya da ajana aktarılırken kullan.
---

# Devam notu

İş: $ARGUMENTS (boşsa bu oturumun işi)

Bu not, yeni oturumun ilk okuyacağı metin olacak ve o oturumun elinde eski sohbet olmayacak. Bu yüzden gereken her bilgi ya notun içinde ya da notta adı geçen dosyada durmalı.

Yazmadan önce çıktıların gerçekten var olduğunu kontrol et: dosyaları aç; depo varsa `git status` ve son commit'lere bak. "Tamamlandı" etiketini yalnız kontrol edilmiş iş taşır. Planlanmış bir takibin kurulmuş olması, çalıştığı anlamına gelmez.

Notta bulunması gerekenler (bu depoda `sablonlar/kapanis.md` alanları):

- başlangıç amacı ve bu oturumda gerçekten yapılan
- çıktıların konumu (dosya yolu veya adres)
- yapılan kontrol ve sonucu; hedefte doğrulanıp doğrulanmadığı
- iş sahibinin bu oturumda verdiği kararlar
- henüz seçilmemiş AI önerileri, ayrı bir liste olarak; bunlar görev taahhüdü değildir
- açık kalanlar ve engelin nedeni
- ilk sonraki adım ve sorumlusu
- aynı işi yeniden oluşturmamak için mevcut kaydın yeri

Kullanıcı bir dosya belirttiyse notu oraya yaz; belirtmediyse iş kaydının devam bölümünü güncelle. Aynı notu iki yerde tutma, zamanla birbirinden ayrılırlar. Bu public rehber deposundaysan `work/` veya `private/` altına yaz; kişisel iş kayıtları public pakete girmemeli. Notun sonuna yeni oturum için kısa bir başlangıç komutu ekle; kapanış şablonundaki hazır metin örnek alınabilir.
