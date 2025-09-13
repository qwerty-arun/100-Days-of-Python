from datetime import datetime

date_string = "16-08-2025 22:15:00"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

print("String:", date_string)
print("Parsed datetime object:", parsed_date)