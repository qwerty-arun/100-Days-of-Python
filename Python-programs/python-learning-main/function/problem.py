print("Password should contain: ")
print("1. 8 characters ")
print("2. At least one uppercase letter (A-Z)")
print("3. At least one lowercase letter (a-z)")
print("4. At least one number")
print("5. At least one special character (!@#$%&*_) ")

def uppercase(password):
	count = 0
	for i in range(0, len(password)):
		if password[i].isupper():
			count += 1
	return count

def lowercase(password):
	count = 0
	for i in range(0, len(password)):
		if password[i].islower():
			count += 1
	return count

def digit(password):
	count = 0
	for i in range(0, len(password)):
		if password[i].isdigit():
			count += 1
	return count

def special(password):
	count = 0
	for i in range(0, len(password)):
		if password[i] == '!' or password[i] == '@' or password[i] == '#' or password[i] == '$' or password[i] == '%' or password[i] == '&' or password[i] == '*' or password[i] == '_':
			count += 1
	return count

check = 0

while True:
	password = input("Enter the password: ")

	if len(password) < 8:
		print("Password should contain at least 8 characters!")

	if uppercase(password) == 0:
		print("Password should contain at least one uppercase letter (A-Z)!")

	if lowercase(password) == 0:
		print("Password should contain at least one lowercase letter (a-z)!")

	if digit(password) == 0:
		print("Password should contain at least one number!")

	if special(password) ==0:
		print("Password should contain at least one special character(!@#$%&*_) !")
	
	if len(password) > 8 and uppercase(password) > 0 and lowercase(password) > 0 and digit(password) > 0 and special(password) > 0:
		print("Valid!")
		break
