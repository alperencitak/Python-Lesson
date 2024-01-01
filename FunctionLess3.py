def yasHesapla(fyil):
    return 2023 - fyil
def emeklilikZamani(yas):
    '''
    Bu fonksiyon kullanıcıdan yasını alıp emekliliğine kaç yıl kaldığını ya da
    emekli olduğunu söylemek için tasarlanmıştır.
    '''
    if yas<=65:
        print(f"Emekliliğinize {65-yas} yıl kaldı")
    else:
        print("Emekli olabilirsiniz.")

yil = int(input("doğum yılınızı girin : "))
print("yaşınız = ",yasHesapla(yil))
emeklilikZamani(yasHesapla(yil))
#print(help(emeklilikZamani))

def deneme(a,b,c,*parametre):
    print(a,b,c)
    return sum((parametre))
print(deneme(10,20,30,40,50,60,70))

def deneme2(*params):
    sum = 0
    for param in params:
        sum += param
    return sum
print(deneme2(10,20,30,40))

def users(**args):
    for key,value in args.items():
        print("{} = {}".format(key,value))
users(name="Ahmet",age="24")

def func(a,b,*args,**kwargs):
    print(a,b,args,kwargs,sep="\n")
func(10,20,30,40,50,key1="value1",key2="value2")