import os

print("PATH:", os.environ.get("PATH"))
print("HOME:", os.environ.get("HOME"))

# set a new variable
os.environ["MY_VAR"] = "PythonOS"
print("MY_VAR:", os.environ["MY_VAR"])