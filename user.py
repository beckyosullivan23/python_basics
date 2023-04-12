"""
user picks a number and the computer guesses the number
"""
import random
def guess(x):
    minnum = 1
    maxnum = x
    answer = ""
    while answer != "c":
        if minnum != maxnum:
            comp_guess = random.randint(minnum, maxnum)
        else:
            comp_guess = minnum
        answer = input("Is " + str(comp_guess) + " too high (H), too low (L) or correct (C)?").lower()
        if answer == "h":
            maxnum = comp_guess - 1
        elif answer == "l":
             minnum = comp_guess + 1
    print("The computer guessed the number " + str(comp_guess) + " as the correct answer")


guess(100)