import math
import time

if __name__ == '__main__':
    def timeMath(func):
        def decorate(*args):
            start = time.time()
            time.sleep(1)
            func(*args)
            stop = time.time()
            print("Time: {}".format(stop-start))

        return decorate
    @timeMath
    def usAlma(a,b):
        print(math.pow(a,b))
    @timeMath
    def factorial(a):
        print(math.factorial(a))

    usAlma(2,3)
    factorial(3)
