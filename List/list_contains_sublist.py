# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output


def is_Sublist(x,y):
    sublist = False

    if y == []:
        sublist = True
    elif x == y:
        sublist = True
    elif len(y) > len(x):
        sublist = False
    else:
        for i in range(len(x)):
            if x[i] == y[0]:
                n = 1
                while(n<len(y) and (x[n+i] == y[n])):
                    n=n+1
                if(n == len(y)):
                    sublist = True
    return sublist

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]

print(is_Sublist(a, b))
print(is_Sublist(a, c))
