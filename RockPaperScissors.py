"""
This program prompts the user to select either Rock, Paper or Scissors.
The program then compares the user's choice to the randomly generated
computer's choice
The results are compared to determine the winner.
"""
from random import randint


options = ["ROCK", "PAPER", "SCISSORS"]
message = {"tie": "Yawn it's a tie!",
           "won": "Yay you won!", "lost": "Aww you lost!"}


def decide_winner(user_choice, computer_choice):
    print("\nYour choice: %s \n" % user_choice)

    print("Computer's choice: %s \n" % computer_choice)

    if user_choice == computer_choice:

        return print(message["tie"])

    elif user_choice == options[0] and computer_choice == options[2]:
        return print(message["won"])

    elif user_choice == options[1] and computer_choice == options[0]:
        return print(message["won"])

    elif user_choice == options[2] and computer_choice == options[1]:
        return print(message["won"])
    else:
        return print(message["lost"])


def main():
    print("========= Rock, Paper or Scissors? ========\n")

    user_choice = input("Enter either Rock, Paper or Scissors: ")

    user_choice = user_choice.upper()

    computer_choice = options[randint(0, 2)]

    decide_winner(user_choice, computer_choice)


if __name__ == '__main__':
    main()
