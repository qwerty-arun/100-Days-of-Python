# Create a generator that yields all even numbers from 1 to n

def even_numbers(n):
    for num in range(1, n + 1):
        if num % 2 == 0:
            yield num

# Example usage:
n = 20
for even in even_numbers(n):
    print(even)