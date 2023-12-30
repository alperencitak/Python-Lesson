citys = ["İstanbul","Ankara","İzmir","Kahramanmaraş","Bolu"]
max5LettersCitys = []
for city in citys:
    result = len(city)<=5
    if result:
        max5LettersCitys.append(city)
print(f"max 5 harften oluşan şehirler = {max5LettersCitys}")

urunler = [
    {"name":"Samsung S6","price":3000},
    {"name":"Samsung S7","price":4000},
    {"name":"Samsung S8","price":5000},
    {"name":"Samsung S9","price":6000},
    {"name":"Samsung S10","price":7000}
]
toplam = 0
for urun in urunler:
    toplam += urun["price"]
print(toplam)

name = "" #False
while not name.strip():
    name = input("İsminiz: ")
print(f"Kayıt tamamlandı {name}")

sayilar = [1,3,5,7,9,12,19,21]
i=0
while i<len(sayilar):
    print(sayilar[i],end=" ")
    i+=1

tekSayılar = []
baslangic = int(input("Alt sınırı giriniz: "))
bitis = int(input("Üst sınırı giriniz: "))
if baslangic%2==0:
    baslangic+=1
i = baslangic
while i <= bitis:
    tekSayılar.append(i)
    i+=2
print(tekSayılar,end=" ")

dizi = []
i = 0
while i<5:
    dizi.append(int(input(f"{i+1}.Sayıyı giriniz: ")))
    i+=1
i = 0
dizi.sort()
print(dizi)

k=0
while k<20:
    k+=1
    if k%2==0:
        continue
    print(k,end=" ")

dizi = "naber"
for i in enumerate(dizi):
    print(i)