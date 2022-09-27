# Challenge1
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

# Challenge2
table = PrettyTable()
# Challenge3
table.add_column('Pokemon Name', ["Pukachu", "Squirite", "Chamander"])
table.add_column('Type', ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
