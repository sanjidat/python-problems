#Generate a random number between 1 and 9 (including 1 and 9).Ask the user to guess the number, then tell them whether they guessed too low,too high, or exactly right.

import random
def guess(num1):
    num2 = random.randint(1,9)
    print(num2)
    if num1 == num2:
        print("Exactly Right")
    elif(num1 < num2):
        print("Too Low")
    elif (num1 > num2):
        print("Too High")

num1=(int(input("Guess a number between 1 and 9:  ")))
guess(num1)
