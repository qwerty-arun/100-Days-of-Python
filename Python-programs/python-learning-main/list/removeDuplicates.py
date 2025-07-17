a = [0,2,5,2,3,4,3]	
b = []
print(a)

for i in range(0, len(a)-1):
	if a[i] not in b:
		b.append(a[i])

print(b)
