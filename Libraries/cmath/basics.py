import cmath

# complex numbers
z1 = complex(3, 4)  # Creates 3 + 4j
z2 = complex(5)    # Creates 5 + 0j
z3 = complex("1-2j") # Creates 1 - 2j from a string
z4 = 2 + 5j
z5 = -8J
print(f"z1: {z1}")
print(f"z2: {z2}")
print(f"z3: {z3}")
print(f"z4: {z4}")
print(f"z5: {z5}")
print(f"Real of z1: {z1.real}")
print(f"Imag of z1: {z1.imag}")
print(f"Conjugate of z1: {z1.conjugate()}")
print(f"Phase of z1: {cmath.phase(z1)}")
print(f"Mag of z1: {abs(z1)}")