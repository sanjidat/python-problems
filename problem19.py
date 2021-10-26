# Count all letters, digits, and special symbols from a given string

str1 = "a87bh@2#"

char = 0
digit = 0
symbol = 0

for i in str1:
    if i.isdigit():
        digit = digit+1
    elif i.isalpha():
        char=char+1
    else:
        symbol=symbol+1
        
print(digit)
print(symbol)
print(char)
