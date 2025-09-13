# Build a generator that reads a file line-by-line and yields only lines containing a given keyword.

def special_lines(keyword):
    with open("example.txt", "r") as file:
        for line in file:
            lis = line.strip(".\n").split()
            for word in lis:
                if word.lower() == keyword.lower():
                    yield line

for line in special_lines("vision"):
    print(line, end="")