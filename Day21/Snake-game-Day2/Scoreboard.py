from turtle import Turtle

FONT = ("Arial", 8, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.goto(0, 278)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(move=False, align=ALIGNMENT, arg=f'Score: {self.score}', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!')
