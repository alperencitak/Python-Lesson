
class ogrenciler():
    def __init__(self,ad,soyad,aldigiNot):
        self.ad = ad
        self.soyad = soyad
        self.aldigiNot = aldigiNot
        if self.aldigiNot >= 45:
            self.sonuc = True
        else:
            self.sonuc = False
        self.bilgiler = f"Ad: {self.ad} - Soyad: {self.soyad} - Aldığı Not: {self.aldigiNot}"

ogrenci1 = ogrenciler("Ahmet","Çakır",85)
ogrenci2 = ogrenciler("Selin","Gökgöz",60)
ogrenci3 = ogrenciler("Metin","Yılmaz",40)
diziNot = ogrenci1.sonuc,ogrenci2.sonuc,ogrenci3.sonuc
diziBilgiler = ogrenci1.bilgiler,ogrenci2.bilgiler,ogrenci3.bilgiler

i = 0
while i<3:
    if diziNot[i] == True:
        print(diziBilgiler[i],"Geçti",sep="  ---  ")
    else:
        print(diziBilgiler[i], "Kaldı", sep="  ---  ")
    i+=1
