# Send values to generators : send data to yield

def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield # wait for the order
    while True:
        print(f"Preparing: {order}")
        order = yield # what if another order comes in, also pauses the program

stall = chai_customer()
next(stall) # start the generator
stall.send("Masala Chai")
stall.send("Lemon Chai")
stall.send("Ginger Chai")