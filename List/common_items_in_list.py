# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"

Output = set(color1) & set(color2)
print(Output)
