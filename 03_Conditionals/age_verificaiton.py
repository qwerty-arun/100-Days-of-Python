def verify_age(age_str: str) -> str:
    # Write your code here
    age_str = int(age_str)
    return "Access Granted" if age_str >= 18 else "Access Denied"
    pass

print(verify_age(2))