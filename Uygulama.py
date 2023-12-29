import hesapmakinesi.hesaplamalar
import oyunlar.oyun

def anamenu():
    print("╔══════════════════════════════╗")
    print("║       PYTHON PROGRAMLAR      ║")
    print("║                              ║")
    print("║       1-Hesap Makinesi       ║")
    print("║           2-Oyunlar          ║")
    print("║          3-Çizimler          ║")
    print("║       Seçiminiz Nedir?       ║")
    print("╚══════════════════════════════╝")
    secim=input()
    if secim=="1":
        hesapmakinesi.hesaplamalar.hmmenu()
        anamenu()
    if secim=="2":
        oyunlar.oyun.oyunmenu()
        anamenu()
    else:
        anamenu()

anamenu()
