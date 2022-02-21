from turtle import  Turtle
import random

class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_rand = random.randint(-280, 280)
        y_rand = random.randint(-280, 280)
        self.goto(x=x_rand, y=y_rand)
