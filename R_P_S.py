# random is here for the random choice we have the computer making.
import random

option = ['Rock', 'Paper', 'Scissors']
quit_loop = False
user_score = 0
computer_score = 0


def comparator(user_input):
    # We want it to re-choose the random choice each time so it goes into the function
    random_option = random.choice(option)
    # We have to declare them 'global' here because otherwise it does not recognize
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
        print("------------------------------------------------------\nHeck yeah! You just showed that "
              "computer who's boss! Congratulations on winning.")
        quit_loop = True
        return print("Thank you for playing!")
    elif computer_score == 5:
        quit_loop = True
        print("------------------------------------------------------\nOh no! The computer has won. :(")
        return print("Thank you for playing!")
    else:
        return


print("Welcome to Rock, Paper, Scissors! made by Rachel Conforti.\nHere are the rules:\n1) When prompted pick "
      "Rock, Paper, or Scissors. \n2) Who ever wins 5 points first wins! \n3) Your responses case sensitive."
      "\n4) Have fun :)")

while quit_loop is not True:
    print("------------------------------------------------------\nWhat is you choice? Rock, Paper, or Scissors?")
    user_input = input()
    comparator(user_input)
    round_checker(user_score, computer_score)

