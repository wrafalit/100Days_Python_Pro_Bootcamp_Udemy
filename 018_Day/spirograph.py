import random
from turtle import Turtle, Screen
screen = Screen()

tim = Turtle()
tim.speed(10)
angle = 5
for _ in range(int(360/angle)):
    tim.circle(50)
    tim.setheading(tim.heading()+ angle)










screen.exitonclick()