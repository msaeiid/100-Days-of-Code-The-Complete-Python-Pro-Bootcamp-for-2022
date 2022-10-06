from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

DELAY = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.title('My Snake Game!')
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.go_up, key='Up')
screen.onkey(fun=snake.go_down, key='Down')
screen.onkey(fun=snake.go_left, key='Left')
screen.onkey(fun=snake.go_right, key='Right')


# reset snake to (0.0) reset scoreboard


game_is_on = True
while game_is_on:
    snake.move_snake()
    time.sleep(DELAY)
    screen.update()

    # Collision to corner of screen detection
    if snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()
        DELAY = 0.1
    # Collision to food
    if snake.head.distance(food) < 15:
        snake.increase_snake()
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        DELAY *= 0.9
    # Collision to tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            DELAY = 0.1

screen.exitonclick()
