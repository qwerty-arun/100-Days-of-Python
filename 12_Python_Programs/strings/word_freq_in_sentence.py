sentence = "I learn python, because I love python ! And And"
words = sentence.rsplit()

print("The words in the sentence: ")
print(words)
print()

unique_words = []

for i in range(0, len(words)):
	if words[i] not in unique_words:
		unique_words.append(words[i])

print("Unique Words in sentence: ")
print(unique_words)
print()

print("Words | Frequency")
for word in unique_words:
	print(f"{word}: {words.count(word)}")
