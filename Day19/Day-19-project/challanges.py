from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

angle = 10
distance = 10


def move_forward():
    tim.forward(distance)


def move_backward():
    tim.backward(distance)


def turn_left():
    #tim.left(angle)
    tim.setheading(tim.heading() + angle)


def turn_right():
    # tim.right(angle)
    tim.setheading(tim.heading() - angle)


def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
