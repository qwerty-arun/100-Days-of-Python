# Lambdas, pure and impure functions

# pure function
def pure_chai(cups):
    return cups * 10

total_chai = 0

# impure function not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups

# recursive
def pour_chai(n):
    print(n)
    if n==0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))

# Lambdas
# You need a quick function for a short time
# Writing a full def function feels unnecessary
# You are passing a function as an argument (like, map, filter, sorted etc)
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)

square = lambda x: x**2
print("Square:", square(2))

add = lambda a,b: a+b
print("Addition", add(1,7))

is_even = lambda x: x%2==0
print("Is even: ", is_even(4))

# Sort a list of tuples by second element
pairs = [(1,3), (2,2), (4,1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted Pairs:",sorted_pairs)

# Filter even numbers from a list
nums = [1,2,3,4,5,6]
evens = list(filter(lambda x: x%2==0, nums))
print("Even no.s", evens)

# Double all elements in list
nums = [1,2,3]
doubled = list(map(lambda x: x*2, nums))
print("Doubled list:", doubled)

# Use with reduce() to find product
from functools import reduce
nums = [1,2,3,4]
product = reduce(lambda x, y: x*y, nums)
print("Product", product)

# Conditional expression (ternary type)
max_of_two = lambda a, b: a if a > b else b
print("Max", max_of_two(10,20))