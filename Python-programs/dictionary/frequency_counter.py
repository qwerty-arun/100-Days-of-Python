sentence = "I learn python, because I love python ! And And"
words = sentence.rsplit()

unique_words = []

for i in range(0, len(words)):
	if words[i] not in unique_words:
		unique_words.append(words[i])

dictionary = {}

print("Words along with their frequencies: ")
for word in unique_words:
	dictionary.update({word: words.count(word)})

for key, value in dictionary.items():
	print(f"{key}: {value}")
