def reverse(s):
	i , j = 0,len(s)

	reverseStr = ""
	while i < j:
		reverseStr = s[i] + reverseStr
		i = i + 1

	return reverseStr


sentence = "I know a madam who teaches malayalam"
words = sentence.split()

print("Original words: ", words)
rev_words = []
for word in words:
	rev_words.append(reverse(word))

print("Reversed Words: ",rev_words)
