a = [0,2,8,19,15]	
b = a[:]
a.sort()
flag = 1
for i in range(1,len(a)):
	if a[i] != b[i]:
		print("Not sorted")
		flag = 0
		break
	else:
		continue
if flag == 1:
	print("Sorted")
