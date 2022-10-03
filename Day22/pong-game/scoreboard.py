from turtle import Turtle

ALIGN = 'center'
FONT = FONT = ("Arial", 50, 'normal')


class Scoreboard(Turtle):
    def __init__(self, x_position, y_position):
        super(Scoreboard, self).__init__()
        self.shape('arrow')
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x_position, y_position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.score}', move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
