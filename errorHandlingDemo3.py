
if __name__ == '__main__':
    # liste = ["1","2","5a","10b","abc"]
    # liste2 = []
    # for x in liste:
    #     try:
    #         liste2.append(int(x))
    #     except Exception as ex:
    #         continue
    # print("Sayı olan elemanlar: {}".format(liste2))
    # meyveler = ["elma", "armut", "çilek", "kiraz"]
    # for sıra, öğe in enumerate(meyveler, 1):
    #     print("{}. {}".format(sıra, öğe))


    # while True:
    #     deger = input("Bir sayı giriniz ya da çıkmak için q giriniz: ")
    #     if deger == 'q':
    #         break
    #     try:
    #         int(deger)
    #     except Exception as ex:
    #         print("Sadece sayı ve 'q' girebilirsiniz!")
    #         continue

    # def checkPassword(parola):
    #     turkceAlf = "çğıöşüÇĞİÖŞÜ"
    #     for i in parola:
    #         if i in turkceAlf:
    #             raise TypeError("Parola türkçe karakter içeremez")
    #         else:
    #             print("Geçerli parola")
    # parola = input("Parola giriniz: ")
    # try:
    #     checkPassword(parola)
    # except TypeError as ex:
    #     print(ex)

    def faktoriyel(sayi):
        if sayi < 0:
            raise ValueError("Negatif Değer Girdiniz!")
        elif sayi == 0:
            return 1
        elif sayi != 1:
            sayi *= faktoriyel(sayi-1)
        return sayi
    try:
        print(faktoriyel(-1))
    except ValueError as ex:
        print(ex)