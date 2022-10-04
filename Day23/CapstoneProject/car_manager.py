from turtle import Turtle
import random

COLORS = ['red', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

LEFT = 180


class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        self.penup()
        self.goto(300, random_y)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed()

    def move_the_car(self, cars_speed):
        self.backward(cars_speed)


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car = random.randint(1, 6)
        if random_car in [1]:
            car = Car()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move_the_car(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
