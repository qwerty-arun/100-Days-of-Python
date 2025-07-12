# zip(), iterates over multiple iteratables
names = ["Ram", "Hitesh", "Aryan", "Ali"]
bills = [40, 70, 120, 65]

for item in zip(names, bills):
    print(item)

# OR
for name, amount in zip(names, bills):
    print(f"{name}: {amount}")