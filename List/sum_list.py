# Write a Python program to sum all the items in a list
# Example sum_list([1,2,-8])
# Return -5

def sum_list(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum

print(sum_list([1,2,-8]))
    
    
