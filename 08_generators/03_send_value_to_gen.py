# Send values to generators : send data to yield

# Example 1
print()
print("Example 1:")
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

# Example 2: generator receives a value
print()
print("Example 2:")
def greeter():
    name = yield "What's your name?"  # First yield: sends out a question
    yield f"Hello, {name}!"  # Second yield: greets with the received name

# Create generator object
g = greeter()

# Start generator (run to first yield)
print(next(g))  # Output: What's your name?

# Send a name into the generator
print(g.send("Alice"))  # Output: Hello, Alice!

# Example 3: Generator echoes values
print()
print("Example 3:")
def echo():
    while True:
        value = yield  # Pause and wait for a value to be sent
        print(f"Received: {value}")

g = echo()
next(g)  # Prime the generator

g.send("Hello")
g.send(42)
g.send([1, 2, 3])

# Example 4: Acuumulator Generator
print()
print("Example 4:")
def accumulator():
    total = 0
    while True:
        num = yield total
        if num is not None:
            total += num

g = accumulator()
print(next(g))      # Output: 0 (initial total)
print(g.send(10))   # Output: 10
print(g.send(5))    # Output: 15
print(g.send(20))   # Output: 35
print(g.send(None))