# Snack suggestion
snack = input("Input Snack: ").lower()
print(snack)

if snack == "cookies" or snack == "samosa":
    print(f"Order was placed! We will serve you: {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")