class Sorular():
    def __init__(self,soru,cevap):
        self.soru = soru
        self.cevap = cevap
    def soruGoster(self):
        print(f"Soru: {self.soru}")

soru1 = Sorular("5 x 9 = ?",45)
soru2 = Sorular("4 % 2 = ?",0)
soru3 = Sorular("18 - 6 = ?", 12)
soru4 = Sorular("36 / 12 = ?", 3)
soru5 = Sorular("29 + 27 = ?", 56)
soruDizi = [soru1,soru2,soru3,soru4,soru5]
dogru,yanlis=0,0
print("--------- QUIZ ---------")
for i in range(5):
    print(soruDizi[i].soruGoster())
    kullanici = int(input("Cevabınız: "))
    if soruDizi[i].cevap == kullanici:
        dogru+=1
    else:
        yanlis+=1
print(f"\n{dogru} doğru\n{yanlis} yanlış")