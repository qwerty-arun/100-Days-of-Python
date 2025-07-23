def verify_age(age_str: str) -> str: # this is called type hints
    # Write your code here
    age_str = int(age_str)
    return "Access Granted" if age_str >= 18 else "Access Denied"
    pass

print(verify_age(2))

# Type Hints
# they are just suggestion for developers