#NUMBERS

# Integers
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is: {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

total_cardamom_pots = 10
pots_per_cup = 3
leftover_pots = total_cardamom_pots % pots_per_cup
print(f"The leftover c pots: {leftover_pots}")

base_flavour_strength = 2
scale_factor = 3
# 2 * 2 * 2
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Scaled flavour: {powerful_flavour}")

# Improve readability
total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")