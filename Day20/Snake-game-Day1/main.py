from Snake import Snake
from turtle import Screen
import time

DELAY = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def run_the_game():
    screen.update()
    game_is_on = True
    while game_is_on:
        snake.move()
        screen.update()
        time.sleep(DELAY)


run_the_game()

screen.exitonclick()
