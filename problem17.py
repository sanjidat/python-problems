# Given two strings, s1 and s2,
# write a program to return a new string made of s1 and s2’s first, middle, and last characters.

s1 = "Alien"
s2 = "Motor"

first = s1[0] + s2[0]
middle = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
last = s1[len(s1)-1] + s2[len(s2)-1]

s3 = first + middle + last
print(s3)
