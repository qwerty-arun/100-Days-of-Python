# Attribute Shadowing
class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "small" # cup is not a variable in the class Chai
print("After changing: ", cutting.temperature)
print("Cup Size: ", cutting.cup)
print("Direct look into the class: ", Chai.temperature)

del cutting.temperature
del cutting.cup
print("After deletion: ", cutting.temperature) 
# If object attribute is not available, it falls back to class attribute value
print("After deletion: ", cutting.cup) # should give you an error