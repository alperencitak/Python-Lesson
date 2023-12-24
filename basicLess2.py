# values = 1,2,3,4,5
# x,*y=values
# print(x,y)
x,y,z=2,5,10
numbers=1,5,7,10,6
#print(int(x/y))
x,*y,z=numbers
#print(x,y,z)
i,toplam=0,0
while i < len(y):
    toplam += y[i]
    i+=1
#print(toplam)

# vize = input("Vize notunuzu giriniz: ")
# vize = int(vize)
# final = input("Final notunuzu giriniz: ")
# final = int(final)
# ortalama = vize*40/100 + final*60/100
# print(ortalama)

name="ahmet"
#print("a" in name)