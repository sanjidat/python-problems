#  Write a Python program to generate all permutations of a list in Python
# Input [1,2,3]
# Output [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

from itertools import permutations

p = permutations([1,2,3])
print(p)

for i in list(p):
    print(i)
