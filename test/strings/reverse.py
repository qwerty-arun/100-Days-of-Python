# Write a function that takes a string and returns it reversed

def reverseString(str):
    reversed = ""
    for char in str:
        reversed = char + reversed
    return reversed

print(reverseString("car"))