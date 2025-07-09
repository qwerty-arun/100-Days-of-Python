spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(spice_mix)
# this is mutable
spice_mix.add("Ginger")
spice_mix.add("Cardamom")
print(spice_mix)
print(f"After spice mix id: {id(spice_mix)}")