sentence = "I learn python, because I love python ! And And"
words = sentence.rsplit()

print("The words in the sentence: ")
print(words)
print()

cap = []

for word in words:
	cap.append(word.capitalize())

print(cap)
