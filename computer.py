"""
Computer picks a random number between 1 and 10, the user has three turns to guess the correct number
"""
import random
def guesses():
    guess = ""
    number = random.randint(1,10)
    guess_counter = 0
    no_left_guess = 3
    out_of_guess = False
    try:
        while guess != number and not(out_of_guess):
            if guess_counter < no_left_guess:
                guess = int(input("Enter a number between 1 and 10:"))
                guess_counter += 1
            else:
                out_of_guess= True

            if out_of_guess:
                print("You're out of guesses")
            elif number == guess:
                print("You guessed correct!")
            elif guess > number:
                print(" That number is too high!")
            else:
                print("That number is too low!")
    except ValueError:
        print("Invalid input.")

    print("The number was " + str(number) +".")

guesses()



