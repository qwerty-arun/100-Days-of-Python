num = int(input("Enter a number: "))
no = num
sum = 0
while no > 0:
	r = no % 10
	sum = sum + r
	no = no // 10

print(f"Sum of digits in {num} is: {sum}")

