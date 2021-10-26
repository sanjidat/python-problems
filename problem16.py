# Given two strings, s1 and s2.
# Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Samira"
s2 = "Diwish"

s1_middle = int(len(s1)/2)
s1_first = s1[:s1_middle]
s1_last = s1[s1_middle:]

s3 = s1_first + s2 + s1_last
print(s3)
