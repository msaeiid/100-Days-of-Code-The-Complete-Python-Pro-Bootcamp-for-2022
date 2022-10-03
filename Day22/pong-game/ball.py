from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        temp_x = self.xcor() + self.x_move
        temp_y = self.ycor() + self.y_move
        self.goto(temp_x, temp_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
