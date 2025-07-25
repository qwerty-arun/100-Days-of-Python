# Given a list of strings, return a dictionary where key = word, value = length

def dic(strings):
    return {word: len(word) for word in strings}

print(dic(["a", "ab", "abc"]))