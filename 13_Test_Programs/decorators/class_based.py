# Write a class-based decorator that limits how many times a function can be called (e.g., max 5 times)

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.calls = 0  # initialize the counter

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Function '{self.func.__name__}' has been called {self.calls} times.")
        return self.func(*args, **kwargs)

@CallCounter
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

# You can access the call counter
print(f"Total calls to 'greet': {greet.calls}")