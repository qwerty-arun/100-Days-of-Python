import os

print("Before:", os.getcwd())
os.chdir("..")   # go one folder up
print("After:", os.getcwd())