# Classes and namespaces

class Chai:
    origin = "India"

print(Chai.origin)

# Adding
Chai.is_hot = True
print(Chai.is_hot)

# Create objects from class Chai
chai1 = Chai()
print(chai1.origin)
print(chai1.is_hot)
chai1.is_hot = False
print(Chai.is_hot)
print(chai1.is_hot)

chai1.flavor = "Masala"
print(chai1.flavor)