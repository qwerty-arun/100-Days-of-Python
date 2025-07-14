chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("darjeeling", "yes", "low") #positional
make_chai(tea="green", sugar="medium", milk= "no") # keywords

def special_chai(*ingrediants, **extras):
    print("Ingrediants", ingrediants)
    print("Extras", extras)

special_chai("Cinnamon", "Cardamom", sweetener="Honey", foam = "yes") #tuple and a dictionary

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order = None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()