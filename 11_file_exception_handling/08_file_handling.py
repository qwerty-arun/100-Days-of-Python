# file = open("order.txt", "w")
# try:
#     file.write("I am learning file handling")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("Ginger Tea - 5 cups")