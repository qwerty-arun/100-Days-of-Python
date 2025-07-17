s = "malayalam"
i, j = 0, len(s) - 1

is_palin = True
while i < j:
	if s[i] != s[j]:
		is_palin = False
		break
	i += 1
	j -= 1

if is_palin:
	print(f"{s} is a Palindrom string!")
else:
	print(f"{s} is not a Palindrome string!")
