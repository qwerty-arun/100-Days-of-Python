# Tuples - denoted by (), they are immutable
masala_spices = ("cardamom", "cloves", "cinnamom")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio , cardamom_ratio = 2, 3
print(f"Ratios G: {ginger_ratio}, C: {cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratios G: {ginger_ratio}, C: {cardamom_ratio}")

# membership

print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")
print(f"Is ginger in masala spices ? {'cinnamom' in masala_spices}")
print(f"Is ginger in masala spices ? {'Cinnamom' in masala_spices}")