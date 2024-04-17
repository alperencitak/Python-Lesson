import re
if __name__ == '__main__':
    result = dir(re)
    str = "Python Ders : RE | MODULE"
    result = re.findall("Python",str)
    result = len(result)
    result = re.split(":",str)
    result = re.sub(":","-",str)
    result = re.search("o",str)
    # result = result.span()
    #result = result.start()
    # result = result.end()
    # result = result.group()
    # result = result.string
    ####################################
    result = re.findall("[abcde]",str)
    result = re.findall("[sat]", str) #s a t var mı
    result = re.findall("[a-z]", str)
    result = re.findall("[^0-9]", str) #0-9 harici bir şey var mı
    result = re.findall("[2-5]", str) # 2-5 arası sayılar var mı
    result = re.findall("..",str) # 2 basamaklı böl
    result = re.findall("...", str) # 3 basamaklı böl
    result = re.findall("Py..on", str) # py ile başlayıp on ile bitenleri al
    result = re.findall("^P", str) # P ile mi başlıyor
    result = re.findall("E$",str) # E ile mi bitiyor
    result = re.findall("SET$",str)
    result = re.findall("De*rs",str) # D ile rs arasında herhangi sayıda e olanlar (0 da olabilir)
    result = re.findall("De+rs",str) # D ile rs arasında herhangi sayıda e olanlar (0 olamaz)
    result = re.findall("on{1}",str) # o arkasından gelen bir tane n var mı
    result = re.findall("on{1,2}", str) # o arkasından en az 1 en fazla 2 tane n var mı
    result = re.findall("[0-9]{2,4}", str) # en az 2 en çok 4 bassamaklı sayılar
    result = re.findall("[0-9]{2}",str) # 2 basamaklı sayı var mı
    result = re.findall("s|n",str) # s ya da n var mı
    result = re.findall("(a|b|c)xz", str) # a b ya da c arkasından xz geliyor mu



    print(result)
