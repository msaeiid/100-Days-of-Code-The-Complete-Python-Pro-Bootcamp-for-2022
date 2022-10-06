from turtle import Turtle

ALIGN = 'center'
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.score = 0
        self.high_score = self.read_data()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score}    High Score: {self.high_score}', font=FONT, align=ALIGN, move=False)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_data(self):
        with open('data.txt', mode='r') as file:
            return int(file.read())

    def save_data(self):
        with open('data.txt', mode='w') as file:
            file.write(f'{self.high_score}')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_data()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'GAME OVER!', font=FONT, align=ALIGN, move=False)
