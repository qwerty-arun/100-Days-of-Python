# 🔹 What is a Decorator?

- In Python, **decorators are functions that modify the behavior of other functions or classes** without changing their code.
- They are usually applied using the `@decorator_name` syntax.
- Decorators take a function as an argument, add some functionality, and return a new function.

---

## 🔹 Simple Example (Without `@`)

```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

def say_hello():
    print("Hello!")

decorated = my_decorator(say_hello)
decorated()
```

### Output:

```
Before the function runs
Hello!
After the function runs
```

---

## 🔹 Using `@` Syntax (Cleaner Way)

```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

(Same output as above, but more readable.)

---

## 🔹 Example 1: Logging Decorator

```python
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

print(add(5, 10))
```

### Output:

```
Calling function: add
add returned 15
15
```

---

## 🔹 Example 2: Timing a Function

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()
```

### Output:

```
Finished!
slow_function took 2.0005 seconds
```

---

## 🔹 Example 3: Authorization / Access Control

```python
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied!")
            return
        return func(user)
    return wrapper

@require_admin
def get_admin_panel(user):
    print(f"Welcome {user}, here is the admin panel.")

get_admin_panel("guest")
get_admin_panel("admin")
```

### Output:

```
Access denied!
Welcome admin, here is the admin panel.
```

---

## 🔹 Example 4: Decorators with Arguments

Decorators themselves can take arguments if wrapped in another function.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Arun")
```

### Output:

```
Hello Arun
Hello Arun
Hello Arun
```

---

## 🔹 Example 5: Stacking Multiple Decorators

```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def get_text():
    return "Hello"

print(get_text())
```

### Output:

```
<b><i>Hello</i></b>
```

---

✅ **In summary:**

- Decorators let you wrap extra functionality around functions.
- They’re widely used in Python frameworks (Flask, Django, FastAPI) for **logging, authentication, caching, etc.**
- You can use them with or without arguments, and even stack them.

---

# 🔹 Class-based Decorators in Python

So far, we saw **function-based decorators**.
But decorators can also be implemented using **classes** by defining a `__call__` method.

👉 In Python, if an object implements `__call__()`, it can be used like a function.

---

## 🔹 Basic Example

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before the function runs")
        self.func()
        print("After the function runs")

@MyDecorator
def say_hello():
    print("Hello!")

say_hello()
```

### Output:

```
Before the function runs
Hello!
After the function runs
```

---

## 🔹 Example 1: Logging with Class Decorator

```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling function: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"{self.func.__name__} returned {result}")
        return result

@Logger
def multiply(a, b):
    return a * b

print(multiply(3, 5))
```

### Output:

```
Calling function: multiply
multiply returned 15
15
```

---

## 🔹 Example 2: Counting Calls

A decorator can keep **state** when written as a class.

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"Function {self.func.__name__} has been called {self.counter} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    print(f"Hello {name}")

greet("Arun")
greet("Arun")
greet("Arun")
```

### Output:

```
Function greet has been called 1 times
Hello Arun
Function greet has been called 2 times
Hello Arun
Function greet has been called 3 times
Hello Arun
```

---

## 🔹 Example 3: Parameterized Class Decorator

We can also pass arguments to class decorators (similar to function decorators with arguments).

```python
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper

@Repeat(3)
def say_hi():
    print("Hi!")

say_hi()
```

### Output:

```
Hi!
Hi!
Hi!
```

---

## 🔹 Example 4: Using `functools.update_wrapper`

When using class decorators, the decorated function loses its original name (`__name__`, `__doc__`).
We can fix this with `functools.update_wrapper`.

```python
import functools

class PreserveInfo:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Running decorated function...")
        return self.func(*args, **kwargs)

@PreserveInfo
def hello():
    """This function says hello."""
    print("Hello!")

print(hello.__name__)  # hello (not 'PreserveInfo')
print(hello.__doc__)   # "This function says hello."
hello()
```

---

✅ **Key Takeaways**

- Class-based decorators are useful when you want to **maintain state** (like counters, caching, etc.).
- They make code **cleaner** when decorators get complex.
- You can add decorator arguments by handling them in `__init__`.

---

# 🔹 Caching / Memoization in Python

**Memoization** is a technique where you **store the results of expensive function calls** and return the cached result when the same inputs occur again.
It’s perfect for **recursive functions** like Fibonacci.

---

## 🔹 Example 1: Manual Memoization with a Decorator

```python
def memoize(func):
    cache = {}  # Dictionary to store results

    def wrapper(n):
        if n in cache:
            print(f"Fetching {n} from cache")
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
```

### Output:

```
Fetching 9 from cache
Fetching 8 from cache
...
55
```

✅ Here, the **decorator stores previous results**, so each Fibonacci number is calculated **only once** instead of multiple times in recursion.

---

## 🔹 Example 2: Using `functools.lru_cache`

Python provides a built-in decorator: `functools.lru_cache` for caching.

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # maxsize=None for unlimited cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))
```

- `lru_cache` = **Least Recently Used cache**.
- Great for functions where **inputs repeat often**.
- `maxsize` limits the number of cached results to avoid memory overflow.

---

## 🔹 Example 3: Caching with Multiple Arguments

Manual caching can also handle multiple arguments:

```python
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Fetching {args} from cache")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def add(a, b):
    print(f"Computing {a} + {b}")
    return a + b

print(add(2, 3))
print(add(2, 3))
```

### Output:

```
Computing 2 + 3
5
Fetching (2, 3) from cache
5
```

---

## 🔹 Example 4: Class-based Memoization

You can also do caching with a **class decorator**, which is useful if you want to maintain state across multiple functions or objects.

```python
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print(f"Fetching {args} from cache")
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

@Memoize
def power(a, b):
    print(f"Calculating {a}^{b}")
    return a ** b

print(power(2, 3))
print(power(2, 3))
```

### Output:

```
Calculating 2^3
8
Fetching (2, 3) from cache
8
```

---

✅ **Key Takeaways for Caching Decorators**

1. Memoization reduces computation by storing previous results.
2. Use `functools.lru_cache` for built-in caching—it’s fast and clean.
3. Class-based caching is useful if you want **more control or stateful caching**.
4. Can handle multiple arguments with `*args`/`**kwargs`.

---
