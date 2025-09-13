num = int(input("Enter a year: "))
print("Leap year!" if (num % 4 ==0 and num % 100 !=0) or num % 400 == 0 else "Nope!")
