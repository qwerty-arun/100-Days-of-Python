s = "banana"
newstr=""

for char in s:
	if char not in newstr:
		newstr += char
print(newstr)
