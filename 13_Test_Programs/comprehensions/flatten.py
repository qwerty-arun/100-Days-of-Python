# Flatten a nested list of integers using list comprehension

# One level flattening
def flatten(nest):
    flattend = []
    for li in nest:
        if type(li) is list:
            for element in li:
                flattend.append(element)
        else:
            flattend.append(li)
    return flattend

# one level
def flatten1(nest):
    return [item for li in nest for item in (li if isinstance(li, list) else [li])]


# any no. of levels (recursion)
def flatten2(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten2(item))  # Recursive call
        else:
            result.append(item)
    return result


print(flatten([1, [2,3], [4,5,6]]))
print(flatten([1, [2,3], [4,5,6, [7, 8]]])) # wont work
print(flatten1([1, [2,3], [4,5,6]]))
print(flatten1([1, [2,3], [4,5,6, [7, 8]]])) # wont work
print(flatten2([1, [2,3], [4,5,6]]))
print(flatten2([1, [2,3], [4,5,6, [7, 8]]])) # oh yes