# A bunch of if statements
import random

option = ['Rock', 'Paper', 'Scissors']
quit_loop = False
user_score = 0
computer_score = 0
# computer_score = 0
# user_score
# user_input = input("Your Choice: ")
# print(user_input)
# Rock > Scissors
# Paper > Rock
# Scissors > Paper

def comparator(user_input):
    random_option = random.choice(option)
    global computer_score
    global user_score
    if (user_input == 'Rock' and random_option == 'Rock' or user_input == 'Paper' and random_option == 'Paper'
            or user_input == 'Scissors' and random_option == 'Scissors'):
        return print("The computer has also chosen: " + random_option + "\nSo it's a Tie - No one gets any points")
    elif (user_input == 'Rock' and random_option == 'Scissors' or user_input == 'Paper' and random_option == 'Rock'
          or user_input == 'Scissors' and random_option == 'Paper'):
        print("The computer has chosen: " + random_option + "\nYou have won this round against the computer! "
                                                            "Point for you!")
        user_score += 1
        return print("\nYour score is: " + str(user_score) + "\nComputer score is: " +  str(computer_score))
    elif random_option == 'Rock' and user_input == 'Scissors' or random_option == 'Paper' and user_input == 'Rock' \
            or random_option == 'Scissors' and user_input == 'Paper':
        print("The computer has chosen: " + random_option + "\nThe computer has won! Point for the computer")
        computer_score += 1
        return print("\nYour score is: " + str(user_score) + "\nComputer score is: " + str(computer_score))
    else:
        return print("Please check your spelling.")


def round_checker(user_score, computer_score):
    global quit_loop
    if user_score == 5:
        print("------------------------------------------------------")
        print("Heck yeah! You just showed that computer who's boss! Congratulations on winning.")
        quit_loop = True
        return print("Thank you for playing!")
    elif computer_score == 5:
        quit_loop = True
        print("------------------------------------------------------")
        print("Oh no! The computer has won. :(")
        return print("Thank you for playing!")
    else:
        return

print("Welcome to Rock, Paper, Scissors! \n\nRules:\nWhen prompted pick 'Rock', 'Paper', or 'Scissors!'. Who ever wins 5 points first wins!.")

while quit_loop is not True:
    print("------------------------------------------------------")
    print("What is you choice? Rock, Paper, or Scisscors? (it is case sensitive)")
    user_input = input()
    comparator(user_input)
    round_checker(user_score, computer_score)

