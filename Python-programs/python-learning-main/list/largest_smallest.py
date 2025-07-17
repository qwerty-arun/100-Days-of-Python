a = [0,1,2,3,4,5]	
largest = 0
smallest= 0
for i in range(1,len(a)):
	if a[i-1] > a[i] :
		largest = a[i]
	else:
		smallest = a[i]
print("Largest: ", largest)
print("Smallest: ", smallest)
