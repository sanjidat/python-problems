#Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

#For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

def sum(x):
    s=0
    for i in range(1,x+1):
        s=s+i
    print(s)
print(sum(int(input("Enter a number"))))
