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

"""
    Some rules :
    Rock wins against scissors 
    Scissors win against paper  
    paper wins against rock
"""
computer_choice  =  random.randint(0, 2)
computer_rps = ""
user_rps  =  ""
print(computer_choice)
user_choice  =  int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

win = ""

if user_choice != computer_choice  :
    # first rule
    if computer_choice == 0 and user_choice == 2:
        win = "Computer"
        computer_rps = rock
        user_rps = scissors

    elif computer_choice == 2 and user_choice == 0:
        win = "User"
        user_rps = rock
        computer_rps = scissors

    # second rule
    if computer_choice == 2 and user_choice == 1:
        win = "Computer"
        computer_rps = rock
        user_rps = scissors

    elif computer_choice == 1 and user_choice == 2:
        win = "User"
        user_rps = rock
        computer_rps = scissors

    # third rule
    if computer_choice == 1 and user_choice == 0:
        win = "Computer"
        computer_rps = rock
        user_rps = scissors

    elif computer_choice == 0 and user_choice == 1:
        win = "User"
        user_rps = rock
        computer_rps = scissors

    if win == "User" :
        print(f"Computer choice  : {computer_rps} \n User choice : {user_rps}")
        print("You win")
    else:
        print(f"Computer choice  : {computer_rps} \n User choice : {user_rps}")
        print("You lose")


else:
    if user_choice == 0 or computer_choice == 0 :
        computer_rps = rock
        user_rps = rock
    elif user_choice == 1 or computer_choice == 1 :
        computer_rps = paper
        user_rps = paper
    elif user_choice == 2 or computer_choice == 2 :
        computer_rps = paper
        user_rps = paper

    print(f"Computer choice  : {computer_rps} \n User choice : {user_rps}")
    print("It's a draw")









