# Smart Token Dispenser

# You are developing a Smart Token Dispenser system, like those found in banks or clinics. This system reset counters based on user activity and needs to run until manually stopped.

# Tasks:
# 1. Create an infinite generator function called token_dispenser(start=1).

# 2. On each call to next(), it should yield the current token number and increment it.

# 3. If a value is passed to the generator using send(), the generator should reset the token number to that new value.

# 4. The generator should handle the .close() method gracefully and print "Dispenser closed." when it is closed.

def token_dispenser(start: int = 1):
    """
    Infinite generator that simulates a token dispenser.
 
    - Yields incrementing token numbers starting from `start`.
    - Accepts input via `send()` to optionally reset the counter to a new value.
    - Gracefully stops if `close()` is called.
    """
    current = start
    try:
        while True:
            new_start = yield current
            if new_start is not None:
                current = new_start
                print(current)
            else:
                current += 1
                print(current)
    except GeneratorExit:
        print("Dispenser closed.")

order = token_dispenser()
next(order)
order.send(5)
next(order)