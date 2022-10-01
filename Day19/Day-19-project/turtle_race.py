from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_dict = {}
very_bottom = -170


def initial():
    for color in colors:
        temp = Turtle(shape='turtle')
        temp.color(color)
        temp.penup()
        global very_bottom
        temp.goto(-230, very_bottom)
        turtle_dict[color] = temp
        very_bottom += 66


def random_move():
    random_turtle = random.choice(colors)
    rand_distance = random.randint(0, 10)
    turtle_dict[random_turtle].forward(rand_distance)
    return turtle_dict[random_turtle]


def Run():
    initial()
    if user_bet:
        is_game_over = True
    while is_game_over:
        moved_turle = random_move()
        if moved_turle.position()[0] >= 230:
            is_game_over = False
            if moved_turle.pencolor() == user_bet:
                print(f"You've won! The {moved_turle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {moved_turle.pencolor()} turtle is the winner!")


Run()

screen.exitonclick()
