# Write a program to print the following start pattern using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


def pattern(x):
    for i in range(1, x+1):
        for j in range(1,i+1):
            print("*", end =" ")
        print("")
    for k in range(x,1,-1):
        for l in range(k,1,-1):
            print("*", end =" ")
        print("")
            
pattern(5)
