import numpy as np

numbers = np.arange(0,76,5)
# print(numbers)
# print(numbers[5],numbers[-1],numbers[0:3],numbers[3],numbers[5:])
# print(numbers[::-1],numbers[3:0:-1])
numbers = numbers.reshape(4,4)
# result = numbers[:,2] # tüm satırlardan 2.indeksteki sütunu al
# result = numbers[1,:] # 1.indeksli satırdan tüm sütunları al
# result = numbers[:,0:2] # tüm satırların 0-2. indeks arasındakileri al
# result = numbers[-1,:] # son satırın tüm sütunları al
# result = numbers[0:2,0:3] # 0-2 indeks arası satırlardan 0-3 arası indeksli sütunları al
# print(numbers)
# print(result)

arr1 = np.arange(0,10)
arr2 = arr1
arr3 = arr1.copy()

# print(arr1)
# print(arr2)
# print(arr3)
# arr1[0] = 5
# print(arr1)
# print(arr2)
# print(arr3)