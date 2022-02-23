from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300,0)


    def move(self):
        self.backward(STARTING_MOVE_DISTANCE)



