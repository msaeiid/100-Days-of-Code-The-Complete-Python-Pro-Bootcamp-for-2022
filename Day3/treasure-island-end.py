print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to treasure Island.\nYour mission is to find the treasure.")

user_message = "You enter a room of beasts. GAME OVER!"

direction = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if direction == 'left':
    come_to_island = input(
        'You come to a lake. There is an island in the middle of the lake. "wait" to wait for a bloat. Type "swim" to swim accross.\n').lower()
    if come_to_island == 'wait':
        doors = input(
            'You arrive at the island unharmed.There is a house with 3 doors,One "red", one "yellow" and one "blue". Which colour do you choose?\n').lower()
        if doors == 'yellow':
            user_message = "You found the treasure. You Win!"
        elif doors == "red":
            user_message = "It's a room full of fire. Game is over"
        elif doors == 'blue':
            user_message = "You enter a room beasts. Game Over!"
        else:
            user_message = "You choose a door that doesn't exists.Game over"
 
    else:
        print("You got attacked by an angry. Game over!")
else:
    user_message = "You fell into a hole.Game OVER!"
print(user_message)
