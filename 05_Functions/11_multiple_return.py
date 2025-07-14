# Handle multiple return 

def make_chai():
    #return "Here is you masala chai"
    print("Here is your masala chai")
    pass

print(make_chai())

def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 100

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0: # early return
        return "Sorry, chai over"
    return "Chai ready!"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100, 20 , 90 #sold, remaining

sold, remaining, _ = chai_report()
print(f"Sold: {sold}")
print(f"Remaining: {remaining}")