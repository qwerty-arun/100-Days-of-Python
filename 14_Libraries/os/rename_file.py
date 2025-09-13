import os

# create a file
with open("old_name.txt", "w") as f:
    f.write("Some content")

# rename file
os.rename("old_name.txt", "new_name.txt")
print("Renamed file to new_name.txt")