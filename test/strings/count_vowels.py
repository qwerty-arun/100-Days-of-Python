# Count the number of vowels in a string

def countVowels(str):
    count = 0
    for char in str:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count

print(countVowels("arun"))