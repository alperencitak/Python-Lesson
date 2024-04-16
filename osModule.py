import os
import datetime
if __name__ == '__main__':
    # result = dir(os)
    # result = os.name
    # os.chdir('C:\\')
    # result = os.getcwd()
    # os.mkdir("newdirectory")
    # os.makedirs("newdirectory/yeniklasor")
    # os.rename("newdirectory","yeniklasör")
    # os.rmdir("newdirectory")
    # os.removedirs("newdirectory/yeniklasor")
    # for dosya in os.listdir("C:\\"):
    #     if dosya.endswith('.sys'):
    #         print(dosya)
    #
    # result = os.stat("Program Files")
    # print(datetime.datetime.fromtimestamp(result.st_ctime))
    # print(datetime.datetime.fromtimestamp(result.st_atime))

    result = os.path.abspath("_os.py")
    result = os.path.dirname("C:/Users/alper/Downloads/PythonProjects/_os.py")
    result = os.path.dirname(os.path.abspath("_os.py"))
    result = os.path.exists("C:/Users/alper/Downloads/PythonProjects/demo.txt") # var mı
    result = os.path.isdir("C:/Users/alper/Downloads/PythonProjects") #klasör mü
    result = os.path.isfile("C:/Users/alper/Downloads/PythonProjects/demo.txt") #dosya mı
    result = os.path.join("C:\\","deneme","deneme1")
    result = os.path.split("C:/Users/alper/Downloads/PythonProjects/demo.txt") # dosya ayırıcı
    result = os.path.splitext("C:/Users/alper/Downloads/PythonProjects/demo.txt") # uzantı ayırıcı
    print(result)


