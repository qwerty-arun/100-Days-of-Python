from fractions import Fraction

f = Fraction(355, 113)  # Approximation of pi
print("Exact fraction:", f)
print("As float:", float(f))

approx = f.limit_denominator(10)
print("Limited denominator:", approx)
