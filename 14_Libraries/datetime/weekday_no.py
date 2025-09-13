from datetime import date

today = date.today()
print("Today is:", today)
print("Weekday Number (0=Monday):", today.weekday())
print("Weekday Name:", today.strftime("%A"))