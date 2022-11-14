import colorgram
from turtle import Screen, Turtle
import random


class HirstPainting:

    def __init__(self):
        self.col_numbers = 10
        self.row_numbers = 10
        self.space = 50
        self.up = 90
        self.left = 180
        self.down = 270
        self.right = 0
        self.screen = Screen()
        self.jim = Turtle()
        self.jim.shape("arrow")
        self.jim.pensize(20)
        self.screen.colormode(255)
        self.jim.speed('fastest')
        self.colors = None
        self.jim.hideturtle()

    def make_random_color_list(self):
        colors = colorgram.extract("images.jpg", 37)
        self.colors = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]

    def initiate_game(self):
        self.colors_list = self.make_random_color_list()
        self.jim.penup()
        temp = (self.left + self.down) / 2
        self.jim.setheading(temp)  # on the way of start
        self.jim.forward(6 * self.space)
        self.jim.setheading(self.right)

    def write_in_row(self, col: int, end_line: bool):
        self.jim.dot(20, self.random_color())
        self.jim.penup()
        if not end_line:
            self.jim.forward(self.space)
            self.jim.pendown()
            return col + self.space
        else:
            self.carriage_return()
            return 0

    def carriage_return(self):
        self.jim.penup()
        self.jim.setheading(self.up)
        self.jim.forward(self.space)
        self.jim.setheading(self.left)
        self.jim.forward((self.row_numbers - 1) * self.space)
        self.jim.setheading(self.right)

    def random_color(self):
        return random.choice(self.colors)

    def run(self):
        self.make_random_color_list()
        self.initiate_game()
        counter = 0
        for dot in range(1, self.row_numbers * self.col_numbers + 1):
            if dot % self.row_numbers == 0:
                counter = self.write_in_row(counter, True)
            else:
                counter = self.write_in_row(counter, False)
        self.screen.exitonclick()


HirstPainting().run()
