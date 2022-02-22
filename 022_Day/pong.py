from turtle import  Screen
from paddle import Paddles
from ball import Ball
from scoreboard import Score
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddles(350)
l_paddle = Paddles(-350)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on =True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision wall top and bottom
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y() #bounce

    # collision with paddle
    if ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # ball goes out of bouds
    if ball.xcor() > 390:
        ball.reset_position()
        score.add_l_point()
    elif ball.xcor() < -390:
        ball.reset_position()
        score.add_r_point()





screen.exitonclick()
