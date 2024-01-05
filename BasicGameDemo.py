import random
oyun=1
zar = random.randint(2,12)
print(zar)
if zar==7 or zar==11:
    print("Kazandınız!")
    oyun=0
elif zar==2 or zar==3 or zar==12:
    print("Kaybettiniz!")
    oyun=0
sonAtilan = zar
while(oyun==1):
    zar = random.randint(2,12)
    print(zar)
    if zar==sonAtilan:
        print("Kazandınız!")
        break
    elif zar==7:
        print("Kaybettiniz!")
        break