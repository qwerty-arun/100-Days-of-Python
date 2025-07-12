# Walrus (:=)
# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")

av_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter size: ")) in av_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Chai Size unavailable")

flavours = ["masala", "ginger", "lemon", "mint"]

print("Availabe flavours: ", flavours)

while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"You chose {flavour} chai")