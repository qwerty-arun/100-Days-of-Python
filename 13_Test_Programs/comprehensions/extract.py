# Extract only even numbers from a list

def even(nums):
    return [num for num in nums if num % 2 == 0]

print(even([1,2,3,4,5]))