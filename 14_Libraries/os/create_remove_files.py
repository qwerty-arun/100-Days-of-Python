import os

# create file
with open("example.txt", "w") as f:
    f.write("Hello, OS module!")

# check if exists
print("File exists?", os.path.exists("example.txt"))

# remove file
os.remove("example.txt")
print("File deleted!")