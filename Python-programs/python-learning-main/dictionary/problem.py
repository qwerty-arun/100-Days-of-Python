dic1 = {"one": 1, "two": 2, "three": 3, "four": 4}
dic2 = {"one": 1, "five": 5, "six": 6, "seven": 7, "four": 8}

merged = {}

# Add all items from dic1
for key, value in dic1.items():
    merged[key] = value

# Add from dic2, sum if key already exists
for key, value in dic2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print(merged)

# One liner
# merged = dic(Counter(dict1) + Counter(dic2))
