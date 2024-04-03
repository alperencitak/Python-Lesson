

if __name__ == "__main__":
    def cheackPassword(password):
        import re
        if len(password) < 6:
            raise Exception("Parola en az 6 karakter olmalıdır!")
        elif not re.search("[a-z]", password):
            raise Exception("Parola en az bir küçük harf içermelidir")
        elif not re.search("[A-Z]", password):
            raise Exception("Parola en az bir büyük harf içermelidir")
        elif not re.search("[0-9]",password):
            raise Exception("Parola en az bir rakam içermelidir!")
        elif re.search("[_@$]",password):
            raise Exception("Parola  alpha numeric içermemelidir!")
        elif re.search("[ ]",password):
            raise Exception("Parola boşluk içermemelidir!")

    password = "123456Ab"
    try:
        cheackPassword(password)
    except Exception as ex:
        print(ex)
    else:
        print("parola oluşturuldu.")
    finally:
        print("finish")