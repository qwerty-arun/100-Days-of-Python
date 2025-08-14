# Given a text, find the top `k` most frequent words

from collections import Counter

def top_k_frequent_words(s, k):
    words = s.split()
    freq = Counter(words)
    return freq.most_common(k)  # Returns a list of (word, count) tuples

# Example usage:
text = "apple orange apple banana banana apple orange grape grape grape"
k = 2
print(top_k_frequent_words(text, k))