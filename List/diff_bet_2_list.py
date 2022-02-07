# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]

list1 = [1, 2, 3, 4]
list2 = [1, 2]

a = set(list1) - set(list2)
Output = list(a)
print(Output)
