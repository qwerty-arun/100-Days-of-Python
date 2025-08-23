# Write a decorator that counts how many times a function has been called

import functools

def call_counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function '{func.__name__}' has been called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0  # Initialize the counter
    return wrapper

@call_counter
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

# Check the counter outside
print(f"Total calls to 'greet': {greet.calls}")