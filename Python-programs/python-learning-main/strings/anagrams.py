def anagram(a, b):
	if len(a) != len(b):
		return False
	
	a_list = a.split()
	b_list = b.split()
	
	for i in range(0, len(a)):
		if b.find(a[i]) == -1:
			return False
	return True

a = "listen"
b = "silent"
if anagram(a,b):
	print("Anagram")
else:
	print("Nope!")
