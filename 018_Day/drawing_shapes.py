from turtle import Turtle, Screen

tim = Turtle()

distance = 100
shape = 3


tim.forward(100)
tim.right(30+90)
tim.forward(100)
tim.right(30+90)
tim.forward(100)
tim.right(30+90)
# tim.forward(100)

i = 0
for _ in range(5):
    shape += 1
    for _ in range(shape):
        tim.forward(distance)
        tim.right((360/shape))











screen = Screen()
screen.exitonclick()