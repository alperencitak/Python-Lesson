class Personel:
    def __init__(self,isim,yas,maas):
        self.isim = isim
        self.yas = yas
        self.maas = maas
    def bilgiler(self):
        print("Personel",self.isim,self.yas,self.maas,sep=" - ")

class People:
    def __init__(self,departman):
        self.departman = departman

class Mudur(Personel): # Inheritance
    def __init__(self,isim,yas,maas,ek_prim):
        super().__init__(isim, yas, maas)
        self.ek_prim = ek_prim

class Cayci(Personel):
    def bilgiler(self): # Overriding
        print("Çaycı",self.isim, self.yas, self.maas, sep=" - ")

class Yonetici(Personel,People): # Multiple Inheritance
    pass                         # ilk yazılan önceliklidir

class Student:
    def __init__(self,ad,soyad,numara):
        self.__ad = ad # private define
        self.__soyad = soyad
        self.__numara = numara
    def getAd(self): # Encapsulation
        return self.__ad
    def setAd(self,ad):
        self.__ad = ad
