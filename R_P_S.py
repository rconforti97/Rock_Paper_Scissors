# random is here for the random choice we have the computer making.
import random

option = ['Rock', 'Paper', 'Scissors']
quit_loop = False
user_score = 0
computer_score = 0

class bcolors:
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[91m'
    ENDC = '\033[0m'

def comparator(user_input):
    # We want it to re-choose the random choice each time so it goes into the function
    random_option = random.choice(option).lower()
    # We have to declare them 'global' here because otherwise it does not recognize
    global computer_score
    global user_score

    if random_option == user_input:
        return print("The computer has also chosen " + random_option + "\nTie - No one gets any points")

    elif (user_input == 'rock' and random_option == 'scissors' or user_input == 'paper' and random_option == 'rock'
          or user_input == 'scissors' and random_option == 'paper'):
        print("The computer has chosen: " + bcolors.blue + random_option + bcolors.ENDC + "\nYou have won this round against the computer! "
                                                            "Point for you!")
        user_score += 1
        return print("\nYour score is: " + str(user_score) + "\nComputer score is: " +  str(computer_score))

    elif random_option == 'rock' and user_input == 'scissors' or random_option == 'paper' and user_input == 'rock'\
            or random_option == 'scissors' and user_input == 'paper':
        print("The computer has chosen: " + bcolors.blue + random_option + bcolors.ENDC + "\nThe computer has won! Point for the computer.")
        computer_score += 1
        return print("\nYour score is: " + str(user_score) + "\nComputer score is: " + str(computer_score))

    else:
        return print(bcolors.warning + "Please check your spelling." + bcolors.ENDC)


def round_checker(user_score, computer_score):
    global quit_loop
    if user_score == 5:
        print("------------------------------------------------------\n" + bcolors.green +
              "Heck yeah! You just showed that computer who's boss! Congratulations on winning." + bcolors.ENDC)
        quit_loop = True
        return print("Thank you for playing!")
    elif computer_score == 5:
        quit_loop = True
        print("------------------------------------------------------\n" + bcolors.green +
              "Oh no! The computer has won. :(" + bcolors.ENDC)
        return print("Thank you for playing!")
    else:
        return


print("\nWelcome to Rock, Paper, Scissors! Made by Rachel Conforti.\nHere are the rules:\n1) When prompted pick "
      "Rock, Paper, or Scissors. \n2) Who ever wins 5 points first wins! \n3) Have fun :)")

while quit_loop is not True:
    print("------------------------------------------------------\nWhat is you choice? Rock, Paper, or Scissors?")
    user_input = input().lower()
    comparator(user_input)
    round_checker(user_score, computer_score)

