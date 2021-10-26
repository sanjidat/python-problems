#Generate a Python list of all the even numbers between 4 to 30

def new(x):
    l = []
    for i in range(4,x):
        if i%2 == 0:
            l.append(i)
    print(l)

    

new(30)
        
