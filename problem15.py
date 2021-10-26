# Create a string made of the first, middle and last character


string = "Senorita"
print("Original String is ", string)

first = string[0]
string_length = len(string)
middle = string[int(string_length/2)]
last = string[-1]

result = first + middle + last
print("Expected Output is ", result)
