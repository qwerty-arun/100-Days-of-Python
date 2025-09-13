# Write a function that takes a string and returns it reversed

def reverseString(str):
    reversed = ""
    for char in str:
        reversed = char + reversed
    return reversed

def reversed(str):
    return str[::-1]

print(reverseString("car"))
print(reversed("computer"))