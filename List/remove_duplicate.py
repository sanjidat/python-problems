# Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output {40, 10, 80, 50, 20, 60, 30}


a = [10,20,30,20,10,50,60,40,80,50,40]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
