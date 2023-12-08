print("""
Toplama (1)
Çıkarma (2)
Çarpma (3)
Bölme (4)
""")

while(1):
    giris = input("Yapmak istediğiniz işlemi seçiniz : ")
    giris = int(giris)

    if giris == 1:
        break
    elif giris == 2:
        break
    elif giris == 3:
        break
    elif giris == 4:
        break
    else:
        print("Yanlış giriş yaptınız tekrar deneyin\n")

if giris == 1:
    sayi1 = input("Toplamak istediğiniz birinci sayı : ")
    sayi2 = input("Toplamak istediğiniz ikinci sayı : ")
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    sonuc = sayi1 + sayi2
elif giris == 2:
    sayi1 = input("Çıkarmak istediğiniz birinci sayı : ")
    sayi2 = input("Çıkarmak istediğiniz ikinci sayı : ")
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    sonuc = sayi1 - sayi2
elif giris == 3:
    sayi1 = input("Çarpmak istediğiniz birinci sayı : ")
    sayi2 = input("Çarpmak istediğiniz ikinci sayı : ")
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    sonuc = sayi1 * sayi2
elif giris == 4:
    sayi1 = input("Bölmek istediğiniz birinci sayı : ")
    sayi2 = input("Bölmek istediğiniz ikinci sayı : ")
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    sonuc = sayi1 / sayi2

print("Sonuc = {}".format(sonuc))