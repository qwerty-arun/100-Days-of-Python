# Implement a coroutine that consumes values and logs them only if they meet a certain condition.

def log_if_greater_than(threshold):
    print(f"Logging values greater than {threshold}")
    while True:
        value = (yield)
        if value > threshold:
            print(f"Logged: {value}")

# Create coroutine object
logger = log_if_greater_than(10)
next(logger)  # Prime the coroutine (advance to first yield)

# Send some values
for v in [5, 12, 8, 15, 7, 22]:
    logger.send(v)

# Output will be:
# Logging values greater than 10
# Logged: 12
# Logged: 15
# Logged: 22