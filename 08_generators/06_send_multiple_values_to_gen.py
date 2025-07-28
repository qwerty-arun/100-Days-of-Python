def chai_customer():
    order = yield
    customer = yield
    while True:
        print(f"Preparing order: {order} for {customer}")
        order = yield
        customer = yield
    
stall = chai_customer()
next(stall) #starts the generator
stall.send("Masala Chai") # send to order
stall.send("Arun") # send to customer
stall.send("Lemon Tea") # next order
stall.send("Raj") # next customer