from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


def move_for():
    tim.forward(10)

def move_back():
    tim.back(10)

def coun_clock():
    tim.left(10)

def clock():
    tim.right(10)

def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(key="w",fun=move_for)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="a",fun=coun_clock)
screen.onkey(key="d",fun=clock)
screen.onkey(key="c",fun=clear)

screen.exitonclick()


