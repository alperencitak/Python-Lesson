while True:
    print("""
    Asal Sayi Bulan Program
    -----------------------
    """)
    sayiStr = input("Bir sayi giriniz : ")
    sayi = int(sayiStr)
    sinir = int(sayi / 2)
    result = False
    for i in range(2, sinir + 1):  # 7,8,9
        if sayi % i == 0:
            result = True
        pass

    if sayi < 2:
        print("Sayiniz asal degildir.")
    else:
        if result == True:
            print("Sayiniz asal degildir.")
        else:
            print("Sayiniz asaldir.")

