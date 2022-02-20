# import colorgram
#
# rgb_list = []
# colors = colorgram.extract("SpotPainting03.jpg",6)
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb_list.append((r,g,b))
# print(rgb_list)
import random
from turtle import Turtle, Screen
screen = Screen()

color_list = [(213, 169, 105), (78, 92, 124), (199, 240, 245), (252, 235, 236)]

tim = Turtle()
screen.colormode(255)

tim.speed(10)
tim.pu()
tim.ht()
y= -200
for _ in range(10):
    tim.goto(-200, y)
    y += 50
    for _ in range(10):
        tim.dot(20, random.choice(color_list));
        tim.forward(50)






screen.exitonclick()