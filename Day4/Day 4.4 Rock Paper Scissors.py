import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


user_chose = int(input(
    "What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_chose = random.randint(0, 2)

if 0 > user_chose or user_chose > 2:
    print('You typed an invalid number, you lose!')
else:

    lst = [rock, paper, scissors]
    print(f"Use chose {lst[user_chose]}")
    print(f"Computer chose {lst[computer_chose]}")

    win_message = "You Win!"
    lose_message = "You Lose!"
    if user_chose == 0 and computer_chose == 2:
        print(win_message)
    elif user_chose == 2 and computer_chose == 1:
        print(win_message)
    elif user_chose == 1 and computer_chose == 0:
        print(win_message)
    elif user_chose == computer_chose:
        print("It's a Draw!")
    else:
        print(lose_message)
