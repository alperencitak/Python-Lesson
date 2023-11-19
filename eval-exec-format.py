#eval() (evaluate = işlemek...)
print("""
+ toplama
- çıkarma
* çarpma
/ bölme
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın.
""")
veri = input("İşleminiz: ")
hesap = eval(veri) #eval() tehlikeli bir fonksiyondur. Kullanılması tavsiye edilmez. (Rastgele komut yetkisi)
print(hesap)

girdi = input(d1) #Kullanıcı print("Hello") yazarsa ekrana 'Hello' yazılacaktır.
exec(girdi)