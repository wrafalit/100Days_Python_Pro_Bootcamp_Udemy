from turtle import Turtle


class Paddles:



    def __init__(self,x):
        self.paddle = Turtle()
        self.paddle.pu()
        self.paddle.color('white')
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.setposition(x,0)

    def up(self):
        y_move = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), y_move)

    def down(self):
        y_move = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), y_move)




