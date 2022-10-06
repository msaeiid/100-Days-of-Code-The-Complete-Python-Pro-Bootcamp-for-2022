from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STEP = 20


class Snake(Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.segments = []
        self.start_x = 0
        self.start_y = 0
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.segments = []
        self.start_x = 0
        self.start_y = 0
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position: tuple):
        segment = Turtle('square')
        segment.color('white')
        # segment.shapesize(stretch_len=1, stretch_wid=1)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def create_snake(self):
        for _ in range(3):
            self.add_segment((self.start_x, self.start_y))
            self.start_x -= STEP

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            temp_x = self.segments[i - 1].xcor()
            temp_y = self.segments[i - 1].ycor()
            self.segments[i].goto(temp_x, temp_y)
        self.segments[0].forward(STEP)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def increase_snake(self):
        self.add_segment(self.segments[-1].position())

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
