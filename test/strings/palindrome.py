# Check if a string is a palindrome, ignoring spaces, punctuation and case

def palindrome(str):
    str.strip()
    i = 0
    j = len(str)-1

    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1

    return True

def optimized(str):
    return str == str[::-1] 

print(palindrome("racecar"))
print(palindrome("race"))

print(optimized("racecar"))
print(optimized("race"))