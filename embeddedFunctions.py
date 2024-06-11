
result = bin(5) # number to binary code
result = bytes(4) # bumber to bytes, cannot be changed
result = bytearray(4) # number to bytes, can be changed
result = chr(54) # ASCII code to character
result = ord("A") # character to ASCII code
result = dir() # see all elements
# def evenNumbers(sayi):
#     if sayi%2==0:
#         return sayi;
# result = filter(evenNumbers, [2,5,6,7,9,3,1])
# for i in result:
#     print(i)
result = format(9,".3f")
# help(bin) # help for function info
result = isinstance(5,int)
result = isinstance('5',int)
result = isinstance('5',str)
# def getDouble(sayi):
#     return sayi*2
# sayilar = [1,2,3,4,5]
# result = map(getDouble,sayilar)
# for i in result:
#     print(i)
isimler = ["burak","ahmet","ayşe"]
notlar = [80,75,90]
result = zip(isimler,notlar)
result = list(result)


print(result)
