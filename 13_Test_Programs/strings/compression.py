# Compress a string using run-length encoding (e.g., "aaabb" -> "a3b2")

def compress(str):
    compressed = ""
    count = 1
    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            count += 1
        else:
            compressed += f"{str[i-1]}{count}"
            count = 1
    compressed += f"{str[-1]}{count}"

    return compressed

print(compress("aaabb"))