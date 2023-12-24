d1 = open("isimler1.txt", encoding="utf-8")
d1_satirlar = d1.readlines()
d2 = open("isimler2.txt", encoding="utf-8")
d2_satirlar = d1.readlines()

liste = ""

for kontrol in d1_satirlar:
    if not kontrol in d2_satirlar:
        liste += kontrol

print(liste)

d1.close()
d2.close()
