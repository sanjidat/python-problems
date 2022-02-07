# Write a Python program to get the smallest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2

def find_max(a):
    max_num = a[0]
    for i in a:
        if (i > max_num):
            max_num = i
    return max_num

print(find_max([1,2,-8,0]))
