# Invert a dictionary: swap keys and values

def inversion(dic):
    print(dic)
    invDic = {value:key for key, value in dic.items()}
    print(invDic)

inversion({"laptop": 1, "monitor": 2})