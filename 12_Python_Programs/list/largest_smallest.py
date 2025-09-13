a = [0,1,2,3,4,5]	
print("Smallest element: ", min(a))
print("Largest element: ", max(a))

smallest = a[0]
largest = a[0]

for num in a:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest element: ", smallest)
print("Largest element: ", largest)