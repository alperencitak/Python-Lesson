def tekrarla(sayiF,kelimeF):
    for i in range(sayiF):
        print(kelimeF)
sayi = 3
kelime = "Hello"
tekrarla(sayi,kelime)

list = []
def makeList(*args):
    for arg in args:
        list.append(arg)
makeList(10,20,30)
print(list)

def asalBul(altS,ustS):
    for i in range(altSinir,ustSinir+1):
        kontrol = 0
        for j in range(2,int(i/2)):
            if(i%j==0):
                kontrol=1
        if kontrol == 0:
            print(i,end=" ")
altSinir = 6
ustSinir = 35
asalBul(altSinir,ustSinir)
