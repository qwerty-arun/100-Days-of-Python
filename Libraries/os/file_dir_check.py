import os

path = "."

print("Is directory?", os.path.isdir(path))
print("Is file?", os.path.isfile(path))
print("Absolute path:", os.path.abspath(path))