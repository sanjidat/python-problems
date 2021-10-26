# Given two strings, s1 and s2.
# Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next,
# the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.

s1 = "Abcdef"
s2 = "ghijkl"

first = s1[0] + s2[len(s2)-1]
middle = s1[1] + s2[len(s2)-2]
last = s1[2:] + s2[:-2]

s3 = first + middle + last

print(s3)

