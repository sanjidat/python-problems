#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.


def reverseorder(x):
    a = x.split()
    b=a[::-1]
    return " ".join(b)

print(reverseorder(str(input("Enter a long strong:  "))))


