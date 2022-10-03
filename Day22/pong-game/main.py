import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle(350, 0)
right_scoreboard = Scoreboard(x_position=200, y_position=200)
left_paddle = Paddle(-350, 0)
left_scoreboard = Scoreboard(x_position=-200, y_position=200)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    direction = ball.move()
    screen.update()
    # Collision to top or bottom wall
    if ball.ycor() in [280, -280]:
        # needs to bounce
        ball.bounce_y()
    # Ball touch the critical point
    if ball.xcor() in [330, -330]:
        # Detect collision to paddle
        if (ball.distance(left_paddle) < 50) or (ball.distance(right_paddle) < 50):
            ball.bounce_x()
        else:
            # Miss the ball
            if ball.xcor() == 330:
                left_scoreboard.increase_score()
                left_scoreboard.update_score()
            elif ball.xcor() == -330:
                right_scoreboard.increase_score()
                right_scoreboard.update_score()
            # time.sleep(1)
            ball.bounce_x()
            ball.reset()

screen.exitonclick()
