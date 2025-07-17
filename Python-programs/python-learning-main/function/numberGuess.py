import random

def randomInt():
	a = random.randint(1,10)
	return a

while True:
	userInput = int(input("Enter a number between 1 and 10: "))
	if userInput == randomInt():
		print("That's correct")
		break
