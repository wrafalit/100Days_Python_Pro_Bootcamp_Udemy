from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.pu()
        segment.goto(position)
        self.segments.append(segment)


    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        self.segments.clear()
        self.create_snake()


    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)
