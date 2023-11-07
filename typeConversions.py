print("Bir sayi girin")
ssayi = input()
sayi = int(ssayi) #input karakter dizisi alır. Bunu integer veri tipine çevirdik.
sayi *=2
print("Girdiginiz sayinin 2 ile carpimi =",sayi)

sayi1str = input("Bir sayi giriniz : ")
sayi2str = input("Bir sayi daha giriniz : ")
sayi1 = int(sayi1str)
sayi2 = int(sayi2str)
sonuc = sayi1 ** sayi2
print(sayi1,"ussu",sayi2,"=",sonuc)

isim = input("Lutfen isminizi giriniz : ")
print("İsminiz : ",isim,sep="")

a = 15
b = "23"
a = str(a)
print(a+" "+b)

number = 231543697
strnumber = str(number)
print("Number'in basamak sayisi =",len(strnumber))
print(len(str(number)))
print(len(str(123456789)))

print(type(12+0j),complex(15),sep="\n")

"""
int() Sayı degerli bir karakter dizisini veya kayan noktalı sayıyı tamsayıya (integer ) çevirir.
float() Sayı degerli bir karakter dizisini veya tamsayıyı kayan noktalı sayıya (2oat ) çevirir.
str() Bir tamsayı veya kayan noktalı sayıyı karakter dizisine (string ) çevirir.
complex() Herhangi bir sayıyı veya sayı degerli karakter dizisini karmasık sayıya (complex) çevirir.
"""
