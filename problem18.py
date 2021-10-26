# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string, so that all lowercase letters should come first.

s1 = "AmErIcA"
u=[]
l=[]
for i in s1:
    if i.islower():
        l.append(i)
    else:
        u.append(i)
s2=''.join(l+u)
print(s2)



