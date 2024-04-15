import json
import os

if __name__ == '__main__':
    class User:
        def __init__(self, username, password, email):
            self.username = username
            self.password = password
            self.email = email

    class UserRepository:
        def __init__(self):
            self.users = []
            self.isLoggedIn = False
            self.currentUser = {}
            self.loadUsers()

        def loadUsers(self):
            if os.path.exists('users.json'):
                try:
                    with open('users.json', 'r', encoding='utf-8') as file:
                        users = json.load(file)
                        for user in users:
                            user = json.loads(user)
                            newUser = User(user["username"],user["password"],user["email"])
                            self.users.append(newUser)
                except Exception:
                    return

        def register(self,user: User):
            self.users.append(user)
            self.savetoFile()
            print("Kullanıcı oluşturuldu")
        def login(self,username,password):
            for user in self.users:
                if user.username == username and user.password == password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("Login Succesful")
                    return
            print("Wrong username or password")
        def logout(self):
            self.isLoggedIn = False
            self.currentUser = {}
            print("Logout Succesful")
        def identity(self):
            if self.isLoggedIn:
                print(f"username: {self.currentUser.username}\nemail: {self.currentUser.email}")
            else:
                print("Before Login Your Account")
        def savetoFile(self):
            list = []
            for user in self.users:
                list.append(json.dumps(user.__dict__))
            with open("users.json","w") as file:
                json.dump(list,file)

    userRepository = UserRepository()
    while True:
        print("Menü".center(50,'*'))
        secim = input('1- Register\n'
                      '2- Login\n'
                      '3- Logout\n'
                      '4- Identity\n'
                      '5- Exit\nSeciminiz: ')
        if secim == '5':
            break
        elif secim=='1':
            username = input("Name: ")
            password = input("Password: ")
            email = input("E-mail: ")
            user = User(username,password,email)
            userRepository.register(user)
        elif secim=='2':
            username = input("Name: ")
            password = input("Password: ")
            userRepository.login(username,password)
        elif secim=='3':
            userRepository.logout()
        elif secim=='4':
            userRepository.identity()
