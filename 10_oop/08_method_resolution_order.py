# Method Resolution Order (MRO)

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(B, C): # swap the order and check
    pass

cup = D()
print(cup.label) # prints B
print(D.__mro__)