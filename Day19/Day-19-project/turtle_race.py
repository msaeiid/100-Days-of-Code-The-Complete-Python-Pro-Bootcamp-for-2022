from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_dict = {}
very_bottom = -170
for color in colors:
    temp = Turtle(shape='turtle')
    temp.color(color)
    temp.penup()
    temp.goto(-230, very_bottom)
    temp.pendown()
    turtle_dict[color] = temp
    very_bottom += 66
screen.exitonclick()
