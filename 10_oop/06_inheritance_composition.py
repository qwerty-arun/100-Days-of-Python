# Inheritance and Composition

# Inheritance
class BaseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f"Preparing: {self.type} chai...")
    
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves")

# Composition
class ChaiShop: # this class doesn't inherit anything
    chai_cls = BaseChai # no need parenthesis, a reference is created to BaseChai

    # value passed to chai_cls, then to BaseChai constructor
    def __init__(self):
        self.chai = self.chai_cls("Regular") 

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai_cls.add_spices() # will give error
fancy.chai.add_spices() # will give error