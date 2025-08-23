# Chain multiple decorators: logging, timing, caching on the same function

import functools
import time

# Logging decorator
def log_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] '{func.__name__}' returned {result}")
        return result
    return wrapper

# Timing decorator
def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] '{func.__name__}' executed in {end - start:.6f}s")
        return result
    return wrapper

# Simple caching decorator
def cache_results(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print(f"[CACHE HIT] {func.__name__}{args, kwargs} → {cache[key]}")
            return cache[key]
        print(f"[CACHE MISS] {func.__name__}{args, kwargs}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper


@log_arguments       # <- logs every call in/out
@timing              # <- measures execution time
@cache_results       # <- caches results (innermost)
def heavy_computation(x, y):
    print("Performing heavy computation...")
    return x ** y

print(heavy_computation(2, 10))   # fresh compute
print(heavy_computation(2, 10))   # cached
print(heavy_computation(3, 5))    # fresh compute
print(heavy_computation(3, 5))    # cached