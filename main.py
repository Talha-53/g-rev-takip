import json
from datetime import datetime

DOSYA_ADI = "gorevler.txt"

def gorevleri_yukle():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Yeni görev listesi başlatılıyor.")
        return []

def gorevleri_kaydet(gorevler_listesi):
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(gorevler_listesi, dosya, indent=4, ensure_ascii=False)

gorevler = gorevleri_yukle()

def gorevleri_listele():
    if not gorevler:
        print("Hiç görev yok.")
    else:
        for i, gorev in enumerate(gorevler, 1):
            durum = "✅" if gorev["tamamlandi"] else "❌"
            print(f"{i}. [{durum}] {gorev['metin']} (Eklendi: {gorev['tarih']})")

def gorev_ekle():
    metin = input("Yeni görevi yazın: ").strip()
    if metin:
        yeni_gorev = {
            "metin": metin,
            "tamamlandi": False,
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)
        print("Görev eklendi.")
    else:
        print("Boş görev eklenemez.")

def gorev_sil():
    gorevleri_listele()
    try:
        sil = int(input("Silinecek görevin numarası: "))
        if 1 <= sil <= len(gorevler):
            silinen = gorevler.pop(sil - 1)
            gorevleri_kaydet(gorevler)
            print(f"'{silinen['metin']}' silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def gorev_tamamla():
    gorevleri_listele()
    try:
        numara = int(input("Tamamlandı olarak işaretlenecek görev numarası: "))
        if 1 <= numara <= len(gorevler):
            gorevler[numara - 1]["tamamlandi"] = True
            gorevleri_kaydet(gorevler)
            print("Görev tamamlandı olarak işaretlendi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def uygulamayi_calistir():
    while True:
        print("\n--- GÖREV TAKİP MENÜ ---")
        print("1 - Görevleri Listele")
        print("2 - Görev Ekle")
        print("3 - Görev Sil")
        print("4 - Görev Tamamla")
        print("5 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            gorevleri_listele()
        elif secim == "2":
            gorev_ekle()
        elif secim == "3":
            gorev_sil()
        elif secim == "4":
            gorev_tamamla()
        elif secim == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

uygulamayi_calistir()
