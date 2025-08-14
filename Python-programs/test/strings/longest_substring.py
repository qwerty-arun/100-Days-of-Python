# Implement a function that finds the longest substring without repeating characters

def longestSubstring(s):
    start = 0
    max_len = 0
    max_substr = ""
    seen = {}

    for end in range(len(s)):
        char = s[end]
        if char in seen and seen[char] >= start:
            # Move the start pointer forward
            start = seen[char] + 1
        
        seen[char] = end
        window_len = end - start + 1
        if window_len > max_len:
            max_len = window_len
            max_substr = s[start:end+1]

    return max_substr

# Test
print(longestSubstring("abasuto"))