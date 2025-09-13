# Write a decorator that logs the function name and its arguments

import functools

def log_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log the function name
        print(f"Calling function: {func.__name__}")
        # Log positional arguments
        if args:
            print(f"  Positional arguments: {args}")
        # Log keyword arguments
        if kwargs:
            print(f"  Keyword arguments: {kwargs}")
        # Call the original function
        result = func(*args, **kwargs)
        # Log the result
        print(f"  Returned: {result}")
        return result
    return wrapper

@log_arguments
def add(a, b, show=False):
    return a + b if not show else f"Sum is {a+b}"

@log_arguments
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

# Test calls
add(2, 3)
add(10, 20, show=True)
greet("Alice")
greet("Bob", msg="Welcome")