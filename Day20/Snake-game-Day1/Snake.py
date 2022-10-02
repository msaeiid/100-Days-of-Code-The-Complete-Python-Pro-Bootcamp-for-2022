from turtle import Turtle

STEP = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            temp_snake = Turtle(shape='square')
            temp_snake.color('white')
            temp_snake.penup()
            temp_snake.goto(position)
            self.segments.append(temp_snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            temp_x = self.segments[i - 1].xcor()
            temp_y = self.segments[i - 1].ycor()
            self.segments[i].goto(temp_x, temp_y)
        self.segments[0].forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
