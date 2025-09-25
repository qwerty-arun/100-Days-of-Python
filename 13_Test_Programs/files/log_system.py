import datetime

def write_log(message, filename="log.txt"):
    # Get current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Format log entry
    log_entry = f"[{timestamp}] {message}\n"

    # Append to log file
    with open(filename, "a") as f:
        f.write(log_entry)

if __name__ == "__main__":
    # Ask user for a custom message
    msg = input("Enter your log message: ")
    write_log(msg)
    print("Message logged successfully!")
