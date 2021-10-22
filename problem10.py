#Calculate the cube of all numbers from 1 to a given number

def cube(x):
    for i in range (1,x+1):
        result = i**3
        print("Cube of", i, "is", result)

cube(int(input("Enter a Number:  ")))
