a = [0,2,5,2,3,4,3]	
b = [4,5,6,9,7,11,3]
c = []

for i in range(0, len(a)):
	for j in range(0, len(b)):
		if a[i] == b[j]:
			c.append(a[i])	

new_c = []
for i in range(0, len(c)-1):
	if c[i] not in new_c:
		new_c.append(c[i])
print(new_c)
