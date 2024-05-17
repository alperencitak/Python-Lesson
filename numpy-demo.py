import numpy as np

# 1- (10,15,30,45,60) değerli dizi
result = np.array([10,15,30,45,60])
# 2- (5-15) arasındaki sayılarla dizi
result = np.arange(5,15)
# 3- (50-100) arasında 5'er 5'er artan dizi
result = np.arange(50,100,5)
# 4- 10 elemanlı sıfırlardan/birlerden oluşan dizi
result = np.zeros(10)
result = np.ones(10)
# 5- 0-100 arası eşit aralıklı 5 sayı üretin
result = np.linspace(0,100,5)
# 6- (10-30) arasında rastgele 5 sayı
result = np.random.randint(10,30,5)
# 7- [-1,1] arası 10 adet sayı
result = np.random.randn(10)
# 8- 3x5 boyutlarında (10-50) arasında random matris oluşturun
array = np.random.randint(10,50,15).reshape(3,5)
result = array
# 9- üretilen matrisin satır ve sütunlarının toplamı
result = array.sum(1)
result = array.sum(0)
# 10- üretilen matriste max,min ve ortalama
result = array.max()
result = array.min()
result = array.mean()
# 11- üretilen matrisin max/min değerinin indeksi
result = array.argmax()
result = array.argmin()
# 12- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanı
array = np.arange(10,20)
result = array[:3:]
# 13- üretilen diziyi ters çevirin
result = array[::-1]
# 14- üretilen matrisin ilk satırını ve 2.satırının 3.sütununu seçiniz
array = array.reshape(2,5)
result = array[0]
result = array[1,2]
# 15- üretilen matrisin tüm satırlarının ilk elemanı
result = array[:,0]
# 16- üretilen matrisin her bir elemanının karesi
result = array**2
# 17- üretilen matriste -50 ve +50 arasında olan çift sayılar
array2 = array[array>-50]
array2 = array2[array2<+50]
result = array2[array2%2==0]
# -----------------------------------------------------------
print(result)