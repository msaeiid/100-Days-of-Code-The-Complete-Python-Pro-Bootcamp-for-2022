from Snake import Snake
from turtle import Screen
import time
from food import Food
from Scoreboard import Scoreboard

DELAY = 0.2

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()
        # Detect collision with wall
        if (snake.head.ycor() or snake.head.xcor()) in [280, -280]:
            game_is_on = False
            scoreboard.game_over()
        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


run_the_game()

screen.exitonclick()
