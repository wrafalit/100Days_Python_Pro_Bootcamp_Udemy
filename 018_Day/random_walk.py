import random
from turtle import Turtle, Screen
screen = Screen()

tim = Turtle()
tim.pensize(10)
tim.speed(8)
angle = [0,90,180,270]
for _ in range(1000):
    tim.forward(20)
    tim.right(random.choice(angle))
    screen.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.pencolor((r,g,b))










screen.exitonclick()