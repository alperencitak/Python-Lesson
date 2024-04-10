
if __name__ == '__main__':
    # file = open("demo.txt","a",encoding="utf-8")
    # file.write("\nTest 4")
    # file2 = open("demo.txt","x",encoding="utf-8")
    # file.close()

    try:
        file3 = open("demo.txt", "r", encoding="utf-8")
        # for i in file3:
        #     print(i,end="")
        # content1 = file3.read(7)
        # content1 = file3.read(3)
        # print("içerik 1")
        # print(content1)
        # content2 = file3.read()
        # print("içerik 2")
        # print(file3.readline(),end="")
        # print(file3.readline())
        # list = file3.readlines()
        # print(list[0])

    except FileNotFoundError as ex:
        print(ex)
    else:
        file3.close()

    # with open("demo2.txt", "r", encoding="utf-8") as file4:
    #     print(file4.read())
    #     print(file4.tell())
    #     print(file4.read())
    #     file4.seek(0)
    #     print(file4.read())
    #     file4.seek(10)
    #     print(file4.read())

    # with open("demo3.txt","r+",encoding="utf-8") as file5:
    #     file5.seek(file5.tell())
    #     file5.write("deneme1\n")
    #     file5.write("deneme2")
    #     file5.seek(0)
    #     print(file5.read())