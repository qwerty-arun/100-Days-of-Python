'''
Vehicle Rental System
- You are designing a Vehicle Rental System that tracks different types of vehicles and their components.


Tasks:

1) Create a class Engine with an attribute horsepower and a method get_engine_info() that returns "150 HP Engine".

2) Create class Vehicle
    - Attributes: brand, model, and an Engine object.

    - Class attribute: total_vehicles (increased by 1 each time a new vehicle is created).

    - Add a method get_details() returning brand, model, and engine info.

    - Add @staticmethod get_vehicle_type() → returns "Generic Vehicle".

    - Add @classmethod get_total_vehicles() → returns total number of vehicles.

    - Add a @property rental_price and corresponding setter that ensures the value is non-negative.-

3) Create a Car class that inherits from Vehicle.

4) Add an attribute seats.

5) Override the get_details() method and use super() to include base details and append "Seats: X".
'''

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        
    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"
        
class Vehicle:
    total_vehicles = 0 
    
    def __init__(self, brand: str, model: str, engine : Engine):
        self.brand = brand
        self.model = model
        self.engine = engine
        self._rental_price = 0
        Vehicle.total_vehicles += 1
        
    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"
    
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles
        
    @property
    def rental_price(self):
        return self._rental_price
    
    @rental_price.setter
    def rental_price(self, price):
        if price >= 0:
            self._rental_price = price
            
    def get_details(self):
        return f"{self.brand} {self.model} - {self.engine.get_engine_info}"

class Car(Vehicle):
    def __init__(self, brand: str, model: str, engine: Engine, seats: int):
        super().__init__(brand, model, engine)
        self.seats = seats
        
    def get_details(self):
        return f"{super().get_details()} - Seats: {self.seats}"