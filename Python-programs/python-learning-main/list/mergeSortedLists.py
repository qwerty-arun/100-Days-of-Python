a = [1,2,5,6,7]
b = [3,4,8]
c = []

c = a + b

for i in range(0, len(c)):
	min = i
	for j in range(i+1, len(c)):
		if(c[j] < c[min]):
			min = j
		
	temp = c[i]
	c[i] = c[min]
	c[min] = temp

print(c)
