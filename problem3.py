#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def diff(x):
    if x > 17:
        return 2*abs(x-17)
    else:
        return x-17
print(diff(int(input("Enter a Random Number: "))))
        
