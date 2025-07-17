print("This is a Calculator App: ")
while True:
	choice = int(input("Enter 1 for add, 2 for sub, 3 for mul, 4 for div and 5 for exit: "))
	if choice == 1:
		print("This is Addition function!")
		a = int(input("Enter first no: "))
		b = int(input("Enter second no: "))
		print(a + b)
	if choice == 2:
		print("This is Subtraction function!")
		a = int(input("Enter first no: "))
		b = int(input("Enter second no: "))
		print(a - b)
	if choice == 3:
		print("This is Multiplication function!")
		a = int(input("Enter first no: "))
		b = int(input("Enter second no: "))
		print(a * b)
	if choice == 4:
		print("This is Division function!")
		a = int(input("Enter first no: "))
		b = int(input("Enter second no: "))
		print(a // b)
	if choice == 5:
		break
