# Write a Python Program for computing the factorial of a given number
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result = result * i
    print(result)
factorial(int(input("Enter a Number:")))
