# map() vs LC
numbers = [1, 2, 3, 4, 5]

# Using map
squares_map = list(map(lambda x: x**2, numbers))

# Using list comprehension
squares_lc = [x**2 for x in numbers]

print(squares_map)  # [1, 4, 9, 16, 25]
print(squares_lc)   # [1, 4, 9, 16, 25]


# filter() vs LC
numbers = [1, 2, 3, 4, 5, 6]

# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension
evens_lc = [x for x in numbers if x % 2 == 0]

print(evens_filter)  # [2, 4, 6]
print(evens_lc)      # [2, 4, 6]


# reduce() vs LC
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce
sum_reduce = reduce(lambda x, y: x + y, numbers)

# Using built-in sum()
sum_builtin = sum(numbers)

print(sum_reduce)   # 15
print(sum_builtin)  # 15
