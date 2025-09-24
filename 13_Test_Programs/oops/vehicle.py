class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def __str__(self):
        print(self.brand)
        print(self.year)

class Car(Vehicle):
    def __init__(self, brand, year, doors, engine_cc):
        super().__init__(brand, year)
        self.doors = doors
        self.engine_cc = engine_cc
    
    def __str__(self):
        print(self.brand)
        print(self.year)
        print(self.doors)
        print(self.engine_cc)

class Bike(Vehicle):
    def __init__(self, brand, year, gears, engine_cc):
        super().__init__(brand, year)
        self.gears = gears
        self.engine_cc = engine_cc

    def __str__(self):
        print(self.brand)
        print(self.year)
        print(self.gears)
        print(self.engine_cc)
    
car = Car("Tata", 2024, 4, 1500)
bike = Bike("Yamaha", 2023, 6, 150)
car.__str__()
bike.__str__()