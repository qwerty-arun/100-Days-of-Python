# Infinite Generators 

def infinite_refill():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_refill()
user2 = infinite_refill()

for _ in range(6):
    print(next(refill))


for _ in range(5):
    print(next(user2))
# There is no inter-mixing of values. 
# You can keep track of various variables using the same function