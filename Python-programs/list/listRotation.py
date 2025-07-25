a = [1,2,3,4,5]	
k = int(input("Enter 'k' to rotate the list right by 'k' positions: "))
rotated = []
for i in range(len(a)-k,len(a)):
	rotated.append(a[i])

for i in range(0, len(a)-k):
	rotated.append(a[i])

print(a)
print(rotated)

