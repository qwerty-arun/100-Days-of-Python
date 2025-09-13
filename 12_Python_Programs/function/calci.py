def add(x,y):
	print(f"{x} + {y} = {x+y}")

def sub(x,y):
	print(f"{x} - {y} = {x - y}")

def mul(x,y):
	print(f"{x} * {y} = {x * y}")
	
def div(x,y):
	print(f"{x} / {y} = {x // y}")


while True:
	choice = int(input("Enter 1 for add, 2 for sub, 3 for mul, 4 for div and 5 for exit: "))
	if choice == 1:
		a = int(input("Enter first no.: "))
		b = int(input("Enter second no.: "))
		add(a,b)

	if choice == 2:
		a = int(input("Enter first no.: "))
		b = int(input("Enter second no.: "))
		sub(a,b)

	if choice == 3:
		a = int(input("Enter first no.: "))
		b = int(input("Enter second no.: "))
		mul(a,b)

	if choice == 4:
		a = int(input("Enter first no.: "))
		b = int(input("Enter second no.: "))
		div(a,b)

	if choice == 5:
		break
