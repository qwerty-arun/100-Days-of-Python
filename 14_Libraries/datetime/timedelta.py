from datetime import datetime, timedelta

today = datetime.now()
print("Today:", today)

# Add 10 days
future = today + timedelta(days=10)
print("10 days later:", future)

# Subtract 30 minutes
past = today - timedelta(minutes=30)
print("30 minutes ago:", past)

# Difference between two dates
birthday = datetime(2025, 12, 25)
diff = birthday - today
print("Days until Christmas:", diff.days)