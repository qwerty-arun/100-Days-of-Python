# Merge two dictionaries and sum the values of common keys

def merge(dic1, dic2):
    result = dic1.copy()
    for key, value in dic2.items():
        result[key] = result.get(key, 0) + value
    return result

print(merge({"one": 1, "two": 2},{"two": 2, "three":3}))