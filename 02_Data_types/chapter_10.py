# Dictionaries

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe : {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe : {chai_recipe}")

# membership test
print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}
# print(f"Order Details (keys): {chai_order.keys()}")
# print(f"Order Details (keys): {chai_order.values()}")
# print(f"Order Details (keys): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("type", "NO note") # try any other than "type", it will print NO note
print(f"Customer note: {customer_note}")