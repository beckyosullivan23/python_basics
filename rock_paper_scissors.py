import random
def rps():
    answer = input("Choose what you want to be, rock 'R', paper 'P' or scissors 'S':\n")
    comp = random.choice(['R', 'P', 'S'])
    if answer == comp:
        return("It's a draw!")
    elif (answer == "R" and comp == "P") or (answer == "P" and comp == "S") or (answer == "S" and comp == "R"):
        return("You lose!")
    elif (answer == "R" and comp == "S") or (answer == "S" and comp == "P") or (answer == "P" and comp == "R"):
        return("You win!")
    else:
        return("Invalid Input.")

print(rps())