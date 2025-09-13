from fractions import Fraction

f = Fraction(0.75)
print("From float:", f)   # Output: 3/4

f2 = Fraction("0.125")    # safer: from string
print("From string:", f2) # Output: 1/8
