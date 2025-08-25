from decimal import Decimal, getcontext

getcontext().prec = 6   # Set global precision
print("Pi approx:", Decimal(1) / Decimal(7))  # limited to 6 digits
