staff = [("Amit", 16), ("Arun", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18: # try <=
        print(f"{name} is eligible to manage the staff")
        break
else: # fallback logic
    print(f"No one is eligible to manage the staff")