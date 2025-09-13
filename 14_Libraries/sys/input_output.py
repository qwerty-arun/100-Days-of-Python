import sys

# Writing to stdout
sys.stdout.write("Enter your name: ")

# Reading from stdin
name = sys.stdin.readline().strip()
print(f"Hello, {name}!")