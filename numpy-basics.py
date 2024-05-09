import numpy as np

# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array

np_array = np.array([1,2,3,4,5,6,7,8,9])
print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)

# print(py_multi)
# print(np_multi)
# print(np_array.ndim) # kaçıncı boyuttan olduğu
# print(np_multi.ndim)
# print(np_array.shape) # sütun satır
# print(np_multi.shape)

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10) # [1,10) dizi oluştur
# result = np.arange(10,101,5) [10,101) dizi oluştur ancak beşer beşer git.
# result = np.zeros(5)
# result = np.ones(5)
# result = np.linspace(0,100,5) # 0-100 arasını 5 eşit parçaya böl.
# result = np.random.randint(0,10)
# result = np.random.randint(20)
# result = np.random.randint(1,20,5) # 1-20 arası random sayı 5 tane
# result = np.random.rand(5) # 0-1 arası 5 random sayı
# result = np.random.randn(5) # -1-1 arası 5 random sayı
# result = np.arange(1,51)
# result = result.reshape(5,10)
# print(result.sum(axis=1)) #satırların toplamı
# print(result.sum(axis=0)) # sütunların toplamı
# result = np.random.randint(1,100,10)
# print(result.max())
# print(result.min())
# print(result.mean()) # ortalama
# print(result.argmax()) # max ' ın indeks numarası
# print(result.argmin())


# print(result)
