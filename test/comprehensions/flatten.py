# Flatten a nested list of integers using list comprehension

def flatten(nest):
    flattend = []
    for li in nest:
        if type(li) is list:
            for element in li:
                flattend.append(element)
        else:
            flattend.append(li)
    return flattend

def flatten1(nest):
    return [item for li in nest for item in (li if isinstance(li, list) else [li])]

print(flatten([1, [2,3], [4,5,6]]))
print(flatten1([1, [2,3], [4,5,6]]))