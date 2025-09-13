s = "aieuo"

vowels = 0
consonants = 0

for i in range(0, len(s)):
	if s[i] == "a" or s[i] == "e" or  s[i] == "i" or s[i] == "o" or s[i] == "u":
		vowels += 1
	else:
		consonants += 1

print(f"String: {s}")
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
