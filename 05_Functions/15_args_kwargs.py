# 1. *args
# Stands for arbitrary positional arguments.
# It lets you pass any number of positional arguments to a function.
# Inside the function, args becomes a tuple.

def add_numbers(*args):
    print(args)  # args is a tuple
    return sum(args)

print(add_numbers(1, 2, 3))       # (1, 2, 3) → 6
print(add_numbers(5, 10, 15, 20)) # (5, 10, 15, 20) → 50

# 2. **kwargs
# Stands for arbitrary keyword arguments.
# It lets you pass any number of keyword arguments to a function.
# Inside the function, kwargs becomes a dictionary.

def print_details(**kwargs):
    print(kwargs)  # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="London")

# 3. Using both `*args` and `**kwargs`
# You can use both in the same function, but `*args` must come before `**kwargs`
def mix_example(a, b, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print("args:", args)
    print("kwargs:", kwargs)

mix_example(1, 2, 3, 4, 5, name="Bob", age=30)

# When to use them?
# Use `*args` when you don't know how many positional arguments will be passed.
# Use `**kwargs` when you don't know how many keyword arguments will be passed.