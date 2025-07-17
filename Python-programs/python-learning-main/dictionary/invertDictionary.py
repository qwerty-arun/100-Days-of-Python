dic = {"one": 1, "two": 2, "three": 3, "four": 4}

invert = {}
print("Original Dictionary: ")
for key, value in dic.items():
	print(f"{key}: {value}")
	invert.update({value: key})

print()
print("Inverted Dictionary: ")
for key, value in invert.items():
	print(f"{key}: {value}")
