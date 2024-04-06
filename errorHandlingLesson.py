


if __name__ == '__main__':
    try:
        print("birinci sayıyı giriniz: ")
        x = int(input())
        print("ikinci sayıyı giriniz: ")
        y = int(input())
        toplam = x / y
        print(f"toplam = {toplam}")
    except Exception as exception:
        print("Error = {}".format(exception))
    else:
        print("Hata yok")
    finally:
        print("Program shutdown")
