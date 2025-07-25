def process_order(item, quantity):
    try:
        price = {"masala": 20}[item] # extract the price of masala chai 
        cost = price * quantity #operator overloading
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be a number")

process_order("ginger", 2)
process_order("masala", "two")