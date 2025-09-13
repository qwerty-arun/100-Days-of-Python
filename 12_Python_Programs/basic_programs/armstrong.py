num = int(input("Enter a number: "))
no = num
sum = 0
while no > 0:
	r = no % 10
	sum = sum + r**3
	no = no // 10

print("Armstrong number!"  if sum == num else "Nope!")

