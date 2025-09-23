# Map -> Applies a function to every element

# Example 1: Convert Temp
celcius = [0, 10, 20, 30, 40, 50]
fahrenheit = list(map(lambda c: (9/5)*c + 32, celcius))
print(fahrenheit)

# Example 2: Convert list of strings to uppercase
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(upper_words)

# Example 3: Without lambda
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))

print(squares)  # [1, 4, 9, 16, 25]


# Filter -> Filters elements based on a condition

# Example 1: Keep only even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)

# Example 2: Words longer than 5 letters
words = ["cat", "elephant", "dog", "giraffe", "hi"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)

# Example 3: Without Lambda
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))

print(evens)  # [2, 4, 6]


# Reduce -> Reduces everything to a single value

# Example 1: Find maximum in a list
from functools import reduce

numbers = [3, 7, 2, 9, 5]

max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num)  # 9

# Example 2: Concatenate all strings
words = ["Python", "is", "fun"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)

# Example 3: Without Lambda
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)

print(product)  # 24