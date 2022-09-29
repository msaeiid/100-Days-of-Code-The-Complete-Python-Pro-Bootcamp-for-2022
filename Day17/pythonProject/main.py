# if we use Turtle class more than three times we should use in this way
import turtle as t
import random

# if we use Turtle class less than two times we should use in this way
# import turtle


tim = t.Turtle()
tim.shape("arrow")


# Challenge 1
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# Challenge 2 dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Challenge 3
#
# degrees = 360
# length = 100
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     random_color = random.choice(color)
#     tim.color(random_color)
#     angle = degrees / num_sides
#     for _ in range(num_sides):
#         tim.right(angle)
#         tim.forward(length)
#
#
# for i in range(3, 10):
#     draw_shape(i)

# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# Challenge 4
# directions = [0, 90, 180, 270]
# tim.pensize(7)
# tim.speed("fastest")
# each_step = 30
# t.colormode(255)
#
#
# def random_color():
#     R = random.randint(0, 255)
#     G = random.randint(0, 255)
#     B = random.randint(0, 255)
#     return (R, G, B)
#
#
# for _ in range(200):
#     tim.color(random_color())
#     random_angle = random.choice(directions)
#     tim.forward(each_step)
#     tim.setheading(random_angle)

# Challenge 5

def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)


def draw_spirograph(size_of_gap: int):
    t.colormode(255)
    tim.speed('fastest')
    tim.color('red')
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
