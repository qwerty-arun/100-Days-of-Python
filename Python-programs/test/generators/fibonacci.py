# Write a generator that yields the first 'n' Fibonnaci numbers

# My approach
def fibonnaci(n):
    first = 0
    second = 1
    fib = []
    fib.append(first)
    fib.append(second)
    yield first
    yield second
    for index in range(0, n - 2): 
        fib.append(fib[index] + fib[index+1]) 
        yield fib[index+2]

for num in fibonnaci(15):
    print(num, end=" ")

print()

# Optimized
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = 10
for num in fibonacci_generator(n):
    print(num, end=" ")