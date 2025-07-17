def palindrome(s):
	if len(s) <= 1: # don't treat single characters as palindromes
		return False

	i, j = 0, len(s) - 1

	is_palin = True
	while i < j:
		if s[i] != s[j]:
			is_palin = False
			break
		i += 1
		j -= 1

	return is_palin


sentence = "I know a madam who teaches malayalam"
words = sentence.split()
print(words)

# using list comprehensions
filtered_words = [word for word in words if not palindrome(word)]

print(filtered_words)
