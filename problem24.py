# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 

m = int(input("enter the number of rows: "))
n = int(input("enter the number of columns: "))

Two_D_Array = [[0 for i in range(n)] for j in range(m)]
for j in range(m):
    for i in range(n):
        Two_D_Array[j][i] =j*i
print(Two_D_Array)
