a = 10.54
b = 25.8

print("sonuc : ",a+b,sep="")
print("sonuc",a+b,"\n",sep=" : ")
#sep=" "(default hali) printte virgul kullanildiginda araya giren degerdir.
#separator = ayirici, ayrac

print("Python")
print("Ders")

print("Python",end=" ")
print("Ders")
#end="\n"(default hali) printin sonunda yapicalak eylemi belirler.

#sep ve end parametresi printin sonunda kullanilir yoksa hata olusur.

print("12345")
print(*"12345")
print(*"12345",sep=" - ")
# * printi suna donusturur = print("1","2","3","4","5")
# * kullanildiktan sonra virgul kullanilamaz.
# Ornek print(*"12345","6789") yazilamaz.
# Ancak print("12345",*"6789") yazilabilir.

print(r"python \n ders \t temel")
# r kullanmak \ isaretini etkisiz birakir.

print("")