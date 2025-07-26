# Given a list of words, group them into anagrams

from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        # Use tuple(sorted(word)) as the key for grouping anagrams
        key = tuple(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

# Example usage:
words = ["bat", "eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)