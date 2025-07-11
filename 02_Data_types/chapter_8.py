# Lists - denoted by [], they are mutable
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(ingredients)
ingredients.remove("water")
print(ingredients)

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"Chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Popped: {last_added}")
print(f"Chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Chai: {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai: {chai_ingredients}")

sugar_levels = [1,7, 99, 44]
print(f"Max: {max(sugar_levels)}")
print(f"Min: {min(sugar_levels)}")

# Operator Overloading
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong Brew: {strong_brew}")

# Bytearray
#bytearray is a mutable sequence of integers in the range of 0 to 255, representing byte values. It is a built-in type that allows for efficient manipulation of binary data. 
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")

my_bytearray = bytearray(5) # Creates a bytearray of 5 null bytes: bytearray(b'\x00\x00\x00\x00\x00')
print(my_bytearray)
my_bytearray = bytearray([65, 66, 67]) # Creates bytearray(b'ABC')
print(my_bytearray)