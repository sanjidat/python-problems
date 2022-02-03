# Write a Python program to check a triangle is valid or not

def triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

side_1 = float(input("Enter the length of side a : "))
side_2 = float(input("Enter the length of side b : "))
side_3 = float(input("Enter the length of side c : "))

if triangle(side_1,side_2,side_3):
    print("Triangle is valid")
else:
    print("Triangle is invalid")
