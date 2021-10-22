#Write a program to print multiplication table of a given number

def mul(x):
    m=0
    for i in range(1,11):
        m=x*i
        print(m)
mul(int(input("Enter a number:  ")))
