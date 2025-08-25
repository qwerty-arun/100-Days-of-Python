# Strings
chai_type = "Ginger Chai"
customer_name = "Arun"

print(f"Order for {customer_name} : {chai_type} please!")

# Slicing and indexing
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"First word, every other letter: {chai_description[0:8:2]}") # you can avoid 0
print(f"Last word: {chai_description[12:]}")
print(f"Reversed sentence: {chai_description[::-1]}")

# Encoding
lable_text = "Chai Special"
encoded_label = lable_text.encode("utf-8")
print(f"Non-Encoded Label: {lable_text}")
print(f"Encoded Label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")