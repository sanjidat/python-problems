# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it


def new(a,b):
    
    def sum(a,b):
        return a+b
    s = sum(a,b)
    
    return s + 5
print(new(20,10))




