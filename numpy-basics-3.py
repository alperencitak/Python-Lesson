import numpy as np

number1 = np.random.randint(10,100,6)
number2 = np.random.randint(10,100,6)
sup = number1 + number2
result = np.sin(number1)
result = np.sqrt(number2)
mnumber1 = number1.reshape(2,3)
mnumber2 = number2.reshape(2,3)
sup2 = mnumber2 + mnumber1
result = np.vstack((mnumber1,mnumber2)) # sütunsal ekleme
result = np.hstack((mnumber1,mnumber2)) # satırsal ekleme
result = number1 >= 50
print(number1[result]) # True olanları yaz

# print(number1,"\n",number2,"\n",sup)
# print(mnumber1,"\n",mnumber2,"\n",sup2)
print(result)
