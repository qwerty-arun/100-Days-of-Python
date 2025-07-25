chai_menu = {"masala": 30, "ginger": 50}

try:
    chai_menu["elaichi"]
except KeyError:
    print("KEYERROR: The key that you are trying to access doesn't exist")

print("Hello Chai")