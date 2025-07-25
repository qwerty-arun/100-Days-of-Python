# Generate a list of squares from 1 to 10 using list comprehensions

def squares(nums):
    return [num ** 2 for num in nums]

print(squares([1,2,3,4,5]))