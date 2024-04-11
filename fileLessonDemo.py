
if __name__ == '__main__':
    def notHesapla(satir):
        satir = satir[:-1]
        liste = satir.split('-')
        ogrenciAdi = liste[0]
        notlar = liste[1].split(',')
        not1 = int(notlar[0])
        not2 = int(notlar[1])
        not3 = int(notlar[2])
        ortalama=(not1+not2+not3)/3
        if ortalama>=90 and ortalama<=100:
            harf="AA"
        elif ortalama >= 85:
            harf="BA"
        elif ortalama >= 65:
            harf="CC"
        else:
            harf="FF"
        return ogrenciAdi + ": " + harf + "\n"
    def notlariOku():
        with open("sinavNotlari.txt","r",encoding="utf-8") as file:
            for satir in file:
                print(notHesapla(satir))
    def notGir():
        ad = input("Öğrenci Adı: ")
        soyad = input("Öğrenci Soyadı: ")
        not1 = input("Öğrenci 1.Not: ")
        not2 = input("Öğrenci 2.Not: ")
        not3 = input("Öğrenci 3.Not: ")

        with open("sinavNotlari.txt","a",encoding="utf-8") as file:
            file.write(ad + " " + soyad + "-" + not1 + "," + not2 + "," + not3 + "\n")
    def notlariKayitEt():
        with open("sinavNotlari.txt","r",encoding="utf-8") as file:
            liste = []
            for satir in file:
                liste.append(notHesapla(satir))
        with open("kayitliNotlar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


    while True:
        islem = input("\n1-Notları oku\n"
                      "2-Not gir\n"
                      "3-Notları kayıt et\n"
                      "4-Çıkış\n"
                      "İşlem = ")
        if islem=='1':
            notlariOku()
        elif islem=='2':
            notGir()
        elif islem=='3':
            notlariKayitEt()
        elif islem=='4':
            break
