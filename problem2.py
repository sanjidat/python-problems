#Compute the GCD of two positive integers:
def gcd(x,y):
    List1=[]
    List2=[]

    for i in range(1,x):
        if x % i == 0:
            List1.append(i)
    
    for j in range(1,y):
        if y % j == 0:
            List2.append(j)
    

    common = set(List1).intersection(set(List2))
    print("GCD ofthe two numbers are = ", max(common))

gcd(12,28)
gcd(336,360)
gcd(4,6)
gcd(24,30)
