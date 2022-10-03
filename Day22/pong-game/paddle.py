from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super(Paddle, self).__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x_position, y_position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        temp_y = self.ycor() + 20
        self.goto(self.xcor(), temp_y)

    def move_down(self):
        temp_y = self.ycor() - 20
        self.goto(self.xcor(), temp_y)
