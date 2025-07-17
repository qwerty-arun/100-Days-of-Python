start = int(input("Enter starting of range: "))
end = int(input("Enter ending of range: "))
for prime in range (start, end+1):
	count = 0
	for i in range (1, prime+1):
		if prime % i == 0:
			count += 1
	if count == 2:
		print(prime)
