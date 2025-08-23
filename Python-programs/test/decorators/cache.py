# Write a decorator that caches the results of a function

import functools

def cache_results(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # use tuple of args + frozen kwargs as key so it's hashable
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print(f"[Cache hit] {func.__name__}{args, kwargs} → {cache[key]}")
            return cache[key]
        
        print(f"[Cache miss] {func.__name__}{args, kwargs}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

@cache_results
def heavy_computation(x, y):
    print("Performing heavy computation...")
    return x ** y

print(heavy_computation(2, 10))   # Computed
print(heavy_computation(2, 10))   # Cached
print(heavy_computation(3, 4))    # Computed
print(heavy_computation(3, 4))    # Cached

# ----------------------------------------------------------
# Inbuilt caching decorator

# from functools import lru_cache

# @lru_cache(maxsize=None)  # unlimited cache
# def heavy_computation(x, y):
#     return x ** y