def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def ikiKat(b):
    return b*2
numbers = [1,2,3,4]
yeniList = list(map(ikiKat, numbers))
print(yeniList)

yeniList2 = list(map(lambda num: num*2,numbers))
print(yeniList2)

def check(sayi):
    return sayi%2==0
yeniList3 = list(filter(check,numbers))
print(yeniList3)

yeniList4 = list(filter(lambda kont: kont%2==0,yeniList))
print(yeniList4)