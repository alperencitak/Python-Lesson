class cars:
    def __init__(self,brand="-",model="-",price="-"):
        self.brand = brand
        self.model = model
        self.price = price
    def showİnfo(self):
        print(f"Brand: {self.brand}",
              f"Model: {self.model}",
              f"Price: {self.price}","",sep="\n")

car1 = cars("Dacia","2015",685000)
car2 = cars("Renault","2012",350000)
car3 = cars()
car1.showİnfo()
car2.showİnfo()
car3.showİnfo()