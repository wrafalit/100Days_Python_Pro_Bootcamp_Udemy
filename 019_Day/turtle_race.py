from turtle import Turtle,Screen
import random

is_race_on = True
screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []


i = 0

for turt in range(6):
    turt = Turtle(shape="turtle")
    turt.color(colors[i])
    turt.pu()
    turt.goto(x= -230, y=-100 + i*30)
    i += 1
    all_turtle.append(turt)

if user_input:
    is_race_on = True

# print(all_turtle)

while is_race_on:

    for t in all_turtle:
        if t.xcor() > 230:
            win = t.pencolor()
            is_race_on = False
            break
        random_dist = random.randint(0, 50)
        t.forward(random_dist)

if user_input == win:
    print("You win bet")
else:
    print("You lose bet! Win color: ", win)


screen.exitonclick()