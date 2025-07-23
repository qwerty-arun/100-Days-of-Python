# Sets - denoted by {}, the elements are unique

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only essentials: {only_in_essential}")

# membership test
print(f"Is 'clove' in essential spices? {'cloves' in optional_spices}")

# frozenset: immutable version of in-built 'set' object

# Creating a frozenset from a list
my_list = [1, 2, 3, 4, 2]
my_frozenset = frozenset(my_list)
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4})

# Creating a frozenset from a string
my_string = "hello"
another_frozenset = frozenset(my_string)
print(another_frozenset)  # Output: frozenset({'o', 'e', 'l', 'h'})
# actually, it prints in any order