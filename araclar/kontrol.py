#!/usr/bin/env python3
"""Paketin dosya kontrolleri.

DOGRULAMA.md'deki elle yapılan kontrollerin tekrar çalıştırılabilir hali:
depo içi Markdown bağlantıları, kod bloğu dengesi, seçili özel veri
örüntüleri ve SHA256SUMS.txt güncelliği.

Kullanım:
    python3 araclar/kontrol.py              # kontrol et
    python3 araclar/kontrol.py --guncelle   # SHA256SUMS.txt'yi yeniden yaz, sonra kontrol et
    python3 araclar/kontrol.py --kati       # checksum farkını da hata say

Yalnız Python standart kütüphanesi kullanır.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
SUMS = "SHA256SUMS.txt"

LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^\s*(```|~~~)")

# Otomatik tarama her hassas bilgiyi bulmaz; bilinen biçimleri yakalar.
OZEL_ORUNTULER = [
    ("yerel kullanıcı yolu", re.compile(r"/Users/[A-Za-z]|/home/[a-z]|[A-Z]:\\\\Users\\\\")),
    ("e-posta adresi", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}")),
    ("API anahtarı biçimi", re.compile(r"sk-[A-Za-z0-9_-]{16,}|sk-ant-[A-Za-z0-9_-]{8,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|xox[abp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}")),
    ("özel sohbet bağlantısı", re.compile(r"chatgpt\.com/c/|claude\.ai/chat/|claude\.ai/code/session_|claude\.ai/share/")),
]
# Bu dosyalarda örüntü eşleşmesi beklenir (lisans metni, bu betiğin kendisi).
OZEL_TARAMA_DISI = {"LICENSE", "araclar/kontrol.py", SUMS}


def dosyalar():
    """Git'in izlediği ve yok sayılmayan dosyalar; git yoksa klasör taraması."""
    try:
        cikti = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=KOK, capture_output=True, text=True, check=True,
        ).stdout
        liste = [s for s in cikti.splitlines() if s and (KOK / s).is_file()]
    except (OSError, subprocess.CalledProcessError):
        liste = [
            str(p.relative_to(KOK)).replace(os.sep, "/")
            for p in KOK.rglob("*")
            if p.is_file() and ".git" not in p.parts
        ]
    return sorted(set(liste))


def baglanti_kontrolu(md_dosyalari):
    hatalar = []
    sayac = 0
    for yol in md_dosyalari:
        metin = (KOK / yol).read_text(encoding="utf-8")
        kod_icinde = False
        for no, satir in enumerate(metin.splitlines(), 1):
            if FENCE.match(satir):
                kod_icinde = not kod_icinde
                continue
            if kod_icinde:
                continue
            for hedef in LINK.findall(satir):
                if re.match(r"^[a-z][a-z0-9+.-]*:", hedef) or hedef.startswith("#"):
                    continue
                sayac += 1
                dosya_kismi = hedef.split("#", 1)[0]
                if not dosya_kismi:
                    continue
                if not (KOK / yol).parent.joinpath(dosya_kismi).resolve().exists():
                    hatalar.append(f"{yol}:{no}: kırık bağlantı -> {hedef}")
    return sayac, hatalar


def kod_blogu_kontrolu(md_dosyalari):
    hatalar = []
    for yol in md_dosyalari:
        acilis = sum(1 for s in (KOK / yol).read_text(encoding="utf-8").splitlines() if FENCE.match(s))
        if acilis % 2:
            hatalar.append(f"{yol}: kapanmamış kod bloğu ({acilis} çit satırı)")
    return hatalar


def ozel_veri_kontrolu(tum):
    hatalar = []
    for yol in tum:
        if yol in OZEL_TARAMA_DISI:
            continue
        try:
            metin = (KOK / yol).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for no, satir in enumerate(metin.splitlines(), 1):
            for ad, oruntu in OZEL_ORUNTULER:
                if oruntu.search(satir):
                    hatalar.append(f"{yol}:{no}: olası {ad}")
    return hatalar


def ozet_listesi(tum):
    satirlar = []
    for yol in tum:
        if yol == SUMS:
            continue
        ozet = hashlib.sha256((KOK / yol).read_bytes()).hexdigest()
        satirlar.append(f"{ozet}  {yol}")
    return "\n".join(satirlar) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--guncelle", action="store_true", help="SHA256SUMS.txt dosyasını yeniden yaz")
    ap.add_argument("--kati", action="store_true", help="checksum farkını hata say")
    args = ap.parse_args()

    tum = dosyalar()
    md = [y for y in tum if y.endswith(".md")]

    if args.guncelle:
        (KOK / SUMS).write_text(ozet_listesi(tum), encoding="utf-8")
        print(f"{SUMS} güncellendi ({len(tum) - (SUMS in tum)} dosya).")

    sayac, hatalar = baglanti_kontrolu(md)
    hatalar += kod_blogu_kontrolu(md)
    hatalar += ozel_veri_kontrolu(tum)

    uyarilar = []
    mevcut = (KOK / SUMS).read_text(encoding="utf-8") if (KOK / SUMS).exists() else ""
    if mevcut != ozet_listesi(tum):
        uyarilar.append(f"{SUMS} güncel değil. Düzeltmek için: python3 araclar/kontrol.py --guncelle")

    print(f"{len(tum)} dosya, {len(md)} Markdown, {sayac} depo içi bağlantı kontrol edildi.")
    for u in uyarilar:
        print(f"::warning::{u}" if os.environ.get("GITHUB_ACTIONS") else f"UYARI: {u}")
    for h in hatalar:
        print(f"::error::{h}" if os.environ.get("GITHUB_ACTIONS") else f"HATA: {h}")

    if hatalar or (args.kati and uyarilar):
        return 1
    print("Kontroller geçti." + (" (uyarı var)" if uyarilar else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
