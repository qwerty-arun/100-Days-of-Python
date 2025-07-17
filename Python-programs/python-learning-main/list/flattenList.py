a=[1, [2,3], 4, [5,6]]
flattened = [] 

for li in a:
	if type(li) is not int:
		for element in li:
			flattened.append(element)
	else:
		flattened.append(li)

print(flattened)
