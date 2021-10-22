#Write a program to calculate the sum of series up to n term.
#For example, if n =5 the series will become 5 + 55 + 555 + 5555 + 55555 = 24690

def sum(x):
    a = 5
    s = 0
    for i in range(0,x):
        s = s+a
        a = (a*10) + 5
    print(s)
sum(5)
