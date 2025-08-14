# Build a mul table as a dictionary with tuple keys: {(2,3): 6}

def mul_table(num):
    table = {}
    for i in range(1, 11):
        table[tuple([num, i])] = num * i 

    return table

def mul_table1(num):
    return {(num,i):num * i for i in range(1,11)}

print(mul_table(2))
print(mul_table1(2))
