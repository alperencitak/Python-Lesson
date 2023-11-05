baslik = "Deneme File Location"
print(baslik, "\n", "-"*len(baslik),sep="")
print(r"C:\Desktop\deneme.txt")

print("Merhaba\rZalim Dunya!") #satırı baştan başlatır.
print("Merhaba\rDunya")

print("düşey\bsekme") #Solundaki bir karakteri siler.
print("düşey\b sekme")
print("düşey\b\b\bsekme")

print("\u0061") #Küçük UNİCODE yazımı yapar.
print("\U00000061") #Büyük UNİCODE yazımı yapar.

import unicodedata
print(unicodedata.name('b')) # \N deki ismini buluyoruz.
print("\N{LATIN SMALL LETTER B}") # \N ismini verdiğimiz harfi yazdırıyoruz.

print("\x4E")
print("\x41") # 16'lık sistemdeki değeri ile harfi yazdırmaya yarar.

f = open("kacisDizi.txt", "w")
print("deneme\fdeneme", file=f) #sayfa başı yapar.
f.close()

r"""
\’ Karakter dizisi içinde tek tırnak isaretini kullanabilmemizi saglar.
\” Karakter dizisi içinde çift tırnak isaretini kullanabilmemizi saglar.
\\ Karakter dizisi içinde \ isaretini kullanabilmemizi saglar.
\n Yeni bir satıra geçmemizi saglar.
\t Karakterler arasında sekme boslugu bırakmamızı saglar.
\u UNICODE kod konumlarını gösterebilmemizi saglar.
\U UNICODE kod konumlarını gösterebilmemizi saglar.
\N Karakterleri UNICODE adlarına göre kullanabilmemizi saglar.
\x Onaltılı sistemdeki bir sayının karakter karsılıgını gösterebilmemizi saglar.
\a Destekleyen sistemlerde, kasa hoparlöründen bir ‘bip’ sesi verilmesini
saglar.
\r Aynı satırın basına dönülmesini saglar.
\v Destekleyen sistemlerde düsey sekme olusturulmasını saglar.
\b Imlecin sola dogru kaydırılmasını saglar
\f Yeni bir sayfaya geçilmesini saglar.
r Karakter dizisi içinde kaçıs dizilerini kullanabilmemizi saglar.
"""