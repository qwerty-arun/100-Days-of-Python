#You are building a Smart Inventory Filter for a retail store.

#Tasks:

# 1. Process a list of product dictionaries, where each product has name, price, and category.

# 2. Use different types of comprehensions to:
# - Extract names of products priced below ₹500 using list comprehension.
# - Extract all unique categories using set comprehension.
# - Create a name-to-price mapping using dictionary comprehension.
# - Generate a list of discounted prices using a generator expression and convert it to a list.

# 3. Return all four outputs as a tuple.

def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    affordable = [item["name"] for item in items if item["price"] < 500]
    categories = {item["category"] for item in items}
    price_map = {item["name"]: item["price"] for item in items}
    discounted_prices = list((int(item["price"] * 0.9) for item in items))
 
    return (affordable, categories, price_map, discounted_prices)