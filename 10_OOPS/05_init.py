class ChaiOrder:
    def __init__(self, type_, size): #constructors
        self.type = type_ # allowed to create on the go
        self.size = size
    
    def summary(self):
        return f"{self.size}ml of {self.type} chai"


order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 150)
print(order_two.summary())

print(ChaiOrder.size)