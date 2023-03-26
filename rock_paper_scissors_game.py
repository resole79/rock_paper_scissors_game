# import module
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
    _______________
---' ______________)
    (         ,-'`)
    (____,-'` ,-'`   
---._____,-'`  
'''

spock = '''
        ____ ____            ____ ____
       (    (    \          /    )    )
        \    \    \        /    /    /
   ____  \    \    \      /    /    /
   (   \  \    \    \    /    /    /
    \   \  \    \    \  /    /    /
     \   \  \          V         /
      \   \  \                  /
       \   \ |                 /
        \   v                 /

'''
# Declare variable
list_of_image = [rock, paper, scissors]
list_of_name = ["Rock", "Paper", "Scissors"]
list_of_image1 = [rock, paper, scissors, lizard, spock]
list_of_name1 = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

rules_dict = {"0, 0": "", "0, 1": "Paper covers Rock", "0, 2": "Rock crushes Scissors",
              "1, 0": "Paper covers Rock", "1, 1": "", "1, 2": "Scissors cuts Paper",
              "2, 0": "Rock crushes Scissors", "2, 1": "Scissors cuts Paper", "2, 2": ""}

rules_dict1 = {"0, 0": "", "0, 1": "Paper covers Rock", "0, 2": "Rock crushes Scissors",
            "0, 3": "Rock crushes Lizard", "0, 4": "Spock vaporizes Rock", "1, 0": "Paper covers Rock", "1, 1": "",
              "1, 2": "Scissors cuts Paper", "1, 3": "Lizard eats Paper", "1, 4": "Paper disproves Spock",
              "2, 0": "Rock crushes Scissors", "2, 1": "Scissors cuts Paper", "2, 2": "",
              "2, 3": "Scissors decapitates Lizard", "2, 4": "Spock smashes Scissors", "3, 0": "Rock crushes Lizard",
              "3, 1": "Lizard eats Paper", "3, 2": "Scissors decapitates Lizard", "3, 3": "",
              "3, 4": "Lizard poisons Spock", "4, 0": "Spock vaporizes Rock", "4, 1": "Paper disproves Spock",
              "4, 2": "Spock smashes Scissors", "4, 3": "Lizard poisons Spock", "4, 4": ""}

# Ask user if want game, which and the player
play = "\nDo you want have a game?. ( Y or N ) : "

game = "\n0: Rock, Paper, Scissors\n1: Rock, Paper, Scissors (Lizard, Spock)"
game += "\nPlease, choice a game "

choice = "\n0 = Rock\n1 = Paper\n2 = Scissors"
choice += "\nWhat do you choose? "

choice1 = "\n0 = Rock\n1 = Paper\n2 = Scissors\n3 = Lizard\n4 = Spock"
choice1 += "\nWhat do you choose? "

while True:

    ask_to_play = input(play).lower()

    if ask_to_play == "y":

        which_game = input(game)

        # User choice game "0"
        if which_game == "0":

            user_choice = input(choice)
            if user_choice == "0" or user_choice == "1" or user_choice == "2":

                computer_choice = random.randint(0, 2)

                print("\nUser choice")

                print(list_of_name[int(user_choice)])
                print(list_of_image[int(user_choice)])

                print("\nComputer choice")

                print(list_of_name[computer_choice])
                print(list_of_image[computer_choice])

                print(rules_dict[f"{user_choice}, {computer_choice}"])

                # if condition to check combination rules
                if user_choice == "0" and computer_choice == 2:
                    print("YOU WIN")
                elif user_choice == "2" and computer_choice == 0:
                    print("YOU LOSE")
                elif int(user_choice) > computer_choice:
                    print("YOU WIN")
                elif int(user_choice) < computer_choice:
                    print("YOU LOSE")
                elif int(user_choice) == computer_choice:
                    print("YOU DRAW")
                else:
                    print("\nSorry, you have uncorrected choice!")
            else:
                print("\nSorry, you have uncorrected choice!")

        # User choice game "1"
        elif which_game == "1":
            user_choice = input(choice1)
            if user_choice == "0" or user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4":
                computer_choice = random.randint(0, 4)

                print("\nUser choice")

                print(list_of_name1[int(user_choice)])
                print(list_of_image1[int(user_choice)])

                print("\nComputer choice")

                print(list_of_name1[computer_choice])
                print(list_of_image1[computer_choice])

                print(rules_dict1[f"{user_choice}, {computer_choice}"])

                # if condition to check combination rules
                if user_choice == "0" and computer_choice == 2:
                    print("YOU WIN")
                elif user_choice == "2" and computer_choice == 0:
                    print("YOU LOSE")
                elif user_choice == "0" and computer_choice == 3:
                    print("YOU WIN")
                elif computer_choice == 0 and user_choice == "3":
                    print("YOU LOSE")
                elif user_choice == "1" and computer_choice == 4:
                    print("YOU WIN")
                elif computer_choice == 1 and user_choice == "4":
                    print("YOU LOSE")
                elif user_choice == "2" and computer_choice == 3:
                    print("YOU WIN")
                elif computer_choice == 2 and user_choice == "3":
                    print("YOU LOSE")
                elif user_choice == "3" and computer_choice == 4:
                    print("YOU WIN")
                elif computer_choice == 3 and user_choice == "4":
                    print("YOU LOSE")
                elif int(user_choice) > computer_choice:
                    print("YOU WIN")
                elif int(user_choice) < computer_choice:
                    print("YOU LOSE")
                elif int(user_choice) == computer_choice:
                    print("YOU DRAW")
                else:
                    print("\nSorry, you have uncorrected choice!")
            else:
                print("\nSorry, you have uncorrected choice!")
        else:
            print("\nSorry, you have uncorrected choice!")
    elif ask_to_play == "n":
        print("\nGoodBye")
        break

    else:
        print("\nSorry, you have uncorrected choice!")
