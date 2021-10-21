#Ask the user for a number and determine whether the number is prime or not.

def prime(x):
    for i in range(2,x-1):
        if x%i == 0:
            return "The Number is not Prime"
        else:
            return "The Number is Prime"

a=prime(int(input("Enter a Number :  ")))
print(a)

