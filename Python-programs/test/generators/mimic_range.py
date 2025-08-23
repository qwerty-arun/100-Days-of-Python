# Write a generator that mimics range(start, stop, step)

def range(start, stop, step):
    if step == 0:
        raise ValueError("Step must not be zero")
    
    if step > 0:
        while start <= stop:
            yield start
            start += step
    else:
        while start >= stop:
            yield start
            start += step

# Example usage:
for even in range(1000, 0, -100):
    print(even, end=" ")