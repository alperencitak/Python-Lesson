

if __name__ == '__main__':
    def cube():
        for i in range(1,5):
            yield i**3

    # iterator = iter(generator)
    # iterator = cube()
    # while True:
    #     try:
    #         print(next(iterator), end=" ")
    #     except StopIteration:
    #         break
    # for i in cube():
    #     print(i)

    # liste = [i**3 for i in range(1,5)]
    liste = (i ** 3 for i in range(1, 5))
    for i in liste:
        print(i,end=" ")