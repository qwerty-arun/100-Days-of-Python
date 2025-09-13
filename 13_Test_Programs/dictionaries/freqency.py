# Count frequency of each character in a string

def freq(str):
    chars = set(str)
    frequency = {}
    for uniq_char in chars:
        count = 0
        for char in str:
            if uniq_char == char:
                count += 1
        frequency[uniq_char] = count
    return frequency

def char_frequency(s):
    freq = {}
    for char in s:
        # If a character is not already in the dictionary, freq.get(char, 0) returns 0, and adds 1.
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage:
result = char_frequency("hello world")
print(result)

print(freq("arunnnn"))