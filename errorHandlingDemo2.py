class Person:
    def __init__(self, name):
        if len(name) > 10:
            raise Exception("Name alanı 10 karakterden fazla olamaz")
        else:
            self.name = name
    def personName(self):
        print(self.name)

if __name__ == '__main__':
    try:
        p1 = Person("Necasettindar")
    except Exception as exception:
        print(exception)
    else:
        p1.personName()
