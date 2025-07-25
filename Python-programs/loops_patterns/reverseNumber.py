num = int(input("Enter a number:  "))
no = num
digits = 0
while no > 0:
	digits += 1
	no = no // 10

no = num
reverse = 0
for i in range(1, digits+1):
	reverse += (no % 10) * (10 ** (digits-i))
	no = no // 10

print(f"Reverse of {num} is: {reverse}")
