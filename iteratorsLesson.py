

if __name__ == '__main__':
    # liste = [1,2,3,4,5]
    #
    # iterator = iter(liste)
    # while True:
    #     try:
    #         print(next(iterator))
    #     except StopIteration as ex:
    #         break

    class MyNumbers:
        def __init__(self,start,stop):
            self.start = start
            self.stop = stop

        def __iter__(self):
            return self

        def __next__(self):
            if self.start <=self.stop:
                x=self.start
                self.start+=1
                return x
            else:
                raise StopIteration

    list = MyNumbers(10,20)
    for x in list:
        print(x)