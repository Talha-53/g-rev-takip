# gorev-takip
DOSYA_ADI = "gorevler.txt"

def gorevleri_yukle():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return [satir.strip() for satir in dosya.readlines()]
    except FileNotFoundError:
        print("Henüz görev dosyası oluşturulmamış. Yeni bir tane oluşturulacak.")
        return []

def gorevleri_kaydet(gorevler_listesi):
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        for gorev in gorevler_listesi:
            dosya.write(gorev + "\n")

gorevler = gorevleri_yukle()

def gorevleri_listele():
    if not gorevler:
        print("Hiç görev yok.")
    else:
        for i, gorev in enumerate(gorevler, 1):
            print(f"{i}. {gorev}")

def gorev_ekle():
    yeni_gorev = input("Yeni görevi yazın: ").strip()
    if yeni_gorev:
        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)
        print("Görev eklendi.")
    else:
        print("Boş görev eklenemez.")

def gorev_sil():
    gorevleri_listele()
    try:
        silinecek = int(input("Silmek istediğiniz görevin numarasını yazın: "))
        if 1 <= silinecek <= len(gorevler):
            silinen = gorevler.pop(silinecek - 1)
            gorevleri_kaydet(gorevler)
            print(f"'{silinen}' silindi.")
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
        print("4 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            gorevleri_listele()
        elif secim == "2":
            gorev_ekle()
        elif secim == "3":
            gorev_sil()
        elif secim == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

uygulamayi_calistir()
