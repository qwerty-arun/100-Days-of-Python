from datetime import datetime

now = datetime.now()

print("Default:", now)
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))
print("Only Date:", now.strftime("%Y/%m/%d"))
print("Weekday Name:", now.strftime("%A"))